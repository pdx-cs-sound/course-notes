## Sound — Pressure Waves

* In this course, we will consider sound in *air*

    * Speed in air is around 1000 feet/s
    * Speed in water is around 5000 feet/s

* Sound is [pressure waves](https://upload.wikimedia.org/wikipedia/commons/8/82/Spherical_pressure_waves.gif)

* Wavelength defined by speed and frequency

        s = fλ

  * s is speed of sound in feet per second
  * f is frequency in cycles per second (Hertz, Hz)
  * λ is wavelength in feet

* Frequency vs wavelength

  * 60Hz ~ 17 feet
  * 1KHz ~ 1 foot
  * 15KHz ~ 1 inch

## Sound — Frequency

* Note that we are assuming a *sinusoidal* wave. Good
  reasons for this described later

* *Absolute* air pressure doesn't matter (within reason)

## Sound — Volume and Power

* Volume is a complicated topic: we will return to it later

* Amplitude of a wave is usually given one of two ways:

    * "Peak-to-peak" (PP) amplitude: the difference between the
      highest and lowest point in a cycle

    * "Root-mean-square" (RMS) amplitude: the "area under
      the curve" of the cycle. For sine waves, we can
      calculate that the RMS amplitude is proportional to
      the PP amplitude

            Arms = App / sqrt(2)

    * Why RMS? Because the power delivered by a signal is
      proportional to the RMS amplitude. In the case of
      sound, the power delivered *is* the RMS amplitude

    * ("110V" line voltage in the US is actually 110V RMS, so
      the peak-to-peak amplitude is about 170V)

* More about [sound power](https://en.wikipedia.org/wiki/Sound_power)

## Sound — Latency

* Latency = delay. For example, how long between when a
  sound is produced and when it is heard

* Delay is not always undesirable: implies storage. A "delay
  line" stores a delayed copy of a signal: this is how
  reverb works

* Latency matters less at lower frequencies due to
  "localization in time": hard to tell when a sound starts
  if it has a long wavelength

## Sound — Superposition

* Sounds that aren't pure sine waves are still usually *cyclic*

* Any repeating sound can be represented by a
  [Fourier Series](https://en.wikipedia.org/wiki/Fourier_series)

* Thus, the sound we hear can actually be plausibly thought
  of as a superposition of sine waves with different
  frequencies and phases

        s(t) = Σ a[i] sin(w[i] t + Φ[i])

  where `a`, `w` and `Φ` are the amplitude, frequency (in
  *radians* — multiply by 2π to get Hz = cycles per second)
  and phase of a sine wave
