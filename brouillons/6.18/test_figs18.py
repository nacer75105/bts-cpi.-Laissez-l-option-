import math, os, xml.dom.minidom as md
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait'):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open('brouillon_6_18.py', encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
for P_ in (2.0, 4.0, 8.0):
    for nf_ in (1.0, 2.0, 3.0, 4.0):
        for f_ in (0.05, 0.15, 0.3):
            s = g['dyn_vis_ecrou'](P_, nf_, 300.0, f_); md.parseString(s); out[f'dyn_{int(P_)}_{int(nf_)}_{f_}'] = s
os.makedirs('figs18', exist_ok=True)
for k, s in out.items():
    open(f'figs18/{k}.svg', 'w', encoding='utf-8').write(s)
html = '<html><body style="background:#fff">' + ''.join(
    f'<h4>{k}</h4>' + s for k, s in out.items()
    if not k.startswith('dyn_') or k in ('dyn_4_1_0.15','dyn_4_3_0.15','dyn_8_4_0.05')) + '</body></html>'
open('figs18/index.html', 'w', encoding='utf-8').write(html)
print('OK', len(out))
