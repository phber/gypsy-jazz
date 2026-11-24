# Builds the Swedish Lucia dance medley. Melodies are from recollection and
# are flagged UNVERIFIED in the score; harmony, form and architecture are
# arrangement work.
DIV, BAR = 12, 48
SHARPS, FLATS = ['F','C','G','D','A','E','B'], ['B','E','A','D','G','C','F']
TYPE = {3:'16th',6:'eighth',12:'quarter',18:'quarter',24:'half',36:'half',48:'whole'}
ACCN = {1:'sharp',-1:'flat',0:'natural'}

def key_alters(f):
    d = {}
    if f > 0:
        for s in SHARPS[:f]: d[s] = 1
    else:
        for s in FLATS[:-f]: d[s] = -1
    return d

def H(root, text, kind, alter=None, b9=False):
    a = '<root-alter>%d</root-alter>' % alter if alter is not None else ''
    d = ('<degree><degree-value>9</degree-value><degree-alter>-1</degree-alter>'
         '<degree-type text="b9">add</degree-type></degree>') if b9 else ''
    return ('      <harmony print-frame="no"><root><root-step>%s</root-step>%s</root>'
            '<kind text="%s">%s</kind>%s</harmony>\n' % (root, a, text, kind, d))

G6=H('G','6','major-sixth');      C6=H('C','6','major-sixth')
F6=H('F','6','major-sixth');      Bb6=H('B','6','major-sixth',-1)
D7=H('D','7','dominant');         G7=H('G','7','dominant')
C7=H('C','7','dominant');         A7=H('A','7','dominant')
A7b9=H('A','7','dominant',b9=True)
Dm6=H('D','m6','minor-sixth');    Gm6=H('G','m6','minor-sixth')
Cm6=H('C','m6','minor-sixth')
Am7=H('A','m7','minor-seventh');  Dm7=H('D','m7','minor-seventh')
Gm7=H('G','m7','minor-seventh')
Em7b5=H('E','m7b5','half-diminished')
Gdim=H('G','dim7','diminished-seventh',1)
SLASH=('      <note><pitch><step>B</step><alter>0</alter><octave>4</octave></pitch>'
       '<duration>12</duration><voice>1</voice><type>quarter</type></note>\n')

def note(ev, fifths, accent=False, slur=None, fermata=False, stacc=False):
    if ev[0] == 'r':
        return ('      <note><rest/><duration>%d</duration><voice>1</voice><type>%s</type>%s</note>\n'
                % (ev[2], TYPE[ev[2]], '<dot/>' if ev[2] in (18,36) else ''))
    step, octv, dur = ev[0], ev[1], ev[2]
    alter = ev[3] if len(ev) > 3 else None
    ka = key_alters(fifths)
    eff = alter if alter is not None else ka.get(step, 0)
    s = '      <note><pitch><step>%s</step>' % step
    if eff or alter is not None: s += '<alter>%d</alter>' % eff
    s += '<octave>%d</octave></pitch><duration>%d</duration><voice>1</voice>' % (octv, dur)
    s += '<type>%s</type>' % TYPE[dur]
    if dur in (18,36): s += '<dot/>'
    if alter is not None and alter != ka.get(step, 0):
        s += '<accidental>%s</accidental>' % ACCN[alter]
    inner = ''
    if slur: inner += '<slur type="%s" number="1"/>' % slur
    arts = ''
    if accent: arts += '<accent/>'
    if stacc: arts += '<staccato/>'
    if arts: inner += '<articulations>%s</articulations>' % arts
    if fermata: inner += '<fermata type="upright"/>'
    if inner: s += '<notations>%s</notations>' % inner
    return s + '</note>\n'

def attrs(fifths=None, mode='major', slash=None, first=False):
    if fifths is None and slash is None and not first: return ''
    s = '      <attributes>\n'
    if first: s += '        <divisions>%d</divisions>\n' % DIV
    if fifths is not None:
        s += '        <key><fifths>%d</fifths><mode>%s</mode></key>\n' % (fifths, mode)
    if first:
        s += '        <time><beats>4</beats><beat-type>4</beat-type></time>\n'
        s += '        <clef><sign>G</sign><line>2</line></clef>\n'
    if slash:
        s += ('        <measure-style><slash type="%s"%s/></measure-style>\n'
              % (slash, ' use-stems="no"' if slash=='start' else ''))
    return s + '      </attributes>\n'

reh  = lambda m: ('      <direction placement="above">\n        <direction-type>'
                  '<rehearsal enclosure="square">%s</rehearsal></direction-type>\n      </direction>\n' % m)
wrds = lambda t: ('      <direction placement="above">\n        <direction-type>'
                  '<words font-style="italic">%s</words></direction-type>\n      </direction>\n' % t)
FLAG = ('      <direction placement="below">\n        <direction-type>'
        '<words font-weight="bold">MELODY UNVERIFIED - from recollection, '
        'check against your own source before performance</words>'
        '</direction-type>\n      </direction>\n')

# ----------------------------------------------------------------- melodies
# (step, octave, duration[, explicit alter])
T1 = [  # Nu ar det jul igen - G major
 [('D',5,6),('D',5,6),('D',5,6),('D',5,6),('B',4,6),('B',4,6),('G',4,12)],
 [('A',4,6),('B',4,6),('C',5,6),('D',5,6),('B',4,12),('G',4,12)],
 [('D',5,6),('D',5,6),('D',5,6),('D',5,6),('B',4,6),('B',4,6),('G',4,12)],
 [('A',4,6),('G',4,6),('A',4,6),('B',4,6),('D',5,12),('r',0,12)],
 [('B',4,6),('B',4,6),('C',5,6),('C',5,6),('D',5,12),('B',4,12)],
 [('C',5,6),('C',5,6),('B',4,6),('A',4,6),('B',4,12),('G',4,12)],
 [('D',5,6),('D',5,6),('D',5,6),('D',5,6),('B',4,6),('B',4,6),('G',4,12)],
 [('A',4,6),('B',4,6),('A',4,6),('G',4,6),('G',4,24)]]
H1 = [{0:G6},{0:G6,2:D7},{0:G6},{0:D7},{0:G6},{0:C6,2:G6},{0:G6,2:D7},{0:G6}]

T2 = [  # Raven raskar over isen - C major
 [('C',5,6),('C',5,6),('D',5,6),('E',5,6),('E',5,6),('D',5,6),('C',5,6),('G',4,6)],
 [('C',5,6),('C',5,6),('D',5,6),('E',5,6),('E',5,6),('D',5,6),('C',5,12)],
 [('G',5,6),('G',5,6),('E',5,6),('E',5,6),('F',5,6),('E',5,6),('D',5,12)],
 [('C',5,6),('D',5,6),('E',5,6),('C',5,6),('G',4,12),('r',0,12)],
 [('E',5,6),('E',5,6),('F',5,6),('G',5,6),('E',5,12),('C',5,12)],
 [('D',5,6),('D',5,6),('E',5,6),('F',5,6),('D',5,12),('B',4,12)],
 [('C',5,6),('D',5,6),('E',5,6),('F',5,6),('G',5,6),('E',5,6),('C',5,12)],
 [('D',5,6),('C',5,6),('B',4,6),('C',5,6),('C',5,24)]]
H2 = [{0:C6},{0:C6},{0:C6,2:G7},{0:C6},{0:C6},{0:Dm7,2:G7},{0:C6,2:G7},{0:C6}]

T3 = [  # Hej tomtegubbar - F major
 [('C',5,6),('C',5,6),('C',5,6),('C',5,6),('A',4,6),('F',4,6),('A',4,12)],
 [('C',5,6),('C',5,6),('D',5,6),('C',5,6),('B',4,12,-1),('A',4,12)],
 [('B',4,6,-1),('B',4,6,-1),('A',4,6),('G',4,6),('A',4,12),('F',4,12)],
 [('G',4,6),('A',4,6),('B',4,6,-1),('G',4,6),('C',5,24)],
 [('C',5,6),('C',5,6),('C',5,6),('C',5,6),('A',4,6),('F',4,6),('A',4,12)],
 [('C',5,6),('C',5,6),('D',5,6),('C',5,6),('B',4,12,-1),('A',4,12)],
 [('B',4,6,-1),('A',4,6),('G',4,6),('F',4,6),('G',4,6),('A',4,6),('B',4,12,-1)],
 [('A',4,6),('G',4,6),('F',4,6),('G',4,6),('F',4,24)]]
H3 = [{0:F6},{0:F6,2:C7},{0:Gm7,2:C7},{0:Gm7,2:C7},{0:F6},{0:F6,2:C7},{0:Bb6,2:C7},{0:F6}]

T4 = [  # Staffan Stalledrang - D minor
 [('D',5,6),('D',5,6),('E',5,6),('F',5,6),('E',5,6),('D',5,6),('A',4,12)],
 [('D',5,6),('E',5,6),('F',5,6),('G',5,6),('F',5,12),('E',5,12)],
 [('D',5,6),('D',5,6),('C',5,6),('B',4,6,-1),('A',4,12),('D',5,12)],
 [('F',5,6),('E',5,6),('D',5,6),('C',5,6,1),('D',5,24)],
 [('A',5,6),('A',5,6),('G',5,6),('F',5,6),('E',5,6),('D',5,6),('E',5,12)],
 [('F',5,6),('E',5,6),('D',5,6),('C',5,6),('D',5,12),('A',4,12)],
 [('B',4,6,-1),('C',5,6),('D',5,6),('E',5,6),('F',5,6),('E',5,6),('D',5,12)],
 [('E',5,6),('D',5,6),('C',5,6,1),('D',5,6),('D',5,24)]]
H4 = [{0:Dm6},{0:Gm6,2:A7},{0:Dm6,2:A7},{0:A7,2:Dm6},{0:Dm6,2:Gm6},
      {0:Dm6,2:A7},{0:Em7b5,2:A7},{0:A7,2:Dm6}]

SHOUT = T1[:7] + [[('A',4,6),('B',4,6),('C',5,6),('D',5,6),('G',5,24)]]

# ----------------------------------------------------------------- assembly
def slur_plan(bar):
    """start/stop slur marks for runs of 3+ consecutive short notes."""
    marks = [None] * len(bar)
    i = 0
    while i < len(bar):
        if bar[i][0] != 'r' and bar[i][2] <= 6:
            j = i
            while j + 1 < len(bar) and bar[j+1][0] != 'r' and bar[j+1][2] <= 6:
                j += 1
            if j - i + 1 >= 3:
                marks[i], marks[j] = 'start', 'stop'
            i = j + 1
        else:
            i += 1
    return marks


def melody_measure(num, bar, harms, fifths, extra='', newsys=False,
                   barline='', accent_first=False, shout=False):
    s = '    <measure number="%d">\n' % num
    if newsys: s += '      <print new-system="yes"/>\n'
    s += extra
    off = 0
    marks = slur_plan(bar)
    for i, ev in enumerate(bar):
        beat = off // DIV
        if off % DIV == 0 and beat in harms: s += harms[beat]
        s += note(ev, fifths,
                  accent=((i == 0 and accent_first) or (shout and off % DIV == 0)),
                  stacc=(shout and i == len(bar) - 1 and ev[0] != 'r'),
                  slur=marks[i])
        off += ev[2]
    assert off == BAR, 'bar %d sums to %d' % (num, off)
    return s + barline + '    </measure>\n'

def slash_measure(num, harms, extra='', newsys=False, barline=''):
    s = '    <measure number="%d">\n' % num
    if newsys: s += '      <print new-system="yes"/>\n'
    s += extra
    for b in range(4):
        if b in harms: s += harms[b]
        s += SLASH
    return s + barline + '    </measure>\n'

out, n = [], 1

# --- [Intro] 4 bars, G -------------------------------------------------
intro_h = [{0:G6}, {0:G6,2:Gdim}, {0:Am7,2:D7}]
for i, h in enumerate(intro_h):
    extra = ''
    if i == 0:
        extra = (attrs(fifths=1, slash='start', first=True) + reh('Intro')
            + '      <direction placement="above">\n        <direction-type>'
              '<metronome parentheses="no"><beat-unit>quarter</beat-unit>'
              '<per-minute>180</per-minute></metronome></direction-type>\n'
              '        <sound tempo="180"/>\n      </direction>\n'
            + wrds('Swedish Lucia dance medley - bright Hot Club swing, one tempo throughout'))
    out.append(slash_measure(n, h, extra=extra, newsys=(i == 0))); n += 1
out.append(melody_measure(n, [('r',0,12),('r',0,12),('D',5,6),('D',5,6,1),('E',5,6),('F',5,6)],
           {0:H('D','9','dominant-ninth')}, 1, extra=attrs(slash='stop'),
           barline='      <barline location="right"><bar-style>light-light</bar-style></barline>\n')); n += 1

SECTIONS = [
  ('A', 'Nu ar det jul igen', T1, H1, 1,  'major', None),
  ('B', 'Raven raskar over isen', T2, H2, 0, 'major', ({0:G6},{0:G7},'link - G to C')),
  ('C', 'Hej tomtegubbar', T3, H3, -1, 'major', ({0:C6},{0:C7},'link - C to F')),
  ('D', 'Staffan Stalledrang', T4, H4, -1, 'minor', ({0:A7b9},{0:A7b9},'link - F to D minor')),
]
for mark, title, mel, har, fifths, mode, lnk in SECTIONS:
    if lnk:
        a, b, label = lnk
        out.append(slash_measure(n, a, extra=attrs(slash='start') + wrds(label), newsys=True)); n += 1
        out.append(slash_measure(n, b)); n += 1
    for i in range(8):
        extra = ''
        if i == 0:
            extra = (attrs(fifths=fifths, mode=mode, slash='stop' if lnk else None)
                     + reh(mark) + wrds(title) + FLAG)
        out.append(melody_measure(n, mel[i], har[i], fifths, extra=extra,
                   newsys=(i % 4 == 0), accent_first=(i in (0, 4)))); n += 1

# --- [E] 16-bar D-minor solo chorus -----------------------------------
solo = [Dm6,Dm6,Em7b5,A7b9, Dm6,Dm6,Em7b5,A7b9,
        Gm6,Gm6,Dm6,Dm6, Em7b5,A7b9,Dm6,A7b9]
for i, ch in enumerate(solo):
    extra, bl = '', ''
    if i == 0:
        extra = (attrs(slash='start')
            + '      <barline location="left"><bar-style>heavy-light</bar-style>'
              '<repeat direction="forward"/></barline>\n'
            + reh('E') + wrds('Solos - D minor swing, repeat as needed'))
    if i == 15:
        bl = ('      <barline location="right"><bar-style>light-heavy</bar-style>'
              '<repeat direction="backward"/></barline>\n')
    out.append(slash_measure(n, {0:ch}, extra=extra, newsys=(i % 4 == 0), barline=bl)); n += 1

# --- link Dm -> G, then [F] shout chorus ------------------------------
out.append(slash_measure(n, {0:A7}, extra=wrds('link - D minor back to G'), newsys=True)); n += 1
out.append(slash_measure(n, {0:D7})); n += 1
for i in range(8):
    extra = ''
    if i == 0:
        extra = (attrs(fifths=1, slash='stop') + reh('F')
                 + wrds('Shout chorus - tune 1 reprise, dig in') + FLAG)
    out.append(melody_measure(n, SHOUT[i], H1[i], 1, extra=extra,
               newsys=(i % 4 == 0), shout=True)); n += 1

# --- [Tag] 4 bars, G --------------------------------------------------
tag = [
 ([('B',4,12),('D',5,12),('G',4,3,1),('B',4,3),('D',5,3),('F',5,3,0),('D',5,12)],
  {0:G6,2:Gdim}),
 ([('E',5,12),('C',5,12),('E',5,12,-1),('C',5,12)], {0:C6,2:Cm6}),
 ([('C',5,12,1),('A',4,12),('C',5,6),('A',4,6),('F',4,12)], {0:A7,2:D7}),
 ([('G',4,48)], {0:G6}),
]
for i, (bar, har) in enumerate(tag):
    extra = reh('Tag') + wrds('Quintette tag - last time only') if i == 0 else ''
    bl = ('      <barline location="right"><bar-style>light-heavy</bar-style></barline>\n'
          if i == 3 else '')
    s = melody_measure(n, bar, har, 1, extra=extra, newsys=(i == 0),
                       barline=bl, accent_first=True)
    if i == 3:
        s = s.replace('<notations><articulations><accent/></articulations></notations>',
                      '<notations><articulations><accent/></articulations>'
                      '<fermata type="upright"/></notations>')
    out.append(s); n += 1

HEAD = '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <work>
    <work-title>Swedish Lucia Dance Medley</work-title>
  </work>
  <identification>
    <creator type="composer">Traditional Swedish</creator>
    <creator type="arranger">Hot Club medley in the style of Reinhardt and Grappelli</creator>
    <rights>Melodies traditional, public domain. MELODIES ENGRAVED FROM RECOLLECTION AND UNVERIFIED - check each head against a trusted source before performance. Harmony, form and arrangement are original.</rights>
    <encoding>
      <software>Manouche Lead Sheet Engraver</software>
      <encoding-date>2026-11-24</encoding-date>
      <supports element="accidental" type="yes"/>
      <supports attribute="new-system" element="print" type="yes" value="yes"/>
    </encoding>
  </identification>
  <defaults>
    <scaling><millimeters>7.2</millimeters><tenths>40</tenths></scaling>
  </defaults>
  <credit page="1"><credit-words justify="center" valign="bottom" font-size="9" font-weight="bold">Melodies engraved from recollection and UNVERIFIED - check each head before performance</credit-words></credit>
  <part-list>
    <score-part id="P1">
      <part-name>Violin / Guitar</part-name>
      <part-abbreviation>Lead</part-abbreviation>
      <score-instrument id="P1-I1"><instrument-name>Violin</instrument-name></score-instrument>
      <midi-device id="P1-I1" port="1"/>
      <midi-instrument id="P1-I1"><midi-channel>1</midi-channel><midi-program>41</midi-program><volume>80</volume><pan>0</pan></midi-instrument>
    </score-part>
  </part-list>
  <part id="P1">
'''
open('/home/user/gypsy-jazz/lucia-medley.musicxml','w').write(
    HEAD + ''.join(out) + '  </part>\n</score-partwise>\n')
print('measures written:', n - 1)
