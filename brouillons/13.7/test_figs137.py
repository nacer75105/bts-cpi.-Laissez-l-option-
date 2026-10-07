import math, os, xml.dom.minidom as md
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ICI, '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait', 'def _diag('):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open(os.path.join(ICI, 'brouillon_13_7.py'), encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
for R in (5.0, 20.0, 50.0):
    for n in (8.0, 36.0, 200.0):
        s = g['dyn_facettes'](R, n); md.parseString(s); out[f'dyn_{R}_{n}'] = s
os.makedirs(os.path.join(ICI, 'figs137'), exist_ok=True)
html = '<html><body style="background:#fff">' + ''.join(f'<h4>{k}</h4>' + s for k, s in out.items()
    if not k.startswith('dyn_') or k in ('dyn_20.0_36.0', 'dyn_50.0_200.0')) + '</body></html>'
open(os.path.join(ICI, 'figs137', 'index.html'), 'w', encoding='utf-8').write(html)
exec("import random\n" + g['GENERATEUR'], g)
for nom in ('gen_seuil_rentabilite', 'gen_facettes_stl'):
    for _ in range(2000):
        x = g[nom]()
        for dd in x['diag']:
            assert abs(dd['v'] - x['rep']) > x['tol'], (x, dd)
print('OK', len(out))
