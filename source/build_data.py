import re, json, sys

TOPIC = re.compile(r'^\*\*((?:P)?\d+(?:\.\d+)*)\s+(.+?)\*\*\s*(.*)$')
OL = re.compile(r'^(\d+)\.\s+(.*)$')


def parse_blocks(lines):
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        l = lines[i].rstrip()
        if not l.strip() or l.strip() == '---':
            i += 1
            continue
        if l.startswith('|'):
            rows = []
            while i < n and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append({'t': 'table', 'rows': rows})
            continue
        if re.match(r'^\s*- ', l) or OL.match(l):
            ordered = bool(OL.match(l))
            items = []
            while i < n:
                s = lines[i].rstrip()
                if not s.strip():
                    break
                m1 = re.match(r'^(\s*)- (.*)$', s)
                m2 = OL.match(s)
                if m1:
                    depth = len(m1.group(1)) // 2
                    txt = m1.group(2)
                elif m2 and not ordered is False:
                    depth = 0
                    txt = m2.group(2)
                elif m2:
                    break
                else:
                    break
                it = {'x': txt}
                if depth:
                    it['d'] = depth
                tm = TOPIC.match(txt)
                if tm and not depth:
                    it['id'] = tm.group(1)
                    it['title'] = tm.group(2).rstrip(':;, ')
                    it['x'] = tm.group(3)
                items.append(it)
                i += 1
            blocks.append({'t': 'ol' if ordered else 'ul', 'items': items})
            continue
        if l.startswith('*') and not l.startswith('**'):
            blocks.append({'t': 'meta', 'x': l})
            i += 1
            continue
        buf = [l]
        i += 1
        while i < n and lines[i].strip() and not lines[i].startswith(('|', '- ', '*', '#')) and not OL.match(lines[i]):
            buf.append(lines[i].rstrip())
            i += 1
        blocks.append({'t': 'p', 'x': ' '.join(buf)})
    return blocks


def count_topics(blocks):
    return sum(1 for b in blocks if b['t'] in ('ul', 'ol') for it in b['items'] if 'id' in it)


def split_h(lines, prefix):
    secs = []
    cur = None
    for l in lines:
        if l.startswith(prefix) and not l.startswith(prefix + '#'):
            cur = {'h': l[len(prefix):].strip(), 'lines': []}
            secs.append(cur)
        elif cur is None:
            secs.append({'h': None, 'lines': [l]}) if not secs else secs[0]['lines'].append(l)
        else:
            cur['lines'].append(l)
    return secs


def parse_volume(vid, md, title, tag, letter):
    lines = md.split('\n')
    # drop h1
    h1 = lines[0].lstrip('# ').strip() if lines and lines[0].startswith('# ') else title
    body = lines[1:] if lines and lines[0].startswith('# ') else lines
    parts_raw = split_h(body, '## ')
    intro_lines = []
    parts = []
    pnum = 0
    unmatched = []
    for sec in parts_raw:
        if sec['h'] is None:
            intro_lines = sec['lines']
            continue
        m = re.match(r'^Part (\d+):\s*(.*)$', sec['h'])
        if m:
            num = int(m.group(1)); ptitle = m.group(2)
        else:
            num = 0 if not any(p['num'] == 0 for p in parts) else 100 + len(parts)
            ptitle = sec['h']
            unmatched.append(sec['h'])
        pid = f'{vid}-{num}'
        mods = split_h(sec['lines'], '### ')
        pages = []
        over = []
        k = 0
        for mm in mods:
            if mm['h'] is None:
                over = mm['lines']
                continue
            k += 1
            bl = parse_blocks(mm['lines'])
            pages.append({'id': f'{pid}-{k}', 'title': mm['h'], 'blocks': bl, 'topics': count_topics(bl)})
        obl = parse_blocks(over)
        parts.append({'id': pid, 'num': num, 'title': ptitle, 'over': obl, 'pages': pages,
                      'topics': count_topics(obl) + sum(p['topics'] for p in pages)})
    return {'id': vid, 'letter': letter, 'title': title, 'tag': tag, 'intro': parse_blocks(intro_lines), 'parts': parts}, unmatched


def main():
    ai = open('ai-product-leader.md').read()
    cc = open('claude-code.md').read()
    ex = open('start-and-elite.md').read()
    exs = ex.split('\n# ')
    start = exs[0]
    elite = '# ' + exs[1]
    vols = []
    unm = {}
    for vid, md, title, tag, letter in [
        ('s', start, 'Start here', 'Orientation, bridge, tracks and freshness', '0'),
        ('a', ai, 'AI Product Leader', 'Volume A', 'A'),
        ('b', cc, 'Claude Code Mastery', 'Volume B', 'B'),
        ('c', elite, 'The Elite Layer', 'Volume C', 'C'),
    ]:
        v, u = parse_volume(vid, md, title, tag, letter)
        vols.append(v)
        unm[vid] = u
    json.dump({'vols': vols}, open('../data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    for v in vols:
        tp = sum(p['topics'] for p in v['parts'])
        pg = sum(len(p['pages']) + 1 for p in v['parts'])
        print(v['id'], v['title'], 'parts', len(v['parts']), 'pages', pg, 'topics', tp, 'unmatched', unm[v['id']])


main()
