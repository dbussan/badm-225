# Original figures for Chapter 11 — Professionalism, Teamwork, and Meetings
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

# 1 — the five fundamentals
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
rows=[('RELIABILITY','deadlines met, promises kept — trust is built on boring consistency',GREEN),
      ('RESPONSIVENESS','acknowledge within a business day, even before the full answer',MOSS),
      ('POLISH','proofread everything — the typo tax is charged against competence',GREEN),
      ('COMPOSURE','never send angry; never match a hostile thread’s temperature',MOSS),
      ('DISCRETION','confidences stay confidences — gossip borrows against your own name',GREEN)]
y=3.2
for t,sub,c in rows:
    box(ax,0.4,y,2.9,0.58,t,fc=c,fs=9.6)
    ax.text(3.55,y+0.29,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.72
save(fig,'ch11_fundamentals.png')

# 2 — the trust account
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
ax.text(5.0,4.1,'THE TRUST ACCOUNT — deposits are small; withdrawals are always larger',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.3,4.3,2.3,'DEPOSITS\n\nkept promises · early warnings\ncredit passed down · specific thanks\nhonest yellows · loops closed',fc=TINT,tc=INK,fs=9.8)
box(ax,5.3,1.3,4.3,2.3,'WITHDRAWALS\n\nsurprises · spin · hoarded credit\nmissed deadlines gone quiet\n“they knew and didn’t tell us”',fc='#F7EAE8',tc=PROOF,fs=9.8)
box(ax,0.4,0.2,9.2,0.9,'High balance = cheap communication: two-line messages get believed.\nEmpty account = every message needs two pages of proof.',fc=GREEN,fs=9.6)
save(fig,'ch11_trust.png')

# 3 — idea conflict vs person conflict
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
ax.text(5.0,4.1,'TWO KINDS OF CONFLICT — grow the first, stop the second',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.2,4.3,2.4,'ABOUT THE IDEA\n\n“the timeline assumes zero vendor\ndelay — that’s the weak joint”\n\nspecific · checkable · aimed at work\nends in a better decision',fc=GREEN,fs=9.6)
box(ax,5.3,1.2,4.3,2.4,'ABOUT THE PERSON\n\n“you always lowball timelines”\n\ngeneral · unfalsifiable · aimed at character\nends in a winner, a loser,\nand a quieter team',fc='#F7EAE8',tc=PROOF,fs=9.6)
box(ax,0.4,0.25,9.2,0.65,'REPAIR: restate as behavior + impact — hard on the problem, soft on the person (Chapter 7’s SBI)',fc=TINT,tc=INK,fs=9.6)
save(fig,'ch11_conflict.png')

# 4 — four team failure modes
fig, ax = plt.subplots(figsize=(8.6,4.0)); ax.set_xlim(0,10); ax.set_ylim(0,4.6); ax.axis('off')
ax.text(5.0,4.3,'FOUR FAILURE MODES — each lives on ambiguity; each fix is daylight',ha='center',fontsize=11.5,color=GREEN,weight='bold')
cells=[(0.4,2.35,'THE FREELOADER','fix: tasks with names and\ndates, in writing'),
       (5.3,2.35,'THE CREDIT TAKER','fix: pass credit publicly and\nimmediately — patterns surface'),
       (0.4,0.5,'THE HIDDEN AGENDA','fix: name the topic; put it\nON the agenda'),
       (5.3,0.5,'THE DOMINATOR','fix: structured turns —\n“let’s hear from everyone”')]
for x,y,t,sub in cells:
    box(ax,x,y+0.75,4.3,0.62,t,fc=GREEN,fs=10.5)
    box(ax,x,y,4.3,0.68,sub,fc=TINT,tc=INK,fs=9.5)
save(fig,'ch11_failuremodes.png')

# 5 — the three-job meeting test
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
ax.text(5.0,3.7,'THE THREE-JOB TEST — meetings earn their cost on exactly three jobs',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,2.0,2.9,1.0,'DECISIONS\nchoices that need\nlive argument',fc=GREEN,fs=9.8)
box(ax,3.55,2.0,2.9,1.0,'CONFLICT\ndisagreement that\nneeds a room',fc=MOSS,fs=9.8)
box(ax,6.7,2.0,2.9,1.0,'CONNECTION\nthe humans behind\nthe usernames',fc=GREEN,fs=9.8)
box(ax,0.4,0.5,9.2,0.9,'None of the three? It’s a MESSAGE wearing a meeting costume.\n8 people × 1 hour × 50 weeks = 400 hours a year of reading aloud.',fc='#F7EAE8',tc=PROOF,fs=9.8)
save(fig,'ch11_meetingtest.png')

# 6 — anatomy of a working meeting
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
steps=[('PURPOSE','outcome named\nin the invite'),('AGENDA','items as outcomes\n+ owner + time box'),('THE ROOM','only the needed;\nnotes to the curious'),('THE RECORD','decisions + owners\n+ dates, within the hour'),('FOLLOW-THROUGH','actions tracked\nto done')]
x=0.3; w=1.78
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.7,w,0.95,t,fc=GREEN,fs=9.4)
    ax.text(x+w/2,1.25,sub,ha='center',va='center',fontsize=9.3,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.17,x+w+0.12,2.17)
    x+=w+0.12
box(ax,0.4,0.25,9.2,0.6,'The live skill in the middle — running the room — rests on written artifacts before and after.',fc=TINT,tc=INK,fs=9.6)
save(fig,'ch11_meeting.png')
print('ch11 figures complete')
