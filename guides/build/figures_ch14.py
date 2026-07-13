# Original figures for Chapter 14 — Interviewing and Follow-Up
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

# 1 — STAR
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
ax.text(5.0,3.3,'STAR — the answer architecture (90 seconds to 2 minutes)',ha='center',fontsize=11.5,color=GREEN,weight='bold')
steps=[('SITUATION','where and when —\ntwo sentences, no more'),('TASK','what YOU were\nresponsible for'),('ACTION','what you specifically did\n— “I,” not “we”'),('RESULT','what changed, with the\nnumber + what you learned')]
x=0.4; w=2.2
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.7,w,0.9,t,fc=GREEN,fs=9.8)
    ax.text(x+w/2,1.2,sub,ha='center',va='center',fontsize=9.3,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.15,x+w+0.13,2.15)
    x+=w+0.13
box(ax,0.4,0.25,9.2,0.6,'The classic failure: a vague, collective middle — “we sort of handled it” — with no measurable end.',fc='#F7EAE8',tc=PROOF,fs=9.6)
save(fig,'ch14_star.png')

# 2 — the eight-story bank
fig, ax = plt.subplots(figsize=(8.6,4.0)); ax.set_xlim(0,10); ax.set_ylim(0,4.6); ax.axis('off')
ax.text(5.0,4.3,'THE EIGHT-STORY BANK — covers nearly every behavioral question',ha='center',fontsize=11.5,color=GREEN,weight='bold')
cells=[('A CONFLICT','worked through, not won'),('A FAILURE','owned + what changed'),('A DEADLINE CRUNCH','triage under pressure'),('A LEADERSHIP MOMENT','with or without the title'),
       ('A PERSUASION','moved without authority'),('A MISTAKE OWNED','fast, clean admission'),('AN INITIATIVE','unasked, delivered'),('A TEAM WIN','your “I” inside the “we”')]
x0,y0=0.4,2.5
for i,(t,sub) in enumerate(cells):
    cx=x0+(i%4)*2.35; cy=y0-(i//4)*1.55
    box(ax,cx,cy+0.55,2.15,0.55,t,fc=GREEN if (i%2==0) else MOSS,fs=8.9)
    ax.text(cx+1.075,cy+0.25,sub,ha='center',va='center',fontsize=8.9,color=INK)
box(ax,0.4,0.15,9.2,0.6,'Source them anywhere legitimate: jobs, courses, clubs, the capstone. Write each once; index by beats.',fc=TINT,tc=INK,fs=9.6)
save(fig,'ch14_storybank.png')

# 3 — the question behind the question
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
ax.text(5.0,4.1,'THE CLASSICS — and what they’re actually asking',ha='center',fontsize=11.5,color=GREEN,weight='bold')
rows=[('“Why do you want to work here?”','= did you research us? Answer with THEIR specifics.',GREEN),
      ('“Your greatest weakness?”','= are you self-aware and improving? Real + non-fatal + the visible fix.',MOSS),
      ('“Why are you leaving?” / “the gap?”','= any red flags? One honest, forward-facing sentence — never a grievance tour.',GREEN),
      ('“Five years from now?”','= fit or layover? Ambition aligned with this role’s actual path.',MOSS)]
y=3.3
for t,sub,c in rows:
    box(ax,0.4,y,3.4,0.62,t,fc=c,fs=9.3)
    ax.text(4.0,y+0.31,sub,ha='left',va='center',fontsize=9.4,color=INK)
    y-=0.78
save(fig,'ch14_classics.png')

# 4 — salary conversation
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
ax.text(5.0,4.1,'THE MONEY CONVERSATION — researched, calm, once',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,2.32,4.3,1.55,'ASKED EARLY\n\n“From what I’ve seen for this role in\nthis region: $58–65K — and I’m\nflexible for the right fit.”\ncalm · sourced · a range that anchors',fc=GREEN,fs=9.3)
box(ax,5.3,2.32,4.3,1.55,'NEGOTIATING THE OFFER\n\n“I’m excited about this role. Given the\naudit experience I bring, is there\nflexibility toward $63K?”\nonce · with a reason · then decide',fc=MOSS,fs=9.3)
box(ax,0.4,1.35,9.2,0.85,'The package is wider than the salary: start date, signing bonus, development budget, remote days —\nwhen the number is fixed, the terms often aren’t.',fc=TINT,tc=INK,fs=9.5)
box(ax,0.4,0.35,9.2,0.7,'Get the final version IN WRITING before resigning anything (Chapter 6’s confirmation rule, maximum stakes).',fc='#F7EAE8',tc=PROOF,fs=9.5)
save(fig,'ch14_salary.png')

# 5 — follow-through timeline
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
ax.text(5.0,3.3,'AFTER THE HANDSHAKE — the follow-through that separates finalists',ha='center',fontsize=11.5,color=GREEN,weight='bold')
steps=[('WITHIN 24 HRS','individual thank-yous —\nspecific moment referenced'),('AT THE DEADLINE','one polite nudge if the\npromised date passes'),('+2 WEEKS','second nudge — then let it\ngo; pipeline keeps moving'),('ANY OUTCOME','gracious reply — rejected,\noffered, or silence')]
x=0.4; w=2.2
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.7,w,0.9,t,fc=GREEN,fs=9.4)
    ax.text(x+w/2,1.2,sub,ha='center',va='center',fontsize=9.0,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.15,x+w+0.13,2.15)
    x+=w+0.13
box(ax,0.4,0.25,9.2,0.6,'Ask the timeline in the room — “what are the next steps, and when should I expect to hear?” — so silence has a shape.',fc=TINT,tc=INK,fs=9.4)
save(fig,'ch14_followup.png')

# 6 — your questions
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
ax.text(5.0,3.7,'YOUR QUESTIONS ARE HALF THE INTERVIEW',ha='center',fontsize=11.5,color=GREEN,weight='bold')
rows=[('THE ROLE','“What does success at ninety days look like?” — you’re already thinking inside the job',GREEN),
      ('THE CRAFT','“What separates the good hires from the great ones here?” — gold, and they love answering',MOSS),
      ('THE TEAM','“How does the team handle disagreement / decide priorities?” — culture, checkably',GREEN),
      ('NEVER FIRST','salary, vacation, remote days — logistics before fit reframes you as a perk shopper',PROOF)]
y=3.0
for t,sub,c in rows:
    box(ax,0.4,y,2.3,0.58,t,fc=c,fs=9.6)
    ax.text(2.95,y+0.29,sub,ha='left',va='center',fontsize=9.2,color=INK)
    y-=0.72
save(fig,'ch14_questions.png')
print('ch14 figures complete')
