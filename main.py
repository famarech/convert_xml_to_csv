import xml.etree.ElementTree as ET
from os.path import abspath


def erase_duplicate(tab):
    tab.sort()
    i = len(tab) - 1
    while i > 0:
        if tab[i - 1] == tab[i]:
            del tab[i]
        i -= 1
    return tab



file = abspath('./datas.xml')

tree = ET.parse(file)
root = tree.getroot()

RANK = 0
MARKS = []

def level(root, count, mark):
    global RANK
    global MARKS
    count += 1
    mark = mark + ' ' + root.tag
    for r in root:
        if r.tag != '':
            if count == RANK:
                MARKS.append(mark + ' ' + r.tag)
            if count > RANK:
                RANK += 1
            level(r, count, mark)
    return count

level(root, 0, '')
l = erase_duplicate(MARKS)
for each in l:
    print(each)