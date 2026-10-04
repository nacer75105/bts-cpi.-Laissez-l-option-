import math, os, xml.dom.minidom as md
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ICI, '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait', 'def _diag('):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open(os.path.join(ICI, 'brouillon_6_21.py'), encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
for _l, cf in g['_CONFIGS']:
    for N in (500.0, 3000.0):
        for mb in (2.0, 20.0):
            s = g['dyn_balourd'](cf, N, mb); md.parseString(s); out[f'dyn_{cf}_{N}_{mb}'] = s
os.makedirs(os.path.join(ICI, 'figs21'), exist_ok=True)
html = '<html><body style="background:#fff">' + ''.join(f'<h4>{k}</h4>' + s for k, s in out.items()
    if not k.startswith('dyn_') or k in ('dyn_statique_3000.0_20.0', 'dyn_dynamique_3000.0_20.0', 'dyn_equilibre_500.0_2.0')) + '</body></html>'
open(os.path.join(ICI, 'figs21', 'index.html'), 'w', encoding='utf-8').write(html)
exec("import random\n" + g['GENERATEUR'], g)
for nom in ('gen_force_balourd', 'gen_cdg_arbre'):
    for _ in range(2000):
        x = g[nom]()
        for dd in x['diag']:
            assert abs(dd['v'] - x['rep']) > x['tol'], (x, dd)
print('OK', len(out))
