# Original figures for Chapter 6 — Positive and Neutral Messages
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

# 1 — direct request pattern
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
steps=[('OPEN with the ask','“Could you send the Q2\nvendor report by Thursday?”'),
       ('EXPLAIN briefly','Why, and why them —\none or two lines'),
       ('DETAIL what’s needed','Format, scope, access —\nas a scannable list'),
       ('CLOSE with date + goodwill','“By Thursday noon keeps us\non schedule — thank you!”')]
for j,(t,sub) in enumerate(steps):
    box(ax,0.3+j*2.45,1.7,2.2,1.0,t,fc=GREEN if j%2==0 else MOSS,fs=9.5)
    ax.text(0.3+j*2.45+1.1,1.5,sub,ha='center',va='top',fontsize=9.3,color=INK)
    if j<3: arr(ax,0.3+j*2.45+2.22,2.2,0.3+(j+1)*2.45-0.02,2.2)
ax.text(5.0,3.3,'The direct request: ask, explain, detail, close',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch6_request.png')

# 2 — the reply skeleton
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
rows=[('ANSWER FIRST','“Yes — the room is yours, 2–4 p.m. Friday.”',GREEN),
      ('DETAILS','Everything they’ll ask next: access, setup, contact',MOSS),
      ('EXTRAS','What they didn’t ask but need: projector code, parking',MOSS),
      ('FORWARD CLOSE','“Anything else before Friday, just ask.”',GREEN)]
y=3.2
for t,sub,c in rows:
    box(ax,0.4,y,2.6,0.65,t,fc=c,fs=10)
    ax.text(3.25,y+0.32,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.82
save(fig,'ch6_reply.png')

# 3 — adjustment grant flow
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
steps=[('GRANT\nimmediately','“A replacement ships\ntoday, free.”'),('EXPLAIN\nwithout excuses','What went wrong,\nbriefly — no blame opera'),('REPAIR\nthe confidence','What prevents a\nrepeat'),('RESTORE\nthe relationship','Forward-looking close;\nno groveling')]
for j,(t,sub) in enumerate(steps):
    box(ax,0.3+j*2.45,1.7,2.2,1.1,t,fc=GREEN if j%2==0 else MOSS,fs=9.5)
    ax.text(0.3+j*2.45+1.1,1.48,sub,ha='center',va='top',fontsize=9.3,color=INK)
    if j<3: arr(ax,0.3+j*2.45+2.22,2.25,0.3+(j+1)*2.45-0.02,2.25)
ax.text(5.0,3.3,'Granting a claim: the adjustment message that keeps the customer',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch6_adjust.png')

# 4 — goodwill 5S
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
items=[('SPECIFIC','names the exact act and its effect'),('SINCERE','no flattery, no agenda smuggled in'),
       ('SHORT','five sentences beat five paragraphs'),('SPONTANEOUS','sent promptly, not at review season'),
       ('SELFLESS','about them — not “reply when you can”')]
for j,(t,sub) in enumerate(items):
    y=3.3-j*0.62
    box(ax,0.5,y-0.15,2.3,0.5,t,fc=GREEN,fs=10)
    ax.text(3.05,y+0.1,sub,ha='left',va='center',fontsize=9.8,color=INK)
ax.text(5.0,3.85,'Goodwill messages: the five S test',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch6_5s.png')

# 5 — claim (complaint) anatomy
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
rows=[('WHAT + WHEN','order number, dates, product — the verifiable record',GREEN),
      ('WHAT WENT WRONG','facts, calmly; attach evidence',MOSS),
      ('WHAT YOU WANT','the specific remedy: refund, replacement, repair',GREEN),
      ('BY WHEN + TONE','deadline, confidence in resolution — anger is leverage wasted',MOSS)]
y=3.2
for t,sub,c in rows:
    box(ax,0.4,y,2.8,0.65,t,fc=c,fs=9.5)
    ax.text(3.45,y+0.32,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.82
save(fig,'ch6_claim.png')

# 6 — instructions pattern
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
rows=[('One step, one action, one line','numbered, imperative verbs first: “Click… Enter… Save…”'),
      ('Preconditions before step 1','what they need in hand BEFORE starting'),
      ('Results after key steps','“You’ll see a green banner” — confirmation checkpoints'),
      ('Warnings BEFORE the step they protect','never after the damage line')]
y=2.6
for t,sub in rows:
    box(ax,0.4,y,3.6,0.58,t,fc=GREEN,fs=9)
    ax.text(4.2,y+0.29,sub,ha='left',va='center',fontsize=9.3,color=INK)
    y-=0.72
ax.text(5.0,3.4,'Writing instructions people can actually follow',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch6_steps.png')

# 7 — goodwill capital compounding
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
xs=[1.0,2.6,4.2,5.8,7.4,9.0]; ys=[0.8,1.05,1.45,1.9,2.35,2.75]
ax.plot(xs,ys,color=GREEN,lw=2.5,marker='o',ms=5)
labels=['a thank-you','a congrats note','credit given\npublicly','a favor\nbefore any ask','the reference\nyou didn’t request','the door that\nopens itself']
for x,y,l in zip(xs,ys,labels):
    ax.text(x,y+0.16,l,fontsize=9.3,color=INK,ha='center')
ax.text(5.0,0.3,'small deposits, compounding for years →',ha='center',fontsize=9.5,color=GOLD,style='italic')
save(fig,'ch6_capital.png')
print('ch6 figures complete')
