## FIR "Windowing" Filters

* In general, simplest low-pass filters: take a "window" of
  past samples, then "round off the corners" by multiplying
  by some symmetric transfer function

* There are *many* window functions, each with their own
  slightly different properties as filters: simple things
  like triangular, plausible things like cosine, and weird
  things like Blackman, Hamming, Hanning

* Note that windowing is also how we deal with edge effects
  of DFT: we make the signal have period equal to the DFT
  size by applying a window, but this also low-passes and
  changes the signal

## FIR Chebyshev "Remez Exchange" Filters

* There's a fancy mathematical trick for approximating a
  given desired filter shape with high accuracy for a given
  filter size

* Involves treating filter coefficients as coefficients of a
  Chebyshev Polynomial, then adjusting the coefficients
  until maximum error is minimized

* Probably not something you want to do yourself, but there
  are programs out there that will do it for you

## IIR Filters

* Can get much better response per unit computation by
  feeding the filter output back into the filter (?!)

* In some applications, a 12th-order IIR filter can replace
  a 1024th-order FIR filter

* Design of these filters really wants a full understanding
  of complex analysis, outside the scope of this course

* Fortunately, many standard filter designs exist:
  Chebyschev, Bessel, Butterworth, Biquad, etc

* Basic operation is the same as FIR, except that you have
  to remember some output:

  $$ y[i] = \frac{1}{k+m}
  \left(x[i-k \ldots i] \cdot a[k \ldots 0] +
  y[i-m-1 \ldots i-1] \cdot a(0 \ldots m)\right) $$

* Always use floating point, as intermediate terms can get
  large / small

* Really, just look up a filter design and implement it:
  probably too hard to "roll your own"

