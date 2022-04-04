## Wavetable Synthesis

* Idea: Save a per-key waveform, play it back when key is
  pressed

* Needs lots of memory (not a problem anymore)

* Conceptual issues

  * Want note to last as long as key is held: looping is needed

  * May not have a wave for every key: pitch shifting is
    needed

  * Wave may have inappropriate envelope: envelope
    generation is desirable

  * May want to modify wave after-the-fact: effects are
    desirable

## Sustain and Looping

* Want to maintain sustain level for as long as key is held
  down

* Infinite time stretching is a thing: usually achieved by
  "looping"

* Loop start and end may be marked manually, or can try to
  infer the sustain region

## Building a Loop: Frequency Domain

* Use DFT on a window of samples

* Stretch the spectrum as desired

* Use inverse DFT

* Need to use overlapping windows to preserve
  frequency changes over time

* Smearing is real

## Building a Loop: Time Domain

* Use *autocorrelation* to try to find a reasonable constant
  period of the sample

  $$ P = argmax_{t} ~~ x[0..] \cdot x[t..] $$

  (where the signal *x* is treated as cyclic)

* Crop the sample so that the start matches the end: usually
  at zero-crossing 

* May need gain and frequency adjustment to avoid cyclic 
  effects

* The longer the sample, the more "real" it will sound and
  the harder it will be to avoid loop effects

## Pitch Shifting

* As we discovered previously, the pitch of the note can be
  shifted by resampling

* Knowing the fundamental pitch of the original sample(s) is
  actually hard (unless the sample comes from a source with
  "known" frequency). Strongest component of DFT *sometimes*
  works.

* Remember, pitch *shifting* is frequency *stretching*.

## Resampling Technique

* Don't want to dynamically resample on every keypress after
  generating a 93-coefficient FIR anti-aliasing filter
  (probably)

* Possibly use small adjustable IIR filter

* Resample to only a few frequencies (octaves, usually) in
  advance, then use linear interpolation during synthesis to
  get final pitch from nearest properly-resampled cache
  element

* As long as close to the sample rate, linear
  interpolation is "good enough"

* Ideally, just have a sample for every key

* Vibrato is a thing

## Wavetable Envelopes

* Question: Do you want the "natural" envelope from the
  sample, a "synthetic" ADSR envelope, or some combination
  of the two?

* This is really a question for the musician, so should
  probably be prepared to use either

* Ideally, sample will come with start and end of sustain
  marked; otherwise you have to guess

## Soundfonts

* Standard file format for wavetables, set up for
  synthesizer consumption

* [File format](http://freepats.zenvoid.org/sf2/sfspec24.pdf)
  is immensely complicated, so use a library and think
  carefully about handling

* "General MIDI" synthesizers are almost always this:
  standard GM soundfonts are readily available

## General MIDI

* [Standard](https://en.wikipedia.org/wiki/General_MIDI) for
  cross-manufacturer synth capabilities

* Most importantly, identifies 128 specific MIDI "programs"
  with 128 "specific" named sounds

* Examples: "Alto Sax" (66), "Blown Bottle" (77), "Rock
  Organ" (19), "Slap Bass 1" (37), "Bagpipe" (110, in
  "Ethnic" sounds category), "Helicopter" (126)

* MIDI channel 10 has its own set of GM percussion sounds

## Other GM Requirments

* 24-voice polyphony: 16 instrument + 8 percussion (?)

* Certain standard MIDI control change messages must be
  honored

* General MIDI Level 2 (GM2) extends all this

* You have heard this *a lot*

