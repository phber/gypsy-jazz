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
| Feel | Bright Hot Club swing, la pompe |
| Tempo | quarter = 180, **one tempo across all four tunes** |
| Meter | 4/4 |
| `<divisions>` | 12 → eighth 6, triplet eighth 4, sixteenth 3 |
| Bar length | **every bar must sum to exactly 48** |
| Lead | Violin / guitar, concert pitch, treble clef, no `<transpose>` |
| Register | keep melody in G4–E6, the Grappelli sweet spot |

## Key scheme (approved)

Rising fourths, then the relative minor, then back to the top for the shout chorus:

```
G major  ->  C major  ->  F major  ->  D minor  ->  G major
 (tune 1)    (tune 2)     (tune 3)     (tune 4)     (shout + tag)
 fifths 1    fifths 0     fifths -1    fifths -1    fifths 1
```

F major and D minor share a key signature, so that pivot needs no `<key>` change.

## Form

| Section | Bars | Key | Content |
|---|---|---|---|
| `[Intro]` | 4 | G | la pompe slash bars, chromatic pickup into the head |
| `[A]` | tune 1 form | G | Nu är det jul igen — head |
| link | 2 | G→C | G6 \| G7 |
| `[B]` | tune 2 form | C | Räven raskar över isen — head |
| link | 2 | C→F | C6 \| C7 |
| `[C]` | tune 3 form | F | Hej tomtegubbar — head |
| link | 2 | F→Dm | A7 \| A7 |
| `[D]` | tune 4 form | Dm | Staffan Stalledräng — minor swing |
| `[E]` | 16 | Dm | solo chorus, slash notation, inside repeat barlines |
| link | 2 | Dm→G | A7 \| D7 |
| `[F]` | tune 1 form | G | shout chorus — tune 1 reprise, riffed |
| `[Tag]` | 4 | G | Quintette tag, C6–Cm6–G6 turnaround |

Tune-section bar counts are deliberately left open: they follow each tune's
real form, which cannot be derived without the melodies.

## Harmony vocabulary (period-correct, 1930s Quintette)

Use only: `major-sixth`, `minor-sixth`, `minor-seventh`, `diminished-seventh`,
`dominant`, `dominant-ninth`, `half-diminished`. No modern alterations.

Idioms to apply:
- dim7 passing chords between I and ii (G6 – G#dim7 – Am7)
- m6 as the minor tonic (Dm6, not Dm7) in the Staffan section
- dominant 9ths on turnarounds
- bIV minor-sixth in the tag (C6 → Cm6 → G6)

## Melody source status

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
