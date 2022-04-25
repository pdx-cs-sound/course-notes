## Audio Effects

* Take an input sound, output a modified version

* All the commercial audio you hear is *heavily* effects
  processed: unprocessed "sounds bad" to a modern ear

* Artistic effects blend into engineering: things like
  limiting amplitude and bandwidth, correcting phase,
  limiting noise, etc are necessary in the audio chain but
  also can sound cool

* Example: Autotuner. Originally for correcting vocalist
  pitch issues, now also used as an artistic effect

## Effects Challenges

* Often "realtime" effects

     * Must have adequate throughput

     * Latency can be a big deal, especially in chains of
       effects

     * (Realtime effects can be used "offline" too)

* Often run on really simple hardware: traditionally analog,
  now tiny microcontrollers

* Complexity of effects chains can be high: "enough knobs,
  but not too many"

* Lots of emulation effects: modeling something else is hard

     * e.g. microphones, amplifiers / speaker cabinets

     * e.g. room effects, telephone effects

## Effects Chains

* Often want to apply multiple effects

* Build DAG for signal processing

    * Splitting is easy in digital

    * Still need to specify mixing for combining signals

    * Challenges: multichannel, latency matching

## Effects Control and Configuration

* So *many* different knobs, displays etc

* Want to save / restore complex effects chain config

* Want to have "metaknobs": simplified control for entire
  effects chain

* Later: plugins and effects "racks"

* Lots of open questions here

## Example: Compression/Expansion

* Idea: Compression — try to hold output volume level more
  steady as function of input volume

* Idea: Expansion — try to make changes in input volume more
  pronounced on output

* Typical implementation: two different linear (in log space
  because volume) gain functions with a "knee"

* Switching functions at knee must not be instantaneous,
  else signal will distort: "attack" time to move to upper
  curve, "decay" time to move back to lower curve

* Used a lot because "professional sound" and because
  always-high volume is desirable

* Demo: `compressor/`

