"""Version-1 Read the materials csv file and create the Apex Materials for apex20211
The provided csv file should not have spaces below the actual written lines
"""
import csv
import apex
import os

apex.disableShowOutput()
isodict = dict()


def createApexIsotropic():
    try:
        myMatl = apex.catalog.getMaterial(name=isodict["name"])
        print("Material with name", isodict["name"], " already exists")

    except:
        # Create material if not already existing
        myMatl = apex.catalog.createMaterial(name=isodict["name"], description="as per csv", color=[255, 0, 0])
        try:
            myMatl.update(elasticModulus=eval(isodict["EM"]), )
        except:
            print("Check if E is supplied")
        try:
            myMatl.update(poissonRatio=eval(isodict["PR"]), )
        except:
            print("Check if P is supplied")
        try:
            myMatl.update(density=eval(isodict["den"]), )
        except:
            print("Check if density is supplied")
        try:
            myMatl.update(thermalExpansionCoeff=eval(isodict["TEC"]), )
        except:
            print("Check if TEC is supplied and its at proper place in csv file")

        try:
            myMatl.update(dampingCoefficient=eval(isodict["damC"]), )
        except:
            print("Check if damp coeff is supplied or at its proper place in csv")
        try:
            myMatl.update(failureLimitsIsotropic={'stressLimitTension': eval(isodict["SLT"]), }, )
        except:
            print("Check if SLT is provided and its at proper place in csv")
        try:
            myMatl.update(failureLimitsIsotropic={'stressLimitCompression': eval(isodict["SLC"]), }, )
        except:
            print("Check if SLC is provided and its proper place in csv")
        try:
            myMatl.update(failureLimitsIsotropic={'stressLimitShear': eval(isodict["SLS"]), }, )
        except:
            print("Check if SLC is provided and its proper place in csv")
        try:
            myMatl.update(description="Isotropic material from KAI csv", )
        except:
            myMatl.update(description="Placeholder for unsupported material type", )


def createApexOrthotropic():
    try:
        myMatl = apex.catalog.getMaterial(name=isodict["name0"])
        print("Material with name", isodict["name0"], " already exists")

    except:
        # Create material if not already existing
        myMatl = apex.catalog.createMaterial(name=isodict["name0"], description="as per csv", color=[0, 0, 255])

        myMatl.update(materialType=apex.attribute.MaterialType.Orthotropic)
        try:
            myMatl.update(elasticityOrthotropic2D={'elasticModulusX': eval(isodict["EM4"]), })
        except:
            pass
        try:
            myMatl.update(elasticityOrthotropic2D={'elasticModulusY': eval(isodict["E10"]), })
        except:
            pass
        try:
            myMatl.update(elasticityOrthotropic2D={'shearModulusXY': eval(isodict["SM28"]), })
        except:
            pass
        try:
            myMatl.update(elasticityOrthotropic2D={'shearModulusYZ': eval(isodict["SM29"]), })
        except:
            pass
        try:
            myMatl.update(elasticityOrthotropic2D={'shearModulusXZ': eval(isodict["SM30"]), })
        except:
            pass
        try:
            myMatl.update(poissonRatio=eval(isodict["PR25"]))
        except:
            pass
        try:
            myMatl.update(density=eval(isodict["density31"]), )
        except:
            pass
        try:
            myMatl.update(dampingCoefficient=eval(isodict["SDM38"]), )
        except:
            pass
        try:
            myMatl.update(thermalExpansionCoeffOrthotropic2D={'thermalExpansionCoeffX': eval(isodict["T32"]), }, )
        except:
            pass
        try:
            myMatl.update(thermalExpansionCoeffOrthotropic2D={'thermalExpansionCoeffY': eval(isodict["T33"]), }, )
        except:
            pass
        # try:
        #     myMatl.update(failureLimitsOrthotropic2D={'stressLimitTensionX': self.Xt, })
        # except:
        #     pass
        # try:
        #     myMatl.update(failureLimitsOrthotropic2D={'stressLimitTensionY': self.Yt, })
        # except:
        #     pass
        # try:
        #     myMatl.update(failureLimitsOrthotropic2D={'stressLimitCompressionX': self.Xc, })
        # except:
        #     pass
        # try:
        #     myMatl.update(failureLimitsOrthotropic2D={'stressLimitCompressionY': self.Yc, })
        # except:
        #     pass
        # try:
        #     myMatl.update(failureLimitsOrthotropic2D={'stressLimitInplaneShear': self.S, })
        # except:
        #     pass


def createApexAnisotropic():
    try:
        myMatl = apex.catalog.getMaterial(name=isodict["name0"])
        print("Material with name", isodict["name0"], " already exists")

    except:
        # Create material if not already existing
        myMatl = apex.catalog.createMaterial(name=isodict["name0"], description="as per csv", color=[0, 255, 0])
        myMatl.update(materialType=apex.attribute.MaterialType.Anisotropic3D, )
        cmElasticityLinear3DAniso = myMatl.getConstitutiveModel(type=apex.attribute.ConstitutiveModelType.Elasticity)

        try:
            # cmElasticityLinear3DAniso = myMatl.getConstitutiveModel(type=apex.attribute.ConstitutiveModelType.Elasticity)
            print("Updating the elastic modulus for 3d anisotropic materials if supplied")
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix11=eval(isodict["S11_4"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix11=eval(isodict["S11_4"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            # cmElasticityLinear3DAniso = myMatl.getConstitutiveModel(type=apex.attribute.ConstitutiveModelType.Elasticity)
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix21=eval(isodict["S12_5"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix21=eval(isodict["S12_5"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            # cmElasticityLinear3DAniso = myMatl.getConstitutiveModel(type=apex.attribute.ConstitutiveModelType.Elasticity)
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix22=eval(isodict["S13_6"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix22=eval(isodict["S13_6"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            # cmElasticityLinear3DAniso = myMatl.getConstitutiveModel(type=apex.attribute.ConstitutiveModelType.Elasticity)
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix31=eval(isodict["S14_7"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix31=eval(isodict["S14_7"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            # cmElasticityLinear3DAniso = myMatl.getConstitutiveModel(type=apex.attribute.ConstitutiveModelType.Elasticity)
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix32=eval(isodict["S15_8"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix32=eval(isodict["S15_8"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            # cmElasticityLinear3DAniso = myMatl.getConstitutiveModel(type=apex.attribute.ConstitutiveModelType.Elasticity)
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix33=eval(isodict["S16_9"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix33=eval(isodict["S16_9"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix41=eval(isodict["S22_10"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix41=eval(isodict["S22_10"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix42=eval(isodict["S23_11"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix42=eval(isodict["S23_11"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix43=eval(isodict["S24_12"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix43=eval(isodict["S24_12"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix44=eval(isodict["S25_13"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix44=eval(isodict["S25_13"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix51=eval(isodict["S26_14"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix51=eval(isodict["S26_14"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix52=eval(isodict["S33_15"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix52=eval(isodict["S33_15"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix53=eval(isodict["S34_16"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix53=eval(isodict["S34_16"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix54=eval(isodict["S35_17"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix54=eval(isodict["S35_17"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix55=eval(isodict["S36_18"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix55=eval(isodict["S36_18"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix61=eval(isodict["S44_19"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix61=eval(isodict["S44_19"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix62=eval(isodict["S45_20"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix62=eval(isodict["S45_20"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix63=eval(isodict["S46_21"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix63=eval(isodict["S46_21"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix64=eval(isodict["S55_22"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix64=eval(isodict["S55_22"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix65=eval(isodict["S56_23"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix65=eval(isodict["S56_23"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        try:
            if cmElasticityLinear3DAniso:
                cmElasticityLinear3DAniso.update(materialMatrix66=eval(isodict["S66_24"]), )
            else:
                cmElasticityLinear3DAniso = apex.attribute.ElasticityLinear3DAniso(materialMatrix66=eval(isodict["S66_24"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmElasticityLinear3DAniso)
        except:
            pass
        print("*" * 30)
        print("Updating the masses for 3d anisotropic materials if supplied")
        cmMass = myMatl.getConstitutiveModel(type=apex.attribute.ConstitutiveModelType.Mass)
        try:
            if cmMass:
                cmMass.update(massDensity=eval(isodict["density31"]), )
            else:
                cmMass = apex.attribute.Mass(massDensity=eval(isodict["density31"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmMass)
        except:
            pass
        print("*" * 30)
        print("Updating the damping for 3d anisotropic if suppled")
        cmViscoElasticity3DAniso = myMatl.getConstitutiveModel(
            type=apex.attribute.ConstitutiveModelType.ViscoElasticity)
        try:
            # print("Updating the damping for 3d anisotropic")
            # cmViscoElasticity3DAniso = myMatl.getConstitutiveModel(type=apex.attribute.ConstitutiveModelType.ViscoElasticity)
            if cmViscoElasticity3DAniso:
                cmViscoElasticity3DAniso.update(strdampingCoefficient=eval(isodict["SDM38"]), )
            else:
                cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(strdampingCoefficient=eval(isodict["SDM38"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        except:
            pass
        # Below items are not avilable in KAI materials csv
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE11=0.1,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE11=0.1,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE21=0.2,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE21=0.2,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE22=0.3,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE22=0.3,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE31=0.4,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE31=0.4,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE32=0.5,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE32=0.5,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE33=0.6,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE33=0.6,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE41=0.8,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE41=0.8,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE42=0.9,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE42=0.9,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE43=0.11,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE43=0.11,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE44=0.12,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE44=0.12,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE51=0.13,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE51=0.13,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE52=0.14,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE52=0.14,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE53=0.15,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE53=0.15,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE54=0.16,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE54=0.16,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE55=0.16, )
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE55=0.16, )
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        #
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE61=0.17,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE61=0.17,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE62=0.18,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE62=0.18,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE63=0.19,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE63=0.19,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE64=0.21,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE64=0.21,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE65=0.21,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE65=0.21,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        # try:
        #     if cmViscoElasticity3DAniso:
        #         cmViscoElasticity3DAniso.update(GE66=0.21,)
        #     else:
        #         cmViscoElasticity3DAniso = apex.attribute.ViscoElasticity3DAniso(GE66=0.21,)
        #         myMatl.addConstitutiveModel(constitutiveModel=cmViscoElasticity3DAniso)
        # except:
        #     pass
        print("Updating the thermal coeff for 3d anisotropic materials is supplied")
        cmThermalExpansionLinear3DAnisotropic = myMatl.getConstitutiveModel(
            type=apex.attribute.ConstitutiveModelType.ThermalExpansion)
        try:
            if cmThermalExpansionLinear3DAnisotropic:
                cmThermalExpansionLinear3DAnisotropic.update(expansionCoefficient11=eval(isodict["T11_32"]), )
            else:
                cmThermalExpansionLinear3DAnisotropic = apex.attribute.ThermalExpansionLinear3DAnisotropic(
                    expansionCoefficient11=eval(isodict["T11_32"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmThermalExpansionLinear3DAnisotropic)
        except:
            pass
        try:
            if cmThermalExpansionLinear3DAnisotropic:
                cmThermalExpansionLinear3DAnisotropic.update(expansionCoefficient22=eval(isodict["T22_33"]), )
            else:
                cmThermalExpansionLinear3DAnisotropic = apex.attribute.ThermalExpansionLinear3DAnisotropic(
                    expansionCoefficient22=eval(isodict["T22_33"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmThermalExpansionLinear3DAnisotropic)
        except:
            pass
        try:
            if cmThermalExpansionLinear3DAnisotropic:
                cmThermalExpansionLinear3DAnisotropic.update(expansionCoefficient33=eval(isodict["T33_34"]), )
            else:
                cmThermalExpansionLinear3DAnisotropic = apex.attribute.ThermalExpansionLinear3DAnisotropic(
                    expansionCoefficient33=eval(isodict["T33_34"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmThermalExpansionLinear3DAnisotropic)
        except:
            pass
        try:
            if cmThermalExpansionLinear3DAnisotropic:
                cmThermalExpansionLinear3DAnisotropic.update(expansionCoefficient12=eval(isodict["T12_35"]), )
            else:
                cmThermalExpansionLinear3DAnisotropic = apex.attribute.ThermalExpansionLinear3DAnisotropic(
                    expansionCoefficient12=eval(isodict["T12_35"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmThermalExpansionLinear3DAnisotropic)
        except:
            pass
        try:
            if cmThermalExpansionLinear3DAnisotropic:
                cmThermalExpansionLinear3DAnisotropic.update(expansionCoefficient23=eval(isodict["T31_36"]), )
            else:
                cmThermalExpansionLinear3DAnisotropic = apex.attribute.ThermalExpansionLinear3DAnisotropic(
                    expansionCoefficient23=eval(isodict["T31_36"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmThermalExpansionLinear3DAnisotropic)
        except:
            pass
        try:
            if cmThermalExpansionLinear3DAnisotropic:
                cmThermalExpansionLinear3DAnisotropic.update(expansionCoefficient13=eval(isodict["T23_37"]), )
            else:
                cmThermalExpansionLinear3DAnisotropic = apex.attribute.ThermalExpansionLinear3DAnisotropic(
                    expansionCoefficient13=eval(isodict["T23_37"]), )
                myMatl.addConstitutiveModel(constitutiveModel=cmThermalExpansionLinear3DAnisotropic)
        except:
            pass


def creatematerial():
    src_dir = os.path.dirname(os.path.realpath(__file__))
    csv_path = os.path.join(src_dir, "material_sample.csv")

    f = open(csv_path, "r")
    # f = open("D:\VIVEK\Current_Projects_B\Code_Development\Geometry\material_sample.csv", "r")
    lines = csv.reader(f)

    # Hard coding the 2d ortho index as per material sheet
    twodortho = ["name0", "", "", "", "EM4", "", "", "", "", "", "E10", "", "", "", "", "", "", "", "", "", "", "",
                 "", "", "", "PR25", "", "", "SM28", "SM29", "SM30", "density31", "T32", "T33", "", "", "", "",
                 "SDM38", "Tref39", ""]

    # Hard coding the isotropic index as per material sheet
    isomat = ["name", "", "", "", "EM", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
              "PR", "den", "TEC",
              "damC", "SLT", "SLC", "SLS"]
    # Hard coding the 3d orthotropic index as per material sheet
    threedaniso = ["name0", "", "", "", "S11_4", "S12_5", "S13_6", "S14_7", "S15_8", "S16_9", "S22_10", "S23_11",
                   "S24_12", "S25_13", "S26_14", "S33_15", "S34_16", "S35_17", "S36_18", "S44_19", "S45_20", "S46_21",
                   "S55_22", "S56_23", "S66_24", "", "", "", "", "", "", "density31", "T11_32", "T22_33", "T33_34", "T12_35",
                   "T31_36", "T23_37", "SDM38", "Tref39", ""]

    for line in lines:
        print(line)
        if (line[2] == "2D Orthotropic") and (len(twodortho) <= len(line)):
            for i in range(len(twodortho)):
                isodict[twodortho[i]] = line[i]
            print("Updating the 2D Orthotropic materials to Apex")
            createApexOrthotropic()
            # print(isodict)
        elif line[2] == "Isotropic" and (len(isomat) <= len(line)):
            for j in range(len(isomat)):
                isodict[isomat[j]] = line[j]
            print("Updating the Isotropic materials to Apex")
            createApexIsotropic()
            # print(isodict)
        elif line[2] == "3D Anisotropic" and (len(threedaniso) <= len(line)):
            for k in range(len(threedaniso)):
                isodict[threedaniso[k]] = line[k]
            print("Updating the 3D Anisotropic materials to Apex")
            createApexAnisotropic()
            print(isodict)

        isodict.clear()
    f.close()

# creatematerial()
if __name__ == "__main__":
    creatematerial()
