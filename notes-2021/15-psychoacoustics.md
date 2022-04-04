## Psychoacoustics: Volume

* [Robinson-Dadson curve](https://media.extron.com/public/technology/img/loudnesscontrol_ts_2-lg.jpg)
  (AKA Fletcher-Munson curve)

* Three frequency bands

    * Below 100 Hz: whatever
    * 100—400 Hz: bass
    * 400Hz—2 Khz: midrange
    * 2—10 KHz: treble
    * 10KHz and up: whatever

* Three volume bands in
  [phon](https://en.wikipedia.org/wiki/Phon): perceived dB
  relative to 1KHz

    * 40 phon: low (A-weighting, midrange)
    * 50 phon: normal (B-weighting, moderate midrange)
    * 70 phon: loud (C-weighting, flat)
    * 100+ phon: aircraft (D-weighting, treble)

## Volume, Loudness, Presence

* Volume knob is "log": ideal midpoint around 50 dB

* Voltage levels are a mess, with multiple
  [standards](https://en.wikipedia.org/wiki/Line_level):
  usually 1—2 Vpp maximum.

* A "loudness" control typically provides a big bass boost
  and a smaller treble boost

    * Solid Extron
      [article](https://www.extron.com/company/article.aspx?id=loudnesscontrol_ts)
      on "loudness" control.

* A
  "[presence](https://www.fender.com/articles/tech-talk/be-in-the-moment-the-presence-control-explained)"
  control gives a treble boost, but with some feedback and
  distortion at high volume (by reducing power amp
  high-frequency negative feedback [or simulating that])

## Psychoacoustics: Harmonics, Stretch Tuning, Masking

* Recall: harmonics are multiples of fundamental frequency
  produced by distortion

* Because the ear is not so sensitive at low and high
  frequencies (at normal volumes), it selectively hears
  midrange harmonics of bass notes

* This means that a piano, for example, needs to be
  "[stretch tuned](https://en.wikipedia.org/wiki/Stretched_tuning)"
  so that the midrange harmonics sound in tune

* The low frequencies are partially "masked"

## Psychoacoustics: Time Scales

* Let's assume a 50Ksps sample rate

* Smallest useful sample chunk for most things: 100 samples,
  2ms

* Fused sound: 500-2500 samples, 10-50 ms

* By 10ms (500s) latencies will be perceptible

* By 20-40ms (1000s-2000s) latencies will be annoying: larger
  latencies are perceived as intolerable

