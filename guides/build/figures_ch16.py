# Original figures for Chapter 16 — Leadership Under Pressure & Influence
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

GREEN='#0E4D33'; MOSS='#5C8A6E'; TINT='#EAF1EB'; GOLD='#8A6410'; INK='#212A26'; PROOF='#B23A31'
OUT = os.path.join(os.path.dirname(__file__), 'fig')
plt.rcParams.update({'font.family':'Calibri','font.size':11})
FS_FLOOR=9.3  # never go below this — matplotlib+Calibri drops glyphs under ~8.8pt

def save(fig,name):
    fig.savefig(os.path.join(OUT,name),dpi=160,bbox_inches='tight',facecolor='white'); plt.close(fig); print('fig:',name)
def box(ax,x,y,w,h,t,fc=GREEN,tc='white',fs=10.5):
    assert fs>=FS_FLOOR, f'font {fs} below floor'
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.04',fc=fc,ec='none'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',color=tc,fontsize=fs)
def arr(ax,x1,y1,x2,y2,c=INK):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=15,color=c,lw=1.7))

# 1 — the pressure protocol
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
ax.text(5.0,3.3,'THE PRESSURE PROTOCOL — four beats, thirty seconds',ha='center',fontsize=11.5,color=GREEN,weight='bold')
steps=[('PAUSE','two breaths before\nany reply'),('FACTS','known vs. assumed —\nwrite both lists'),('FRAME','their stakes,\nnot yours'),('FORWARD','the next concrete\naction, owned + timed')]
x=0.4; w=2.2
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.6,w,1.05,t,fc=GREEN,fs=9.8)
    ax.text(x+w/2,1.05,sub,ha='center',va='center',fontsize=9.4,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.12,x+w+0.13,2.12)
    x+=w+0.13
box(ax,0.4,0.2,9.2,0.55,'Survives every crisis size — from a hot email to a plant shutdown.',fc=TINT,tc=INK,fs=9.6)
save(fig,'ch16_protocol.png')

# 2 — the first hour
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
ax.text(5.0,3.9,'THE FIRST HOUR OF A CRISIS',ha='center',fontsize=11.5,color=GREEN,weight='bold')
rows=[('ACKNOWLEDGE','to your own people first — silence reads as concealment',GREEN),
      ('ASSIGN','three hats: comms, the fix, the log — ideally three heads',MOSS),
      ('PROMISE THE CADENCE','“updates at 10, 2, and 5” — whether anything changed or not',GREEN),
      ('FEED THE GRAPEVINE FACTS','outrun the informal network with official truth',MOSS)]
y=3.3
for t,sub,c in rows:
    box(ax,0.4,y,2.9,0.6,t,fc=c,fs=9.5)
    ax.text(3.55,y+0.3,sub,ha='left',va='center',fontsize=9.4,color=INK)
    y-=0.75
save(fig,'ch16_firsthour.png')

# 3 — Carnegie core
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
ax.text(5.0,4.1,'THE CARNEGIE CORE — attributed to How to Win Friends (1936)',ha='center',fontsize=11,color=GREEN,weight='bold')
rows=[('DON’T CRITICIZE, CONDEMN, COMPLAIN','triggers defense, not change — diagnose systems, correct behavior',GREEN),
      ('GIVE HONEST, SINCERE APPRECIATION','the five-S goodwill note IS this principle, stamped',MOSS),
      ('AROUSE AN EAGER WANT','frame every ask in THEIR interests',GREEN),
      ('BECOME GENUINELY INTERESTED IN PEOPLE','outperforms trying to be interesting, everywhere',MOSS)]
y=3.4
for t,sub,c in rows:
    box(ax,0.4,y,4.1,0.62,t,fc=c,fs=9.3)
    ax.text(4.75,y+0.31,sub,ha='left',va='center',fontsize=9.3,color=INK)
    y-=0.78
save(fig,'ch16_carnegie.png')

# 4 — correcting without crushing
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
ax.text(5.0,3.7,'CORRECTING WITHOUT CRUSHING',ha='center',fontsize=11.5,color=GREEN,weight='bold')
steps=[('HONEST PRAISE\nFIRST','real, specific —\nthe foundation'),('THE BEHAVIOR,\nINDIRECTLY','“I’ve made this\nmistake too”'),('QUESTIONS,\nNOT ORDERS','“what would\nprevent this?”'),('SAVE FACE','private correction,\npublic dignity')]
x=0.3; w=2.28
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.6,w,1.1,t,fc=GREEN,fs=9.3)
    ax.text(x+w/2,1.1,sub,ha='center',va='center',fontsize=9.3,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.15,x+w+0.1,2.15)
    x+=w+0.1
box(ax,0.4,0.3,9.2,0.55,'Goal: changed behavior AND an intact contributor — either alone is failure.',fc=TINT,tc=INK,fs=9.5)
save(fig,'ch16_correcting.png')

# 5 — reputation to live up to
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
ax.text(5.0,3.3,'GIVE THEM A REPUTATION TO LIVE UP TO',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.6,4.3,1.2,'“You’re the most careful\nreviewer on this team.”\n\nMust be true at least\nin trajectory.',fc=GREEN,fs=9.6)
box(ax,5.3,1.6,4.3,1.2,'The person defends that\nreputation with behavior.\n\nSpoken standards become\nidentity — identity self-enforces.',fc=MOSS,fs=9.4)
box(ax,0.4,0.35,9.2,0.9,'Corrects harder than any reprimand, and hurts better: “this slipped, which surprised me —\nyour work is usually the standard.”',fc=TINT,tc=INK,fs=9.4)
save(fig,'ch16_reputation.png')
print('ch16 figures complete')
