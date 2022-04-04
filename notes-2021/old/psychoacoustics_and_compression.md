## A Look At A Sample

* Let's consider a 16-bit audio sample:

        00 010100000101 01

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

## Audio Compression

* Idea: build a simple parameterized approximate model of
  the audio signal

    * In the time domain
    * In the frequency domain

* Transmit the parameters as part of the compressed scheme

* A choice remains:

  * Transmit the *residue* (error in approximation) as a
    separate compressed stream: lossless compression

  * Throw the residue away: lossy compression

* Lossless (e.g. FLAC) is going to be limited for a lot of
  kinds of sounds. The fancier the model, the more kinds of
  sounds that can be compressed well

* Lossy is harder, because mustn't throw away stuff that
  wrecks the sound. Psychoacoustics is needed. Tends to be
  done in frequency domain; models are generalized

## Audio Compression: Stereo

* Typical to take a stereo pair and turn it into a mono
  channel *(l + r) / 2* and a side channel *(l - r)*

* The side channel is typically low amplitude, and so can be
  compressed easily

* Side benefit: mono channel is easily extracted

## Audio Compression: FLAC

* Predict in time domain using polynomial model or Linear
  Predictive Code

* Encode residue using Rice codes (related to Huffman codes)

* Reliable compression > 2×

* Remember: the noise must be compressed and recreated also

## Psychoacoustics: Volume

* Solid Extron
  [article](https://www.extron.com/company/article.aspx?id=loudnesscontrol_ts)

* [Robinson-Dadson curve](https://www.extron.com/technology/img/loudnesscontrol_ts_2-lg.jpg)
  (AKA Fletcher-Munson curve)

* Three frequency bands

    * Below 100 Hz: whatever
    * 100—1000 Hz: bass
    * 1—6 Khz: midrange
    * 6—10 KHz: treble
    * 10KHz and up: whatever

* Three volume bands

    * 40 phon: low (A-weighting, midrange)
    * 70 phon: normal (B-weighting, moderate midrange)
    * 100 phon: loud (C-weighting, flat)
    * 100+ phon: aircraft (C-weighting, treble)

## Volume, Loudness, Presence

* Volume knob is log: ideal midpoint around 50 dB

* Voltage levels are a mess, with multiple
  [standards](https://en.wikipedia.org/wiki/Line_level):
  usually 1—2 Vpp maximum.

* A "loudness" control typically provides a big bass boost
  and a smaller treble boost

* A
  "[presence](https://www.fender.com/articles/tech-talk/be-in-the-moment-the-presence-control-explained)"
  control gives a treble boost, but with some feedback and
  distortion at high volume

## Psychoacoustics: Harmonics, Stretch Tuning, Masking

* Recall: harmonics are multiples of fundamental frequency
  produced by distortion

* Because the ear is not so sensitive at low and high
  frequencies (at normal volumes), it selectively hears
  midrange harmonics of bass notes

* This means that a piano, for example, needs to be
  "[stretch tuned]($@RESOURCEVIEWBYID*85@$)"
  so that the midrange harmonics sound in tune

* The low frequencies are partially "masked"

## Psychoacoustics: Time Scales

* Let's assume a 50Ksps sample rate

* Smallest useful sample chunk for most things: 100 samples,
  50Hz, 2ms

* Fused sound: 500-2500 samples, 10-50 ms

* By 20ms (1000s) latencies will be perceptible

* By 100ms (5000s) latencies will be annoying: larger
  latencies are perceived as intolerable

## Application: Lossy Compression ala MP3

* Good Ars Technica
  [MP3 tutorial](https://arstechnica.com/features/2007/10/the-audiofile-understanding-mp3-compression/)

* High-level view:

    * Split the input signal up into a bunch of frequency
      bands using a "polyphase filter"

    * In each band:

        * Use an FFT to figure out what's going on

        * Use a DCT to get a power spectrum (noise subframes
          are speshul)

        * Quantize the spectrum to reduce the number of bits
          (giving power errors due to noise)

        * Huffman-encode the quantized coefficients to get a
          compact representation

    * Combine all the compressed quantized coefficients to get
      a frame

* The details are quite complex: see something like Ogg
  Vorbis for a cleaner version


