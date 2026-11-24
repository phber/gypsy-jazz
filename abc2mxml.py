"""Minimal ABC-subset parser -> MusicXML note elements.

Converts the ABC that transcription archives publish into the exact
<note> elements a lead sheet needs, so melodies are transcribed
mechanically rather than by hand.
"""
import re

DIVISIONS = 12
STEPS = 'CDEFGAB'
# key signature -> set of sharped/flatted steps
SHARPS = ['F','C','G','D','A','E','B']
FLATS  = ['B','E','A','D','G','C','F']
KEYFIFTHS = {'C':0,'G':1,'D':2,'A':3,'E':4,'B':5,'F#':6,'C#':7,
             'F':-1,'Bb':-2,'Eb':-3,'Ab':-4,'Db':-5,'Gb':-6,
             'Am':0,'Em':1,'Bm':2,'F#m':3,'C#m':4,'Dm':-1,'Gm':-2,'Cm':-3,
             'Ddor':-1,'Ador':0,'Edor':1,'Gdor':-2}
TYPE = {3:'16th',4:'eighth',6:'eighth',8:'quarter',9:'eighth',12:'quarter',
        16:'half',18:'quarter',24:'half',36:'half',48:'whole',2:'32nd'}
DOTTED = {9,18,36,42}
ACCNAME = {1:'sharp',-1:'flat',0:'natural',2:'double-sharp',-2:'flat-flat'}

def key_alters(k):
    f = KEYFIFTHS[k]
    d = {}
    if f > 0:
        for s in SHARPS[:f]: d[s] = 1
    else:
        for s in FLATS[:-f]: d[s] = -1
    return d

def _apply_broken(cur, mark):
    """ABC broken rhythm: 'a>b' dots a and halves b; 'a<b' is the reverse.
    Called once the SECOND note of the pair has been appended."""
    if len(cur) < 2: return
    a, b = cur[-2], cur[-1]
    n = len(mark)
    num, den = (3, 1) if n == 1 else (7, 3) if n == 2 else (15, 7)
    if mark[0] == '>':
        total = a['dur'] + b['dur']
        a['dur'] = total * num // (num + den) if False else a['dur'] * 3 // 2
        b['dur'] = b['dur'] // 2
    else:
        a['dur'] = a['dur'] // 2
        b['dur'] = b['dur'] * 3 // 2


TOKEN = re.compile(r"""
    (?P<chordsym>"[^"]*")
  | (?P<grace>\{[^}]*\})
  | (?P<slurop>\()
  | (?P<slurcl>\))
  | (?P<broken>[<>]+)
  | (?P<tie>-)
  | (?P<bar>\|\]|\[\||\|\||:\||\|:|\||\[[12])
  | (?P<note>(?P<acc>\^{1,2}|_{1,2}|=)?(?P<letter>[A-Ga-gz])(?P<oct>[',]*)(?P<num>\d+)?(?P<slash>/+)?(?P<den>\d+)?)
  | (?P<space>\s+)
  | (?P<other>.)
""", re.X)

def parse(abc_body, L='1/8', key='C'):
    """Return list of measures; each measure is a list of event dicts."""
    num, den = (int(x) for x in L.split('/'))
    base = DIVISIONS * 4 * num // den          # L:1/8 -> 6 with divisions=12
    kalt = key_alters(key)
    measures, cur = [], []
    bar_acc = {}                                # accidentals active this bar
    pending_chord = None
    pending_broken = None
    slur_open = False
    for m in TOKEN.finditer(abc_body):
        kind = m.lastgroup
        if m.group('chordsym'):
            pending_chord = m.group('chordsym').strip('"')
        elif m.group('broken'):
            pending_broken = m.group('broken')
        elif m.group('bar'):
            if cur: measures.append(cur); cur = []
            bar_acc = {}
        elif m.group('note'):
            letter = m.group('letter')
            # duration
            d = base
            if m.group('num'): d = base * int(m.group('num'))
            if m.group('slash'):
                div = int(m.group('den')) if m.group('den') else 2 ** len(m.group('slash'))
                d = base // div
            if letter == 'z':
                cur.append({'rest':True,'dur':d,'chord':pending_chord})
                pending_chord = None
                if pending_broken: _apply_broken(cur, pending_broken); pending_broken = None
                continue
            step = letter.upper()
            octv = 5 if letter.islower() else 4
            octv += m.group('oct').count("'") - m.group('oct').count(',')
            # accidental: explicit this note, else carried in bar, else key
            a = m.group('acc')
            if a:
                alter = {'^':1,'^^':2,'_':-1,'__':-2,'=':0}[a]
                bar_acc[(step,octv)] = alter
                explicit = True
            elif (step,octv) in bar_acc:
                alter = bar_acc[(step,octv)]; explicit = False
            else:
                alter = kalt.get(step, 0); explicit = False
            cur.append({'step':step,'oct':octv,'dur':d,'alter':alter,
                        'explicit':explicit,'inkey':kalt.get(step,0)==alter,
                        'chord':pending_chord,
                        'slur':'start' if m.group(0) and slur_open else None})
            pending_chord = None
            if pending_broken:
                _apply_broken(cur, pending_broken); pending_broken = None
    if cur: measures.append(cur)
    return measures

def note_xml(ev, accent=False, slur=None, indent='      '):
    if ev.get('rest'):
        return ('%s<note><rest/><duration>%d</duration><voice>1</voice>'
                '<type>%s</type>%s</note>\n' % (indent, ev['dur'], TYPE[ev['dur']],
                '<dot/>' if ev['dur'] in DOTTED else ''))
    s = '%s<note><pitch><step>%s</step>' % (indent, ev['step'])
    if ev['alter']: s += '<alter>%d</alter>' % ev['alter']
    s += '<octave>%d</octave></pitch><duration>%d</duration><voice>1</voice>' % (ev['oct'], ev['dur'])
    s += '<type>%s</type>' % TYPE[ev['dur']]
    if ev['dur'] in DOTTED: s += '<dot/>'
    if not ev['inkey']: s += '<accidental>%s</accidental>' % ACCNAME[ev['alter']]
    n = ''
    if slur: n += '<slur type="%s" number="1"/>' % slur
    if accent: n += '<articulations><accent/></articulations>'
    if n: s += '<notations>%s</notations>' % n
    return s + '</note>\n'

def summarise(measures, expect):
    """Report each bar's pitch list and whether it sums to `expect`."""
    rows, ok = [], True
    for i, mm in enumerate(measures, 1):
        tot = sum(e['dur'] for e in mm)
        names = ' '.join(('rest' if e.get('rest') else
                 e['step'] + {1:'#',-1:'b',0:'',2:'##',-2:'bb'}[e['alter']] + str(e['oct']))
                 + '/' + str(e['dur']) for e in mm)
        flag = '' if tot == expect else '  <-- SUM %d, EXPECTED %d' % (tot, expect)
        if tot != expect: ok = False
        rows.append('  bar %-3d %-4d %s%s' % (i, tot, names, flag))
    return ok, rows


# ---------------------------------------------------------------- CLI
def main(argv):
    import argparse
    ap = argparse.ArgumentParser(
        description='Convert an ABC tune body into MusicXML <note> elements '
                    'for a lead sheet, and audit every bar length.')
    ap.add_argument('--abc', required=True, help='ABC tune body (no headers)')
    ap.add_argument('--key', default='C', help='ABC K: field, e.g. G, F, Dm, Am')
    ap.add_argument('--len', dest='L', default='1/8', help='ABC L: field, e.g. 1/8')
    ap.add_argument('--meter', default='4/4', help='ABC M: field, e.g. 4/4 or 3/4')
    ap.add_argument('--octave', type=int, default=0,
                    help='transpose by whole octaves (1 = up an octave)')
    ap.add_argument('--xml', action='store_true', help='emit MusicXML instead of a report')
    a = ap.parse_args(argv)

    bn, bd = (int(x) for x in a.meter.split('/'))
    expect = DIVISIONS * 4 * bn // bd
    ms = parse(a.abc, L=a.L, key=a.key)
    if a.octave:
        for mm in ms:
            for e in mm:
                if not e.get('rest'): e['oct'] += a.octave

    ok, rows = summarise(ms, expect)
    if not a.xml:
        print('meter %s  key %s  L:%s  -> every bar must sum to %d' % (a.meter, a.key, a.L, expect))
        print('bars parsed: %d' % len(ms))
        for r in rows: print(r)
        print('\nALL BARS CORRECT LENGTH:', ok)
        return 0 if ok else 1

    if not ok:
        import sys as _s
        print('refusing to emit XML: bar length audit failed', file=_s.stderr)
        for r in rows:
            if 'EXPECTED' in r: print(r, file=_s.stderr)
        return 1
    for i, mm in enumerate(ms, 1):
        print('    <measure number="%d">' % i)
        for j, e in enumerate(mm):
            if e.get('chord'):
                print('      <!-- chord: %s -->' % e['chord'])
            print(note_xml(e, accent=(j == 0)), end='')
        print('    </measure>')
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))
