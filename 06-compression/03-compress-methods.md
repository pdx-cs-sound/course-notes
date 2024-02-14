## Stereo

* Idea: Left and right stereo channels are highly correlated

* Typical to take a stereo pair and turn it into a mono
  channel *(l + r) / 2* and a side channel *(l - r)*

* The side channel is typically low amplitude, and so can be
  compressed easily

* Side benefit: mono channel is easily extracted

## Downsampling

* Idea: Most audio has low amplitudes at higher frequencies

* Downsample the signal, transmit that

* Loss is pretty noticeable at high compression rates; maybe
  need some residue coding

* The signal path may be band-limited anyhow: embedded
  devices, guitar pedals, etc

* MP3 (discussed in a bit) is a surprisingly close cousin to
  this scheme

## Log-Companding

* Idea: Small differences in large amplitudes matter
  less. In particular, human hearing is log-amplitude

* To best represent a signal in a fixed number of bits,
  squash the encoding so that there are fewer codes for
  larger amplitudes

* Classic: 8-bit
  [µ-Law](https://en.wikipedia.org/wiki/%CE%9C-law_algorithm),
  [A-law](https://en.wikipedia.org/wiki/A-law_algorithm)

* µ-Law: 14 bits in, 8 bits out

    * Continuous

      $$y[n] = \mathrm{sgn}(x[n]) \frac{\ln(1 + \mu |x[n]|)}{\ln(1 + \mu)}$$

      where µ is 255 (more or less, I think)

    * Discrete version is given by big approximation table

* A-Law: 13 bits in, 8 bits out; slightly gentler squashing

## POTS

* US Plain Ol' Telephone Service (POTS) compression is downsampling to
  8000 sps and then µ-Law encoding to 8 bits, so 64000 bps
  (*cf* ISDN)

* Lossy, but turns out to be good enough to sound OK for voice

* Originally implemented entirely analog: the digital thing
  is a replicant

* Characteristic telephone sound is mostly this

## FLAC

* Predict in time domain using polynomial model or Linear
  Predictive Code

* Encode residue using Rice codes (related to Huffman codes)

* Reliable compression of about 2×

* Remember: the noise must be compressed and recreated also

## Lossy Compression ala MP3

* Good Ars Technica
  [MP3 tutorial](https://arstechnica.com/features/2007/10/the-audiofile-understanding-mp3-compression/)

* High-level view:

    * Split the input signal up into a bunch of frequency
      bands using a "polyphase filter"

    * In each band:

        * Use an FFT to figure out what's going on

        * Use a DCT to get a power spectrum (noise subframes
          are speshul)

        * Quantize the spectrum to reduce the number of bits
          (giving power errors due to noise)

        * Huffman-encode the quantized coefficients to get a
          compact representation

    * Combine all the compressed quantized coefficients to get
      a frame

* The details are quite complex: see something like Ogg
  Vorbis for a cleaner version
