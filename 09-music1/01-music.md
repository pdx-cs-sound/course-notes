## Music

* Just any ol' sounds people find pleasing

* We will work in the "classical" realm of notes and note
  combinations

* Further, we will work in the "western" paradigm with
  particular "scales" and "chords" and stuff

## Review: Notes

* A note is a sound with a perceived frequency ("pitch") and
  duration

* 440Hz is A above middle C (MIDI key 69)

* Split the octave between 440Hz and 880Hz into 12 equal
  parts with the same ol' identity

  $$ f = 440 \cdot 2^{(k - 69)/12} $$

* Formula holds down to near 0Hz and up to infinity

## Review: Relative Pitch

* The ear (usually) only hears relative pitch

* We could have started with *any* base frequency rather
  than 440 and done the same thing

* For example, we could have chosen

  $$ 440 \cdot 2^{(k - 71)/12} \approx
     493.88 \cdot 2^{(k - 69)/12} $$

* Then we would have a scale "two half-steps up" from 440

## The Piano Keyboard Is Special

* White keys going from middle C to next C up define a
  "C major scale"

* A scale is a set of notes within an octave

* The C major scale has seven notes: MIDI key numbers

        60, 62, 64, 65, 67, 69 (, 71)
   
* The pattern here is in "half-steps":

        0, +2, +2, +1, +2, +2, +2 (, +1)

* If we repeat this same pattern of half-steps starting from
  any key on the keyboard, we get a major scale

* All major scales sound alike: "happy", "default"

## Stupid Note Names

* We name the white keys on the piano by letter. We use A
  for key 69, and go up/down by eights

* This means that our C-major scale is

       C, D, E, F, G, A, B, C

* A black key can be thought of as a half-step up from the
  white key just to its left, or a half-step down from the
  white key just to its right

* Each black key gets two names: a "sharp" name `♯` for
  the "half-step-up" case, and a "flat" name `♭` for the
  "half-step-down" case

* Thus key number 70, a black key, can be thought of as
  A♯ or B♭

* In textual notation, you'll often see `#` for `♯` and `b`
  for `♭`

* (In general, "sharp" means "toward higher frequencies" and
  "flat" means "toward lower frequencies")

## Example: Relative Major Scales

* Let's work out the D major scale

    * start with D (key 62)

    * Then go +2, +2, +1, +2, +2, +2 (, +1)

    * So D, E, F# (Gb), G, A, B, C# (Db), D

## Note Duration

* Divide music into "beats": typically 45-130 bpm
  ([classical beat rates](https://symphonynovascotia.ca/faqs/symphony-101/how-do-musicians-know-how-fast-to-play-a-piece-and-why-are-the-terms-in-italian/))

* If a note's duration is a single beat, it is usually a
  "quarter note" (because reasons, see below)

* Note duration is typically 1/16 to 4 beats but can vary
  outside that range: mostly "snap-quantized" to the beats

## Measures — Time Signature

* Group up beats into measures: collections usually of 4,
  sometimes of 3, occasionally others

* This defines the "time signature" of a piece of music:
  this is usually written as a fraction

* For example, a time signature of 4/4 says that the music
  will be grouped into 4-beat sections, with each beat a
  quarter note

* 4/4 is known as "common time" `𝄴`, because it is… well, common

## Note Dynamics

* How loud or soft are notes played?

    * Volume of piece
    * Volume of section
    * Volume of individual notes: "accent"

* First beat of a measure is usually accented

* A piece in 4/4 will usually have an a smaller accent at
  beat 3 or 4

## Make "A Piece Of Music"

* Pick a beat rate

* Pick a time signature

* Pick notes and note properties

* (Notes can overlap)

## Notation

* But probably don't want to memorize it, so need to record
  somehow

    * Record audio performance (but how to repeat it?)

    * Record MIDI key down/up events (but how to
      read/analyze it?)

    * Some kind of "music notation"
