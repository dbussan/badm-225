# Original figures for Chapter 12 — Business Presentations
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

GREEN='#0E4D33'; MOSS='#5C8A6E'; TINT='#EAF1EB'; GOLD='#8A6410'; INK='#212A26'; PROOF='#B23A31'
OUT = os.path.join(os.path.dirname(__file__), 'fig')
plt.rcParams.update({'font.family':'Calibri','font.size':11})

def save(fig,name):
    fig.savefig(os.path.join(OUT,name),dpi=160,bbox_inches='tight',facecolor='white'); plt.close(fig); print('fig:',name)
def box(ax,x,y,w,h,t,fc=GREEN,tc='white',fs=10.5):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.04',fc=fc,ec='none'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',color=tc,fontsize=fs)
def arr(ax,x1,y1,x2,y2,c=INK):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=15,color=c,lw=1.7))

# 1 — build order
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
ax.text(5.0,3.3,'BUILD THE TALK IN THIS ORDER — slides come LAST',ha='center',fontsize=11.5,color=GREEN,weight='bold')
steps=[('TAKEAWAY','the one repeatable\nsentence — first'),('THREE POINTS','the MECE reasons\nthat carry it'),('EVIDENCE','number · story ·\ndemonstration'),('OPEN + CLOSE','built once you know\nwhat they frame'),('SLIDES','the visual aid to a\ntalk that exists')]
x=0.3; w=1.78
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.6,w,0.9,t,fc=GREEN if si!=4 else GOLD,fs=9.4)
    ax.text(x+w/2,1.12,sub,ha='center',va='center',fontsize=9.3,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.05,x+w+0.12,2.05)
    x+=w+0.12
box(ax,0.4,0.15,9.2,0.6,'A talk built by opening the slide tool first becomes a tour of slides — structure by template, not by thought.',fc=TINT,tc=INK,fs=9.6)
save(fig,'ch12_buildorder.png')

# 2 — talk frame: open/roadmap/body/close
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
rows=[('THE HOOK','their stakes in sentence one — a number, a story, a question. Never an apology.',GREEN),
      ('THE ROADMAP','“cost, fix, decision” — three stops, named; the pyramid’s second layer, read aloud',MOSS),
      ('THE BODY','three points, each proven — number, story, or demonstration in rotation',GREEN),
      ('Q&A','questions taken BEFORE the close — never let a tangent be the last word',MOSS),
      ('THE CLOSE','the echo (takeaway, again) + the ask (concrete, dated). “Thank you” is not a closing.',GREEN)]
y=3.5
for t,sub,c in rows:
    box(ax,0.4,y,2.4,0.6,t,fc=c,fs=9.8)
    ax.text(3.05,y+0.3,sub,ha='left',va='center',fontsize=9.4,color=INK)
    y-=0.75
save(fig,'ch12_frame.png')

# 3 — billboard vs document slide
fig, ax = plt.subplots(figsize=(8.6,4.0)); ax.set_xlim(0,10); ax.set_ylim(0,4.6); ax.axis('off')
ax.text(5.0,4.3,'BILLBOARD OR DOCUMENT? — one deck cannot do both jobs',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.15,4.3,2.75,'THE PRESENTATION DECK\n\none point per slide\nreadable in three seconds\nbig type · visuals ARE the point\nmeaningless without the speaker\n(by design)',fc=GREEN,fs=9.8)
box(ax,5.3,1.15,4.3,2.75,'THE LEAVE-BEHIND\n\nsections + takeaway titles\nfull evidence, readable alone\nbuilt for the forward,\nthe absent, the archive\nsent AFTER the talk',fc=MOSS,fs=9.8)
box(ax,0.4,0.2,9.2,0.6,'Announce it up front — “a full copy comes to you after” — and buy back every eye in the room.',fc=TINT,tc=INK,fs=9.6)
save(fig,'ch12_billboard.png')

# 4 — the voice toolbox
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
rows=[('PACE','aim slower than natural — what feels sluggish inside sounds composed outside',GREEN),
      ('THE PAUSE','two silent seconds after a big point = a spotlight; “um” spends it',MOSS),
      ('VOLUME','speak to the back row’s chair; variation is emphasis, monotone is a lullaby',GREEN),
      ('INFLECTION','downward endings state; uptalk turns findings into questions — don’t',MOSS)]
y=3.2
for t,sub,c in rows:
    box(ax,0.4,y,2.4,0.62,t,fc=c,fs=10)
    ax.text(3.05,y+0.31,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.78
save(fig,'ch12_voice.png')

# 5 — rehearsal passes
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
ax.text(5.0,3.1,'THREE PASSES, ALL ALOUD — reading silently rehearses nothing',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.5,2.9,1.1,'PASS 1 · SHAPE\ntalk it through rough;\nfind the sticking joints',fc=GREEN,fs=9.6)
box(ax,3.55,1.5,2.9,1.1,'PASS 2 · TIME\ncut to 90% of the slot;\nQ&A eats the margin',fc=MOSS,fs=9.6)
box(ax,6.7,1.5,2.9,1.1,'PASS 3 · SIMULATE\nstanding, timed, recorded;\nreview once, kindly',fc=GREEN,fs=9.6)
arr(ax,3.3,2.05,3.55,2.05); arr(ax,6.45,2.05,6.7,2.05)
box(ax,0.4,0.3,9.2,0.75,'Memorize only the joints: the first minute, the transitions, the close.\nThe middles stay conversational, from bullets.',fc=TINT,tc=INK,fs=9.6)
save(fig,'ch12_rehearsal.png')

# 6 — Q&A protocol
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
steps=[('RESTATE','the room hears it;\nyou buy five seconds'),('ANSWER','briefly — then STOP;\nno three-minute tours'),('BRIDGE','stray questions return\nto the takeaway'),('COMMIT','stumped? own it +\ndeliver by a date')]
x=0.4; w=2.2
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.7,w,0.9,t,fc=GREEN,fs=9.8)
    ax.text(x+w/2,1.22,sub,ha='center',va='center',fontsize=9.3,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.15,x+w+0.13,2.15)
    x+=w+0.13
box(ax,0.4,0.25,9.2,0.6,'Prepare the five questions you’d ask if you wanted to sink this talk. You already know what they are.',fc='#F7EAE8',tc=PROOF,fs=9.6)
save(fig,'ch12_qa.png')
print('ch12 figures complete')
