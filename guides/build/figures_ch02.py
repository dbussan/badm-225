# Original figures for Chapter 2 — Planning Business Messages
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle

GREEN='#0E4D33'; MOSS='#5C8A6E'; TINT='#EAF1EB'; GOLD='#8A6410'; INK='#212A26'; PROOF='#B23A31'
OUT = os.path.join(os.path.dirname(__file__), 'fig')
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'font.family':'Calibri','font.size':11})

def save(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=160, bbox_inches='tight', facecolor='white')
    plt.close(fig); print('fig:', name)

def box(ax,x,y,w,h,t,fc=GREEN,tc='white',fs=10.5):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.04',fc=fc,ec='none'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',color=tc,fontsize=fs)

def arr(ax,x1,y1,x2,y2,c=INK,two=False):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='<|-|>' if two else '-|>',mutation_scale=15,color=c,lw=1.7))

# 1 — writing process phases
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
phases=[('PLAN','Purpose · audience ·\nbenefit · channel',4.4,GREEN),('DRAFT','Get it down,\nnot perfect',2.4,MOSS),('REVISE','Reader’s eyes ·\npolish · proof',2.6,GREEN)]
x=0.3
for name,sub,w,c in phases:
    box(ax,x,1.5,w,1.1,name,fc=c,fs=13)
    ax.text(x+w/2,1.28,sub,ha='center',va='top',fontsize=9.5,color=INK)
    x+=w+0.15
ax.text(5.0,3.1,'Where professionals spend the effort — planning is half the work',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch2_process.png')

# 2 — purpose statement anatomy
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
box(ax,0.3,2.0,3.0,1.0,'WHO must act?\n(the reader)',fc=GREEN)
box(ax,3.5,2.0,3.0,1.0,'WHAT exactly\nshould they do?',fc=MOSS)
box(ax,6.7,2.0,3.0,1.0,'WHY would\nthey want to?',fc=GREEN)
arr(ax,1.8,1.9,4.4,1.15); arr(ax,5.0,1.9,5.0,1.2); arr(ax,8.2,1.9,5.7,1.15)
box(ax,1.4,0.35,7.2,0.8,'“So that the director (who) approves the $2,400 license (what)\nbecause it saves six staff-hours weekly (why).”',fc=TINT,tc=INK,fs=10)
save(fig,'ch2_purpose.png')

# 3 — audience rings
fig, ax = plt.subplots(figsize=(7.0,4.6)); ax.set_xlim(0,10); ax.set_ylim(0,7); ax.axis('off'); ax.set_aspect('equal')
for r,c,a in [(3.3,'#DFE9E2',1),(2.4,'#BDD4C4',1),(1.5,MOSS,1),(0.75,GREEN,1)]:
    ax.add_patch(Circle((5,3.4),r,fc=c,ec='white',lw=2))
ax.text(5,3.4,'PRIMARY\nacts on it',ha='center',va='center',color='white',fontsize=9.5,weight='bold')
ax.text(5,5.1,'SECONDARY — will read it later (the forward, the file)',ha='center',fontsize=9.5,color=INK)
ax.text(5,5.95,'GATEKEEPERS — decide whether it reaches the primary reader',ha='center',fontsize=9.5,color=INK)
ax.text(5,6.7,'HIDDEN — legal, HR, competitors, the public record',ha='center',fontsize=9.5,color=INK)
ax.annotate('',xy=(5,4.05),xytext=(5,4.85),arrowprops=dict(arrowstyle='-|>',color=INK))
ax.annotate('',xy=(5,4.95),xytext=(5,5.75),arrowprops=dict(arrowstyle='-|>',color=INK))
ax.annotate('',xy=(5,5.85),xytext=(5,6.5),arrowprops=dict(arrowstyle='-|>',color=INK))
save(fig,'ch2_audience.png')

# 4 — you-view transformation
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
box(ax,0.3,2.2,4.5,1.4,'WRITER-VIEW (I/we)\n“We are pleased to announce\nour new evening hours.”',fc='#F1E9E7',tc=INK,fs=10)
box(ax,5.2,2.2,4.5,1.4,'YOU-VIEW\n“You can now shop\nweeknights until 9 p.m.”',fc=GREEN,fs=10)
arr(ax,4.85,2.9,5.15,2.9,c=GOLD)
box(ax,0.3,0.4,4.5,1.2,'“I have approved your request.”',fc='#F1E9E7',tc=INK,fs=10)
box(ax,5.2,0.4,4.5,1.2,'“Your request is approved —\nyour new hours begin Monday.”',fc=GREEN,fs=10)
arr(ax,4.85,1.0,5.15,1.0,c=GOLD)
save(fig,'ch2_youview.png')

# 5 — tone dial
fig, ax = plt.subplots(figsize=(8.6,2.6)); ax.set_xlim(0,10); ax.set_ylim(0,3); ax.axis('off')
ax.add_patch(Rectangle((0.4,1.3),9.2,0.7,fc=TINT,ec=INK,lw=1))
for xx,t in [(1.3,'Formal report'),(3.4,'Client letter'),(5.4,'Internal email'),(7.3,'Team chat'),(9.0,'—')]:
    if t!='—':
        ax.plot([xx,xx],[1.3,2.0],color=INK,lw=1)
        ax.text(xx,2.15,t,ha='center',fontsize=9.5,color=INK)
ax.text(0.4,0.85,'MOST FORMAL — no contractions, precise, documented',fontsize=9,color=INK)
ax.text(9.6,0.85,'MOST CASUAL — contractions,\nfirst names, emoji if the room allows',fontsize=9,color=INK,ha='right')
ax.text(5.0,2.75,'One professional voice, dialed to the occasion — never two personalities',ha='center',fontsize=11,color=GREEN,weight='bold')
save(fig,'ch2_tone.png')

# 6 — message planner canvas
fig, ax = plt.subplots(figsize=(8.6,4.2)); ax.set_xlim(0,10); ax.set_ylim(0,5); ax.axis('off')
cells=[(0.3,3.4,'1 · PURPOSE\nWhat should the reader\nKNOW or DO?'),(3.55,3.4,'2 · AUDIENCE\nWhat do they know, feel,\nfear, want?'),(6.8,3.4,'3 · BENEFIT\nWhy would THEY\nwant to say yes?'),
       (0.3,1.0,'4 · CHANNEL\nRich or lean?\nRecord needed?'),(3.55,1.0,'5 · OPENING\nThe main point,\nstated first'),(6.8,1.0,'6 · CALL TO ACTION\nSpecific act + deadline\n(“reply with your date”)')]
for x,y,t in cells:
    box(ax,x,y,2.95,1.9,t,fc=TINT,tc=INK,fs=10)
    ax.add_patch(FancyBboxPatch((x,y+1.55),2.95,0.35,boxstyle='round,pad=0.01,rounding_size=0.02',fc=GREEN,ec='none'))
    ax.text(x+1.475,y+1.72,t.split('\n')[0],ha='center',va='center',color='white',fontsize=10,weight='bold')
ax.text(5.0,0.35,'Six boxes, two minutes — cheaper than one misunderstood email',ha='center',fontsize=10.5,color=GOLD,style='italic')
save(fig,'ch2_planner.png')

# 7 — resistance loop
fig, ax = plt.subplots(figsize=(8.6,2.9)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
steps=[('List their\nobjections','Before writing —\nhonestly'),('Address the\nbig two','In the message,\nnot after it'),('Show, don’t\nclaim','Evidence beats\nadjectives'),('Make yes\neasy','Small ask ·\nclear next step')]
for i,(t,sub) in enumerate(steps):
    box(ax,0.3+i*2.45,1.5,2.2,1.2,t,fc=GREEN if i%2==0 else MOSS,fs=10.5)
    ax.text(0.3+i*2.45+1.1,1.28,sub,ha='center',va='top',fontsize=9,color=INK)
    if i<3: arr(ax,0.3+i*2.45+2.22,2.1,0.3+(i+1)*2.45-0.02,2.1)
ax.text(5.0,3.1,'Writing for the skeptical reader',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch2_resistance.png')
print('ch2 figures complete')
