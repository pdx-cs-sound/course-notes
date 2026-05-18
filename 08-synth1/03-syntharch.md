## Synthesizer Architecture

* General flow: midi from controller → controller status →
  note management, concurrent note play → effects

* Playing a note: volume / mixing / compression, envelope,
  limiting polyphony

* Synthesizing a tone: so many choices, per-note effects
  (filtering with filter envelope, bends, etc)
  
* Classic is "Eurorack": voltage-controlled bespoke hardware

  * Waveform generator(s): probably monophonic, but maybe
    demuxed poly

  * Low-Frequency Oscillator(s) (LFO)

  * Resonant Filter(s)

  * Fancy sequencers, effects, etc
