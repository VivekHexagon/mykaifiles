import xml.etree.ElementTree as ET
import pandas as pd
import os
"""Version1 this code reads the XML and create the pandas data frame"""
src_dir = os.path.dirname(os.path.realpath(__file__))
xml_path = os.path.join(src_dir, "quadcopter.xml")

tree = ET.parse(xml_path)
root = tree.getroot()

def assembly_information():
    print("Assembly ------  Information ")
    assembly_info = []
    for assembly in root.iter('assembly'):
        for name in assembly:
            if name.tag == 'name':
                assembly_info.append(name.text)
    print("Number of Assemblies =",len(assembly_info))
    print("Assembly Names :")
    print(assembly_info)

print("*" * 30)


titles = []
val = []
xmldata = dict()
def parts_information():
    for part in root.iter('part'):
        # print("*" * 10)
        titles.clear()
        for i in part:
            # print(i.tag,i.text)
            titles.append(i.tag)
            val.append(i.tag)
            val.append(i.text)
    # print(titles)
    # print(val)
    for j in range(len(titles)):
        xmldata[titles[j]] = []
    for j in range(len(titles)):
        for k in range(len(val)):
            if titles[j] == val[k]:
                xmldata[titles[j]].append(val[k+1])
    # print(xmldata)
    df = pd.DataFrame(xmldata)
    print("Parts ---- Information ")
    print(df)
    return df

if __name__ == "__main__":
    assembly_information()
    print()
    parts_information()
    # print(aa("name"))

