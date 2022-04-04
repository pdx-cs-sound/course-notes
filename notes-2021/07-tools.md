## Audio Is Invisible

* Working with audio is a pain — can only experience it by
  hearing

  * Can't take in a whole sound at once

  * Can't detect a lot of what's going on

  * Ear is in the frequency domain

## Audio Frameworks

* Linux, Windows, Mac, Android: no common standard for
  OS audio, really

* [PortAudio](http://www.portaudio.com) tries to provide a
  common API

* I will mostly talk about Linux audio here, because it is
  what I know best

## Linux Audio Frameworks

* Typically several parts: drivers, system software, library
  interface, UI tooling

* [OSS](http://www.opensound.com/oss.html): a sad piece of
  history

  * Still common to use the OSS compatibility device
    (`/dev/dsp`) provided by ALSA for simple audio things

* [ALSA](http://www.alsa-project.org) provides Linux kernel
  drivers and a library that does some shared-memory stuff
  between processes

  * Let me know if you want some class time on ALSA: it's a
    beast, but I do know a tiny bit about how it works / how
    to configure it

* [PulseAudio](https://www.freedesktop.org/wiki/Software/PulseAudio/)
  provides system software atop ALSA, etc; library API
  supports various GUI programs — this is what most systems use

* [Jack](http://jackaudio.org/) provides an alternative to
  PulseAudio aimed at low-latency audio routing for
  pro-grade music and sound stuff — this is what most
  "special" tools use

* Integration between PulseAudio and Jack seems to actually
  work these days, mostly…

* The new Linux buzz is around
  [PipeWire](https://gitlab.freedesktop.org/pipewire/pipewire/)
  which is PulseAudio and Jack compatible and also does
  video. But it is Linux-only for now, which may be a
  problem.

## Audio Tools

* Huge range of function

  * Generate: e.g. [FluidSynth](http://www.fluidsynth.org),
    various languages e.g. [CSound](http://csound.com))

  * Record / Play / Edit: simple e.g. `parecord` and `paplay` from
    [PulseAudio](http://www.freedesktop.org/wiki/Software/PulseAudio/)
    to complex e.g. [Ardour](http://ardour.org)

  * Process: e.g. the [LADSPA](http://www.ladspa.org) plugin
    suite and frameworks

## General-Purpose Tools

* We will concentrate on "Swiss Army Knife" utility tools
  for now

  * [SoX](http://sox.sourceforge.net/), *literally* "the
    Swiss Army knife of sound programs"

  * [Audacity](http://www.audacityteam.org), a
    cross-platform GUI tool with more emphasis on recording,
    playback and editing

* More about these tools after we've understood
  frequency-domain and DSP a bit better

