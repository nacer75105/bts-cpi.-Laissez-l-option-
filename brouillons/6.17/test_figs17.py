import math, os, xml.dom.minidom as md
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait'):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open('brouillon_6_17.py', encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
for a_ in ('rot','la','pg','piv'):
    for b_ in ('rot','la','pg','piv'):
        s = g['dyn_arbre_deux_paliers'](a_, b_); md.parseString(s); out[f'dyn_{a_}_{b_}'] = s
import shutil; os.makedirs('figs17', exist_ok=True)
for k, s in out.items():
    open(f'figs17/{k}.svg', 'w', encoding='utf-8').write(s)
html = '<html><body style="background:#fff">' + ''.join(
    f'<h4>{k}</h4>' + s for k, s in out.items()
    if not k.startswith('dyn_') or k in ('dyn_rot_la','dyn_pg_pg','dyn_piv_piv')) + '</body></html>'
open('figs17/index.html', 'w', encoding='utf-8').write(html)
print('OK', len(out))
