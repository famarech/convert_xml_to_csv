import xml.etree.ElementTree as ET
from os.path import abspath

def how_many(root):
    number = 0
    for r in root:
        number += 1
    return number

def labels(root):
    labels = []
    for r in root.iter():
        labels.append(r.tag)
    return list(set(labels))

def unordered_data(root):
    unordered = []
    for i in range(how_many(root)):
        dict_temp = {}
        for r in root[i].iter():
            if r.text[0] != '\n':
                dict_temp[r.tag] = r.text
        unordered.append(dict_temp)
    return unordered

def ordered_data(root):
    ordered = []
    l = labels(root)
    unordered = unordered_data(root)
    for i in range(how_many(root)):
        temp = ['']*len(l)
        for k, v in unordered[i].items():
            column = l.index(k)
            temp[column] = v
        ordered.append(temp)
    return ordered

def main(file_out):
    file_in = abspath('./datas.csv')
    tree = ET.parse(file_out)
    root = tree.getroot()

    with open(file_in, 'w') as f:
        f.write(';'.join(labels(root)))
        f.write('\n')
        for line in ordered_data(root):
            f.write(';'.join(line))
            f.write('\n')

file_out = abspath('./datas.xml')
main(file_out)