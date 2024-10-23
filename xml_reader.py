import xml.dom.minidom as minidom

DATASET_PATH = 'currency.xml'

def get_objects(elements):
    list = []
    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Name':
                    if child.firstChild.nodeType == 3:
                        name = child.firstChild.data
                if child.tagName == 'Nominal':
                    if child.firstChild.nodeType == 3:
                        nominal = child.firstChild.data
        if nominal == '1':
            list.append(name)
    return(list)

if __name__ == '__main__':
    with open(DATASET_PATH) as xml_file:
        xml_data = xml_file.read()
        dom = minidom.parseString(xml_data)
        dom.normalize()
        elements = dom.getElementsByTagName('Valute')
        names_list = get_objects(elements)
        print(', '.join(names_list))