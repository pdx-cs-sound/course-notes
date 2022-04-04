## Sources Of PCM "Approximation"

* Band-limited via Nyquist (approximation in time)

* Quantization due to finite representation (approximation
  in amplitude)

* Assumes an idealized sampling clock — clock "skew" and
  "jitter" is a thing for real clocks

## Digital To Analog Conversion

* Need to take a binary number to a voltage

* Classic method: direct conversion via [R/2R Ladder](https://upload.wikimedia.org/wikipedia/commons/4/41/R2r-ladder.png)

    * Very fast, simple

    * Accuracy issues are real: bit voltages and component
      values must be matched pretty exactly

* Classic method: [*Pulse Width Modulation*](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/PWM%2C_3-level.svg/1920px-PWM%2C_3-level.svg.png) (PWM)

    * Digital all the way to single-wire output

    * Arbitrary resolution dependent on timing

    * Really hard to get the filtering right for audio
      applications: want super-high pulse rate

* Fancy methods: can talk about later if folks are interested

## Analog To Digital Conversion

* Convert voltage on wire to binary number

* This is the "hard" direction: the DAC tricks aren't
  entirely invertible

* One common approach uses some combination of DACs and
  comparators to try to make the DAC output match the
  analog input

* [Discussion](https://en.wikipedia.org/wiki/Analog-to-digital_converter#Direct-conversion)

