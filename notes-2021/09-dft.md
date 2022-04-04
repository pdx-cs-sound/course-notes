## The Discrete-Time Fourier Transform

* Let's "get rid of" the infinities by just taking limits

  $$ \hat{f}(\omega) = \lim_{W \rightarrow \infty} \int_{-W}^{W} f(t) e^{-i \omega t} dt $$

  A very long signal relative to its period should be well-approximated

* Now a fiddly argument ensues. If the signal is periodic,
  we should be able to replace the limits by the period:
  after all, it doesn't change anything

  $$ \hat{f}(\omega) = \int_{0}^{P} f(t) e^{-i \omega t} dt $$

* Let's turn the integral
  [into a sum](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)
  by treating \\(f(t)\\) as a series of *impulses*: nonzero
  only at discrete timesteps

  $$ X[k] = \sum_{n=0}^{N-1} x[n] e^{-i k n / N} $$

* The frequency-domain value at *unit frequency k*, namely
  \\(X[k]\\) has been written as a weighted sum of the
  discrete time-domain values \\(x[i]\\) over the period
  \\(N\\)

* The inverse transformation works similarly

  $$ x[n] = \frac{1}{2 \pi N} \sum_{k=0}^{N-1} X[k] e^{i k n / N} $$

## Notes On The DFT

* The \\(X\\)s are still complex (!)

* The inverse is computed only as the sum of discrete
  frequencies

* Be careful about the amplitude. The bin amplitudes grow
  like \\(N\\): there's different conventions about where to
  put the \\(1/N\\) to scale them back. I am following
  Wikipedia here, and putting the scaling in the inverse
  transform.

* This math is so full of fiddly that it is really easy to
  get it screwed up

* Frequency resolution is a function of sampled period

  The sampling rate is handled here by unit frequency. Frequency
  needs to be scaled by the sample rate to be meaningful: if
  you do a 1024-point DFT of a signal sampled at 1024 × 48
  samples per second, each bin of the DFT result represents
  about 24Hz of signal

* Windowing is a thing: next lecture. In brief, because the
  signal is treated as cyclic, truncating the signal so that
  the left and right ends don't match up (at all
  frequencies!) is… bad

