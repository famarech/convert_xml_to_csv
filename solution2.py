import xml.etree.ElementTree as ET
import csv
from os.path import abspath

csv_name = 'xcsv_test.csv'

xml_data = '''
<livres>
    <livre>
        <nom>
            Tintin et milou
            <auteur>Hergé</auteur>
        </nom>
    </livre>
    <livre>
        <nom>
            Les aventures de Titi
            <auteur>Lui</auteur>
        </nom>
    </livre>
</livres>'''


root =  ET.XML(xml_data)

data1 = []
data2 = {}
first_tag = ''
k=0

for child in root.iter():
    t = child.tag

    if(child.keys()):
        for attr in child.keys(): t += ' {} = {}'.format(attr,child.get(attr))

    if(t not in data1): data1.append(t)

    if(child.text):
        if len(child.text.split()) > 0:
            if(first_tag == ''):
                first_tag = t
                data2[k] = []
            else:
                if(t == first_tag):
                    k += 1
                    data2[k] = []

            t = child.text.lstrip().rstrip()
            data2[k].append(t)

with open(csv_name, 'w', newline = '') as csvfile:
    _writer = csv.writer(csvfile, delimiter=';')
    _writer.writerow(data1)
    for data in data2.values(): _writer.writerow(data)