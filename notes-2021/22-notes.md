## Synthesis

* Make a sound: contrast with analysis, effects

* Many popular approaches

    * Wavetables

    * Additive / Subtractive

    * Frequency Modulation

    * Some really fancy stuff

## Notes

* A "note" is a sound with a fixed frequency

* Briefly: Western music uses a "12-tone scale"

    * Remember that the ear hears frequency on log / exp
      scale

    * An "octave" is a frequency that is twice some other frequency

    * We divide an octave into 12 parts: with a base frequency
      *f*, we have

      $$ \textrm{note}_i(f) = f \cdot 2^{i/12} $$

* For example: 

  \begin{eqnarray\*}
    \textrm{note}\_{0}(f) &=& f \\\\
    \textrm{note}\_{12}(f) &=& 2f \\\\
    \textrm{note}\_{-24}(f) &=& \frac{f}{4}
  \end{eqnarray\*}

* There is a bunch of music theory here for future

## Key Numbers, Note Names

* For Western scales, the base frequency is 440Hz, because reasons

* We can use a numbering based on piano keys as a standard:
  MIDI "key number"

* In MIDI 440Hz A is key 69; we call this the A in "octave
  4" or A4

* We give the notes letter names with a possible "sharp" or
  "flat" modifier

          Key   Freq    Name    Octave
          69    440     A       4
          70    466.16  B♭/A♯
          71    493.88  B
          72    523.25  C
          73    554.37  D♭/C♯
          74    587.33  D
          75    622.25  E♭/D♯
          76    659.26  E
          77    698.46  F
          78    739.99  F♯/G♭
          79    783.99  G
          80    830.61  A♭/G♯
          81    880     A       5

* The "why" of all this is a future lecture

## Note Timing

* Notes start at a particular time, have a particular
  *duration* (how long they continue to play)

* For now, will think of this as an "on time" and "off time"
  for the note

* There's a whole complicated theory here, but we don't need
  it yet

* Typically start times are 4 to 30ms apart or thereabouts,
  durations are 4ms and up

* Notes may overlap: "polyphony". Some instruments
  (including some synths) are monophonic: one note at a
  time, so start of next note is end of current

