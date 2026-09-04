"""Generate the "Anatomy & Physiology of Hearing" PowerPoint deck.

Audience: engineers (technical, no medical background).
Scope: anatomy & physiology only (psychoacoustics is out of scope).

Run:
    pip install -r requirements.txt
    python generate_deck.py

Output:
    hearing_anatomy_physiology.pptx  (in the current directory)
"""

from pptx import Presentation
from pptx.util import Pt

OUTPUT_FILE = "hearing_anatomy_physiology.pptx"

# python-pptx default template layout indices:
#   0 = Title Slide, 1 = Title and Content, 2 = Section Header,
#   5 = Title Only, 6 = Blank
LAYOUT_TITLE = 0
LAYOUT_CONTENT = 1
LAYOUT_SECTION = 2

prs = Presentation()


def add_title_slide(title, subtitle):
    slide = prs.slides.add_slide(prs.slide_layouts[LAYOUT_TITLE])
    slide.shapes.title.text = title
    if len(slide.placeholders) > 1:
        slide.placeholders[1].text = subtitle
    return slide


def add_section_slide(title):
    slide = prs.slides.add_slide(prs.slide_layouts[LAYOUT_SECTION])
    slide.shapes.title.text = title
    return slide


def add_content_slide(title, bullets, notes=None):
    """Add a title + bulleted-content slide with optional speaker notes.

    `bullets` is a list of either strings (level-0 bullets) or
    (text, level) tuples for indented sub-bullets.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[LAYOUT_CONTENT])
    slide.shapes.title.text = title

    body = slide.placeholders[1]
    tf = body.text_frame
    tf.clear()

    for i, item in enumerate(bullets):
        if isinstance(item, tuple):
            text, level = item
        else:
            text, level = item, 0

        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = text
        p.level = level
        p.font.size = Pt(18)

    if notes:
        slide.notes_slide.notes_text_frame.text = notes

    return slide


# ---------------------------------------------------------------------------
# Slide 1 — Title
# ---------------------------------------------------------------------------
add_title_slide(
    "Anatomy & Physiology of Hearing",
    "An engineering-oriented introduction — from acoustic signal to neural sensation",
)

# ---------------------------------------------------------------------------
# Slide 2 — Agenda
# ---------------------------------------------------------------------------
add_content_slide(
    "Agenda",
    [
        "Ch.0  Hearing by the numbers (fun facts hook)",
        "Ch.1  Why we need hearing",
        "Ch.2  From sound to the brain",
        "Ch.3  Anatomy & physiology of the ear (core)",
        "Ch.4  Main pathologies",
    ],
    notes="Roadmap for the talk. Scope is anatomy & physiology only; "
    "psychoacoustics is out of scope and mentioned only to set the boundary.",
)

# ===========================================================================
# Chapter 0 — Hearing by the numbers
# ===========================================================================
add_section_slide("Chapter 0 — Hearing by the numbers")

add_content_slide(
    "Surprising facts about hearing (I)",
    [
        "Never rests: no \u201cearlids\u201d \u2014 hearing works even while we sleep",
        "Hearing before birth: the fetus responds to sound from ~week 25 of gestation",
        "Enormous dynamic range: softest\u2192loudest \u2248 10^6 in pressure (~120 dB)",
        "Astonishing sensitivity: at threshold the eardrum moves less than the",
        ("diameter of a hydrogen atom (~10^-11 m)", 1),
        "Smallest bones in the body: the three ossicles (malleus, incus, stapes)",
    ],
    notes="Attention-grabbing hook. Several facts foreshadow later chapters: "
    "dynamic range, sensitivity, and the ossicles all return in Ch.2 and Ch.3.",
)

add_content_slide(
    "Surprising facts about hearing (II)",
    [
        "Fastest sense: auditory reaction (~8\u201310 ms) beats vision \u2014 that\u2019s why alarms are sounds",
        "The ear emits sound: otoacoustic emissions \u2014 an active amplifier, not a passive mic",
        "Microsecond localization: the brain resolves interaural time differences down to ~10 \u00b5s",
        "Acoustic ranging vs long-distance signaling:",
        ("bats/dolphins echolocate with high precision", 1),
        ("alphorns, elephants (infrasound) and whales communicate over very long distances", 1),
        "Wide frequency span: 20 Hz\u201320 kHz \u2248 10 octaves",
    ],
    notes="Keep it light and fast. Land on the range/precision contrast to bridge "
    "into \u201cwhy hearing matters.\u201d The OAE point is a teaser for Ch.3.",
)

# ===========================================================================
# Chapter 1 — Why we need this sense
# ===========================================================================
add_section_slide("Chapter 1 — Why we need hearing")

add_content_slide(
    "Why hearing matters",
    [
        "Communication and danger/alarm detection",
        "Engineering-relevant properties vs vision:",
        ("omnidirectional", 1),
        ("always-on", 1),
        ("no line-of-sight required", 1),
        "Works in the dark, around corners, while asleep",
    ],
    notes="Frames hearing as an always-on, 360\u00b0 early-warning + communication sensor.",
)

add_content_slide(
    "Evolution & animal examples",
    [
        "Hearing appears widely across animals",
        "Middle ear of mammals and birds evolved independently \u2014 convergent evolution",
        ("(NOT \u201chearing evolved from birds\u201d)", 1),
        "Examples: owls (localization), bats (echolocation), varied frequency ranges",
        "Human specificity: abstract ideas via words, plus emotions and music",
    ],
    notes="Stresses the convergent-evolution accuracy point: the avian and mammalian "
    "middle ear arose separately from different jaw bones.",
)

# ===========================================================================
# Chapter 2 — From sound to the brain
# ===========================================================================
add_section_slide("Chapter 2 — From sound to the brain")

add_content_slide(
    "Big picture: mechanical stimulus \u2192 neural sensation",
    [
        "Hearing = a signal chain converting a mechanical stimulus into a neural sensation",
        "Chain: acoustic wave \u2192 outer/middle ear \u2192 inner ear (transduction) \u2192 nerve \u2192 cortex",
    ],
    notes="Introduces the transducer / signal-chain mental model engineers can anchor to.",
)

add_content_slide(
    "Paths of mechanical stimuli",
    [
        "Air conduction (normal path)",
        "Bone conduction (skull \u2192 cochlea)",
        "Basic acoustic wave properties: pressure variation, frequency, amplitude, propagation",
    ],
    notes="Bone conduction explains why your own voice sounds different on a recording.",
)

add_content_slide(
    "Key acoustic quantities (for engineers)",
    [
        "Sound pressure & intensity; the dB SPL scale (logarithmic)",
        "Frequency; audible range 20 Hz \u2013 20 kHz",
        "Psychoacoustics = relation between a physical attribute and a sensation",
        ("OUT OF SCOPE for this deck", 1),
    ],
    notes="Sets units and explicitly bounds the talk to anatomy/physiology.",
)

# ===========================================================================
# Chapter 3 — Anatomy & Physiology of the ear (core)
# ===========================================================================
add_section_slide("Chapter 3 — Anatomy & physiology of the ear")

add_content_slide(
    "Ear signal-chain overview (anchor diagram)",
    [
        "Outer \u2192 Middle \u2192 Inner \u2192 Nerve \u2192 Cortex",
        "Outer: collect & funnel sound",
        "Middle: impedance matching",
        "Inner: mechanical \u2192 electrical transduction + frequency analysis",
        "Nerve/Cortex: encoding & perception",
        "Revisited in Chapter 4 to map pathologies",
    ],
    notes="This is the recurring anchor diagram \u2014 we come back to it in Ch.4 to "
    "organize the pathologies by lesion site.",
)

# --- 3.1 Outer & middle ear ---
add_content_slide(
    "Outer & middle ear: collecting & amplifying sound",
    [
        "Pinna: captures sound, provides some directional cues",
        "Ear canal: acoustic resonance amplifies mid frequencies",
        "Ossicles (malleus, incus, stapes): transmit vibration to the oval window",
    ],
    notes="Think of the outer/middle ear as the pre-amp + coupling stage of the chain.",
)

add_content_slide(
    "Impedance matching (the key engineering slide)",
    [
        "Problem: air (low impedance) \u2192 cochlear fluid (high impedance)",
        ("naive coupling would lose ~99% of the energy", 1),
        "Solution \u2248 an impedance-matching transformer, ~30 dB gain, via:",
        ("Surface-area ratio: large tympanic membrane \u2192 small oval window", 1),
        ("Ossicular lever action", 1),
    ],
    notes="The money-slide for this audience. Frame it explicitly as impedance "
    "matching: the middle ear recovers energy that would otherwise reflect off "
    "the air\u2013fluid boundary.",
)

add_content_slide(
    "Protection & pressure equalization",
    [
        "Stapedius (acoustic) reflex: muscle stiffens the chain to attenuate loud sounds",
        "Eustachian tube: equalizes middle-ear pressure with ambient",
    ],
    notes="Reflex = a limited, relatively slow AGC (attack too slow for impulses). "
    "Tube = static pressure balance (the ear-popping on a plane).",
)

# --- 3.2 Inner ear ---
add_content_slide(
    "Cochlea & the traveling wave",
    [
        "Fluid-filled, coiled structure",
        "The basilar membrane carries a traveling wave (von B\u00e9k\u00e9sy)",
        "Membrane mechanics vary base\u2192apex (stiff\u2192compliant)",
    ],
    notes="Mechanics set up the frequency analysis before any neural processing.",
)

add_content_slide(
    "Tonotopy",
    [
        "Frequency-to-place mapping:",
        ("base = high frequency", 1),
        ("apex = low frequency", 1),
        "A spatial spectral analyzer \u2014 preserved all the way to cortex",
    ],
    notes="Analogy: a mechanical filter bank / an FFT-by-place. Each location is "
    "tuned to a characteristic frequency.",
)

add_content_slide(
    "Hair cells: inner vs outer",
    [
        "Inner hair cells: the true sensory transducers",
        ("carry most afferent fibers to the brain", 1),
        "Outer hair cells: motility \u2014 act as the local amplifier",
    ],
    notes="Sensing vs actuating roles are physically separated: inner cells report, "
    "outer cells amplify.",
)

add_content_slide(
    "Hair-cell transduction (mechanical \u2192 electrical)",
    [
        "Stereocilia deflection",
        "\u2192 mechanically-gated ion channels open",
        "\u2192 receptor potential",
        "\u2192 neurotransmitter release",
        "\u2192 nerve spikes",
    ],
    notes="The literal mechanotransduction step engineers want to see: a "
    "direct mechanical-to-electrical conversion, no chemical intermediary to open "
    "the channel.",
)

add_content_slide(
    "Cochlear amplifier & otoacoustic emissions (OAEs)",
    [
        "Outer-hair-cell activity = active feedback",
        ("improves sensitivity & frequency selectivity", 1),
        "The ear can emit sound (OAEs)",
        ("basis of newborn hearing screening", 1),
    ],
    notes="An active, nonlinear amplifier \u2014 not a passive microphone. This is why "
    "the ear can be so sensitive and sharply tuned.",
)

add_content_slide(
    "Aside: vestibular (balance) function",
    [
        "Same inner-ear labyrinth also houses the balance organs",
        ("semicircular canals + otoliths", 1),
        "Flagged as an aside \u2014 not part of the auditory path",
    ],
    notes="Acknowledge the shared real estate (and shared nerve), then move on \u2014 "
    "balance is not the focus of this deck.",
)

# --- 3.3 Auditory pathway & cortex ---
add_content_slide(
    "Auditory pathway",
    [
        "Cochlear nerve \u2192 brainstem nuclei \u2192 thalamus \u2192 auditory cortex",
        "Multiple processing stages, not a single wire",
    ],
    notes="Substantial subcortical processing happens before we \u201chear\u201d \u2014 e.g. "
    "binaural comparison already begins in the brainstem.",
)

add_content_slide(
    "Cortex & binaural hearing",
    [
        "Cortical specialization and tonotopic organization preserved",
        "Binaural hearing enables localization:",
        ("ITD \u2014 interaural time difference", 1),
        ("ILD \u2014 interaural level difference", 1),
        "Physiology level only (localization mechanisms, not perception)",
    ],
    notes="Two sensors + differencing = spatial hearing. Kept at the physiological "
    "level to stay out of psychoacoustics.",
)

# ===========================================================================
# Chapter 4 — Main pathologies
# ===========================================================================
add_section_slide("Chapter 4 — Main pathologies")

add_content_slide(
    "Classification by lesion site",
    [
        "Conductive (transmission) \u2014 outer / middle ear",
        "Sensorineural (perception) \u2014 inner ear / hair cells",
        "Central / retrocochlear \u2014 nerve and central pathway",
    ],
    notes="Reuse the signal-chain to organize disease: where along the chain is the "
    "problem?",
)

add_content_slide(
    "Sensorineural I",
    [
        "Presbycusis (age-related): loss starting at high frequencies",
        "Acoustic trauma / noise-induced: outer-hair-cell / stereocilia damage",
    ],
    notes="The most common sensorineural causes. Note mammalian hair cells do not "
    "regenerate, so this damage is permanent.",
)

add_content_slide(
    "Sensorineural II",
    [
        "Ototoxicity: some drugs damage hair cells (e.g. certain antibiotics, chemo)",
        "Genetic hearing loss & syndromes",
    ],
    notes="Molecular / hereditary causes. Genetics is a large and growing field in "
    "audiology.",
)

add_content_slide(
    "Conductive",
    [
        "Otosclerosis: stapes fixation",
        "Ear infections (otitis)",
        "Other transmission-related losses (perforation, ossicular issues, wax)",
    ],
    notes="Mechanical-path problems \u2014 often treatable (surgery, drainage, removal).",
)

add_content_slide(
    "Central / retrocochlear",
    [
        "Acoustic neuroma (vestibular schwannoma)",
        "Central pathway lesions",
        "Completes the lesion-site logic (nerve/central, per Ch.3.3)",
    ],
    notes="Added to close the loop from sensor to cortex: the problem can also be "
    "past the cochlea.",
)

add_content_slide(
    "Summary: pathology \u2194 signal chain",
    [
        "Outer / middle ear \u2192 conductive",
        "Inner ear / hair cells \u2192 sensorineural",
        "Nerve / central \u2192 retrocochlear / central",
        "Key takeaway: locate the lesion, name the loss",
    ],
    notes="Ties Ch.4 back to the Ch.3 anchor diagram. Closing slide: the whole talk "
    "is one signal chain, from acoustic wave to neural sensation \u2014 and each "
    "pathology is a break at a specific stage.",
)

# ---------------------------------------------------------------------------
prs.save(OUTPUT_FILE)
print(f"Wrote {OUTPUT_FILE} with {len(prs.slides._sldIdLst)} slides.")
