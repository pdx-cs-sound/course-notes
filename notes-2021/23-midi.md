## MIDI

* Musical Instrument Digital Interface
  ([MIDI](https://www.midi.org/specifications-old/item/the-midi-1-0-specification),
  requires free registration): ancient unidirectional
  standard for keyboard to synth communication (*Prophet
  600*, 1982); replaced analog "control voltage" schemes

* "Instrument" is a synth. "Controller" is a keyboard or
  something

* Physical interface is… a thing. Two-wire serial interface
  on 5-pin DIN connector (also AT keyboard connector). 5ma
  current loop with optical isolation required. 31250 bps
  (halfway between 19200 and 38400, ugh) 8N1 (each byte
  transmitted as eight bits followed by one "stop bit")

* USB MIDI
  [Device Class](https://www.usb.org/sites/default/files/midi10.pdf)
  trades jitter and (maybe) latency for simplicity and
  throughput; MIDI←→USB interfaces start around $10 on
  Amazon.

## MIDI Protocol

* 1-3 byte messages

    * 1st byte is "Status Byte" with high bit set, 

    * Rest are data bytes

    * Special case: "System Exclusive" status messages are
      arbitrary length, terminated by status message
      (usually EOX)

* 16 "channels" used to address specific instruments:
  management can get fairly complicated. "Thru" MIDI is part
  of standard for chaining instruments; latency is a thing
  here

* Key messages (pun intended): Note-On, Note-Off. These can
  have "velocity" of press and release encoded

* Support for pitch bend, continuous controllers, pushbuttons.
  Volume, Balance, Pan, Expression etc are standardized

* Bank / Program / Patch support for changing instrument sound

* Much, much more: read the spec

## MIDI Timing, Sequencing, "MIDI Files"

* Keyboards are realtime, but MIDI can handle

    * Synchronizing messages to specific times

    * Driving a sequencer on-beat

    * Playing *MIDI files:* standard format for timed
      MIDI messages

## Silencing An Instrument

* No great way to tell whether a serial MIDI controller has
  been disconnected

* Easy to end up with "stuck notes" after failing to receive
  NOTE OFF messages for this or other reasons

* Instrument should have easy local way to silence; should
  respond to ALL NOTES OFF and ALL SOUNDS OFF messages

## Working With MIDI

* Get a library. This stuff gets a bit complicated

* For a controller: figure out what you want to be able to
  make an instrument do; figure out what minimum set of
  messages will make an instrument do that

* For an instrument: figure out what you want the instrument
  be able to do; figure out what message you have to and are
  willing to respond to

* Start bare-bones, add functionality incrementally

## Why Not My Computer Keyboard?

* N-key rollover?

* Not so many keys

* Ergonomics are awful

    * No velocity
    * Clicky
