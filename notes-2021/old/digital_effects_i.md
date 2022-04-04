## Delay

* One capability of computers that we haven't talked about
  much is the ability to store a signal and give back a
  delayed copy of it

* This is pretty much unobtanium for analog systems

* Many of the effects we will be looking at make heavy use
  of this

* Data structure is a *queue* of samples: typical
  implementation is a *ring buffer*

## Ring Buffer Example

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

## Effect

* Term is used lots of ways, but basic idea…

* Take in a sound, modify it in a specific way, put it out

* Often "realtime" effects, so latency and throughput matter

* Realtime effects can be used "offline" too

## LADSPA

* "Linux Audio Developers Simple Plugin API" <http://www.ladspa.org>

* Example of effects "plugin" architecture: c.f. LV2, VSP,
  Juce, etc etc

* Idea: Provide loadable "modules" with a known API for

    * Accepting sample streams
    * Accepting control streams (same thing?)
    * Accepting control parameters
    * Emitting output streams
    * Providing GUI information for rendering

* Plugins are available from many places, shipped with Linux
  distros, etc

* Plugin "host" is responsible for loading and plugging
  together plugins: we will use Audacity for non-realtime demos

* Global plugin ID registry

## An Example Plugin: mu-law

* Let's look at a plugin and try it out

* Effect:
  [μ-law](https://en.wikipedia.org/wiki/Μ-law_algorithm) encoding

* Used for telephony to raise quiet parts of signal above
  line noise

* Simple time-domain transformation: no history at all

* How does it sound?

## Implementing In SWH

* Uses XML as a metadata format for C code (!)

* Makes the plugin syntax and semantics clearer

* Requires some XML tools

## Example Plugin: Valve

* Simulation of a tube amplifier

* Uses limited history to do some filtering as well as
  distortion

* Based on a Norwegian
  [thesis](https://web.archive.org/web/20050212035653/http://www.notam02.no/~rbendiks/Diplom/Kurveforming.html#Overstyring%20bruk)
  
* How does it sound?

## Example: Compression/Expansion

* Idea: Compression — try to hold output volume level more
  steady as function of input volume

* Idea: Expansion — try to make changes in input volume more
  pronounced on output

* Typical implementation: two different linear (in log space
  because volume) gain functions with a "knee"

* Effect at knee must not be instantaneous, else signal will
  distort: "attack" time to move to upper curve, "decay"
  time to move back to lower curve

* Used a lot because "professional sound" and because
  always-high volume is desirable

* Demo: Audacity built-in

