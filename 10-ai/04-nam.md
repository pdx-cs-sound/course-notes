# Neural Amp Modeler (NAM): How It Works

A brief, simplified outline of the DSP and ML behind NAM.

The useful framing up front: this is the *nonlinear* counterpart to capturing an
impulse response. A speaker cabinet is, near enough, a linear time-invariant
system, so a single IR plus convolution captures it. An amp's tube/clipping
stages are *nonlinear* — gain depends on level, so no single IR exists. NAM is an
open-source, non-parametric amp modeler that captures a device as a black box,
learning the nonlinear input $\to$ output map directly from audio.

## The ML side: model and training

1. **Problem framing.** Treat the amp (or pedal) as an unknown function mapping a
   dry DI input stream to the processed output stream. NAM learns this as a
   regression: predict output sample $y[n]$ from a window of recent input samples
   $x[n-N{+}1], \dots, x[n]$. It's a *snapshot* — one fixed knob setting per
   model, not conditioned on the controls (unlike parametric commercial products
   such as Neural DSP).

2. **Data capture (the DSP-flavored part).** Play a standardized DI file through
   the real device and record the output, giving an aligned input/target pair.
   The standard input is a deliberately varied signal (~3 min 10 s) chosen to
   exercise the device across levels and content; roughly three minutes of audio
   has been shown to suffice. A latency-calibration step time-aligns target to
   input before training — a sample offset here poisons the fit.

3. **Architecture (default: feedforward WaveNet).** NAM's flagship is a WaveNet
   adapted to run *feedforward* rather than autoregressively. The core is a stack
   of dilated convolutional layers. The key ingredients:
   - **Causal** convolutions: each output depends only on past samples.
   - **Dilated (atrous)** convolutions: layers skip samples so the receptive
     field grows exponentially with depth, reaching tens of milliseconds of
     context cheaply.
   - **Gated activations** inside each layer, with $1\times1$ linear mixers.

   A typical config is a channel dimension of 16, kernel size 3, a $1\times1$
   mixer, and an 18-layer dilation pattern. The "standard" NAM architecture
   stacks two WaveNet modules of different widths in series; LSTM and plain
   ConvNet variants also exist.

4. **Loss function.** Train by minimizing the **error-to-signal ratio (ESR)** —
   squared error normalized by the target's energy, so quiet passages aren't
   drowned out by loud ones:

   $$\text{ESR} = \frac{\sum_n \bigl(y_p[n] - \hat{y}_p[n]\bigr)^2}{\sum_n y_p[n]^2}$$

   Both signals are first run through a **pre-emphasis** high-pass filter,

   $$H(z) = 1 - 0.95\,z^{-1},$$

   because without it the model tends to struggle at higher frequencies. An
   optional DC-offset term is sometimes added (notably for the recurrent
   variant). Training runs on PyTorch Lightning.

## The DSP side: runtime inference

5. **Real-time convolution, but nonlinear.** At inference the trained net slides
   its receptive-field window over the incoming signal (block by block),
   producing output in real time. Mechanically this resembles the partitioned
   convolution used to apply an IR — except the dilated-conv stack with its
   nonlinear gated activations *is* the operator, so it reproduces compression,
   sag, and clipping that a linear IR cannot. It runs on a decent (not
   top-of-the-line) CPU.

6. **Export and deploy.** The trained model is exported to the `.nam` format and
   loaded into a real-time plugin (the C++ NAM Core), typically as a VST3/AU in a
   DAW. In practice you chain it with a separate linear cabinet IR + convolution:
   NAM for the nonlinear amp, an IR loader for the speaker.

## Caveat: aliasing

Because the model is nonlinear, the gated activations generate harmonics above
Nyquist that fold back as **aliasing** — an active research area. The usual
mitigations are oversampling the model at inference or smoothing the activation
functions.

## Sources

- WaveNet architecture in NAM Core — DeepWiki:
  <https://deepwiki.com/sdatkinson/NeuralAmpModelerCore/2.3.1-wavenet-architecture>
- NAM repository overview (workflow, `.nam` export, architectures) — DeepWiki:
  <https://deepwiki.com/sdatkinson/neural-amp-modeler>
- Full-featured training, PyTorch Lightning — NAM docs:
  <https://neural-amp-modeler.readthedocs.io/en/latest/tutorials/full.html>
- "Slimmable NAM" (the standard = two stacked WaveNets of differing width):
  <https://openreview.net/pdf?id=hZJesTnnix>
- PANAMA: Parametric Neural Amp Modeling (NAM as non-parametric baseline; feedforward WaveNet):
  <https://arxiv.org/html/2509.26564v1>
- "Aliasing Reduction in Neural Amp Modeling by Smoothing Activations" (config: 16 ch, kernel 3, 18-layer dilations; pre-emphasis $H(z)=1-0.95z^{-1}$):
  <https://arxiv.org/pdf/2505.04082>
- Damskägg/Wright, "Real-Time Guitar Amplifier Emulation with Deep Learning" (ESR loss, pre-emphasis, ~3 min sufficient):
  <https://www.mdpi.com/2076-3417/10/3/766>
- "A Review of Neural Network-Based Emulation of Guitar Amplifiers" (ESR, pre-emphasis, DC term):
  <https://www.mdpi.com/2076-3417/12/12/5894>
