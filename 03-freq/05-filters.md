## Filters

* Change amplitude / phase of frequencies of sound

* Many applications

    * "Tone" control, "Equalizer"

    * Effects, e.g. "wah"

    * Band limiting for antialiasing, resampling, etc

    * Etc etc

## Common Ideal Filter Shapes

* Usually 0-1 with Passband, Stopband: goal is to block some
  range of frequencies while leaving others alone

* [Filter Shapes](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/filter-fil79.gif):
  Low Pass, High Pass, Bandpass, Band Notch

## Units and Normalization

* Common to leave out sampling rate and gain in DSP

    * In time domain, samples are just numbered

    * In frequency domain, frequencies range from 0..1
      where 1 is the Nyquist limit

    * Amplitude is normalized to -1..1 in time domain,
      0..1 in frequency domain

* We have already talked about $\omega$, dB

    * There are several dB scales floating around

## Filter "Quality" Measures

* The ideal low pass filter is a
  "[brick wall](https://en.wikipedia.org/wiki/Sinc_filter)":

    * Gain in passband is exactly 1 for all frequencies

    * Gain in stopband is exactly 0 for all frequencies

    * Transition is instantaneous (vertical) at corner frequency

## Analog Filters

* Made of electricity: resistors, capacitors, inductors,
  op-amps, etc.

* Analog filters are simple, of necessity

* Analog filters are kind of meh: typically use as few of them as
  possible when digital is available

* Obvious example:
  [anti-aliasing](https://resources.pcb.cadence.com/blog/2020-anti-aliasing-filter-design-and-applications-in-sampling)
  and DC removal
  "[blocking](https://www.knowles.com/docs/default-source/default-document-library/dc-blocking-filter.pdf?sfvrsn=6)"
  (typically a [blocking capacitor](https://electronics.stackexchange.com/questions/18301/how-does-a-capacitor-block-dc))for DAC and ADC


## Aside: Linear Time-Invariant Systems

* Normal filter definition / requirement

* Output signal is a linear function of input signal ("no distortion")

    * Preserves frequencies of input waves

* Output signal does not depend on input time

    * Signals are notionally infinite, so this is a hard
      constraint

* Analog filters are LTI
