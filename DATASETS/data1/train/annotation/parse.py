import xml.etree.ElementTree as ET

file=open("X2-10-0.xml",'rt')
xmlcontent=file.read()
print(xmlcontent)
tree=ET.fromstring(xmlcontent)
print(tree[1])
##for i in tree:
##    print(i)
objects=tree.findall('object')
print(len(objects))
for obj in objects:
    name=obj.find('name').text
    xmin=obj.find('bndbox').find('xmin').text
    ymin=obj.find('bndbox').find('ymin').text
    xmax=obj.find('bndbox').find('xmax').text
    ymax=obj.find('bndbox').find('ymax').text
    
    

