# Anatomy & Physiology of Hearing — Presentation Generator

A Python script that programmatically builds a PowerPoint deck introducing the
**anatomy and physiology of hearing** for an audience of **engineers with a
technical background but no medical training**.

The deck (~28 slides) covers only anatomy and physiology. Psychoacoustics is
explicitly out of scope and is mentioned only to set boundaries.

## Contents

- `generate_deck.py` — builds the presentation using [`python-pptx`](https://python-pptx.readthedocs.io/).
- `requirements.txt` — Python dependency.

## Structure

1. **Why we need hearing** — communication, alarm, evolution (convergent), human specificity.
2. **From sound to the brain** — mechanical stimulus → neural sensation, air/bone conduction, key acoustic quantities (dB SPL, 20 Hz–20 kHz).
3. **Anatomy & physiology of the ear** (core):
   - 3.1 Outer & middle ear — impedance adaptation (surface-area ratio + ossicular lever ≈ 30 dB, an impedance-matching transformer), stapedius reflex, Eustachian tube.
   - 3.2 Inner ear — the transducer: traveling wave, tonotopy, inner vs outer hair cells, hair-cell transduction, cochlear amplifier & OAEs, a note on vestibular/balance function.
   - 3.3 Auditory pathway & cortex — pathway, cortical specialization, binaural hearing (ITD/ILD).
4. **Main pathologies** — classified by lesion site (conductive / sensorineural / central), with a summary mapping each pathology to the signal chain.

## Usage

```bash
pip install -r requirements.txt
python generate_deck.py
```

This writes **`hearing_anatomy_physiology.pptx`** to the repository root. Open it
in PowerPoint (or Keynote / LibreOffice Impress) and apply your own template or
branding as needed.
