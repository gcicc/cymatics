# Cymatics — Sound Frequencies Made Visible

Watch sand particles settle into intricate geometric patterns in response to sound frequencies. A mesmerizing intersection of music, mathematics, and physics.

## Features

- **Frequency Control** — Slider from 100 Hz to 2000 Hz creates different Chladni patterns
- **Live Audio** — Web Audio API generates tones while particles settle
- **Preset Patterns** — Five presets for iconic patterns:
  - 200 Hz: Simple Cross
  - 440 Hz: Star (A note)
  - 660 Hz: Hexagonal
  - 880 Hz: Radial
  - 1200 Hz: Dense Lattice
- **Microphone Mode** — Sing or hum and watch patterns respond to your voice frequency
- **Color Themes** — Sand, Blue, Gold, Neon
- **Offline Support** — PWA with service worker caching

## How It Works

Cymatics simulates the physics of Chladni plates—vibrating surfaces where particles of sand accumulate at nodal lines (zones of zero displacement) while being repelled from antinodes (zones of maximum movement).

The mathematical model:
```
Amplitude = sin(n·π·r/L) · cos(m·θ)
```

Where `n` and `m` are mode numbers derived from the frequency, `r` is the radial distance from the center, and `θ` is the angle.

Particles experience a force away from high-amplitude zones and gradually settle at the nodes as the vibration dampens—creating deeply satisfying geometric patterns unique to each frequency.

## Installation

### On Your Phone (Immediate)

1. Visit: **https://gcicc.github.io/cymatics/**
2. On iOS: Tap Share → Add to Home Screen
3. On Android: Menu ⋮ → Install App

### Local Development

```bash
git clone https://github.com/gcicc/cymatics.git
cd cymatics
python generate-icons.py  # Regenerate icons if needed
# Open index.html in a browser
```

## Technical Stack

- **Vanilla JS** — No frameworks
- **Canvas API** — For graphics and particle simulation
- **Web Audio API** — For tone generation and microphone input
- **Service Worker** — For offline support
- **PWA Manifest** — For install-to-home-screen support

## Files

- `index.html` — Complete app (styles, scripts, markup all inline)
- `manifest.json` — PWA metadata
- `sw.js` — Service worker for caching
- `generate-icons.py` — Python script to generate app icons

## Design System

- **Colors**: Sand (#d4af8b) on Dark (#0d1117)
- **Fonts**: Cormorant Garamond (display) + Inter (body)
- **Themes**: Sand on Black, White on Blue, Gold on Dark, Neon on Dark

## Keyboard Controls

- **Slider** — Change frequency or volume
- **Preset buttons** — Jump to iconic patterns
- **Vibrate** — Scatter particles and start tone
- **Reset** — Randomize particle positions
- **Mic** — Toggle microphone input mode

## Browser Support

- Modern browsers with:
  - Canvas API
  - Web Audio API
  - Service Worker support
  - Responsive Web Design

## License

Keystone Apps Portfolio — Personal project.

## Inspiration

Based on the centuries-old phenomenon of Chladni figures, discovered by Ernst Florens Friedrich Chladni in the 1780s. A perfect example of how sound becomes visible.
