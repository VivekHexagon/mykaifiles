import apex
import parse_xml
from apex.construct import Point3D, Point2D
""" Version 1, this code can read the data frame and change the attributes for parts
only mesh type this time"""
apex.setScriptUnitSystem(unitSystemName = r'''mm-kg-s-N-K''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(applicationSettingsGeometry = applicationSettingsGeometry)
model_1 = apex.currentModel()
xmldata = parse_xml.parts_information()

# row_numbers = len(xmldata)
# col_numbers = len(xmldata.columns)
parts = model_1.getParts(recursive = True)
print("Model ", model_1.name, " contains ", parts.len(), "Parts")

i = 0

for part in parts:
    if part.name == xmldata['name'][i]: # get this info from XML
        part_1 = apex.getPart(pathName= part.getPathName())
        part_1.addUserAttribute(userAttributeName='Mesh Type'
                                , stringValue=xmldata["offset"][i]) # get this info from XML
        print("Attributes changed for :",part.name)

    i += 1

