"""Swedish Lucia dance medley v2.

Melodies are read directly out of the user-supplied MusicXML files - no hand
transcription. Each tune keeps its OWN meter (3/4, 3/4, 3/4, 2/4) with a
constant quarter-note pulse, so the medley is one tempo throughout.
Harmony, form, links, solo changes and tag are arrangement work.
"""
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-gypsy-jazz/6c085e37-0341-50ff-b193-5c1685285cce/scratchpad/tools')
from extract_lib import melody

SRC = '/tmp/claude-0/-home-user-gypsy-jazz/6c085e37-0341-50ff-b193-5c1685285cce/scratchpad/mxl/'
DIV = 12
TYPE = {3:'16th',6:'eighth',9:'eighth',12:'quarter',18:'quarter',24:'half',
        30:'half',36:'half',48:'whole'}
DOTTED = {9,18,36}
ACCN = {1:'sharp',-1:'flat',0:'natural',2:'double-sharp',-2:'flat-flat'}
SH=['F','C','G','D','A','E','B']; FL=['B','E','A','D','G','C','F']
def ka(f):
    d={}
    if f>0:
        for s in SH[:f]: d[s]=1
    else:
        for s in FL[:-f]: d[s]=-1
    return d

def H(root, text, kind, alter=None, b9=False):
    a='<root-alter>%d</root-alter>'%alter if alter is not None else ''
    d=('<degree><degree-value>9</degree-value><degree-alter>-1</degree-alter>'
       '<degree-type text="b9">add</degree-type></degree>') if b9 else ''
    return ('      <harmony print-frame="no"><root><root-step>%s</root-step>%s</root>'
            '<kind text="%s">%s</kind>%s</harmony>\n'%(root,a,text,kind,d))

G6=H('G','6','major-sixth');   C6=H('C','6','major-sixth')
D7=H('D','7','dominant');      G7=H('G','7','dominant')
A7=H('A','7','dominant');      B7=H('B','7','dominant')
B7b9=H('B','7','dominant',b9=True)
Am7=H('A','m7','minor-seventh');  Dm7=H('D','m7','minor-seventh')
Em6=H('E','m6','minor-sixth');    Em7=H('E','m7','minor-seventh')
Cm6=H('C','m6','minor-sixth')
F_m7b5=H('F','m7b5','half-diminished',1)
Gdim=H('G','dim7','diminished-seventh',1)

def slashnote():
    return ('      <note><pitch><step>B</step><alter>0</alter><octave>4</octave></pitch>'
            '<duration>12</duration><voice>1</voice><type>quarter</type></note>\n')

def note(ev, fifths, accent=False, slur=None, stacc=False, fermata=False):
    if ev[0]=='r':
        return ('      <note><rest/><duration>%d</duration><voice>1</voice><type>%s</type>%s</note>\n'
                %(ev[2],TYPE[ev[2]],'<dot/>' if ev[2] in DOTTED else ''))
    step,octv,dur = ev[0],ev[1],ev[2]
    alter = ev[3] if len(ev)>3 else 0
    need_acc = alter != ka(fifths).get(step,0)
    s='      <note><pitch><step>%s</step>'%step
    if alter or need_acc: s+='<alter>%d</alter>'%alter
    s+='<octave>%d</octave></pitch><duration>%d</duration><voice>1</voice>'%(octv,dur)
    s+='<type>%s</type>'%TYPE[dur]
    if dur in DOTTED: s+='<dot/>'
    if need_acc: s+='<accidental>%s</accidental>'%ACCN[alter]
    inner=''
    if slur: inner+='<slur type="%s" number="1"/>'%slur
    arts=''
    if accent: arts+='<accent/>'
    if stacc: arts+='<staccato/>'
    if arts: inner+='<articulations>%s</articulations>'%arts
    if fermata: inner+='<fermata type="upright"/>'
    if inner: s+='<notations>%s</notations>'%inner
    return s+'</note>\n'

def attrs(fifths=None,mode='major',beats=None,slash=None,first=False):
    if fifths is None and beats is None and slash is None and not first: return ''
    s='      <attributes>\n'
    if first: s+='        <divisions>%d</divisions>\n'%DIV
    if fifths is not None:
        s+='        <key><fifths>%d</fifths><mode>%s</mode></key>\n'%(fifths,mode)
    if beats is not None:
        s+='        <time><beats>%d</beats><beat-type>4</beat-type></time>\n'%beats
    if first: s+='        <clef><sign>G</sign><line>2</line></clef>\n'
    if slash:
        s+=('        <measure-style><slash type="%s"%s/></measure-style>\n'
            %(slash,' use-stems="no"' if slash=='start' else ''))
    return s+'      </attributes>\n'

reh=lambda m:('      <direction placement="above">\n        <direction-type>'
  '<rehearsal enclosure="square">%s</rehearsal></direction-type>\n      </direction>\n'%m)
wr=lambda t:('      <direction placement="above">\n        <direction-type>'
  '<words font-style="italic">%s</words></direction-type>\n      </direction>\n'%t)

def slur_plan(bar):
    marks=[None]*len(bar); i=0
    while i<len(bar):
        if bar[i][0]!='r' and bar[i][2]<=9:
            j=i
            while j+1<len(bar) and bar[j+1][0]!='r' and bar[j+1][2]<=9: j+=1
            if j-i+1>=3: marks[i],marks[j]='start','stop'
            i=j+1
        else: i+=1
    return marks

def mel_measure(num,bar,harms,fifths,barlen,extra='',newsys=False,barline='',
                accent_first=False,shout=False,fermata_last=False):
    s='    <measure number="%d">\n'%num
    if newsys: s+='      <print new-system="yes"/>\n'
    s+=extra
    off=0; marks=slur_plan(bar)
    for i,ev in enumerate(bar):
        if off%DIV==0 and (off//DIV) in harms: s+=harms[off//DIV]
        s+=note(ev,fifths,
                accent=((i==0 and accent_first) or (shout and off%DIV==0)),
                slur=marks[i],
                stacc=(shout and i==len(bar)-1 and ev[0]!='r'),
                fermata=(fermata_last and i==len(bar)-1))
        off+=ev[2]
    assert off==barlen,'bar %d sums to %d, expected %d'%(num,off,barlen)
    return s+barline+'    </measure>\n'

def slash_measure(num,harms,beats,extra='',newsys=False,barline=''):
    s='    <measure number="%d">\n'%num
    if newsys: s+='      <print new-system="yes"/>\n'
    s+=extra
    for b in range(beats):
        if b in harms: s+=harms[b]
        s+=slashnote()
    return s+barline+'    </measure>\n'

# ---------------------------------------------------------------- melodies
nu,_,_,_   = melody(SRC+'t5/score.xml','P1')
rav,_,_,_  = melody(SRC+'t4/score.xml','P1')
hej,_,_,_  = melody(SRC+'t2/score.xml','P1')
staf,_,_,_ = melody(SRC+'t1/lg-170673187.xml','P1')

# "Nu ar det jul igen": first half (flat 0-3) + the pass that cadences on the
# tonic (flat 12-15). The other passes are further verses/variants.
NU = nu[0:4] + nu[12:16]
# "Raven": bars 1-7, then bar 17 which is the clean 36-unit form of bar 8
# (the source splits bar 8 across a system, leaving 30 + a 6-unit pickup).
RAV = rav[0:7] + [rav[16]]
HEJ = hej[0:16]            # full 16-bar AABA
STAF = staf[0:14]          # full 14 bars, 2/4

NU_H  = [{0:G6},{0:G6},{0:G6},{0:D7},{0:C6},{0:G6},{0:Am7,2:D7},{0:G6}]
RAV_H = [{0:C6},{0:C6},{0:C6},{0:G7},{0:C6},{0:C6},{0:Dm7,2:G7},{0:G7,2:C6}]
HEJ_H = [{0:C6},{0:C6},{0:G7},{0:C6},{0:C6},{0:C6},{0:G7},{0:C6,2:G7},
         {0:C6},{0:Am7},{0:G7},{0:C6},{0:C6},{0:C6},{0:G7},{0:C6}]
STAF_H= [{0:Em6},{0:Em6},{0:Em6},{0:Em6,1:B7},{0:B7},{0:B7,1:Em6},{0:Em6},
         {0:Em6,1:B7},{0:Em7},{0:Am7},{0:C6},{0:Em6},{0:B7},{0:Em6}]

# ---------------------------------------------------------------- assembly
FLAG=('      <direction placement="below">\n        <direction-type>'
      '<words font-weight="bold">Melody transcribed from the supplied source score'
      '</words></direction-type>\n      </direction>\n')
out=[]; n=1

# [Intro] 3 slash bars + a pickup bar, G major 3/4
for i,h in enumerate([{0:G6},{0:G6,2:Gdim},{0:Am7,2:D7}]):
    extra=''
    if i==0:
        extra=(attrs(fifths=1,mode='major',beats=3,slash='start',first=True)+reh('Intro')
          +'      <direction placement="above">\n        <direction-type>'
            '<metronome parentheses="no"><beat-unit>quarter</beat-unit>'
            '<per-minute>180</per-minute></metronome></direction-type>\n'
            '        <sound tempo="180"/>\n      </direction>\n'
          +wr('Swedish Lucia dance medley - Hot Club swing. Quarter note stays constant '
              'throughout; the meter changes with each tune.'))
    out.append(slash_measure(n,h,3,extra=extra,newsys=(i==0))); n+=1
out.append(mel_measure(n,[('r',0,12),('r',0,6),('D',4,6),('E',4,6),('F',4,6,1)],
    {0:D7},1,36,extra=attrs(slash='stop'),
    barline='      <barline location="right"><bar-style>light-light</bar-style></barline>\n')); n+=1

cur_fifths, cur_beats = 1, 3      # set by the intro
SECTIONS=[
 ('A','Nu ar det jul igen',          NU,  NU_H,  1,'major',3,36,None),
 ('B','Raven raskar over isen',      RAV, RAV_H, 0,'major',3,36,({0:G6},{0:G7},'link - G to C')),
 ('C','Hej tomtegubbar',             HEJ, HEJ_H, None,None,None,36,({0:Dm7},{0:G7},'link - turnaround in C')),
 ('D','Staffan var en stalledrang',  STAF,STAF_H,1,'minor',2,24,({0:F_m7b5},{0:B7b9},'link - C to E minor')),
]
for mark,title,mel,har,fifths,mode,beats,barlen,lnk in SECTIONS:
    if lnk:
        a,b,label=lnk
        out.append(slash_measure(n,a,3,extra=attrs(slash='start')+wr(label),newsys=True)); n+=1
        out.append(slash_measure(n,b,3)); n+=1
    for i in range(len(mel)):
        extra=''
        if i==0:
            kf = fifths if (fifths is not None and fifths != cur_fifths) else None
            bt = beats  if (beats  is not None and beats  != cur_beats)  else None
            if kf is not None: cur_fifths = kf
            if bt is not None: cur_beats = bt
            extra=(attrs(fifths=kf,mode=mode or 'major',beats=bt,
                         slash='stop' if lnk else None)
                   +reh(mark)+wr(title)+FLAG)
        out.append(mel_measure(n,mel[i],har[i],fifths if fifths is not None else 0,
                   barlen,extra=extra,newsys=(i%4==0),accent_first=(i%4==0))); n+=1

# [E] 16-bar E-minor solo chorus, back in 3/4
solo=[Em6,Em6,F_m7b5,B7b9, Em6,Em6,Am7,Am7, Em6,Em6,C6,B7b9, Em6,Am7,B7b9,Em6]
for i,ch in enumerate(solo):
    extra,bl='',''
    if i==0:
        _bt = 3 if cur_beats != 3 else None
        cur_beats = 3
        extra=(attrs(beats=_bt,slash='start')
          +'      <barline location="left"><bar-style>heavy-light</bar-style>'
            '<repeat direction="forward"/></barline>\n'
          +reh('E')+wr('Solos - E minor valse swing, repeat as needed'))
    if i==15:
        bl=('      <barline location="right"><bar-style>light-heavy</bar-style>'
            '<repeat direction="backward"/></barline>\n')
    out.append(slash_measure(n,{0:ch},3,extra=extra,newsys=(i%4==0),barline=bl)); n+=1

# link E minor -> G, then [F] shout chorus
out.append(slash_measure(n,{0:Am7},3,extra=wr('link - E minor to G'),newsys=True)); n+=1
out.append(slash_measure(n,{0:D7},3)); n+=1
for i in range(8):
    extra=''
    if i==0:
        extra=(attrs(slash='stop')+reh('F')
               +wr('Shout chorus - Nu ar det jul igen reprise, dig in')+FLAG)
    out.append(mel_measure(n,NU[i],NU_H[i],1,36,extra=extra,
               newsys=(i%4==0),shout=True)); n+=1

# [Tag]
tag=[([('B',4,12),('D',5,12),('G',4,3,1),('B',4,3),('D',5,3),('F',5,3,0)],{0:G6,2:Gdim}),
     ([('E',5,12),('C',5,12),('E',5,12,-1)],{0:C6,2:Cm6}),
     ([('C',5,12),('A',4,12),('F',4,12,1)],{0:Am7,2:D7}),
     ([('G',4,36)],{0:G6})]
for i,(bar,har) in enumerate(tag):
    extra=reh('Tag')+wr('Quintette tag - last time only') if i==0 else ''
    bl='      <barline location="right"><bar-style>light-heavy</bar-style></barline>\n' if i==3 else ''
    out.append(mel_measure(n,bar,har,1,36,extra=extra,newsys=(i==0),barline=bl,
               accent_first=True,fermata_last=(i==3))); n+=1

HEAD='''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <work><work-title>Swedish Lucia Dance Medley</work-title></work>
  <identification>
    <creator type="composer">Traditional Swedish</creator>
    <creator type="arranger">Hot Club medley in the style of Reinhardt and Grappelli</creator>
    <rights>Melodies traditional, public domain. Melodies transcribed from source scores supplied by the user. Harmony, form and arrangement are original.</rights>
    <encoding>
      <software>Manouche Lead Sheet Engraver</software>
      <encoding-date>2026-11-25</encoding-date>
      <supports element="accidental" type="yes"/>
      <supports attribute="new-system" element="print" type="yes" value="yes"/>
    </encoding>
  </identification>
  <defaults><scaling><millimeters>7.2</millimeters><tenths>40</tenths></scaling></defaults>
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
    HEAD+''.join(out)+'  </part>\n</score-partwise>\n')
print('measures written:',n-1)
