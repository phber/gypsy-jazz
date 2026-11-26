"""Read the chord chart out of a source MusicXML, with beat positions,
optionally transposing roots, and map each kind into the agreed Django palette."""
import xml.etree.ElementTree as ET
STEPS='CDEFGAB'; OFF=[0,2,4,5,7,9,11]
def tr_root(step, alter, dstep=1, dsemi=2):
    di=STEPS.index(step); pitch=OFF[di]+alter
    nd=(di+dstep)%7; carry=(di+dstep)//7
    return STEPS[nd], (pitch+dsemi)-(OFF[nd]+12*carry)

# source kind -> (display text, MusicXML kind).  Simplifications: 9ths and
# altered dominants become plain 7ths; diminished triads become dim7 (how a
# Hot Club chart spells a passing diminished); tonic 6ths are dropped.
MAP={'major':('','major'), 'minor':('m','minor'),
     'dominant':('7','dominant'), 'dominant-ninth':('7','dominant'),
     'minor-seventh':('m7','minor-seventh'),
     'diminished':('dim7','diminished-seventh'),
     'diminished-seventh':('dim7','diminished-seventh'),
     'half-diminished':('m7b5','half-diminished'),
     'major-sixth':('','major'), 'minor-sixth':('m6','minor-sixth'),
     'major-seventh':('','major'), 'augmented-seventh':('7','dominant'),
     'dominant-11th':('7','dominant'), 'dominant-13th':('7','dominant')}

def chart(path, pid, dstep=0, dsemi=0, scale_to=12):
    """-> {bar_index0: {beat0: (root_step, root_alter, text, kind)}}"""
    t=ET.parse(path)
    for e in t.iter():
        if '}' in e.tag: e.tag=e.tag.split('}',1)[1]
    part=[p for p in t.getroot().findall('part') if p.get('id')==pid][0]
    div=int(part.findtext('measure/attributes/divisions'))
    sc=scale_to//div
    out={}
    for bi,m in enumerate(part.findall('measure')):
        off=0; here={}
        for el in m:
            if el.tag=='harmony':
                rs=el.findtext('root/root-step')
                ra=el.find('root/root-alter')
                al=int(ra.text) if ra is not None else 0
                if dstep or dsemi: rs,al=tr_root(rs,al,dstep,dsemi)
                k=el.findtext('kind')
                if k not in MAP:            # unknown kind -> nearest sane thing
                    k='dominant' if '7' in (el.find('kind').get('text') or '') else 'major'
                text,kind=MAP[k]
                beat=(off*sc)//12
                here[beat]=(rs,al,text,kind)
            elif el.tag=='note' and el.find('chord') is None and el.find('grace') is None:
                off+=int(el.findtext('duration'))
        if here: out[bi]=here
    return out

def fill(chart_, nbars):
    """carry each chord forward so every bar has one; returns list of dicts"""
    res=[]; last=None
    for i in range(nbars):
        h=dict(chart_.get(i,{}))
        if 0 not in h:
            if last is not None: h[0]=last
        if h:
            last=h[max(h)]
        res.append(h)
    return res
