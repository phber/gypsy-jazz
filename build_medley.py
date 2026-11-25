"""Swedish Lucia dance medley v3 - simple.

Harmony is plain triads plus dominant 7ths only: no sixths on tonics, no
dim7, no half-diminished, no altered dominants. Melodies run long - the full
form of each tune straight out of the user's source files.
"""
import sys
sys.path.insert(0,'/tmp/claude-0/-home-user-gypsy-jazz/6c085e37-0341-50ff-b193-5c1685285cce/scratchpad/tools')
from extract_lib import melody
SRC='/tmp/claude-0/-home-user-gypsy-jazz/6c085e37-0341-50ff-b193-5c1685285cce/scratchpad/mxl/'
DIV=12
TYPE={3:'16th',6:'eighth',9:'eighth',12:'quarter',18:'quarter',24:'half',36:'half',48:'whole'}
DOTTED={9,18,36}
ACCN={1:'sharp',-1:'flat',0:'natural'}
SH=['F','C','G','D','A','E','B']; FL=['B','E','A','D','G','C','F']
def ka(f):
    d={}
    if f>0:
        for s in SH[:f]: d[s]=1
    else:
        for s in FL[:-f]: d[s]=-1
    return d

# ---- the ONLY three chord types used: triad major, triad minor, dominant 7
def CH(root, kind):
    text,k = {'M':('','major'),'m':('m','minor'),'7':('7','dominant')}[kind]
    return ('      <harmony print-frame="no"><root><root-step>%s</root-step></root>'
            '<kind text="%s">%s</kind></harmony>\n'%(root,text,k))
G=CH('G','M'); C=CH('C','M'); D7=CH('D','7'); G7=CH('G','7')
Em=CH('E','m'); B7=CH('B','7'); Am=CH('A','m')

SLASH=('      <note><pitch><step>B</step><alter>0</alter><octave>4</octave></pitch>'
       '<duration>12</duration><voice>1</voice><type>quarter</type></note>\n')

def note(ev,fifths,accent=False,slur=None,fermata=False):
    if ev[0]=='r':
        return ('      <note><rest/><duration>%d</duration><voice>1</voice><type>%s</type>%s</note>\n'
                %(ev[2],TYPE[ev[2]],'<dot/>' if ev[2] in DOTTED else ''))
    step,octv,dur=ev[0],ev[1],ev[2]
    alter=ev[3] if len(ev)>3 else 0
    need=alter!=ka(fifths).get(step,0)
    s='      <note><pitch><step>%s</step>'%step
    if alter or need: s+='<alter>%d</alter>'%alter
    s+='<octave>%d</octave></pitch><duration>%d</duration><voice>1</voice>'%(octv,dur)
    s+='<type>%s</type>'%TYPE[dur]
    if dur in DOTTED: s+='<dot/>'
    if need: s+='<accidental>%s</accidental>'%ACCN[alter]
    inner=''
    if slur: inner+='<slur type="%s" number="1"/>'%slur
    if accent: inner+='<articulations><accent/></articulations>'
    if fermata: inner+='<fermata type="upright"/>'
    if inner: s+='<notations>%s</notations>'%inner
    return s+'</note>\n'

def attrs(fifths=None,mode='major',beats=None,slash=None,first=False):
    if fifths is None and beats is None and slash is None and not first: return ''
    s='      <attributes>\n'
    if first: s+='        <divisions>%d</divisions>\n'%DIV
    if fifths is not None: s+='        <key><fifths>%d</fifths><mode>%s</mode></key>\n'%(fifths,mode)
    if beats is not None: s+='        <time><beats>%d</beats><beat-type>4</beat-type></time>\n'%beats
    if first: s+='        <clef><sign>G</sign><line>2</line></clef>\n'
    if slash: s+=('        <measure-style><slash type="%s"%s/></measure-style>\n'
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

def mel(num,bar,harms,fifths,barlen,extra='',newsys=False,barline='',
        accent_first=False,fermata_last=False):
    s='    <measure number="%d">\n'%num
    if newsys: s+='      <print new-system="yes"/>\n'
    s+=extra
    off=0; marks=slur_plan(bar)
    for i,ev in enumerate(bar):
        if off%DIV==0 and (off//DIV) in harms: s+=harms[off//DIV]
        s+=note(ev,fifths,accent=(i==0 and accent_first),slur=marks[i],
                fermata=(fermata_last and i==len(bar)-1))
        off+=ev[2]
    assert off==barlen,'bar %d = %d, want %d'%(num,off,barlen)
    return s+barline+'    </measure>\n'

def sl(num,harms,beats,extra='',newsys=False,barline=''):
    s='    <measure number="%d">\n'%num
    if newsys: s+='      <print new-system="yes"/>\n'
    s+=extra
    for b in range(beats):
        if b in harms: s+=harms[b]
        s+=SLASH
    return s+barline+'    </measure>\n'

# ------------------------------------------------- melodies, full forms
nu,_,_,_ =melody(SRC+'t5/score.xml','P1')
rav,_,_,_=melody(SRC+'t4/score.xml','P1')
hej,_,_,_=melody(SRC+'t2/score.xml','P1')
stf,_,_,_=melody(SRC+'t1/lg-170673187.xml','P1')

NU = nu[0:16]                      # both 8-bar passes = 16 bars
# Raven: the source splits bar 8 into 30 units + a 6-unit pickup bar. Merge
# them back into one 36-unit bar, which keeps the pickup instead of dropping it.
RAV = rav[0:7] + [rav[7]+rav[8]] + rav[9:17]       # 16 bars
HEJ = hej[0:16]                    # full AABA
STF = stf[0:14]                    # full tune

NU_H  = [{0:G},{0:G},{0:G},{0:D7},{0:C},{0:G},{0:D7},{0:G}]*2
RAV_H = [{0:C},{0:C},{0:C},{0:G7}, {0:C},{0:C},{0:G7},{0:G7},
         {0:C},{0:G7},{0:G7},{0:C}, {0:C},{0:C},{0:G7},{0:C}]
HEJ_H = [{0:C},{0:C},{0:G7},{0:C}, {0:C},{0:C},{0:G7},{0:C},
         {0:C},{0:C},{0:C},{0:G7}, {0:C},{0:C},{0:G7},{0:C}]
STF_H = [{0:Em},{0:Em},{0:Em},{0:B7}, {0:B7},{0:B7},{0:Em},{0:B7},
         {0:Em},{0:Em},{0:Am},{0:Em}, {0:B7},{0:Em}]

# ------------------------------------------------- assembly (90 bars)
out=[]; n=1
# [Intro] 4 pompe bars in G
for i,h in enumerate([{0:G},{0:G},{0:D7},{0:D7}]):
    extra=''
    if i==0:
        extra=(attrs(fifths=1,mode='major',beats=3,slash='start',first=True)+reh('Intro')
          +'      <direction placement="above">\n        <direction-type>'
            '<metronome parentheses="no"><beat-unit>quarter</beat-unit>'
            '<per-minute>180</per-minute></metronome></direction-type>\n'
            '        <sound tempo="180"/>\n      </direction>\n'
          +wr('Swedish Lucia dance medley - Hot Club swing, la pompe. '
              'Quarter note constant throughout.'))
    out.append(sl(n,h,3,extra=extra,newsys=(i==0))); n+=1

def section(mark,title,m,h,fifths,mode,beats,barlen,stop_slash,cur):
    global n
    res=[]
    for i in range(len(m)):
        extra=''
        if i==0:
            kf = fifths if fifths!=cur[0] else None
            bt = beats  if beats !=cur[1] else None
            cur[0],cur[1]=fifths,beats
            extra=(attrs(fifths=kf,mode=mode,beats=bt,
                         slash='stop' if stop_slash else None)
                   +reh(mark)+wr(title))
        res.append(mel(n,m[i],h[i],fifths,barlen,extra=extra,
                   newsys=(i%4==0),accent_first=(i%4==0))); n+=1
    return res

cur=[1,3]
out+=section('A','Nu ar det jul igen',NU,NU_H,1,'major',3,36,True,cur)
# link G -> C
out.append(sl(n,{0:G},3,extra=attrs(slash='start')+wr('link'),newsys=True)); n+=1
out.append(sl(n,{0:G7},3)); n+=1
out+=section('B','Raven raskar over isen',RAV,RAV_H,0,'major',3,36,True,cur)
out+=section('C','Hej tomtegubbar',HEJ,HEJ_H,0,'major',3,36,False,cur)
# link C -> E minor
out.append(sl(n,{0:Am},3,extra=attrs(slash='start')+wr('link'),newsys=True)); n+=1
out.append(sl(n,{0:B7},3)); n+=1
out+=section('D','Staffan var en stalledrang',STF,STF_H,1,'minor',2,24,True,cur)

# [E] solo chorus, stays in E minor 2/4
solo=[Em,Em,Em,Em, B7,B7,Em,Em, Em,Em,Am,Am, B7,B7,Em,Em]
for i,ch in enumerate(solo):
    extra,bl='',''
    if i==0:
        extra=(attrs(slash='start')
          +'      <barline location="left"><bar-style>heavy-light</bar-style>'
            '<repeat direction="forward"/></barline>\n'
          +reh('E')+wr('Solos - E minor, repeat as needed'))
    if i==15:
        bl=('      <barline location="right"><bar-style>light-heavy</bar-style>'
            '<repeat direction="backward"/></barline>\n')
    out.append(sl(n,{0:ch},2,extra=extra,newsys=(i%4==0),barline=bl)); n+=1

# [Tag] 4 bars, E minor 2/4
tag=[([('B',4,6),('G',4,6),('E',4,12)],{0:Em}),
     ([('F',4,12,1),('D',4,12,1)],{0:B7}),
     ([('E',4,6),('G',4,6),('B',4,12)],{0:Em}),
     ([('E',4,24)],{0:Em})]
for i,(bar,h) in enumerate(tag):
    extra=attrs(slash='stop')+reh('Tag')+wr('Tag - last time only') if i==0 else ''
    bl='      <barline location="right"><bar-style>light-heavy</bar-style></barline>\n' if i==3 else ''
    out.append(mel(n,bar,h,1,24,extra=extra,newsys=(i==0),barline=bl,
               accent_first=True,fermata_last=(i==3))); n+=1

HEAD='''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 4.0 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="4.0">
  <work><work-title>Swedish Lucia Dance Medley</work-title></work>
  <identification>
    <creator type="composer">Traditional Swedish</creator>
    <creator type="arranger">Hot Club medley in the style of Reinhardt and Grappelli</creator>
    <rights>Melodies traditional, public domain, transcribed from source scores supplied by the user. Harmony and form are original.</rights>
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
print('measures:',n-1)
