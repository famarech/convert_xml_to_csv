import json
import xmltodict

with open("datas.xml") as xmldatas:
    data = xmldatas.read()
xml_dict = xmltodict.parse(data)

# Conversion de OrderedDict en Dict
# Juste pour une meilleur lecture
xml_dict = json.loads(json.dumps(xml_dict))
print(xml_dict)

