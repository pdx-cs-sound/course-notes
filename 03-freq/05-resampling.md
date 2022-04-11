## Resampling — Sample Rate Conversion

* Given: A signal at some fixed sampling rate *s*

* Wanted: A signal at some different sampling rate *r* that
  represents *the same signal*

* Obvious approach: drop or duplicate samples to get the new
  rate

* Obvious approach is wrong: Nyquist will punish this

## Example: 2× Downsampling 48000 sps → 24000 sps

* Obvious approach would drop every other sample

* But Nyquist says that frequencies above 12 KHz will be
  aliased: this sounds *terrible*

## Example: 2× Upsampling 24000 sps → 48000 sps

* Obvious approach would double every sample

* But this will produce "jaggies" at every other sample:
  these will translate to 12KHz noise that will be quite
  objectionable

## Solution: Low-Pass Filtering

* If we remove the unwanted frequencies, then everything
  turns out OK

* To downsample 2×, low-pass at half the input bandwidth and then
  you can safely take every other sample

* To upsample 2×, double each sample and then low-pass at
  half the output bandwidth to get rid of the noise

* Both solutions use an *anti-aliasing filter*: a
  brick-wall-as-possible low-pass filter

## Digital Filtering Is Expensive: Time-Domain Kludge

* Just average adjacent samples before downsampling; average
  adjacent samples after upsampling

* The average is essentially a bad digital filter here: will
  work OK but not great

## Applying A Digital Filter

* Remember how an FIR digital filter works:

  $$y[i] = \sum_{j=0}^{N-1} a[j] x[i - j]$$

  where the *a[j]* are filter coefficients derived from some
  kind of black magic

* In Python

        y = []
        for i in range(N, len(x)):
            y0 = 0
            for j in range(N):
                y0 += a[j] * x[i - j]
            y.append(y0)

* Oops: the output signal `y` will be `N` shorter than
  the input. May want to stick `N` zeros on the front of `x`
  and then start from 0 instead of `N` or something

## Aside: Python, `numpy`, `scipy`

* The previous loop is going to be crazily slow in Python
  (at least 40× C): running time *M N* where *M* is the
  length of `x`

    * Use `numpy` arrays with `convolve()`:

             y = []
             for i in range(N, len(x)):
                y0 = numpy.convolve(x[i-N+1:i+1], a)
                y.append(y0)

    * Go all the way with `scipy` and `lfilter()`

             y = scipy.signal.lfilter(a, [1], x)

* More C-like speed: still not gonna be super-fast for long
  filters

## Filter and Decimate, Interpolate and Filter

* OK, so we have a plan for downsampling and upsampling by 2×

* 2× is just a special case: the plan works for any
  *integer* multiple or submultiple

* But as the rates get more dramatic, good filters get
  longer and longer

* We need to allow our filter function to have a transition
  band: sharper transition bands make good filters longer
  and longer

* Can handle *rational* factors by upsampling to numerator
  frequency and down to denominator: ⅔× = 2× up, 3× down

* This gets gross for ratios close to 1, e.g. 44100 / 48000
  = 147 / 160 so about 300× work

* Clever algorithms for
  [ASRC](https://ieeexplore.ieee.org/document/6082271) exist
