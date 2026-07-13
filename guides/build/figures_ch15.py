# Original figures for Chapter 15 — AI, Agents & Professional Communication
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

# 1 — floor vs ceiling
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
ax.text(5.0,3.9,'THE FLOOR ROSE. THE CEILING DIDN’T MOVE.',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.2,4.3,2.3,'THE FLOOR\n\ncompetent prose,\nnearly free\n\nrouting drafting is\nno longer a\ndifferentiator',fc=MOSS,fs=9.8)
box(ax,5.3,1.2,4.3,2.3,'THE CEILING\n\nknowing what’s true,\nwhat matters, what\nthe moment requires\n\nexactly where\nit always was',fc=GREEN,fs=9.8)
box(ax,0.4,0.25,9.2,0.65,'Use the tools fully. Verify ruthlessly. Invest in the ceiling.',fc=TINT,tc=INK,fs=9.8)
save(fig,'ch15_floorceiling.png')

# 2 — capability map
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
ax.text(5.0,4.1,'WHAT IT’S GREAT AT / WHERE IT FAILS',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.1,4.3,2.6,'GREAT AT (use freely)\n\nfirst drafts of routine genres\nrewriting & tone shifts\ncritique on demand\nbrainstorming options\nsingle-error sweeps',fc=GREEN,fs=9.6)
box(ax,5.3,1.1,4.3,2.6,'FAILS AT (verify or avoid)\n\nfacts, numbers, names\ncitations that don’t exist\nanything after training data ends\nyour specific context\njudgment calls',fc='#F7EAE8',tc=PROOF,fs=9.6)
box(ax,0.4,0.2,9.2,0.65,'Both columns follow from one mechanism: it predicts plausible next words. Fluency is the product; truth is incidental.',fc=TINT,tc=INK,fs=9.4)
save(fig,'ch15_capability.png')

# 3 — verification pipeline
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
ax.text(5.0,3.3,'THE VERIFICATION PIPELINE — runs on every AI draft',ha='center',fontsize=11.5,color=GREEN,weight='bold')
steps=[('FLAG','mark every load-bearing\nclaim: facts, numbers,\nnames, citations'),('TRACE','each one to a real\nsource you can open'),('FIX','correct, source, or\ndelete — no third option'),('OWN','ship it as yours —\nbecause now it is')]
x=0.4; w=2.2
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.6,w,1.05,t,fc=GREEN,fs=9.8)
    ax.text(x+w/2,1.05,sub,ha='center',va='center',fontsize=8.8,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.12,x+w+0.13,2.12)
    x+=w+0.13
box(ax,0.4,0.2,9.2,0.55,'The more precise an unverified AI claim, the more suspicious it should be.',fc='#F7EAE8',tc=PROOF,fs=9.4)
save(fig,'ch15_pipeline.png')

# 4 — never-delegate list
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
ax.text(5.0,3.7,'WHAT NOT TO DELEGATE — EVER',ha='center',fontsize=11.5,color=GREEN,weight='bold')
rows=[('GOODWILL MESSAGES','thanks, congratulations, condolences — the pause IS the message',GREEN),
      ('APOLOGIES','ownership ghostwritten is ownership faked',MOSS),
      ('PERFORMANCE FEEDBACK','SBI requires having SEEN the behavior',GREEN)]
y=3.0
for t,sub,c in rows:
    box(ax,0.4,y,3.1,0.58,t,fc=c,fs=9.6)
    ax.text(3.75,y+0.29,sub,ha='left',va='center',fontsize=9.4,color=INK)
    y-=0.72
box(ax,0.4,0.55,9.2,0.55,'The common thread: wherever the message IS the relationship, the drafting IS the sincerity.',fc=TINT,tc=INK,fs=9.4)
save(fig,'ch15_neverdelegate.png')

# 5 — agent mandate
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
ax.text(5.0,3.7,'DELEGATING TO AGENTS WITHOUT ABDICATING',ha='center',fontsize=11.5,color=GREEN,weight='bold')
rows=[('SCOPE IN WRITING','what it may do, must ask about, must never touch',GREEN),
      ('GATE THE IRREVERSIBLE','sending, deleting, purchasing get human review',MOSS),
      ('START NARROW','widen scope with evidence — a trust ladder for tools',GREEN),
      ('AUDIT ON CADENCE','spot-check what it did, not just what it reported',MOSS)]
y=3.0
for t,sub,c in rows:
    box(ax,0.4,y,3.1,0.58,t,fc=c,fs=9.4)
    ax.text(3.75,y+0.29,sub,ha='left',va='center',fontsize=9.3,color=INK)
    y-=0.72
save(fig,'ch15_agentmandate.png')

# 6 — appreciation portfolio
fig, ax = plt.subplots(figsize=(9.6,4.0)); ax.set_xlim(0,10); ax.set_ylim(0,4.6); ax.axis('off')
ax.text(5.0,4.3,'SKILLS THAT APPRECIATE AS DRAFTING GETS FREE',ha='center',fontsize=11.5,color=GREEN,weight='bold')
cells=[('JUDGMENT','what’s true,\nwhat matters'),('VERIFICATION','source\ndiscipline'),('THE BRIEF','specifying\nwork precisely'),
       ('RELATIONSHIPS','trust, presence,\nthe room'),('EDITING','B-minus draft\n→ your A')]
x0=0.25
w=1.86
for i,(t,sub) in enumerate(cells):
    box(ax,x0+i*(w+0.08),1.5,w,1.7,t+'\n\n'+sub,fc=GREEN if i%2==0 else MOSS,fs=9.4)
save(fig,'ch15_appreciation.png')
print('ch15 figures complete')
