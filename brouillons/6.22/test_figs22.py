import math, os, xml.dom.minidom as md
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ICI, '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait', 'def _diag('):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open(os.path.join(ICI, 'brouillon_6_22.py'), encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
for D1 in (10.0, 40.0):
    for D2 in (50.0, 200.0):
        for F1 in (50.0, 500.0):
            s = g['dyn_presse'](D1, D2, F1); md.parseString(s); out[f'dyn_{D1}_{D2}_{F1}'] = s
os.makedirs(os.path.join(ICI, 'figs22'), exist_ok=True)
html = '<html><body style="background:#fff">' + ''.join(f'<h4>{k}</h4>' + s for k, s in out.items()
    if not k.startswith('dyn_') or k in ('dyn_10.0_200.0_500.0', 'dyn_40.0_50.0_50.0')) + '</body></html>'
open(os.path.join(ICI, 'figs22', 'index.html'), 'w', encoding='utf-8').write(html)
exec("import random\n" + g['GENERATEUR'], g)
for nom in ('gen_presse_hydraulique', 'gen_poussee_archimede'):
    for _ in range(2000):
        x = g[nom]()
        for dd in x['diag']:
            assert abs(dd['v'] - x['rep']) > x['tol'], (x, dd)
print('OK', len(out))
