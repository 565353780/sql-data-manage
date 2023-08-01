from itertools import takewhile, repeat


def getLineNum(txt_file_path):
    buffer = 1024 * 1024
    with open(txt_file_path, 'r', encoding='utf-8') as f:
        buf_gen = takewhile(lambda x: x, (f.read(buffer)
                                          for _ in repeat(None)))
        return sum(buf.count('\n') for buf in buf_gen)


def splitLineData(line_data, remove_quotes=False):
    if remove_quotes:
        line_data = line_data.replace('"', '')

    return line_data.split('\n')[0].split('\t')
