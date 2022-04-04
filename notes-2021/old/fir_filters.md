## Convolution

* You can think of a particular output of our DFT filter
  as having been calculated by *convolution* of a sequence
  of coefficients with a sequence of input samples

  $$ X[k] = \sum_{n=0}^{N-1} x[n] e^{-i k n / N} $$

  $$ = \sum_{n=0}^{N-1} a[n] x[n] $$

* It turns out that this convolution process is standard in
  filtering: we multiply past input samples by fixed linear
  coefficients and then add them up to get the current
  sample value.

* Interestingly, *multiplication in the frequency domain is
  convolution in the time domain*. This means that we can
  use a DFT as a convolution operator if we like

## FIR Filters

* We characterize filters in terms of *impulse response*:
  what if you have an input sample consisting of a single
  pulse of amplitude 1 and then zeros forever?

* Taking a look at the DFT sum, our DFT filter will treat an
  impulse anywhere in its window identically (linear
  time-invariant). When the pulse leaves the window, the DFT
  will then say 0 forever

* We call this *Finite Impulse Response*: an impulse
  presented to the filter will eventually go away

## IIR Filters

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

## Simple FIR Lowpass Filter

* Let's design an FIR lowpass filter

* First, some notation: \\(x[i]\\) is the ith sample of input,
  \\(y[i]\\) is the nth sample of output. Amplitude of sample is
  assumed -1..1

* Filter equation:

  $$ y[i] = \frac{x[i] + x[i - 1]}{2} $$

* Why is this a low-pass filter? For higher frequencies if
  sample \\(x[i]\\) is positive sample \\(x[i - 1]\\) will
  tend to be negative, so they will tend to cancel. For
  lower frequencies the sample \\(x[i]\\) will be close to
  \\(x[i - 1]\\) so they will reinforce

* This filter is kind of bad: the frequency response doesn't
  have much of a "knee" at all

* On the other hand, this filter is stupidly cheap to
  implement, and has very little latency: the output depends
  only on the current and previous samples

## "Higher Filter Orders"

* One way to improve a filter is to cascade copies

* Filter functions multiply, but it gets a little weird

## Wider FIR Filters

* Normally, you want a much sharper knee

* To get that, you typically use more of the history

* For standard FIR filters, it is common to use
  thousands of samples of history

* General FIR filter:

  $$ y[i] = \frac{1}{k} x[i-k \ldots i] \cdot a[k \ldots 0] $$

  So \\(k\\) multiplications and additions per sample

* Now the cost is greater, and the latency is higher, but
  the quality can be *very* good

* Where do the coefficients \\(a\\) come from? Digital
  filter design, next lecture

## Inversion, Reversal, Superposition

* Why the obsession with lowpass? For one, it's the most
  commonly-used filter in audio

* Also because we can get the other kinds "for free" from
  the lowpass

    * Inversion: Negate all coefficients and add 1 to the
      "center" coefficient — this flips the spectrum, so
      high-pass

    * Reversal: Reverse the order of coefficients — this
      reverses the spectrum, so high-pass

    * Superposition: Average the coefficients of two
      equal-length filters — this gives a spectrum that is
      the product of the filters. If one is low-pass and the
      other high-pass, this is band-notch. We can then
      invert to get bandpass.


