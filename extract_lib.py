import xml.etree.ElementTree as ET
def strip_ns(t):
    for e in t.iter():
        if '}' in e.tag: e.tag=e.tag.split('}',1)[1]
    return t
def melody(path, pid, voice='1'):
    """-> (bars, fifths, beats, beat_type); bars = list of list of events.
    event = ('r',0,dur) for rest, or (step, octave, dur, alter)."""
    t=strip_ns(ET.parse(path))
    part=[p for p in t.getroot().findall('part') if p.get('id')==pid][0]
    div=int(part.findtext('measure/attributes/divisions'))
    assert 12 % div == 0, div
    sc=12//div
    tm=part.find('measure/attributes/time')
    k=part.find('measure/attributes/key')
    bars=[]
    for m in part.findall('measure'):
        evs=[]
        for n in m.findall('note'):
            if (n.findtext('voice') or '1')!=voice: continue
            if n.find('chord') is not None or n.find('grace') is not None: continue
            d=int(n.findtext('duration'))*sc
            if n.find('rest') is not None: evs.append(('r',0,d))
            else:
                p=n.find('pitch'); al=p.findtext('alter')
                # capture tie direction so tied notes survive the round trip
                tie=''.join(sorted(t.get('type') or '' for t in n.findall('tie')))
                evs.append((p.findtext('step'), int(p.findtext('octave')), d,
                            int(al) if al else 0, tie))
        bars.append(evs)
    return bars, int(k.findtext('fifths')), int(tm.findtext('beats')), int(tm.findtext('beat-type'))
