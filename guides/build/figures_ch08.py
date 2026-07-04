# Original figures for Chapter 8 — Persuasive Messages
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon

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

# 1 — AIDA
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
steps=[('ATTENTION','A hook that belongs\nto the READER:\nproblem, stat, question'),
       ('INTEREST','Their situation,\nnamed accurately —\nproof you understand it'),
       ('DESIRE','Evidence: numbers,\npilots, social proof —\nobjections answered'),
       ('ACTION','One small, specific,\ndated ask —\nyes made easy')]
for j,(t,sub) in enumerate(steps):
    box(ax,0.3+j*2.45,1.7,2.2,1.05,t,fc=GREEN if j%2==0 else MOSS,fs=10)
    ax.text(0.3+j*2.45+1.1,1.48,sub,ha='center',va='top',fontsize=9.3,color=INK)
    if j<3: arr(ax,0.3+j*2.45+2.22,2.22,0.3+(j+1)*2.45-0.02,2.22)
ax.text(5.0,3.3,'The AIDA sequence: a persuasion pipeline, not a paint-by-numbers',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch8_aida.png')

# 2 — appeals triangle
fig, ax = plt.subplots(figsize=(7.6,4.2)); ax.set_xlim(0,10); ax.set_ylim(0,5); ax.axis('off')
ax.add_patch(Polygon([[5,4.4],[1.2,0.8],[8.8,0.8]],closed=True,fc=TINT,ec=GREEN,lw=2))
box(ax,3.9,4.0,2.2,0.75,'ETHOS\ncredibility',fc=GREEN,fs=10)
box(ax,0.4,0.35,2.6,0.75,'PATHOS\nvalues & emotion',fc=MOSS,fs=10)
box(ax,7.0,0.35,2.6,0.75,'LOGOS\nevidence & logic',fc=MOSS,fs=10)
ax.text(5,2.3,'A persuasive message\nbalances all three —\nthe weakest leg\nis where it fails',ha='center',va='center',fontsize=10.5,color=INK)
save(fig,'ch8_appeals.png')

# 3 — Cialdini principles
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
items=[('RECIPROCITY','give first — the favor precedes the ask'),
       ('CONSISTENCY','small yeses grow: pilots before rollouts'),
       ('SOCIAL PROOF','“4 of 5 regional labs already switched”'),
       ('LIKING','rapport is groundwork, not garnish'),
       ('AUTHORITY','cite the credential, the data, the expert'),
       ('SCARCITY','real deadlines and limits — never invented ones')]
for j,(t,sub) in enumerate(items):
    y=3.6-j*0.62
    box(ax,0.5,y-0.15,2.5,0.5,t,fc=GREEN,fs=9.5)
    ax.text(3.25,y+0.1,sub,ha='left',va='center',fontsize=9.6,color=INK)
ax.text(5.0,4.15,'Six levers of influence (Cialdini) — each ethical only when the claim is true',ha='center',fontsize=11,color=GREEN,weight='bold')
save(fig,'ch8_cialdini.png')

# 4 — two-sided argument
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
box(ax,0.3,2.0,4.5,1.2,'ONE-SIDED\nOnly your case.\nWorks ONLY on the\nalready-convinced',fc='#F1E9E7',tc=INK,fs=10)
box(ax,5.2,2.0,4.5,1.2,'TWO-SIDED + REBUTTAL\n“Yes, it costs $2,400 — here’s the\nsix-week payback.” Wins with\nskeptics and survives scrutiny',fc=GREEN,fs=10)
ax.text(5.0,1.4,'Name the strongest objection yourself — credibility is earned at the point of concession',ha='center',fontsize=10.5,color=GOLD,style='italic')
ax.text(5.0,0.7,'(And weak throwaway arguments DILUTE strong ones — quality beats quantity.)',ha='center',fontsize=9.5,color=INK)
save(fig,'ch8_twosided.png')

# 5 — commitment ladder
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
rungs=[('“Read the one-pager?”',0.5,2.6),('“Join the 20-min demo?”',2.8,1.9),('“Run a two-week pilot?”',5.1,1.2),('“Adopt team-wide”',7.4,0.5)]
for j,(t,x,y) in enumerate(rungs):
    box(ax,x,y+0.6,2.3,0.7,t,fc=MOSS if j<3 else GREEN,fs=9.5)
    if j<3: arr(ax,x+2.0,y+0.55,x+2.6,y+0.35,c=GOLD)
ax.text(5.0,3.7,'The commitment ladder: each small yes makes the next one natural',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch8_ladder.png')

# 6 — audience position spectrum
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
import matplotlib.patches as mp
ax.add_patch(mp.Rectangle((0.4,1.5),9.2,0.7,fc=TINT,ec=INK,lw=1))
for x,t,c in [(1.6,'HOSTILE',PROOF),(3.7,'SKEPTICAL',GOLD),(5.8,'NEUTRAL',INK),(8.2,'SUPPORTIVE',GREEN)]:
    ax.text(x,1.85,t,ha='center',va='center',fontsize=10,color=c,weight='bold')
notes=[(1.6,'goal: reduce hostility,\nnot win today'),(3.7,'two-sided + evidence;\nsmall first ask'),(5.8,'benefits + clear action'),(8.2,'make acting easy NOW')]
for x,t in notes:
    ax.text(x,0.95,t,ha='center',va='top',fontsize=9.3,color=INK)
ax.text(5.0,2.85,'Calibrate the ask to the audience’s starting position',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch8_spectrum.png')

# 7 — proposal skeleton
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
rows=[('HOOK','the reader’s problem, quantified: “We re-enter every sample twice.”',GREEN),
      ('SOLUTION + VALUE','what, and what it does to THEIR numbers (WTP/WTS language)',MOSS),
      ('EVIDENCE','pilot data · reference customers · the strongest objection, answered',GREEN),
      ('COST, FRAMED','against the cost of doing nothing — the honest comparison',MOSS),
      ('THE ASK','one small dated step: “30-minute demo Thursday?”',GREEN)]
y=3.4
for t,sub,c in rows:
    box(ax,0.4,y,2.7,0.62,t,fc=c,fs=9.5)
    ax.text(3.35,y+0.31,sub,ha='left',va='center',fontsize=9.3,color=INK)
    y-=0.78
save(fig,'ch8_proposal.png')
print('ch8 figures complete')
