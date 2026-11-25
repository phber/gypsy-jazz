# Swedish Lucia Dance Medley — arrangement spec

Status: **architecture approved, blocked on melody transcriptions.**
Engrave as soon as verified melodies for the four tunes are in hand.

## Tunes (in medley order)

1. Nu är det jul igen
2. Räven raskar över isen
3. Hej tomtegubbar
4. Staffan Stalledräng (minor-swing contrast section)

All traditional Swedish — public domain, no licensing constraint.

## Global settings

| Setting | Value |
|---|---|
| Feel | Hot Club swing, la pompe |
| Tempo | quarter = 180, **constant throughout** |
| Meter | **changes per tune** - see below. The quarter note never changes, so it is one tempo. |
| `<divisions>` | 12 |
| Bar length | 3/4 bars = 36 units, 2/4 bars = 24 units |
| Lead | Violin / guitar, concert pitch, treble clef, no `<transpose>` |

## Meters and keys - TAKEN FROM THE SUPPLIED SOURCES

The original 4/4 plan was wrong. None of the four tunes is in 4/4:

| Tune | Meter | Key | Form |
|---|---|---|---|
| Nu ar det jul igen | **3/4** | G major | 8 bars |
| Raven raskar over isen | **3/4** | C major | 8 bars |
| Hej tomtegubbar | **3/4** | C major | 16 bars, AABA |
| Staffan var en stalledrang | **2/4** | E minor | 14 bars |

Key scheme: **G -> C -> C -> E minor -> G**. E minor is the relative minor of
G and shares its signature, so the return to G for the shout chorus needs no
signature change. Signature changes land at bars 1 (fifths 1), 15 (0) and
43 (1). Meter changes at bars 1 (3/4), 43 (2/4) and 57 (3/4).

## Form (86 bars)

| Section | Bars | Meter | Key | Content |
|---|---|---|---|---|
| `[Intro]` | 1-4 | 3/4 | G | 3 pompe slash bars + a D-E-F# pickup bar |
| `[A]` | 5-12 | 3/4 | G | Nu ar det jul igen |
| link | 13-14 | 3/4 | G->C | G6 \| G7 |
| `[B]` | 15-22 | 3/4 | C | Raven raskar over isen |
| link | 23-24 | 3/4 | C | Dm7 \| G7 turnaround |
| `[C]` | 25-40 | 3/4 | C | Hej tomtegubbar |
| link | 41-42 | 3/4 | C->Em | F#m7b5 \| B7b9 minor ii-V |
| `[D]` | 43-56 | **2/4** | E minor | Staffan var en stalledrang |
| `[E]` | 57-72 | 3/4 | E minor | 16-bar slash solo chorus, repeat barlines |
| link | 73-74 | 3/4 | Em->G | Am7 \| D7 |
| `[F]` | 75-82 | 3/4 | G | shout chorus, tune 1 reprise |
| `[Tag]` | 83-86 | 3/4 | G | G#dim7 arpeggio, C6-Cm6, fermata |

## Harmony vocabulary (period-correct, 1930s Quintette)

Use only: `major-sixth`, `minor-sixth`, `minor-seventh`, `diminished-seventh`,
`dominant`, `dominant-ninth`, `half-diminished`. No modern alterations.

Idioms to apply:
- dim7 passing chords between I and ii (G6 – G#dim7 – Am7)
- m6 as the minor tonic (Dm6, not Dm7) in the Staffan section
- dominant 9ths on turnarounds
- bIV minor-sixth in the tag (C6 → Cm6 → G6)

## Melody sources - RESOLVED

The user supplied authoritative MusicXML for all four medley tunes and for
Sankta Lucia. Copies are in `sources/`. Melodies are extracted from them
programmatically by `extract_lib.py` and emitted by `build_medley.py`, so no
melody is hand-transcribed. A fidelity check compares every engraved head bar
against its source: 54 of 54 match.

Two source quirks worth remembering:
- `raven-raskar-over-isen`: the source splits bar 8 across a system, leaving a
  30-unit measure plus a 6-unit pickup. Bar 17 is the same phrase as one clean
  36-unit bar, so the build uses that.
- `nu-ar-det-jul-igen`: 42 measures of verses and variants. The build uses the
  first half (flat 0-3) plus the pass that cadences on the tonic (flat 12-15).

## Superseded: earlier melody source hunt

**All four tunes await melodies supplied by the user.** Web sources are
exhausted or unreachable; do not spend further effort on them.

### Tune 1 - candidate found and REJECTED

A transcription of "Naa er det jul igjen" was retrieved from the John Chambers
Scandinavian collection (two variants, keys D and G, cross-validating exactly).
The user confirmed it is the **Danish song, not the Swedish tune**. Discarded.
Do not reuse it. Lesson: a cognate Scandinavian title does not imply a cognate
melody.

### Source attempts - all exhausted or failing

| Source | Result | Retry? |
|---|---|---|
| `trillian.mit.edu/~jc/music/abc/Scand/` | 200, index read. Only hit was the Danish tune (rejected). No Raven/Raskar, Tomtegubbar or Staffan entry. `XmasSvensk1.abc` read in full: holds only "Ett barn ar fodd denna dag", "Julottan", "Svensk Jul #1" | no - exhausted |
| `abcnotation.com/searchTunes` | timeout on 4 queries, twice over | no - service unreliable |
| `folkwiki.se` | 503, four attempts across two days | no |
| `folktunefinder.com` | 403 Forbidden | no - permanent |
| `pvv.ntnu.no/.../hej_tomtegubber.pdf` | 502 | no |
| `bethsnotesplus.com` | 200 but lyrics only, melody paywalled | no |

### Input format the user will send

Any of: ABC, MusicXML, MIDI, or plain note names with rhythm. For note names,
per tune: the key, the meter, and bar-by-bar note names with durations, e.g.

```
Tune: Raven raskar over isen
Key: C   Meter: 4/4
bar 1: G8 G8 A8 G8 E4 C4
bar 2: ...
```

where the trailing number is the note value (4 = quarter, 8 = eighth,
8. = dotted eighth, 16 = sixteenth). Octave marks only where it jumps.

Flag any tune that is NOT in 4/4 - the medley assumes one shared tempo in
4/4, and a 3/4 tune would force either a recast or a plan change.

## When melodies arrive

Run them through the transcriber rather than engraving by hand:

```bash
python3 -I abc2mxml.py --meter 4/4 --key G --len 1/8 --abc "<abc body>"
```

That reports every bar's pitches and length. Add `--xml` to emit MusicXML
`<note>` elements; it refuses to emit if any bar is the wrong length.
Use `--octave 1` to lift a low transcription into the violin register.

Any input format works as a starting point — ABC, MusicXML, MIDI, or plain
note names with rhythm.
