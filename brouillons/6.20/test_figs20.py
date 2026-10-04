import math, os, xml.dom.minidom as md
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ICI, '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait', 'def _diag('):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open(os.path.join(ICI, 'brouillon_6_20.py'), encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
for ch, _v in g['_CHOIX_CHARGES']:
    for C0 in (5.0, 18.0, 30.0, 40.0):
        s = g['dyn_point_fonctionnement'](ch, C0); md.parseString(s); out[f'dyn_{ch[:5]}_{C0}'] = s
os.makedirs(os.path.join(ICI, 'figs20'), exist_ok=True)
html = '<html><body style="background:#fff">' + ''.join(f'<h4>{k}</h4>' + s for k, s in out.items()
    if not k.startswith('dyn_') or k in ('dyn_Quadr_18.0', 'dyn_Hyper_40.0')) + '</body></html>'
open(os.path.join(ICI, 'figs20', 'index.html'), 'w', encoding='utf-8').write(html)
exec("import random\n" + g['GENERATEUR'], g)
for nom in ('gen_point_fonctionnement', 'gen_pompe_hydraulique'):
    for _ in range(2000):
        x = g[nom]()
        for dd in x['diag']:
            assert abs(dd['v'] - x['rep']) > x['tol'], (x, dd)
print('OK', len(out))
