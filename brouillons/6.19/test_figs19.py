import math, os, xml.dom.minidom as md
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait'):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open('brouillon_6_19.py', encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
for r_ in ('6205', 'NU205'):
    for P_ in (0.5, 2.0, 6.0):
        for N_ in (300.0, 1500.0, 3000.0):
            s = g['dyn_duree_roulement'](r_, P_, N_); md.parseString(s); out[f'dyn_{r_}_{P_}_{int(N_)}'] = s
os.makedirs('figs19', exist_ok=True)
for k, s in out.items():
    open(f'figs19/{k}.svg', 'w', encoding='utf-8').write(s)
html = '<html><body style="background:#fff">' + ''.join(
    f'<h4>{k}</h4>' + s for k, s in out.items()
    if not k.startswith('dyn_') or k in ('dyn_6205_2.0_1500','dyn_NU205_2.0_1500')) + '</body></html>'
open('figs19/index.html', 'w', encoding='utf-8').write(html)
print('OK', len(out))
