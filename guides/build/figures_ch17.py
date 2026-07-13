# Original figures for Chapter 17 — Strategy for Communicators
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

GREEN='#0E4D33'; MOSS='#5C8A6E'; TINT='#EAF1EB'; GOLD='#8A6410'; INK='#212A26'; PROOF='#B23A31'
OUT = os.path.join(os.path.dirname(__file__), 'fig')
plt.rcParams.update({'font.family':'Calibri','font.size':11})
FS_FLOOR=9.3

def save(fig,name):
    fig.savefig(os.path.join(OUT,name),dpi=160,bbox_inches='tight',facecolor='white'); plt.close(fig); print('fig:',name)
def box(ax,x,y,w,h,t,fc=GREEN,tc='white',fs=10.5):
    assert fs>=FS_FLOOR, f'font {fs} below floor'
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.04',fc=fc,ec='none'))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',color=tc,fontsize=fs)
def arr(ax,x1,y1,x2,y2,c=INK):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=15,color=c,lw=1.7))

# 1 — the value stick
fig, ax = plt.subplots(figsize=(6.6,5.4)); ax.set_xlim(0,10); ax.set_ylim(0,10.6); ax.axis('off')
ax.text(5.0,10.2,'THE VALUE STICK',ha='center',fontsize=12,color=GREEN,weight='bold')
box(ax,3.0,7.9,4.0,1.1,'WTP\nwillingness to pay',fc=GREEN,fs=10.5)
box(ax,3.0,6.1,4.0,1.1,'PRICE',fc=MOSS,fs=10.5)
box(ax,3.0,4.3,4.0,1.1,'COST',fc=MOSS,fs=10.5)
box(ax,3.0,2.5,4.0,1.1,'WTS\nwillingness to sell',fc=GREEN,fs=10.5)
ax.annotate('',xy=(7.3,8.45),xytext=(7.3,6.65),arrowprops=dict(arrowstyle='<->',color=GOLD,lw=1.6))
ax.text(7.9,7.55,'customer\ndelight',ha='left',va='center',fontsize=9.4,color=GOLD)
ax.annotate('',xy=(7.3,6.65),xytext=(7.3,4.85),arrowprops=dict(arrowstyle='<->',color=INK,lw=1.6))
ax.text(7.9,5.75,'firm\nmargin',ha='left',va='center',fontsize=9.4,color=INK)
ax.annotate('',xy=(7.3,4.85),xytext=(7.3,3.05),arrowprops=dict(arrowstyle='<->',color=GOLD,lw=1.6))
ax.text(7.9,3.95,'supplier/\nemployee\nsurplus',ha='left',va='center',fontsize=9.3,color=GOLD)
box(ax,0.3,0.4,9.4,1.5,'Value created = WTP minus WTS. Profit, delight, and good jobs are all\nslices of that one stick.',fc=TINT,tc=INK,fs=9.8)
save(fig,'ch17_valuestick.png')

# 2 — three levers
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
ax.text(5.0,3.7,'THE ONLY THREE LEVERS — locate every initiative, or call it activity',ha='center',fontsize=11,color=GREEN,weight='bold')
box(ax,0.4,1.7,2.9,1.3,'RAISE WTP\nmake customers’\nlives better',fc=GREEN,fs=9.6)
box(ax,3.55,1.7,2.9,1.3,'CUT REAL COST\nsame value,\nless spend',fc=MOSS,fs=9.6)
box(ax,6.7,1.7,2.9,1.3,'LOWER WTS\nmake working with\nyou better',fc=GREEN,fs=9.6)
box(ax,0.4,0.35,9.2,1.05,'Moving price alone captures differently but creates nothing — the lever\nthat looks like strategy and isn’t.',fc='#F7EAE8',tc=PROOF,fs=9.5)
save(fig,'ch17_levers.png')

# 3 — trade-offs
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
ax.text(5.0,3.7,'STRATEGY IS CHOOSING WHAT TO BE BAD AT',ha='center',fontsize=11.3,color=GREEN,weight='bold')
box(ax,0.4,1.7,4.3,1.4,'STRADDLING\n\nchasing every driver averages\nthe value proposition into\n“fine” — and “fine” has the\nWTP of a shrug',fc='#F7EAE8',tc=PROOF,fs=9.4)
box(ax,5.3,1.7,4.3,1.4,'TRADE-OFFS\n\npicking the drivers you\ncompete on and accepting\nvisible weakness on the\nrest — deliberately',fc=GREEN,fs=9.4)
box(ax,0.4,0.35,9.2,1.05,'The test: a strategy tells you what to STOP doing. If nothing got harder\nto justify, no strategy was made.',fc=TINT,tc=INK,fs=9.5)
save(fig,'ch17_tradeoffs.png')

# 4 — proposal in value language
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
ax.text(5.0,3.3,'WRITING PROPOSALS IN VALUE LANGUAGE',ha='center',fontsize=11.3,color=GREEN,weight='bold')
steps=[('NAME THE LEVER','WTP up, cost down,\nor WTS down — pick one'),('PRICE THE STATUS QUO','“no” is never free —\nquantify the drift'),('SHOW THE ARITHMETIC','breakeven, not just\neffort spent')]
x=0.4; w=2.9
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.6,w,1.1,t,fc=GREEN,fs=9.6)
    ax.text(x+w/2,1.12,sub,ha='center',va='center',fontsize=9.3,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.15,x+w+0.12,2.15)
    x+=w+0.12
box(ax,0.4,0.25,9.2,0.6,'One lever per proposal, argued deep — the dilution effect (Chapter 8) applies to value claims too.',fc=TINT,tc=INK,fs=9.4)
save(fig,'ch17_proposal.png')
print('ch17 figures complete')
