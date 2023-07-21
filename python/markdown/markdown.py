import re


def parse(markdown):
    lines = markdown.split('\n')
    html = ''
    for i, line in enumerate(lines):
        if line.startswith('#'):
            html += heading(line)
        elif line.startswith('*'):
            html += listitem(i, lines)
        elif len(line) > 0:
            html += paragraph(line)
        else:
            continue
    html = add_inline_styles(html)
    return html

def heading(line):
    m = re.match(r'^(#*)\s{1}(.*)', line)
    level = len(m.group(1))
    return f'<h{level}>{m.group(2)}</h{level}>'

def listitem(i, lines):
    html = ''
    if i == 0 or not lines[i-1].startswith('*'):
        html += '<ul>'
    html += f'<li>{lines[i][2:]}</li>'
    if i + 1 == len(lines) or not lines[i+1].startswith('*'):
        html += '</ul>'
    return html

def paragraph(line):
    return f'<p>{line}</p>'
    
def add_inline_styles(html):
    p1 = re.compile(r'(.*?)__(.+?)__(.*?)')
    html = p1.sub(r'\1<strong>\2</strong>\3', html)
    p2 = re.compile(r'(.*?)_(.+?)_(.*?)')
    html = p2.sub(r'\1<em>\2</em>\3', html)
    return html
