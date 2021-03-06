## Generative Synthesis

* Idea: Use simple waveforms and filters to generate complex
  sounds.

* A pipe organ is an additive synthesizer; the electric
  organ builds on that idea

* Remember, any periodic sound can be represented as the sum
  of sinusoids

* But that isn't too practical, so tricks are used

## Harmonics

* Recall that a distorted sinusoid has "harmonics": multiples
  of the fundamental frequency

  * Square wave, triangle have odd harmonics
    (square's are stronger)

  * Sawtooth has all harmonics

  * Various other waves have even and/or odd harmonics

* Organ plan: Make power-of-two pipe lengths for each note
  ("ranks") with adjustable volume

* But start with distorted sinusoids so even more harmonic
  content

* Can add non-octave multiples for even more interesting
  sounds

* Electric organ "oscillators"; synthesizer "VCO"
  (Voltage-Controlled Oscillator)

## Envelope

* Organ only manages quickish attack to sustain level,
  quickish release

* Probably want (at least) an ADSR envelope (next) so that
  sounds can have attack or decay

* May want each note to have *multiple envelopes* to control
  other things

## Envelope: Attack, Decay, Sustain, Release

* [ADSR](https://blog.landr.com/adsr-envelopes-infographic/)
  model is standard envelope description

  * Attack: short ramp-up at start of note

  * Decay: short ramp-down just after attack

  * Sustain: constant hold level when decay is complete

  * Release: short ramp-down after key is released

* Remember, volume is in dB: these ramps should be log-scaled

* Often linear ramps, sometimes smoothed

* Used in pretty much every kind of synthesis

## Tremolo, Vibrato

* Both desirable effects: modulate Voltage Controlled
  Oscillator ("VCO") with Low Frequency Oscillator ("LFO")

  * Tremolo: modulate amplitude

  * Vibrato: modulate frequency

## Filtering

* Sounds have different character depending on harmonic
  content

* May want global filter (lowpass, bandpass, fancy) to
  control overall sound shape

* May want per-note filters that *track* the note: Voltage
  Controlled Filter ("VCF").  Often bandpass, used to get
  resonance effects etc

* Filter often controlled by Low Frequency Oscillator
  ("LFO") and/or ADSR

## Noise

* Adding filtered noise is good

* Several kinds and scales would be nice: white noise,
  scalable max frequency

* Use very slow noise as a control to modulate pitch etc

## Effects

* Almost any of the effects we discussed are nice additions
  to a synth

* Reverb and delay effects are particularly common

## Controllers

* Big strength of additive synthesis: be able to turn the
  knobs (you have knobs, right?) in real-time to modulate
  the sound

* This is why most MIDI keyboards have a pitch wheel and mod
  wheel: ideally the pitch wheel can be used for other things

* MIDI controller boards are really common, with lots of
  knobs and pushpads and other fancy things

## Modeling Natural Sources

* Weird sounds are great, but it's also great to imitate
  orchestral instruments etc

* String "pads" are fairly easy to achieve

* Wind instruments are a bit sketch: use filtered "breath" noise and
  resonant filters

* Brass instruments are meh: they have fairly fancy
  changes in frequency over time. They are basically
  subtractive instruments

* Plucked strings are pretty garbage, really: hard to do
  well ([Karplus-Strong](https://en.wikipedia.org/wiki/Karplus%E2%80%93Strong_string_synthesis))

