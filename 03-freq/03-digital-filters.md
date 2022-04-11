## Digital Filters

* Idea: get signal into system as close to Nyquist as
  possible

* Do filtering mostly in software (or digital hardware)

* Can build *much* better filters


## DFT Filters

* Obvious approach: Convert to frequency domain, scale the
  frequencies you don't want, convert back

* For real-time filter output, this in principle means doing
  a DFT and inverse DFT at every sample position, which
  seems…expensive to get one sample out

* Can cheat by sliding the window more than one, but you
  will lose time information from your signal

* Also, DFT has *ripple*: frequencies between bin centers
  will be slightly lower than they should be, since they are
  split between two bins and the sum of gaussians there
  isn't quite 1

* Frequency resolution can be an issue: a 128-point FFT on a
  24KHz sample will produce roughly 200Hz bins, so the
  passband is going to be something like 400Hz, which is
  significant

## FIR and IIR Filters

* We characterize filters in terms of *impulse response*:
  what if you have an input sample consisting of a single
  pulse of amplitude 1 and then zeros forever?

* Taking a look at the DFT sum, our DFT filter will treat an
  impulse anywhere in its window identically (linear
  time-invariant). When the pulse leaves the window, the FFT
  will then say 0 forever

* We call this *Finite Impulse Response*: an impulse
  presented to the filter will eventually go away

* A trick that we will explore is to actually use past filter
  *outputs* as well as inputs to decide the next filter output

* In this case, an impulse will make it into the outputs,
  which means that it will be looped back into the inputs:
  *Infinite Impulse Response*

* Of course, the IIR filter should reduce the amplitude of
  the impulse over time, else badness. Such a filter is a
  *stable* filter

* IIR filters have cheap implementation (analog or digital)
  per unit quality, but:

    * Are less flexible

    * Are harder to design

    * Have lots of issues with stability, noise, numerics
