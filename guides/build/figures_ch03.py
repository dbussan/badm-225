# Original figures for Chapter 3 — Organizing and Drafting Business Messages
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
def arr(ax,x1,y1,x2,y2,c=INK):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=15,color=c,lw=1.7))

# 1 — direct vs indirect strategy
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
ax.text(2.6,3.9,'DIRECT — receptive or neutral readers',ha='center',fontsize=11,color=GREEN,weight='bold')
for j,(t,c) in enumerate([('MAIN POINT',GREEN),('Details / reasons',MOSS),('Goodwill close',MOSS)]):
    box(ax,0.4,2.9-j*0.85,4.4,0.7,t,fc=c,fs=10)
ax.text(7.5,3.9,'INDIRECT — resistant readers, bad news',ha='center',fontsize=11,color=GREEN,weight='bold')
for j,(t,c) in enumerate([('Buffer / context',MOSS),('Reasons FIRST',MOSS),('MAIN POINT, then pivot forward',GREEN)]):
    box(ax,5.3,2.9-j*0.85,4.4,0.7,t,fc=c,fs=10)
save(fig,'ch3_strategy.png')

# 2 — outline tree
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
box(ax,3.4,3.4,3.2,0.8,'PURPOSE\n(the one job)',fc=GREEN,fs=10)
mains=[('I. Cost',0.7),('II. Quality',3.9),('III. Timeline',7.1)]
for t,x in mains:
    box(ax,x,1.9,2.2,0.75,t,fc=MOSS,fs=10)
    arr(ax,x+1.1,2.68,5.0-(5.0-(x+1.1))*0.15,3.35)
subs=[('A. quotes\nB. payback',0.7),('A. pilot data\nB. reviews',3.9),('A. phases\nB. risks',7.1)]
for t,x in subs:
    box(ax,x,0.45,2.2,1.05,t,fc=TINT,tc=INK,fs=9.5)
    arr(ax,x+1.1,1.55,x+1.1,1.86)
save(fig,'ch3_outline.png')

# 3 — paragraph anatomy
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
box(ax,0.4,2.9,9.2,0.8,'TOPIC SENTENCE — the paragraph’s one claim, stated first',fc=GREEN,fs=11)
box(ax,0.9,1.9,8.2,0.75,'SUPPORT — evidence, example, or explanation for THAT claim only',fc=MOSS,fs=10.5)
box(ax,0.9,1.0,8.2,0.7,'COHERENCE — transitions and echoed key words tie sentences together',fc=MOSS,fs=10.5)
box(ax,0.4,0.1,9.2,0.65,'UNITY TEST: any sentence not serving the topic sentence belongs in another paragraph',fc=TINT,tc=INK,fs=10)
save(fig,'ch3_paragraph.png')

# 4 — active vs passive
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
box(ax,0.3,2.2,4.5,1.4,'ACTIVE — the default\n“Maria approved the budget.”\nActor visible · shorter · faster to decode',fc=GREEN,fs=10)
box(ax,5.2,2.2,4.5,1.4,'PASSIVE — the tool\n“The budget was approved.”\nUse when actor is unknown, obvious,\nor better left unnamed',fc=MOSS,fs=10)
box(ax,0.3,0.4,9.4,1.2,'WARNING ZONE: passive that HIDES accountability —\n“Mistakes were made” · “The sample was mislabeled” — name the actor when the reader needs the actor',fc='#F7EAE8',tc=PROOF,fs=10)
save(fig,'ch3_voice.png')

# 5 — topic & stress positions
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
box(ax,0.4,1.6,2.8,0.9,'TOPIC POSITION\nsentence opening:\nold info, the familiar',fc=MOSS,fs=9.5)
box(ax,3.4,1.6,3.2,0.9,'…the middle carries\nthe connective tissue…',fc=TINT,tc=INK,fs=9.5)
box(ax,6.8,1.6,2.8,0.9,'STRESS POSITION\nsentence end:\nnew info, the emphasis',fc=GREEN,fs=9.5)
ax.text(5.0,2.9,'Readers expect sentences to flow old → new (Gopen & Swan, 1990)',ha='center',fontsize=11,color=GREEN,weight='bold')
ax.text(5.0,1.0,'“The committee rejected the proposal” vs. “The proposal was rejected — by the full committee.”',ha='center',fontsize=9.5,color=INK,style='italic')
ax.text(5.0,0.55,'Put what you want remembered where the reader’s emphasis naturally lands: the end.',ha='center',fontsize=9.5,color=INK)
save(fig,'ch3_stress.png')

# 6 — sentence rhythm
fig, ax = plt.subplots(figsize=(8.6,2.8)); ax.set_xlim(0,10); ax.set_ylim(0,3.2); ax.axis('off')
lens=[18,22,7,25,12]
labels=['18','22','7  ←  the punch','25','12']
for j,(L,lab) in enumerate(zip(lens,labels)):
    w=L/25*7.5
    ax.add_patch(Rectangle((0.6,2.5-j*0.5),w,0.32,fc=GREEN if L==7 else MOSS,ec='none'))
    ax.text(0.62+w+0.15,2.66-j*0.5,lab+' words',fontsize=9.5,color=INK,va='center')
ax.text(5.0,3.05,'Vary sentence length — monotony anesthetizes, variety emphasizes',ha='center',fontsize=11,color=GREEN,weight='bold')
save(fig,'ch3_rhythm.png')

# 7 — chunking
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
box(ax,0.3,1.3,4.4,1.5,'ONE WALL OF TEXT\n14 items in a paragraph\n= working-memory overflow',fc='#F1E9E7',tc=INK,fs=10)
box(ax,5.3,1.9,4.4,0.9,'GROUPED: 3 headed lists of 4–5\n= readable, recallable, actionable',fc=GREEN,fs=10)
box(ax,5.3,0.85,4.4,0.85,'Working memory holds ~7 ± 2 chunks\n(Miller, 1956) — chunk FOR the reader',fc=TINT,tc=INK,fs=9.5)
arr(ax,4.75,2.05,5.25,2.2,c=GOLD)
save(fig,'ch3_chunk.png')
print('ch3 figures complete')
