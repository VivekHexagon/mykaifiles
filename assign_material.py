"""Version-1 As per XML database assign the material to parts in apex20211
Isotropic materials are supported, orthotropic and anisotropic need to define the coordinates
"""
import apex
import parse_xml


# apex.disableShowOutput()

def assignmaterial():
    xml_data = parse_xml.parts_information()
    model_1 = apex.currentModel()
    # _target = apex.EntityCollection()
    parts = model_1.getParts(recursive = True)
    print("Model ", model_1.name, " contains ", parts.len(), "Parts")
    j = 0
    for part in parts:
        _target = apex.EntityCollection()
        if xml_data["material_type"][j] == "Isotropic":
            _target.append(apex.getPart(pathName=part.getPathName()))
            unknown_3 = apex.catalog.getMaterial(name=xml_data["material"][j])
            print(unknown_3.name)
            # _target.append(apex.getPart(pathName="Model/Quadcopter/Upper frame/Motor support leg 4"))
            apex.attribute.assignMaterial(material=unknown_3, target=_target)
        else:
            pass

        j += 1

if __name__ == "__main__":
    assignmaterial()
