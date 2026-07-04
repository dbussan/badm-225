# Original figures for Chapter 7 — Negative Messages
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

# 1 — indirect pattern
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
steps=[('BUFFER','Honest common ground —\nnot a decoy of false hope'),
       ('REASONS','The why, BEFORE the no —\nso the no arrives pre-justified'),
       ('THE NEWS','Once. Clear. Brief.\nNo euphemism, no repetition'),
       ('PIVOT FORWARD','Alternatives, next steps,\nwhat you CAN do')]
for j,(t,sub) in enumerate(steps):
    box(ax,0.3+j*2.45,1.7,2.2,1.05,t,fc=GREEN if j%2==0 else MOSS,fs=9.5)
    ax.text(0.3+j*2.45+1.1,1.48,sub,ha='center',va='top',fontsize=9.3,color=INK)
    if j<3: arr(ax,0.3+j*2.45+2.22,2.22,0.3+(j+1)*2.45-0.02,2.22)
ax.text(5.0,3.3,'The indirect pattern: reasons before refusal',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch7_indirect.png')

# 2 — buffer types
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
rows=[('AGREEMENT','“You’re right that turnaround time matters more than ever.”'),
      ('APPRECIATION','“Thank you for the careful proposal — the cost analysis was thorough.”'),
      ('FACTS','“The committee reviewed all fourteen applications this cycle.”'),
      ('GOOD NEWS FIRST','“Your first request is approved. On the second…”'),
      ('UNDERSTANDING','“I know how much planning went into the March date.”')]
y=3.4
for t,sub in rows:
    box(ax,0.4,y,2.6,0.58,t,fc=GREEN,fs=9.5)
    ax.text(3.25,y+0.29,sub,ha='left',va='center',fontsize=9.3,color=INK)
    y-=0.72
ax.text(5.0,4.0,'Buffers that work — and none of them promise a yes',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch7_buffers.png')

# 3 — the news sentence
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
box(ax,0.3,2.4,4.5,1.2,'EVASION\n“It may prove difficult at this\njuncture to accommodate…”\nReader can’t even find the no',fc='#F1E9E7',tc=INK,fs=9.5)
box(ax,5.2,2.4,4.5,1.2,'CRUELTY\n“Denied. Your proposal failed\non multiple criteria.”\nThe no, weaponized',fc='#F7EAE8',tc=PROOF,fs=9.5)
box(ax,2.2,0.5,5.6,1.3,'THE CRAFT\n“We can’t fund the March cohort this year.”\nOnce · clear · brief · then pivot forward',fc=GREEN,fs=10.5)
arr(ax,2.5,2.35,3.7,1.85,c=GOLD); arr(ax,7.5,2.35,6.3,1.85,c=GOLD)
save(fig,'ch7_news.png')

# 4 — what you CAN do
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
rows=[('The alternative','“The September cohort has space — I can hold a seat until Friday.”'),
      ('The partial yes','“We can fund two of the three positions.”'),
      ('The path back','“Reapply after six months of P&L responsibility — here’s what would strengthen it.”'),
      ('The referral','“Meridian Labs runs exactly this analysis; ask for Dr. Chen.”')]
y=2.8
for t,sub in rows:
    box(ax,0.4,y,2.4,0.55,t,fc=MOSS,fs=9.5)
    ax.text(3.05,y+0.27,sub,ha='left',va='center',fontsize=9.2,color=INK)
    y-=0.68
ax.text(5.0,3.25,'The pivot: every no should carry whatever yes exists',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch7_pivot.png')

# 5 — apology anatomy
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
rows=[('OWN IT','“I missed the deadline I committed to.” No “mistakes were made,” no “if you were offended.”',GREEN),
      ('NAME THE IMPACT','“…which delayed your review by a week.” Proof you understand the cost.',MOSS),
      ('REPAIR + PREVENT','What you’re doing now, and what stops a repeat.',GREEN),
      ('STOP','No third apology. No self-flagellation tour. The reader needs the fix, not your feelings.',MOSS)]
y=3.2
for t,sub,c in rows:
    box(ax,0.4,y,2.5,0.65,t,fc=c,fs=9.5)
    ax.text(3.15,y+0.32,sub,ha='left',va='center',fontsize=9.0,color=INK)
    y-=0.82
save(fig,'ch7_apology.png')

# 6 — MUM effect
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
xs=[1.2,3.2,5.2,7.2,9.0]; ys=[2.6,2.2,1.7,1.1,0.6]
ax.plot(xs,ys,color=PROOF,lw=2.5,marker='o',ms=5)
for x,y,l in [(1.2,2.6,'problem found\n(small, fixable)'),(5.2,1.7,'delay: “next week,\nafter the demo”'),(9.0,0.6,'problem surfaces itself\n(large, public)')]:
    ax.text(x,y+0.18,l,fontsize=9.3,color=INK,ha='center')
ax.text(5.0,3.15,'The MUM effect: bad news travels slowest when it matters most (Rosen & Tesser, 1970)',ha='center',fontsize=10.5,color=GREEN,weight='bold')
save(fig,'ch7_mum.png')

# 7 — channel pairing for bad news
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
box(ax,0.4,1.6,4.3,1.2,'RICH FIRST\nConversation or call:\nempathy, questions absorbed,\ndignity protected',fc=GREEN,fs=10)
box(ax,5.3,1.6,4.3,1.2,'LEAN SECOND\nWritten follow-up same day:\nthe record, the terms,\nthe next steps',fc=MOSS,fs=10)
arr(ax,4.75,2.2,5.25,2.2,c=GOLD)
ax.text(5.0,3.1,'Serious bad news is a pairing, not a channel choice',ha='center',fontsize=11.5,color=GREEN,weight='bold')
ax.text(5.0,0.9,'Email-only for consequential personal bad news reads as cowardice — because it usually is.',ha='center',fontsize=9.5,color=INK,style='italic')
save(fig,'ch7_pairing.png')
print('ch7 figures complete')
