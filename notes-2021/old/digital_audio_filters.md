## Digital Filters

* Idea: get signal into system as close to Nyquist as
  possible

* Do filtering mostly in software (or digital hardware)

* Can build *much* better filters

## Aside: Number Representation

* How shall we represent samples for this kind of
  processing?

* Obvious choice: integers at sampling resolution

    * Can get weird for 24-bit, so promote to 32?

    * Math is tricky: overflow etc. Promote to next higher
      size?

    * What resolution to output? May have more or less
      precision than started with

    * Fast

* Obvious choice: floating-point

    * Scale input to -1..1 or 0..1

    * 32 or 64 bit? (32-bit conveniently has 24 bits of
      precision)

    * Issues of precision and resolution *mostly* go
      away (Inf and NaN).

    * Fast with HW support, slow otherwise especially on
      8-bit hardware

* Less obvious choice: "fixed-point"

    * Treat integer as having implicit fixed "binary point"

            0.100101100000001   =~  0.585968017578125
            1.001011000000001   =~ -0.171905517578125 (sign-magnitude)
                                =~ -0.828094482421875 (twos-complement)

            10010110.00000001   =~ -105.99609375 (twos-complement)

    * Fiddly, especially for languages that don't allow
      implementing a fixed-point type with normal arithmetic

    * Slightly slower than integer: must keep the decimal in
      the right place

    * Typical used on integer-only embedded systems,
      "[DSP chips](https://en.wikipedia.org/wiki/Motorola_56000)"

* Strongly suggest 64-bit floating point for this course:
  just say no to a bunch of annoying bugs

## DFT Filters

* Obvious approach: Convert to frequency domain, scale the
  frequencies you don't want, convert back

* For real-time filter output, this in principle means doing
  a DFT and inverse DFT at every sample position, which
  *seems* expensive to get one sample out

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

