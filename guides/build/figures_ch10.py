# Original figures for Chapter 10 — Proposals and Formal Reports
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

# 1 — formal report architecture
fig, ax = plt.subplots(figsize=(8.6,4.4)); ax.set_xlim(0,10); ax.set_ylim(0,5.0); ax.axis('off')
rows=[('FRONT MATTER','cover · title page · transmittal · table of contents · executive summary',GREEN),
      ('BODY','introduction → findings/analysis (the pyramid, transcribed) → conclusions → recommendations',MOSS),
      ('BACK MATTER','references · appendices — the verification layer',GREEN)]
y=3.9
for t,sub,c in rows:
    box(ax,0.4,y,2.7,0.75,t,fc=c,fs=10.5)
    ax.text(3.35,y+0.37,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=1.05
box(ax,0.4,0.5,9.2,0.9,'THREE READERS, THREE PATHS: the decider reads the executive summary · the implementer\nreads the body · the auditor reads the appendices — design all three paths deliberately',fc=TINT,tc=INK,fs=10)
save(fig,'ch10_architecture.png')

# 2 — executive summary anatomy
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
rows=[('THE SITUATION','one or two sentences — why this document exists',MOSS),
      ('THE ANSWER','the recommendation + its strongest number',GREEN),
      ('THE REASONS','the pyramid’s second layer, compressed to a sentence each',MOSS),
      ('THE ASK','decision needed, by whom, by when',GREEN),
      ('THE RULE','written LAST · placed FIRST · standalone — most readers read nothing else',GOLD)]
y=3.5
for t,sub,c in rows:
    box(ax,0.4,y,2.8,0.62,t,fc=c,fs=9.5)
    ax.text(3.45,y+0.31,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.78
save(fig,'ch10_execsum.png')

# 3 — proposal types map
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
box(ax,0.4,2.4,4.4,1.1,'SOLICITED\nthey asked (RFP) — compliance\nwith their structure is scored\nbefore your content is read',fc=GREEN,fs=9.5)
box(ax,5.2,2.4,4.4,1.1,'UNSOLICITED\nyou spotted the need — you must\nsell the PROBLEM before the\nsolution (Chapter 8’s hook)',fc=MOSS,fs=9.5)
box(ax,0.4,0.9,4.4,1.1,'INTERNAL\nresources, changes, projects —\nthe justification report’s\nbig sibling',fc=MOSS,fs=9.5)
box(ax,5.2,0.9,4.4,1.1,'EXTERNAL\ncontracts, grants, partnerships —\nformal apparatus + binding\ncommitments (write like a contract)',fc=GREEN,fs=9.5)
ax.text(5.0,3.9,'The proposal quadrants — each shifts the burden of proof',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch10_proptypes.png')

# 4 — proposal skeleton (full)
fig, ax = plt.subplots(figsize=(8.6,4.2)); ax.set_xlim(0,10); ax.set_ylim(0,4.8); ax.axis('off')
rows=[('PROBLEM / NEED','their pain, quantified — the reason money should move'),
      ('PROPOSED SOLUTION','what, how, and why THIS approach'),
      ('PLAN & SCHEDULE','phases, milestones, deliverables — dated'),
      ('STAFFING / QUALIFICATIONS','why YOU — ethos with evidence'),
      ('BUDGET','itemized, justified, framed against the cost of the problem'),
      ('EVALUATION & RISKS','how success is measured; what could go wrong and the mitigations')]
y=3.9
for t,sub in rows:
    box(ax,0.4,y,3.1,0.58,t,fc=GREEN,fs=9.3)
    ax.text(3.75,y+0.29,sub,ha='left',va='center',fontsize=9.4,color=INK)
    y-=0.72
save(fig,'ch10_propskeleton.png')

# 5 — source credibility ladder
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
rows=[('PRIMARY DATA','your measurements, surveys, pilots — strongest, and yours to defend',GREEN,'white'),
      ('PEER-REVIEWED / OFFICIAL','journals, standards bodies, government statistics',GREEN,'white'),
      ('REPUTABLE SECONDARY','industry reports, quality journalism — verify the underlying source',MOSS,'white'),
      ('VENDOR / ADVOCACY','useful, interested — corroborate before load-bearing use',TINT,INK),
      ('UNSOURCED WEB / AI OUTPUT','never load-bearing — trace to a real source or drop the claim',"#F7EAE8",PROOF)]
y=3.3
for t,sub,fc,tc in rows:
    box(ax,0.4,y,3.3,0.6,t,fc=fc,tc=tc,fs=9)
    ax.text(3.95,y+0.3,sub,ha='left',va='center',fontsize=9.3,color=INK)
    y-=0.74
save(fig,'ch10_sources.png')

# 6 — citation integrity
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
rows=[('QUOTE','their exact words → quotation marks + citation'),
      ('PARAPHRASE','their idea, your words → citation still required'),
      ('COMMON KNOWLEDGE','undisputed, widely available → no citation'),
      ('YOUR ANALYSIS','your conclusions from cited evidence → the part that’s yours')]
y=2.7
for t,sub in rows:
    box(ax,0.4,y,2.6,0.55,t,fc=GREEN,fs=9.5)
    ax.text(3.25,y+0.27,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.68
ax.text(5.0,3.15,'What needs a citation — the boundary that protects your credibility',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch10_citation.png')

# 7 — the RFP compliance matrix
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
box(ax,0.4,2.2,9.2,0.8,'RFP SAYS: “Proposals must include sections A–F, max 20 pages, 12pt, due 7/15 at 2:00 PM CT, via portal”',fc=GREEN,fs=10)
rows=[('Their structure = your structure','mirror their section names and order — evaluators score with a checklist'),
      ('Every “shall/must” goes in a compliance matrix','requirement → where addressed → page number'),
      ('Deadlines are cliffs, not targets','2:01 PM is a non-submission; portals crash at 1:55')]
y=1.6
for t,sub in rows:
    box(ax,0.4,y,3.6,0.5,t,fc=MOSS,fs=8.9)
    ax.text(4.2,y+0.25,sub,ha='left',va='center',fontsize=9.3,color=INK)
    y-=0.62
save(fig,'ch10_rfp.png')
print('ch10 figures complete')
