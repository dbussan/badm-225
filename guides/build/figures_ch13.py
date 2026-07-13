# Original figures for Chapter 13 — The Job Search and Résumés in the Digital Age
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

# 1 — campaign vs volume
fig, ax = plt.subplots(figsize=(8.6,3.8)); ax.set_xlim(0,10); ax.set_ylim(0,4.4); ax.axis('off')
ax.text(5.0,4.1,'TWO WAYS TO RUN A SEARCH',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.1,4.3,2.5,'THE VOLUME GAME\n\nsame résumé to 200 postings\nno research → no tailoring → no signal\ncompeting at the funnel’s widest point\nfeels productive; converts at\nlottery rates',fc='#F7EAE8',tc=PROOF,fs=9.6)
box(ax,5.3,1.1,4.3,2.5,'THE CAMPAIGN\n\n15–25 researched targets that fit\neach application tailored to the\nposting’s own language\nwarm paths hunted before portals\nslower per app · far better per offer',fc=GREEN,fs=9.6)
box(ax,0.4,0.2,9.2,0.6,'Three tailored applications a week, every week, beats thirty in a panicked weekend.',fc=TINT,tc=INK,fs=9.6)
save(fig,'ch13_campaign.png')

# 2 — the seven-second scan
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
ax.text(5.0,3.7,'THE FIRST READ IS A ~7-SECOND SCAN — design for where the eyes go',ha='center',fontsize=11.5,color=GREEN,weight='bold')
rows=[('TOP THIRD','name · summary line · current title — the scan’s home base',GREEN),
      ('LEFT EDGE','job titles, employers, dates, bolded lead-ins — the F-pattern’s rail',MOSS),
      ('NUMBERS','“38%”, “$12K”, “team of 6” — digits catch scanning eyes; adjectives don’t',GREEN),
      ('EVERYTHING ELSE','read only if the scan earns a second pass — never load-bearing',MOSS)]
y=3.0
for t,sub,c in rows:
    box(ax,0.4,y,2.6,0.58,t,fc=c,fs=9.8)
    ax.text(3.25,y+0.29,sub,ha='left',va='center',fontsize=9.5,color=INK)
    y-=0.72
save(fig,'ch13_scan.png')

# 3 — achievement bullet formula
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
ax.text(5.0,3.3,'THE ACHIEVEMENT BULLET — verb, task, measurable result',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.8,2.7,0.9,'ACTION VERB\n“Cut…”',fc=GREEN,fs=10)
box(ax,3.4,1.8,3.0,0.9,'THE TASK\n“…intake errors by redesigning\nthe tracking checklist…”',fc=MOSS,fs=9.4)
box(ax,6.7,1.8,2.9,0.9,'THE RESULT\n“…errors down 38%,\nzero audit findings”',fc=GREEN,fs=9.6)
arr(ax,3.1,2.25,3.4,2.25); arr(ax,6.4,2.25,6.7,2.25)
box(ax,0.4,0.35,9.2,1.0,'DUTY BULLET: “Responsible for quality documentation” — any holder of the job could write it.\nACHIEVEMENT BULLET: only YOU can write it. That is the entire difference.',fc=TINT,tc=INK,fs=9.7)
save(fig,'ch13_bullet.png')

# 4 — ATS pipeline
fig, ax = plt.subplots(figsize=(8.6,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
ax.text(5.0,3.3,'HOW THE ATS ACTUALLY READS YOU',ha='center',fontsize=11.5,color=GREEN,weight='bold')
steps=[('PARSE','your file becomes\na database record'),('MATCH','recruiters search\nkeywords + filters'),('RANK','high-match records\nsurface; others never do'),('HUMAN SCAN','the 7-second read —\nonly now')]
x=0.4; w=2.2
for si,(t,sub) in enumerate(steps):
    box(ax,x,1.7,w,0.9,t,fc=GREEN,fs=9.8)
    ax.text(x+w/2,1.22,sub,ha='center',va='center',fontsize=9.3,color=INK)
    if si<len(steps)-1: arr(ax,x+w,2.15,x+w+0.13,2.15)
    x+=w+0.13
box(ax,0.4,0.25,9.2,0.6,'Parse failure = invisibility: tables, text boxes, headers, and graphics simply don’t exist in your record.',fc='#F7EAE8',tc=PROOF,fs=9.6)
save(fig,'ch13_ats.png')

# 5 — cover letter skeleton
fig, ax = plt.subplots(figsize=(8.6,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4.2); ax.axis('off')
rows=[('THE HOOK','their role + your thesis — why this fit is real (never “I am writing to apply”)',GREEN),
      ('THE EVIDENCE','two proofs from your record, aimed at their two biggest needs',MOSS),
      ('THE COMPANY CLAUSE','one sentence proving you researched THEM — the anti-mail-merge signal',GREEN),
      ('THE CLOSE','confident ask for the conversation + logistics',MOSS)]
y=3.3
for t,sub,c in rows:
    box(ax,0.4,y,3.0,0.62,t,fc=c,fs=9.8)
    ax.text(3.65,y+0.31,sub,ha='left',va='center',fontsize=9.4,color=INK)
    y-=0.78
box(ax,0.4,0.25,9.2,0.6,'Three to four paragraphs, one page hard. A persuasive message (Chapter 8) where the product is you.',fc=TINT,tc=INK,fs=9.6)
save(fig,'ch13_coverletter.png')

# 6 — the consistency audit
fig, ax = plt.subplots(figsize=(8.6,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4.0); ax.axis('off')
ax.text(5.0,3.7,'THE CONSISTENCY AUDIT — the person online and on paper must be colleagues',ha='center',fontsize=11.5,color=GREEN,weight='bold')
box(ax,0.4,1.6,2.9,1.5,'THE RÉSUMÉ\ntitles · dates\nachievements\nthe paper story',fc=GREEN,fs=9.8)
box(ax,3.55,1.6,2.9,1.5,'THE PROFILE\nheadline · about\nactivity · photo\nthe searchable story',fc=MOSS,fs=9.8)
box(ax,6.7,1.6,2.9,1.5,'THE SEARCH RESULTS\npage one, logged out —\nknow it before\nthey do',fc=GREEN,fs=9.8)
box(ax,0.4,0.45,9.2,0.75,'Dates and titles must MATCH: discrepancies read as dishonesty even when they’re sloppiness.\nRecruiters cross-check as a screening step.',fc='#F7EAE8',tc=PROOF,fs=9.5)
save(fig,'ch13_audit.png')
print('ch13 figures complete')
