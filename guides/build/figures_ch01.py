# Original figures for the Chapter 1 study guide — course palette, clean flat style.
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

GREEN='#0E4D33'; MOSS='#5C8A6E'; TINT='#EAF1EB'; GOLD='#8A6410'; INK='#212A26'; PROOF='#B23A31'
OUT = os.path.join(os.path.dirname(__file__), 'fig')
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'font.family':'Calibri','font.size':11})

def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=160, bbox_inches='tight', facecolor='white')
    plt.close(fig); print('fig:', name)

def box(ax, x, y, w, h, text, fc=GREEN, tc='white', fs=11, ec='none'):
    ax.add_patch(FancyBboxPatch((x,y), w, h, boxstyle='round,pad=0.02,rounding_size=0.04',
                 fc=fc, ec=ec, lw=1.2))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', color=tc, fontsize=fs, wrap=True)

def arrow(ax, x1, y1, x2, y2, color=INK, style='-|>'):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2), arrowstyle=style, mutation_scale=16,
                 color=color, lw=1.8))

# 1 — communication process loop
fig, ax = plt.subplots(figsize=(8.6, 3.4)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
steps = [('Sender\nhas an idea',0.2),('Encodes it\ninto words',2.2),('Transmits via\na channel',4.2),
         ('Receiver\ndecodes it',6.2),('Meaning is\nreconstructed',8.2)]
for i,(t,x) in enumerate(steps):
    box(ax, x, 2.2, 1.6, 1.3, t, fc=GREEN if i%2==0 else MOSS)
    if i < 4: arrow(ax, x+1.62, 2.85, x+2.18, 2.85)
box(ax, 2.2, 0.3, 5.6, 0.9, 'FEEDBACK — the return message that reveals what actually landed', fc=TINT, tc=INK)
arrow(ax, 7.0, 1.25, 8.6, 2.15, color=GREEN); arrow(ax, 2.2, 0.75, 0.9, 2.15, color=GREEN)
ax.text(5.0, 3.85, 'NOISE (physical · semantic · psychological) can strike at every stage',
        ha='center', color=PROOF, fontsize=10.5, style='italic')
save(fig, 'process.png')

# 2 — media richness continuum
fig, ax = plt.subplots(figsize=(8.6, 2.6)); ax.set_xlim(0,10); ax.set_ylim(0,3); ax.axis('off')
chans=[('Face-to-face',GREEN),('Video call',GREEN),('Phone call',MOSS),('Email / memo',MOSS),('Text / chat','#8FA89A')]
for i,(c,col) in enumerate(chans):
    box(ax, 0.2+i*1.95, 1.2, 1.75, 0.95, c, fc=col, fs=10.5)
arrow(ax, 0.3, 0.55, 9.7, 0.55, color=GOLD)
ax.text(0.3, 0.15, 'RICHEST — carries tone, expression, instant feedback', fontsize=9.5, color=INK)
ax.text(9.7, 0.15, 'LEANEST — fast, documented,\neasily misread', fontsize=9.5, color=INK, ha='right')
ax.text(5.0, 2.55, 'The media richness continuum', ha='center', fontsize=12, color=GREEN, weight='bold')
save(fig, 'richness.png')

# 3 — channel choice matrix
fig, ax = plt.subplots(figsize=(7.2, 4.6)); ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
ax.add_patch(Rectangle((1.2,1.2),8.4,8.0, fc='white', ec=INK, lw=1.2))
ax.plot([5.4,5.4],[1.2,9.2], color=INK, lw=1); ax.plot([1.2,9.2],[5.2,5.2], color=INK, lw=1)
cells = [(1.4,5.4,'Routine + no record needed:\nchat or quick call',TINT),
         (5.6,5.4,'Sensitive or complex:\nrich channel FIRST\n(face-to-face / video)',GREEN),
         (1.4,1.4,'Routine + record needed:\nemail or memo',TINT),
         (5.6,1.4,'Sensitive AND binding:\nrich conversation,\nthen written confirmation',MOSS)]
for x,y,t,c in cells:
    box(ax, x, y, 3.6, 3.6, t, fc=c, tc=('white' if c in (GREEN,MOSS) else INK), fs=10.5)
ax.text(5.3, 0.5, 'Need for a permanent record →', ha='center', fontsize=11, color=INK)
ax.text(0.55, 5.2, '← Sensitivity / complexity', va='center', rotation=90, fontsize=11, color=INK)
save(fig, 'matrix.png')

# 4 — listening stages with leak
fig, ax = plt.subplots(figsize=(8.6, 2.9)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
st=[('Hear','passive'),('Focus','attention\nchooses'),('Interpret','meaning\nassigned'),('Evaluate','fact vs.\nopinion'),('Respond\n& retain','what you\nkeep')]
for i,(t,sub) in enumerate(st):
    box(ax, 0.2+i*1.95, 1.5, 1.75, 1.1, t, fc=GREEN if i%2==0 else MOSS, fs=11)
    ax.text(0.2+i*1.95+0.875, 1.15, sub, ha='center', va='top', fontsize=9, color=INK)
    if i<4: arrow(ax, 0.2+i*1.95+1.77, 2.05, 0.2+(i+1)*1.95-0.02, 2.05)
ax.text(5.0, 3.1, 'Listening fails silently in the middle stages — you can nod while interpreting wrongly',
        ha='center', fontsize=10.5, color=PROOF, style='italic')
save(fig, 'listening.png')

# 5 — noise types
fig, ax = plt.subplots(figsize=(8.6, 2.5)); ax.set_xlim(0,10); ax.set_ylim(0,3); ax.axis('off')
noise=[('PHYSICAL','Loud vent, bad connection,\ncluttered slide — fix the\nenvironment or channel'),
       ('SEMANTIC','Jargon, vague wording —\nfix the words for THIS\naudience'),
       ('PSYCHOLOGICAL','Stress, bias, distraction —\nfix timing, tone, and trust')]
for i,(t,d) in enumerate(noise):
    box(ax, 0.3+i*3.25, 1.5, 2.95, 1.1, t, fc=GREEN, fs=12)
    ax.text(0.3+i*3.25+1.475, 1.3, d, ha='center', va='top', fontsize=9.5, color=INK)
save(fig, 'noise.png')

# 6 — context cultures continuum
fig, ax = plt.subplots(figsize=(8.6, 2.7)); ax.set_xlim(0,10); ax.set_ylim(0,3.2); ax.axis('off')
ax.add_patch(Rectangle((0.4,1.4),9.2,0.7, fc=TINT, ec=INK, lw=1))
ax.add_patch(Rectangle((0.4,1.4),4.6,0.7, fc=MOSS, ec='none'))
ax.text(2.7,1.75,'LOW-CONTEXT', ha='center', va='center', color='white', weight='bold')
ax.text(7.4,1.75,'HIGH-CONTEXT', ha='center', va='center', color=INK, weight='bold')
ax.text(0.4,0.95,'Meaning lives in the explicit words · directness = respect · the contract carries the weight',
        fontsize=9.5, color=INK)
ax.text(9.6,2.5,'Meaning rides on relationship, tone, situation · indirectness = respect · trust carries the weight',
        fontsize=9.5, color=INK, ha='right')
ax.text(5.0, 3.0, 'Hall’s context continuum (Beyond Culture, 1976)', ha='center', fontsize=11.5, color=GREEN, weight='bold')
save(fig, 'context.png')
print('all figures done')
