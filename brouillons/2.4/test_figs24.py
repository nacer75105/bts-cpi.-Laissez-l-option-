import math, os, xml.dom.minidom as md
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ICI, '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait', 'def _diag('):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open(os.path.join(ICI, 'brouillon_2_4.py'), encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
for D in (11.0, 11.12, 11.27):
    for e in (0.0, 0.18, 0.23, 0.35):
        s = g['dyn_bonus_mm'](D, e); md.parseString(s); out[f'dyn_{D}_{e}'] = s
os.makedirs(os.path.join(ICI, 'figs24'), exist_ok=True)
html = '<html><body style="background:#fff">' + ''.join(f'<h4>{k}</h4>' + s for k, s in out.items()
    if not k.startswith('dyn_') or k in ('dyn_11.12_0.23', 'dyn_11.0_0.23', 'dyn_11.27_0.35')) + '</body></html>'
open(os.path.join(ICI, 'figs24', 'index.html'), 'w', encoding='utf-8').write(html)
exec("import random\n" + g['GENERATEUR'], g)
for _ in range(2000):
    x = g['gen_bonus_mmr']()
    for dd in x['diag']:
        assert abs(dd['v'] - x['rep']) > x['tol'], (x, dd)
print('OK', len(out))
