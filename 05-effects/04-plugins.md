## Effects "Plugin" Architecture

* Compare VST, LADSPA, LV2, JUCE, etc etc

* "Linux Audio Developers Simple Plugin API" <http://www.ladspa.org>

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

## "Low-Latency Professional Audio"

* JACK (Linux), ASIO (Windows)

* Alternate framework for handling audio from the driver
  level up

* Idea: Keep effects latency minimal by providing
  low-latency metered interfaces

* Idea: Provide standard interfaces for "pro gear" effects
  chains

* Nightmarish to work with

* Better: use an RTOS instead of a desktop OS; also
  nightmarish to work with

## Effects Rack

* Need something to plug into

    * Specify effects chain

    * Provide control interface

    * Run signals through effects

* Classic cockpit problem

    * Effects racks were once literally racks of analog
      effects: connections via ¼" audio cable, knobs on front

    * Emulating this is maybe not *ideal*, but *familiar*

* Good GUI is hard

* Example: Calf Jack Rack <https://calf-studio-gear.org/>

## An Example Plugin: mu-law

* Let's look at a plugin and try it out

* Effect:
  [μ-law](https://en.wikipedia.org/wiki/Μ-law_algorithm) encoding

* Used for telephony to raise quiet parts of signal above
  line noise

* Simple time-domain transformation: no history at all

* How does it sound?

## Implementing In SWH LADSPA

* <http://github.com/BartMassey/swh-ladspa>

* Uses XML as a metadata format for C code (!)

* Makes the plugin syntax and semantics clearer

* Requires some XML tools

## Example Plugin: Valve

* Simulation of a tube amplifier

* Uses limited history to do some filtering as well as
  distortion

* Based on a Norwegian thesis, since lost.
  
* How does it sound?
