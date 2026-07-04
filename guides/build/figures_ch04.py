# Original figures for Chapter 4 — Revising Business Messages
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

# 1 — three-pass system
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
passes=[('PASS 1 · STRUCTURE','Right strategy? Main point\nfindable? Sections earn\ntheir place?'),
        ('PASS 2 · SENTENCES','Concise? Clear? Active?\nParallel? Old→new flow?'),
        ('PASS 3 · PROOF','Spelling, names, numbers,\ndates — what spellcheck\ncannot catch')]
for j,(t,sub) in enumerate(passes):
    box(ax,0.3+j*3.25,1.7,2.95,1.0,t,fc=GREEN if j%2==0 else MOSS,fs=10.5)
    ax.text(0.3+j*3.25+1.475,1.5,sub,ha='center',va='top',fontsize=9,color=INK)
    if j<2: arr(ax,0.3+j*3.25+2.97,2.2,0.3+(j+1)*3.25-0.02,2.2)
ax.text(5.0,3.3,'Three passes, three altitudes — never all at once',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch4_passes.png')

# 2 — the shrink
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
box(ax,0.3,1.3,4.5,2.2,'BEFORE · 43 words\n“Please be advised that in the event\nthat you should have any questions\nor concerns pertaining to the above-\nreferenced matter, do not hesitate to\nreach out to the undersigned at your\nearliest convenience.”',fc='#F1E9E7',tc=INK,fs=9)
box(ax,5.6,1.9,4.1,1.0,'AFTER · 6 words\n“Questions? Call me any time.”',fc=GREEN,fs=11)
arr(ax,4.85,2.4,5.55,2.4,c=GOLD)
ax.text(7.65,1.45,'Same meaning. 86% lighter.\nThe reader keeps the difference.',ha='center',fontsize=9.5,color=INK,style='italic')
save(fig,'ch4_shrink.png')

# 3 — concrete ladder
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
rungs=[('“improved performance”','abstract — believe me',0.4,'#F1E9E7',INK),
       ('“faster support responses”','directional — trust me',2.9,'#DFE9E2',INK),
       ('“cut response time 9 hrs → 2.1 hrs in the 90-day pilot”','concrete — check me',5.4,GREEN,'white')]
for t,sub,y,fc,tc in rungs:
    box(ax,0.5,y/1.6,9.0,0.85,t+'   ·   '+sub,fc=fc,tc=tc,fs=10.5)
ax.text(5.0,3.75,'Climb down the abstraction ladder until the claim is checkable',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch4_ladder.png')

# 4 — what spellcheck misses
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
misses=[('Real words,\nwrong place','manger / manager\nform / from\npubic / public'),
        ('Homophones','their / there\nits / it’s\naffect / effect'),
        ('Names &\nnumbers','Katherine vs Kathryn\n$45,000 vs $450,000\nMarch 12 vs March 21'),
        ('Grammar\nghosts','subject–verb slips\ndangling modifiers\nmissing words you\nread as present')]
for j,(t,sub) in enumerate(misses):
    box(ax,0.3+j*2.45,1.9,2.2,1.1,t,fc=GREEN,fs=10)
    ax.text(0.3+j*2.45+1.1,1.7,sub,ha='center',va='top',fontsize=8.8,color=INK)
ax.text(5.0,3.35,'Spellcheck passes all of these — proofreading exists because software can’t read',ha='center',fontsize=11,color=PROOF,weight='bold')
save(fig,'ch4_spellcheck.png')

# 5 — cooling curve
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
xs=[0.8,2.4,4.0,5.6,7.2,8.8]; ys=[0.7,1.5,2.1,2.45,2.6,2.7]
ax.plot(xs,ys,color=GREEN,lw=2.5,marker='o',ms=5)
for x,y,l in [(0.8,0.7,'just finished:\nyou read what you\nMEANT to write'),(4.0,2.1,'hours later:\nerrors surface'),(8.8,2.7,'next morning:\na stranger’s eyes')]:
    ax.text(x,y+0.18,l,fontsize=8.8,color=INK,ha='center')
ax.text(5.0,3.2,'The cooling curve: distance converts the writer back into a reader',ha='center',fontsize=11.5,color=GREEN,weight='bold')
ax.text(5.0,0.25,'time since drafting →',ha='center',fontsize=9.5,color=INK)
save(fig,'ch4_cooling.png')

# 6 — proof routine matrix
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
rout=[('Read ALOUD','Ears catch what eyes forgive:\nmissing words, clunks, tone'),
      ('One error type\nper sweep','Numbers-only pass ·\nnames-only pass · its/it’s pass'),
      ('Change the\ncostume','Print it, or change font/size —\nfamiliarity blindness resets'),
      ('The last-thing\ncheck','Subject line, recipient list,\nattachment — the classic trio')]
for j,(t,sub) in enumerate(rout):
    box(ax,0.3+j*2.45,2.0,2.2,1.2,t,fc=GREEN if j%2==0 else MOSS,fs=10)
    ax.text(0.3+j*2.45+1.1,1.8,sub,ha='center',va='top',fontsize=8.8,color=INK)
ax.text(5.0,3.7,'Four proofreading routines that actually work',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch4_routines.png')

# 7 — conciseness targets
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
targets=[('Long lead-ins','“I am writing this email to let you know that…” → (delete)'),
         ('There is / It is openers','“There are three issues that remain” → “Three issues remain”'),
         ('Redundant pairs','“each and every” · “final outcome” · “past history” → pick one'),
         ('Flabby phrases','“due to the fact that” → “because” · “at this point in time” → “now”'),
         ('Hedges & intensifiers','“very unique” · “quite significant” · “really important” → cut'),
         ('Noun stacks','“employee parking permit application process revision” → untangle with verbs')]
for j,(t,sub) in enumerate(targets):
    y=3.5-j*0.62
    ax.add_patch(FancyBboxPatch((0.4,y-0.2),2.6,0.5,boxstyle='round,pad=0.02',fc=GREEN,ec='none'))
    ax.text(1.7,y+0.05,t,ha='center',va='center',color='white',fontsize=9.5,weight='bold')
    ax.text(3.3,y+0.05,sub,ha='left',va='center',fontsize=9.3,color=INK)
save(fig,'ch4_targets.png')
print('ch4 figures complete')
