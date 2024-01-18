## A Look At A Sample

* Let's consider a 16-bit audio sample:

        00 010100000101 01

  or 24-bit sample

        00 01010000010101010000 01

* Sample consists of

    * Headroom: Not recorded at maximum amplitude to avoid
      clipping

    * Signal: The actual audio

    * Noise: The low-order bits are typically garbage

* The signal and noise blend together

* As signals are manipulated, more noise creeps up into the
  signal bits because addition and multiplication

## Clipping

* Artifact of fixed-range representation of PCM sample:
  floating-point samples are basically unclippable

* If the amplitude to be represented goes over the max
  possible value or under the min, what to do?

* Not much except clamp (clip) the sample as close as you
  can get it

* Net effect: tops clipped off waves

* This happens in analog systems also because max/min
  voltages

* Discontinuity introduces harmonics: bad distortion

* This is why headroom

## Noise

* Several kinds of common audio noise

    * Uniform "white noise": easy to make with a computer

    * "Pink noise" that rolls off linearly with frequency ("1/f
      noise", "flicker noise")

    * "Brownian noise" ("1/f^2 noise") from random walk in time
      domain

    * Check out this
      [Wikipedia article](https://en.wikipedia.org/wiki/Colors_of_noise)
      on noise colors

## Audio Compression — Model and Residue

* Idea: Build a simplified *model* of the audio signal —
  requires less space to represent.

* Maybe the model is good enough for purpose: lossy
  compression

* Otherwise send the model along with the *residue* — the
  difference between the model and the true signal: lossless
  compression

* The residue might be a bit compressible too

## Audio Compression — Model

* Goal: build a simple parameterized approximate model of
  the audio signal

* Time domain model

    * Audio signals tend to be "smooth" continuous and have
      continuous derivatives

    * Model the signal as lines or polynomials or splines

* Frequency domain model

    * Audio signals tend to be periodic; frequencies tend to
      vary slowly

    * Model the spectrum with quantization in frequency and
      amplitude

    * Phase is confusing

## Audio Compression — Residue

* The residue can often look like noise

* Still, the amplitude of the residue should be small
  relative to the signal amplitude

* Common compression schemes — Huffman coding, Rice coding,
  arithmetic coding — take advantage of amplitude
  distribution of residue

## Lossless vs Lossy Compression

* Lossless (e.g. FLAC) is going to be limited for a lot of
  kinds of sounds. The fancier the model, the more kinds of
  sounds that can be compressed well

* Doing lossy well is harder, because mustn't throw away
  stuff that wrecks the sound. Psychoacoustics is
  needed. Tends to be done in frequency domain; models are
  generalized
