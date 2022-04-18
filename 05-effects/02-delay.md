## Delay Effects

* One capability of computers that we haven't talked about
  much is the ability to store a signal and give back a
  delayed copy of it

* This is pretty much unobtanium for analog systems.
  Digital delay is crazily cheap and good

* Amount of delay determines effect

    * Small delay (< 10ms): Phase cancellation, localization

    * Moderate delay (10-100ms): "Ensemble" effect
      ([example](http://www.cloneensemble.com/audio/cloneens.mp3))

    * Moderate to long delay (50-500ms): Reverb and echo effects

* Multiple delay effects can be combined; delayed signal can
  be chained with other effects

* Usually feed delayed signal back into input for reverb /
  echo effects

* Wet/dry is a big thing with delay effects, e.g. echo — how
  much reverb signal to feed through (wet) vs original
  signal (dry)

## Ring Buffer

* Delay data structure is a *queue* of samples: typical
  implementation is a *ring buffer*

        len = 100
        buffer = [0]*len
        head = 0
        tail = 0
        empty = True

        def queue(s):
            assert empty or head != tail
            buffer[tail] = s
            tail = (tail + 1) % len
            empty = False

        def dequeue():
            assert not empty
            s = buffer[head]
            head = (head + 1) % len
            empty = head == tail
            return s

## Effect: Reverb and Room Effects

* Idea: Signal + delayed copies simulating resonance and
  bouncing

* Typically longish delays (100ms+)

* Typically delayed copies are filtered and damped

* Output-to-input copy is pretty standard

* Really fancy 3D sound modeling is a thing: leads into
  general acoustics (study of physical sound)

