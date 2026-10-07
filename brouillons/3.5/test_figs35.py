import math, os, xml.dom.minidom as md
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ICI, '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait', 'def _diag('):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open(os.path.join(ICI, 'brouillon_3_5.py'), encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
for sg in (60.0, 140.0, 260.0):
    for Kt in (1.0, 2.5, 3.0):
        s = g['dyn_fatigue'](sg, Kt); md.parseString(s); out[f'dyn_{sg}_{Kt}'] = s
os.makedirs(os.path.join(ICI, 'figs35'), exist_ok=True)
html = '<html><body style="background:#fff">' + ''.join(f'<h4>{k}</h4>' + s for k, s in out.items()
    if not k.startswith('dyn_') or k in ('dyn_140.0_2.5', 'dyn_60.0_1.0')) + '</body></html>'
open(os.path.join(ICI, 'figs35', 'index.html'), 'w', encoding='utf-8').write(html)
exec("import random\n" + g['GENERATEUR'], g)
for nom in ('gen_charpy_energie', 'gen_flexion_3points'):
    for _ in range(2000):
        x = g[nom]()
        for dd in x['diag']:
            assert abs(dd['v'] - x['rep']) > x['tol'], (x, dd)
print('OK', len(out))
