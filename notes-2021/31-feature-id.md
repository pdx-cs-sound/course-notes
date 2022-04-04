## Analyzing Sound Signals

* Some things to do:

  * Identify beats, tempo
  
  * Identify time signature

  * Identify notes, melody, bass line
  
  * Identify key

  * Identify chords, harmonies

* All of these are hard!

* Caveat: Will mostly talk about pop

## Beat Id: Direct Methods

* Convert signal to power by squaring each sample (maybe
  sqrt, maybe log)

* Search for impulse "spikes" in power

  * Lowpass filter to smooth the signal

  * Look for spikes above some reference
    amplitude. Autodetect amplitude?

  * Look for high second derivative (difference) of 
    power

* Select based on expectations about time

  * Beats are unlikely to occur less than a few milliseconds
    apart

  * Leading edge of beat is unlikely to be more than a
    millisecond long
    
* Can distinguish drumbeat (noise) from note attack
  (spectral)

* Limitations of all this are many:

  * Heuristic, so much tuning is required. ML?
  
  * Music signals are complex: beats buried in signal,
    irregular beats, drum rolls, etc

## Tempo Id

* Take input beats and find "appropriate" periodicity

* Multiple and partial beats exist, so looking for the
  "fundamental" beat frequency
  
  * Tempo likely in the range of 60-300 bpm

  * Use a "Phase-Locked Loop" architecture or an
    autocorrelator to detect dominant beat frequency

## Time Signature Id

* Look for accented beats: 4/4 !.x. 3/4 !.. 6/8 !..x.. etc

* Look for chord changes: see below

## Note Id

* Can get very fancy

* Simple method

  * Build a filter bank
  
  * Watch for changes in power at key frequencies. Tuning?
  
  * Lots of heuristics are helpful

  * Harmonics are a pain
  
* <http://github.com/pdx-cs-sound/findnotes>
  
* Fancy paper: <https://www.sciencedirect.com/science/article/pii/S2212017316303279>
  
## Melody, Bass Line Id

* Look for top and bottom sounding notes

* Rests are an issue

## Key, Chord Id

* See which major or minor scale notes in key signature are
  most consonant with found notes
  
* See which chords that make sense for the key seem to be
  present

* Keep in mind that borrowed chords are a real thing, so
  improve heuristic scores by considering them

* Chord stacks are a pain

* ML may be really helpful here?

## State of the Art

* Is not that great

* Garage Band cheats and uses MIDI/keys rather than notes?
  But transcription is *cool*

* Shazam, SoundHound etc identify songs by first few notes
  of melody (also by soft matching against signal, which is
  not really analysis)

* Bunch of modern projects out there: Google around
