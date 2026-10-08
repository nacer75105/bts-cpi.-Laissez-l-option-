import math, os, xml.dom.minidom as md
ICI = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ICI, '..', '..', 'app.py'), encoding='utf-8').read()
g = {'math': math}
head = src[:src.index('def projection_europeenne')]
exec(head[head.index('TRAIT = '):], g)
for nom in ('def fr(', 'def _fr_court', 'def _k_defs', 'def _k_fl', 'def _k_apparait', 'def _diag('):
    i = src.index(nom); j = src.index('\ndef ', i + 10); exec(src[i:j], g)
exec(open(os.path.join(ICI, 'brouillon_12_9.py'), encoding='utf-8').read(), g)
out = {}
for k, (t, f) in g['FIGURES_NOUVELLES'].items():
    s = f(); md.parseString(s); out[k] = s
os.makedirs(os.path.join(ICI, 'figs129'), exist_ok=True)
open(os.path.join(ICI, 'figs129', 'index.html'), 'w', encoding='utf-8').write(
    '<html><body style="background:#fff">' + ''.join(f'<h4>{k}</h4>' + s for k, s in out.items()) + '</body></html>')
print('OK', len(out))
