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

## Blocker: melody sources

No verified notation obtained. All sources failed:

| Source | Result | Retry? |
|---|---|---|
| `abcnotation.com/searchTunes` | timeout, 3 queries × 2 attempts | maybe — timeouts may clear |
| `new.folktunefinder.com/tunes/9454` (Räven) | 403 Forbidden | no — permanent |
| `folktunefinder.com/tunes/9454` | 403 Forbidden | no — permanent |
| `folkwiki.se` | 503 Service Unavailable | **yes — likely transient** |
| `pvv.ntnu.no/~raaness/.../hej_tomtegubber.pdf` | 502 Bad Gateway | **yes — likely transient** |
| `bethsnotesplus.com` | 200 but lyrics only; melody behind member login | no |

Also untried: the John Chambers Scandinavian ABC collection mirrored under
`trillian.mit.edu/~jc/music/abc/Scand` — never reached, because the search
pages that index it all timed out.

Do **not** engrave any of these four melodies from memory without marking the
head as unverified in the score. A wrong melody in notation is worse than no
melody, because players trust notation.

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
