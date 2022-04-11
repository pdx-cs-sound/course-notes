## The Discrete Fourier Transform

* A discrete frequency-domain representation for a discrete
  time-domain PCM signal

  $$ X[k] = \sum_{n=0}^{N-1} x[n] e^{-i k n / N} $$

## Windowing

* $x[n]$ is treated as *cyclic*: it is assumed that the
  length of $x$ is exactly the period of the signal

* If you have a cycle-and-a-half of a sine, it's going to
  look like there's a sharp edge in it

* To fix this, we taper off the signal toward the ends of
  the DFT by multiplying it by a
  [window function](https://en.wikipedia.org/wiki/Window_function). For
  example, a "sine window" applies as

  $$ sin(\pi n / N) x[n] $$

* Sadly, this also acts as a low-pass filter. There are
  various tradeoffs between filtering and smoothing. It's
  something of a black art, and mostly beyond this course

## Goertzel Filters

* The DFT can be thought of as a
  [Gaussian Filter](https://en.wikipedia.org/wiki/Gaussian_filter)
  bank like [this](http://wiki.besa.de/index.php?title=File:Spectral_%285%29.gif)

* The transform as given is $O(N^2)$, because we do
  $O(N)$ work to compute each bin

* But we can compute for just some of the bins if we like: even
  one. Just fix $k$

  $$ X[k] = \sum_{n=0}^{N-1} x[n] e^{-i k n / N} $$

* This is the so-called "Goertzel filter". I've used these a
  lot as a narrow bandpass filter

## The Fast Fourier Transform

* A dynamic programming trick gets the time complexity of
  the DFT down to $O(N \lg N)$

* No, I'm not going to explain it here: treat it as a black box

* The FFT gives exactly the same answers as the DFT, just faster

* Limitation: The FFT requires a power-of-two number of samples

    * OK, there are fancy FFTs that work by *prime
      factoring* the number of samples. Many small factors
      are better

    * Powers of two have many small factors

* Limitation: The output frequencies must be distributed
  linearly, which may not be what you wished for

## The Discrete Cosine Transform

* Usually you don't care about phase information

* The
  [DCT](https://en.wikipedia.org/wiki/Discrete_cosine_transform)
  gives you something similar to the FFT, but only
  magnitudes

* Still can be done $O(N lg N)$

* The DCT has a different set of boundary conditions

* DCTs are used a lot in compression and processing, for
  example in MPEG

## Spectra of Triangle Wave, Square Wave

* [Triangle](https://en.wikipedia.org/wiki/Triangle_wave), [square](https://en.wikipedia.org/wiki/Square_wave): Fundamental plus "odd harmonics"

  * Harmonic is a multiple of the fundamental. So odd
    harmonics of *f* appear at *3f*, *5f*, etc

    * For square wave

      $$ x[t] = sin(\omega t) + \frac{1}{3} sin(3 \omega t) + \frac{1}{5} sin(5 \omega t) + \ldots $$

    * For triangle wave

      $$ x[t] = sin(\omega t) - \frac{1}{9} sin(3 \omega t) + \frac{1}{25} sin(5 \omega t) + \ldots $$

## Spectra In General

* Odd and sometimes even harmonics are a characteristic of
  many kinds of distortion

* "Total Harmonic Distortion" measures this by inputting a
  sine wave and seeing what harmonics come out

* "White noise" (random samples): Flattish noise spectrum
  ("noise is a sum of random frequencies")

## Frequency Localization In Time

* Fundamentally ill-defined: FT only works right on an
  infinite periodic signal, throws away all information
  about changes in frequency

* Heisenbergy: Smaller DFT gives more local information
  about frequency, but at the cost of poorer accuracy. Low
  frequency signals, in particular, will not be captured

* "Overlapping" heuristic: Do a DFT, slide over a few
  samples, do it again

* Overlapping won't save you from abrupt changes: compare
  with windowing

## DFT Application: Frequency Analysis

* Pretty straightforward: do the DFT, look for peaks etc in
  the spectrum

* Still have to do the analysis of the spectrum, which
  involves some kind of other math or heuristics

* There are more sensitive frequency analysis methods that
  do not involve the DFT

## DFT Application: Filtering

* Pretty straightforward: do the DFT, adjust frequencies as
  desired, do the inverse DFT

* See localization in time: will end up doing "overlapping
  windowed" DFT to track changes input frequencies

* Expensive compared to "direct" filtering, which we will
  discuss next time

## DFT Application: Lossy Compression

* Do DFTs, remove "unwanted" stuff

* Depends pretty hard on psychoacoustics

* We will talk more about audio compression later in the
  course
