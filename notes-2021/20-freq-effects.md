## Effect: Tremolo / Vibrato

* Vibrato: Oscillate the pitch of a signal. Resample as an
  effect (later), or just mess with the instrument

* Tremolo: Oscillate the volume of a signal. Easy effect

* **But…**: "The tremolo arm on your favorite guitar, for
  example, is actually a vibrato arm."
  ([source](https://www.sweetwater.com/insync/what-is-the-difference-between-vibrato-and-tremolo/))
  So these terms are used interchangeably.

## Effect: Wah

* Classic frequency-domain effect

* Idea: lowpass filter with variable passband

* Human vocal tract is subtractive via low-pass filters:
  "ooh" is low-pass, "aah" is less low-pass (note inverse
  connection to speaker size)

* My sample implementation uses FIR filters

* More
  [typical implementation](http://www.matthieuamiguet.ch/blog/diy-guitar-effects-python)
  is with an IIR filter cascade (need to keep number of
  coefficients small to be able to update the filter in
  reasonable
  time). [Biquad sections](https://en.wikipedia.org/wiki/Digital_biquad_filter)
  are a popular choice, as here.

* See above for fancy demos

## Effect: Flanger / Phaser / Chorus

* [Flanger](https://www.dsprelated.com/freebooks/pasp/Flanging.html):
  Mix original signal with varying delay of few ms; creates
  varying "comb filter" by phase cancellation ([Nyquist](https://www.audacityteam.org/about/nyquist/) [plugin](https://forum.audacityteam.org/viewtopic.php?t=95059))

* Phaser: Simulation of flanger using cascade of biquad
  "all-pass filters" to get multiple phase cancellations.
  Originally an analog flanger substitute, but different
  enough to survive (Audacity effect)

* [Chorus](https://ccrma.stanford.edu/~jos/pasp/Chorus_Effect.html):
  Use a multi-tap delay line and vary the tap positions to
  get varying delay and frequency shift. Less pronounced
  than ensemble effect (Nyquist [plugin](https://forum.audacityteam.org/viewtopic.php?t=68007))

* These terms are used pretty interchangeably; no standard
  vocab

## Effect: Resampling

* Not normally an "effect": just a thing. We've talked about
  it in detail.

* As an effect: "sped up" (Chipmunks) or "slowed down"
  (sleepy) version of the sound

## Effect: Frequency Stretching

* Frequency domain equivalent of resampling

* Idea: lengthen or shorten a signal while keeping its
  harmonic content the same

    * Time domain: Try to find the period of the signal,
      interpolate whole periods; useful period may be
      impractically long

    * Frequency domain: Take DFT, scale it up or down
      (interpolate / decimate in frequency domain), take inverse
      DFT; Fourier uncertainty is a problem, multiscale is hard

* The difficulty of this plan is why video is time-scaled
  rather than audio

* AKA pitch-shifting, because pitch is log-frequency, so
  multiplication becomes addition

