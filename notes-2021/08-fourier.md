## Sound Is Frequencies

* Most sounds have high periodicity

* Fourier's Theorem (FOO-ree-YAY or thereabouts) says that
  an infinitely repeating sound can be represented as a sum
  of sinusoids

* The ear hears/decomposes a sum of sinusoids

* Yet PCM is a sequence of samples over time: frequency is
  not represented

    * The Nyquist Limit is hard to think of as a signal change
      over time thing

## Time and Frequency

* We have: a continuous waveform, a function \\(f(t)\\)
  representing sound pressure

* We want: a continuous *spectrum*, showing the amplitude
  and phase of sine waves at every frequency \\(\hat{f}(\omega)\\)

* Wait, amplitude and phase from a single function? Yes,
  representing a frequency as a complex number with the usual
  geometric interpretation

  $$ f(\omega) = a + b i $$

  $$ |f(\omega)| = \sqrt{a^2 - b^2} $$

  $$ \theta(f(\omega)) = tan^{-1}(a, b) $$

* Note: you will see both *i* and *j* for \\(\sqrt{-1}\\) in
  different contexts

* Note: we freely mix between *angular frequency*
  \\(\omega\\) and "normal" frequency *f* (dammit — we'll be
  using *f* as a symbol for both frequency and a generic
  function) via

  $$ \omega = 2 \pi f $$

  because once around the circle is one cycle

## The Euler Formula

* [Euler's Formula](https://en.wikipedia.org/wiki/Euler%27s_formula) says complex exponential is a sinusoid:

  $$ e^{i (\omega t + \theta)} = cos(\omega t + \theta) + i~sin(\omega t + \theta) $$

  $$ = e^{i \omega t} e^{i \theta} $$

* Starting point for "[phasor analysis](https://en.wikibooks.org/wiki/Electronics/Phasors)"

* Now our sum of sinusoids can be represented as a sum of
  exponentials, making things easier (?)

## The Time Domain and the Frequency Domain

* Reminder: Fourier claims that every \\(f(t)\\) can be
  represented as some \\(\hat{f}(\omega)\\) (more or less)

* We think of the first kind of thing as "in the time
  domain", the second as "in the frequency domain"

* Converting from a single frequency to its time domain
  representation is "easy":

  $$ f(t) = e^{-i \omega t} $$

* Even for a single sinusoid, converting the other way isn't
  immediately obvious

## Continuous Fourier Decomposition: The Fourier Transform

* Let's just get the [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform) out there:

  $$ \hat{f}(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i \omega t} dt $$

    * The minus sign in the exponent is easy to lose

    * The infinite integral is alarming

    * Still, we now can math up what we wanted

* What about going the other way? Turns out that

  $$ f(t) = \frac{1}{2 \pi} \int_{-\infty}^{\infty} \hat{f}(\omega) e^{i \omega t} d\omega $$

* So the transform is *almost* self-inverse
