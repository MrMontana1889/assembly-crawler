import sys
import clr

sys.path.append('D:\\repos\\assembly-crawler\\Output\\TestAssemblyNET48\\bin\\Debug')
assem = clr.AddReference('TestAssemblyNET48')

from TestAssemblyNET48.Water import OpenFlowsWater

print(assem)
print(assem.Location)

OpenFlowsWater.StartSession()
wm = OpenFlowsWater.Open("")
print(wm)
p = wm.Network.Pipes.Create()
print(p)
p.Input.Diameter = 1.0
print(f"Diameter {p.Input.Diameter}")

OpenFlowsWater.EndSession()

# The following is to use the OFW Python wrapper not yet released into p4 and only available locally
# -----------------------------------------------------------------------------------
# sys.path.append('D:\\p4\\Glacier\\Products\\WaterGEMS\\Output\\_Starter\\x64\\Debug')
# assem = clr.AddReference('OpenFlows.Water.Python')

# print(assem)
# print(assem.Location)

# from OpenFlows.Water.Python import OpenFlowsWaterAPI

# OpenFlowsWaterAPI.StartWaterGEMSSession()
# filename = "D:\\p4\\Glacier\\Products\\WaterGEMS\\Development\\Runtime\\Samples\\Example1.wtg"
# wm = OpenFlowsWaterAPI.OpenModel(filename)
# p = wm.Network.Pipes.Elements()[0]
# print(f"Diameter: {p.Input.Diameter}")
# p.Input.Diameter = 1.0
# print(f"Diameter: {p.Input.Diameter}")

# OpenFlowsWaterAPI.EndWaterGEMSSession()