## Electrical Representation

* Represent sound pressure as a voltage on a wire

* The classic: telephone

* Allows for transmission, processing

## Microphone

* Turn sound into voltage or current

* Microphone varies resistance, capacitance, voltage or
  current (reversed speaker) depending on air pressure
  differential between front and back

* End result is a voltage representing instantaneous sound
  pressure

* Microphones are bad: noisy, nonlinear devices; often
  limiting factor in sound chain

## Speakers

* Turn voltage into air pressure change

* Wire solenoid attached to paper cone
  [like this](https://www.youtube.com/watch?v=Qu5sqpFDYn8)

* Typically in a resonant cavity (speaker cabinet)

* Speaker solenoid roughly tracks *change in current*
  through the wire, which makes things complicated
  (impedance matters)

* Need wavelength to be long for low frequency to move
  enough air: big speaker "woofer"

    * C.f. [Huygens's Principle](https://en.wikipedia.org/wiki/Huygens–Fresnel_principle)

* Need response time to be fast for high frequency: tiny
  speaker, maybe piezoelectric — "tweeter"

## Attenuation / Amplification

* Simplest transformation

* Attenuation: Sound out linearly less than sound in

* Easy to attenuate in all the obvious ways

* Amplification: Sound out linearly greater than sound in

* Amplification usually requires electronics

## Signal Path

* We now know how to build something like a telephone or
  record player or stomp box:

    * Use a microphone to convert air pressure to voltage

    * Maybe process the voltage somehow: store it somewhere
      or modify it with circuitry

    * Use a speaker to convert voltage back to sound

## Distortion

* Ideally, electric signal exactly represents sound pressure

* In practice, the signal path may introduce *distortion*

    * Nonlinearity: the signal doesn't accurately track the
      sound pressure

    * History: the past signal influences the current signal

* We will talk about "harmonic distortion" (THD) at some
  point

* Some "distortions" are deliberate, because we are used to
  hearing distorted sounds and so they "sound good"

## Feedback

* "Feedback" is a classic oscillation effect:

    * Sound coming out the speaker and back into the
      microphone interacts with speaker + microphone + air as
      a resonance

    * The resonant frequency depends on the distance between
      microphone and speaker (air delay), and on the
      frequency response of the loop

    * If the loop has net positive gain at some frequencies
      (amplification)…

## Limitations

* Representation of analog sound as an electrical signal is
  potentially awesome: high accuracy in time, can represent
  very high and low frequencies well

* In practice, there are problems:

    * Any "noise" (unwanted signal) is also very accurately
      represented. It is easy to accidentally generate
      voltage noise in an analog system, which will be
      accurately represented / amplified as well

    * Analog signal storage devices are clunky, and don't work
      well: records, tapes, etc

    * Manipulating electrical signals requires complex,
      expensive and special-purpose electronics

    * "Audiophiles" love this stuff, so you have to deal with
      them (could be worst problem)

