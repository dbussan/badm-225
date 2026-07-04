# Original figures for Chapter 9 — Informal Reports
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

# 1 — report family map
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
box(ax,3.4,3.5,3.2,0.7,'INFORMAL REPORTS',fc=GREEN,fs=11)
box(ax,0.5,2.0,4.3,0.9,'INFORMATIONAL\nreport what IS: progress, trip,\nmeeting minutes, incident',fc=MOSS,fs=9.5)
box(ax,5.2,2.0,4.3,0.9,'ANALYTICAL\nrecommend what SHOULD BE:\njustification, feasibility, comparison',fc=MOSS,fs=9.5)
arr(ax,4.2,3.45,2.65,2.95); arr(ax,5.8,3.45,7.35,2.95)
ax.text(2.65,1.55,'reader asks: “what happened?”',ha='center',fontsize=9.5,color=INK,style='italic')
ax.text(7.35,1.55,'reader asks: “what should we do?”',ha='center',fontsize=9.5,color=INK,style='italic')
box(ax,1.5,0.4,7.0,0.7,'The test: does the report end in a RECOMMENDATION? → analytical rules apply',fc=TINT,tc=INK,fs=10)
save(fig,'ch9_family.png')

# 2 — pyramid principle
fig, ax = plt.subplots(figsize=(8.6,4.0)); ax.set_xlim(0,10); ax.set_ylim(0,4.6); ax.axis('off')
box(ax,3.3,3.6,3.4,0.75,'THE ANSWER\n“Renew with TechServe”',fc=GREEN,fs=10)
for x,t in [(0.9,'Cost:\nsaves $22K/yr'),(3.9,'Risk:\nswitching costs\nexceed savings'),(6.9,'Quality:\nsupport beats\nall bidders')]:
    box(ax,x,2.1,2.3,1.0,t,fc=MOSS,fs=9.5)
    arr(ax,x+1.15,3.15,5.0,3.55)
for x in [0.9,3.9,6.9]:
    box(ax,x,0.7,2.3,1.0,'evidence · data\nexhibits · sources',fc=TINT,tc=INK,fs=9.5)
    arr(ax,x+1.15,1.75,x+1.15,2.05)
ax.text(5.0,4.5,'The pyramid: answer first, grouped reasons beneath, evidence beneath those (Minto)',ha='center',fontsize=11,color=GREEN,weight='bold')
save(fig,'ch9_pyramid.png')

# 3 — progress report skeleton
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
rows=[('STATUS LINE','“On track for Aug 16 go-live” — or not; one sentence, no suspense',GREEN),
      ('DONE','completed since last report, with dates',MOSS),
      ('IN PROGRESS','current work, expected completion',MOSS),
      ('BLOCKED / RISKS','what threatens the date, what you’re doing, what you need',PROOF),
      ('NEXT + ASK','next period’s plan; any decision needed from the reader',GREEN)]
y=3.4
for t,sub,c in rows:
    box(ax,0.4,y,2.6,0.6,t,fc=c,fs=9.5)
    ax.text(3.25,y+0.3,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.76
save(fig,'ch9_progress.png')

# 4 — table vs chart chooser
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
box(ax,0.3,2.2,4.5,1.3,'TABLE when readers need\nEXACT VALUES\nlookup · comparison of specifics ·\naudit trails',fc=GREEN,fs=10)
box(ax,5.2,2.2,4.5,1.3,'CHART when readers need\nTHE SHAPE\ntrend · proportion · outlier ·\ncomparison at a glance',fc=MOSS,fs=10)
box(ax,0.3,0.5,9.4,1.2,'EITHER WAY: title states the takeaway (“Response times fell 41%”), units labeled,\nsource named, axis starts at zero unless clearly marked — the display makes ONE point',fc=TINT,tc=INK,fs=10)
save(fig,'ch9_tablechart.png')

# 5 — incident report anatomy
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
rows=[('WHAT HAPPENED','facts in time order, actors named (Ch. 3’s active voice)',GREEN),
      ('IMPACT','what it cost: injuries, downtime, product, exposure',MOSS),
      ('ROOT CAUSE','why — the honest chain, not the convenient stop',MOSS),
      ('CORRECTIVE ACTIONS','owner + date for each; “identified” is not “assigned”',GREEN),
      ('PREVENTION','the system change that makes recurrence hard',GOLD)]
y=3.4
for t,sub,c in rows:
    box(ax,0.4,y,3.0,0.6,t,fc=c,fs=9.5)
    ax.text(3.65,y+0.3,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.76
save(fig,'ch9_incident.png')

# 6 — minutes that matter
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
box(ax,0.3,1.6,4.5,1.3,'TRANSCRIPT MINUTES\nwho said what, in order —\nlong, late, unread,\noccasionally dangerous',fc='#F1E9E7',tc=INK,fs=10)
box(ax,5.2,1.6,4.5,1.3,'DECISION MINUTES\ndecisions · owners · deadlines ·\nopen questions — one page,\nsent same day',fc=GREEN,fs=10)
arr(ax,4.85,2.2,5.15,2.2,c=GOLD)
ax.text(5.0,0.9,'Nobody needs the debate reconstructed; everybody needs to know what was decided and who owns it.',ha='center',fontsize=9.5,color=INK,style='italic')
save(fig,'ch9_minutes.png')

# 7 — the report pipeline
fig, ax = plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
steps=[('DEFINE','the question the\nreport answers'),('GATHER','data, sources,\nevidence'),('CONCLUDE','the answer —\nBEFORE structuring'),('PYRAMID','answer → reasons →\nevidence'),('DRAFT+REVISE','Chapters 3–4,\napplied')]
for j,(t,sub) in enumerate(steps):
    box(ax,0.3+j*1.96,1.6,1.75,0.95,t,fc=GREEN if j%2==0 else MOSS,fs=9.5)
    ax.text(0.3+j*1.96+0.875,1.4,sub,ha='center',va='top',fontsize=9.3,color=INK)
    if j<4: arr(ax,0.3+j*1.96+1.77,2.07,0.3+(j+1)*1.96-0.02,2.07)
ax.text(5.0,3.05,'Reports are built backward: conclude first, then structure the case',ha='center',fontsize=11.5,color=GREEN,weight='bold')
save(fig,'ch9_pipeline.png')
print('ch9 figures complete')
