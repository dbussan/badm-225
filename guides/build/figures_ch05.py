# Original figures for Chapter 5 — Short Workplace Messages and Digital Media
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

GREEN='#0E4D33'; MOSS='#5C8A6E'; TINT='#EAF1EB'; GOLD='#8A6410'; INK='#212A26'; PROOF='#B23A31'
OUT = os.path.join(os.path.dirname(__file__), 'fig')
plt.rcParams.update({'font.family':'Calibri','font.size':11})

def save(fig,name):
    fig.savefig(os.path.join(OUT,name),dpi=160,bbox_inches='tight',facecolor='white'); plt.close(fig); print('fig:',name)
def box(ax,x,y,w,h,t,fc=GREEN,tc='white',fs=10.5):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.04',fc=fc,ec='none'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',color=tc,fontsize=fs)

# 1 — anatomy of a working email
fig, ax = plt.subplots(figsize=(8.6,4.6)); ax.set_xlim(0,10); ax.set_ylim(0,5.4); ax.axis('off')
rows=[('SUBJECT','“Approve Q3 budget rev by Fri 7/10” — the message’s job, searchable forever',GREEN),
      ('GREETING','“Hi Dana,” — match the relationship, not your mood',MOSS),
      ('SENTENCE 1','The main point. The ask. The news. HERE.',GREEN),
      ('BODY','Support in list or short paragraphs — one screen',MOSS),
      ('CALL TO ACTION','Specific act + date, standing alone at the end',GREEN),
      ('SIGNATURE','Name · title · org · phone — your professional letterhead',MOSS)]
y=4.6
for t,sub,c in rows:
    box(ax,0.4,y,2.4,0.62,t,fc=c,fs=10)
    ax.text(3.05,y+0.31,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.78
save(fig,'ch5_email.png')

# 2 — subject line formulas
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
rows=[('ACTION','verb + object + date','“Approve vendor list by Thu”'),
      ('INFO','topic + takeaway','“Server migration done — all normal”'),
      ('QUESTION','the actual question','“OK to move standup to 9:30?”'),
      ('THREAD RESCUE','new topic = new subject','“WAS: budget / NOW: hiring req”')]
y=3.3
for t,f,e in rows:
    box(ax,0.4,y,1.9,0.6,t,fc=GREEN,fs=10)
    ax.text(2.55,y+0.3,f,ha='left',va='center',fontsize=9.5,color=INK,style='italic')
    ax.text(5.6,y+0.3,e,ha='left',va='center',fontsize=9.5,color=GOLD)
    y-=0.82
ax.text(5.0,3.85,'Subject lines: the five words that decide whether the rest get read',ha='center',fontsize=11,color=GREEN,weight='bold')
save(fig,'ch5_subject.png')

# 3 — channel etiquette matrix
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
cols=['EMAIL','CHAT / TEAMS','TEXT / SMS']
props=[('Response window','~1 business day','minutes–hours','minutes (urgent only)'),
       ('Formality','professional letter-lite','conversational','brief, personal'),
       ('Best for','records, decisions,\nexternal, multi-point','quick questions,\ncoordination','time-critical logistics'),
       ('Never for','instant needs','decisions needing records','anything confidential\nor complex')]
for j,c in enumerate(cols):
    box(ax,2.4+j*2.55,3.7,2.35,0.55,c,fc=GREEN,fs=10)
y=3.0
for label,a,b,c in props:
    box(ax,0.3,y,1.95,0.6,label,fc=MOSS,fs=9)
    for j,v in enumerate([a,b,c]):
        box(ax,2.4+j*2.55,y,2.35,0.6,v,fc=TINT,tc=INK,fs=9.3)
    y-=0.72
save(fig,'ch5_channels.png')

# 4 — thread hygiene
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
rules=[('Reply vs Reply-All','Reply-all only when every name\nneeds every word'),
       ('New topic = new thread','Don’t bury a hiring decision\nin “RE: RE: FW: lunch”'),
       ('CC = FYI, To = action','People in To act;\npeople in CC are informed'),
       ('BCC = exit ramp','Moving someone off a thread?\n“Moving Dana to BCC with thanks”')]
for j,(t,sub) in enumerate(rules):
    box(ax,0.3+j*2.45,1.9,2.2,1.1,t,fc=GREEN if j%2==0 else MOSS,fs=9.5)
    ax.text(0.3+j*2.45+1.1,1.7,sub,ha='center',va='top',fontsize=9.3,color=INK)
ax.text(5.0,3.35,'Thread hygiene: the etiquette that keeps inboxes navigable',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch5_threads.png')

# 5 — the permanence gradient
fig, ax = plt.subplots(figsize=(8.6,2.8)); ax.set_xlim(0,10); ax.set_ylim(0,3.2); ax.axis('off')
ax.add_patch(Rectangle((0.4,1.4),9.2,0.7,fc=TINT,ec=INK,lw=1))
ax.add_patch(Rectangle((0.4,1.4),6.2,0.7,fc=MOSS,ec='none'))
ax.add_patch(Rectangle((0.4,1.4),3.0,0.7,fc=GREEN,ec='none'))
for x,t in [(1.9,'EMAIL & DOCS\ndiscoverable, archived'),(5.0,'CHAT / TEAMS\nlogged & exportable'),(8.3,'“DISAPPEARING”\nscreenshots never do')]:
    ax.text(x,1.75,t,ha='center',va='center',color='white' if x<7 else INK,fontsize=9,weight='bold')
ax.text(5.0,2.75,'The permanence gradient: write everything as if legal will read it — because legal can',ha='center',fontsize=11,color=GREEN,weight='bold')
ax.text(5.0,0.9,'Workplace systems are employer property: assume logging, retention, and discovery on all of them.',ha='center',fontsize=9.5,color=INK,style='italic')
save(fig,'ch5_permanence.png')

# 6 — response-time expectations
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
rows=[('Client / external email','same business day acknowledgment, even if “full answer Friday”'),
      ('Manager’s direct question','hours, not days — silence reads as avoidance'),
      ('Team chat @mention','within the working session'),
      ('FYI / CC traffic','no reply owed — that’s what CC means'),
      ('After-hours anything','next business day, unless your role says otherwise — protect the norm')]
y=2.8
for t,sub in rows:
    box(ax,0.4,y,3.1,0.52,t,fc=GREEN,fs=9)
    ax.text(3.7,y+0.26,sub,ha='left',va='center',fontsize=9.3,color=INK)
    y-=0.62
save(fig,'ch5_response.png')

# 7 — professional presence pyramid
fig, ax = plt.subplots(figsize=(7.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
tiers=[(2.9,3.2,4.2,0.75,'PUBLIC POSTS\nassume permanent, employer-visible',PROOF,'white'),
       (2.4,2.3,5.2,0.75,'WORK PLATFORMS\nemployer property — logged, exportable',GREEN,'white'),
       (1.4,1.4,7.2,0.75,'PROFESSIONAL PROFILES (LinkedIn etc.)\nyour standing portfolio — curate it',MOSS,'white'),
       (0.4,0.5,9.2,0.75,'PRIVATE CHANNELS\nstill one screenshot from public',TINT,INK)]
for x,y,w,h,t,fc,tc in tiers:
    box(ax,x,y,w,h,t,fc=fc,tc=tc,fs=9.5)
save(fig,'ch5_presence.png')
print('ch5 figures complete')
