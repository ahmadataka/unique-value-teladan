"""Add clickable links to named text shapes in the exported lesson deck."""
import json
from pathlib import Path
import sys
import zipfile
import xml.etree.ElementTree as ET

P = 'http://schemas.openxmlformats.org/presentationml/2006/main'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
PKG = 'http://schemas.openxmlformats.org/package/2006/relationships'
ET.register_namespace('p', P)
ET.register_namespace('a', A)
ET.register_namespace('r', R)

src = Path(sys.argv[1])
links = json.loads(Path(sys.argv[2]).read_text())
with zipfile.ZipFile(src) as z:
    data = {n: z.read(n) for n in z.namelist()}
for item in links:
    name = f'ppt/slides/slide{item["slide"]}.xml'
    relname = f'ppt/slides/_rels/slide{item["slide"]}.xml.rels'
    tree = ET.fromstring(data[name])
    rels = ET.fromstring(data[relname]) if relname in data else ET.Element(f'{{{PKG}}}Relationships')
    used = {e.get('Id') for e in rels}
    count = 1
    while f'rIdLink{count}' in used:
        count += 1
    rid = f'rIdLink{count}'
    target = next(s for s in tree.findall(f'.//{{{P}}}sp')
                  if s.find(f'{{{P}}}nvSpPr/{{{P}}}cNvPr').get('name') == item['name'])
    for run in target.findall(f'.//{{{A}}}r'):
        props = run.find(f'{{{A}}}rPr')
        if props is None:
            props = ET.Element(f'{{{A}}}rPr')
            run.insert(0, props)
        ET.SubElement(props, f'{{{A}}}hlinkClick', {f'{{{R}}}id': rid})
    ET.SubElement(rels, f'{{{PKG}}}Relationship', {
        'Id': rid, 'Type': R + '/hyperlink', 'Target': item['url'], 'TargetMode': 'External'})
    data[name] = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
    data[relname] = ET.tostring(rels, encoding='utf-8', xml_declaration=True)
tmp = src.with_suffix('.linked.pptx')
with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as z:
    for name, content in data.items():
        z.writestr(name, content)
tmp.replace(src)
print(f'Added {len(links)} hyperlinks')
