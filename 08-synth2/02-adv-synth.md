## FM Synthesis

* Old idea for making interesting sounds with cheap hardware

* Now used digitally because easier to implement accurately
  
* Idea: Think about an LFO being used to provide vibrato

  $$ y[t] = \sin(\omega_0 (t + a ~ \sin(\omega_l t)) $$
  
* Well, what happens when \\(w_l\\) gets above 100Hz or so?

* Turns out, can be modeled as a bunch of harmonics and
  subharmonics of \\(w_0\\)

* This is the same as FM radio: use an audio signal to make
  vibrato on a radio signal!

## FM Refs

* Wikipedia has a decent
  [explanation](https://en.wikipedia.org/wiki/Frequency_modulation_synthesis):
  note "operators"

* Some nice samples and a tutorial are [here](https://www.attackmagazine.com/technique/tutorials/introduction-fm-synthesis/)

* The classic synth is the [Yamaha
  DX7](http://www.synthfool.com/docs/Yamaha/DX_Series/Yamaha%20DX7%20Operating%20Manual.pdf). [Dexed](https://asb2m10.github.io/dexed/)
  is a faithful open-source emulation
  
## Granular Synthesis

* Recall our discussion of sound time scales earlier

* 1-50ms is an interesting duration: long enough that tones
  will be heard as tones, but too short to hear individual
  notes
  
* Idea: Break a sample into overlapping chunks in this time
  range and treat them as separate "music particles" or
  "granules"
  
* Various games can now be played with the granules: pitch
  shifting (resample the individual granuals), time
  stretching (replicate or omit granules), fun synthesis
  effects (e.g. emit randomly-sampled granules)
  

## Granular Refs

* [Wikipedia](https://en.wikipedia.org/wiki/Granular_synthesis)

* The Granular Synthesis
  [resource](https://granularsynthesis.com/)
  
* Really nice audio
  [tutorial](https://www.izotope.com/en/blog/music-production/the-basics-of-granular-synthesis.html)


## Physical Modeling

* Idea: Quit trying to be so clever. Build a model of the
  instrument and run the model to make simulated sound
  
* Way harder than sampling synth, but likely to produce way
  better results
  
* Pipe organ is pretty close to perfect:
  [Hauptwerk](https://www.hauptwerk.com) has some amazing
  commercial software combining sampling (for individual
  pipes) with physical modeling (for the instrument as a
  whole)

* Piano isn't bad:
  [Physis](https://www.youtube.com/watch?v=tKthfL7K5qk?t=120)
  has a nice demo

* Plucked string modeling is kind of terrible in general:
  [Karplus-Strong](https://en.wikipedia.org/wiki/Karplus–Strong_string_synthesis)
  is basic plan.

* Proper modeling requires solving acoustic systems; really
  hard math and physics. Drums are an active area of
  research

## Synth Architecture(s)

* A synth is fundamentally async: want to take input from
  the musician while generating sound on the output

* Worth thinking about how that should work

    * Concurrency / parallelism is generally inefficient

    * Hard realtime requirements on both input and output

* Usual plan: three tasks, two threads

    * Retrieve input from the musician

    * Synthesize an output

    * Output samples

* Split is somewhere in the middle, but where?

## The "Pull Model"

* I recommend the simple, but sometimes inefficient, "pull
model"

    * When a sample is needed, call a sample mixer, which
      calls sample generators, which call each other. There
      may be a complex flowgraph to interpret

    * The sources in the flowgraph are a set of
      currently-playing "notes" (sample buffers) and a set
      of control values.  When a note is played out, it is
      removed from the note set

    * When a key is pressed, add a note to the note set

    * When a key is released, find the note that it
      generated and mark it as releasing

    * When a control is changed, update the control value

## Evaluating Pull

* Advantages

    * Sample generation gets priority. Good because
      underruns are the worst

    * Many audio libraries are already callback driven

    * No "lookahead" on key and control changes

* Disadvantages

    * Have to have some synchronization around control value
      and sample buffer access

    * Fairness is hard: musician may be "locked out" of the instrument

    * Overhead can be high — laziness is expensive

