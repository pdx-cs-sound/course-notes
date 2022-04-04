## Additive and Subtractive Synthesis

* Idea: Instead of using a wavetable, use "principled" sound
  generators

* A pipe organ is an additive synthesizer; the electric
  organ builds on that idea

* Remember, any periodic sound can be represented as the sum
  of sinusoids

* But that isn't too practical, so tricks are used

## Harmonics

* Recall that a distorted sinusoid has "harmonics": multiples
  of the fundamental frequency

  * Square wave has strong odd harmonics

  * Triangle, various other waves have odd harmonics,
    sometimes even harmonics

* Organ plan: Make power-of-two pipe lengths for each note
  ("ranks") with adjustable volume

* But start with distorted sinusoids so even more harmonic
  content

* Can add non-octave multiples for even more interesting
  sounds

* Electric organ "oscillators"; synthesizer "VCO"

## Envelope

* Organ only manages quickish attack to sustain level,
  quickish release

* Probably want an ADSR envelope (at least) so that
  sounds can have attack or decay

* May want each note to have *multiple envelopes* to control
  other things

## Tremolo, Vibrato

* Both desirable effects: modulate VCO with "LFO"

  * Tremolo: modulate amplitude

  * Vibrato: modulate frequency

## Filtering

* Sounds have different character depending on harmonic
  content

* May want global filter (lowpass, bandpass, fancy) to
  control overall sound shape

* May want per-note filters that *track* the note: "VCF".
  Typically bandpass, used to get resonance effects etc

* Filter may be modded with LFO, ADSR

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
  knobs and other fancy things

## Modeling Natural Sources

* Weird sounds are great, but it's also great to imitate
  orchestral instruments etc

* String "pads" are fairly easy to achieve

* Wind instruments are a bit sketch: use filtered "breath" noise and
  resonant filters

* Brass instruments are meh: they have fairly fancy
  changes in frequency over time. They are basically
  subtractive instruments

* Plucked strings are pretty garbage, really: hard to do well

