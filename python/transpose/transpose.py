def transpose(lines):
    lines = lines.split('\n')
    transposed_lines = []
    m_length = max_length(lines)
    for i, line in enumerate(lines):
        max_to_right = max_length(lines[i:])
        if len(line) < max_to_right:
            lines[i] = line.ljust(max_to_right)
    for i in range(0,m_length):
        new_line = ''
        for line in lines:
            try:
                new_line += line[i]
            except IndexError:
                continue
        transposed_lines.append(new_line)
    return '\n'.join(transposed_lines)

def max_length(lines):
    return max(len(line) for line in lines)


