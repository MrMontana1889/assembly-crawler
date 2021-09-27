import sys
import clr

# sys.path.append('.\\Output\\TestAssemblyNET48\\bin\\Debug')
# assem = clr.AddReference('TestAssemblyNET48')

# from TestAssemblyNET48.Water import OpenFlowsWater

# print(assem)
# print(assem.Location)

# OpenFlowsWater.StartSession()
# wm = OpenFlowsWater.Open("")
# print(wm)
# p = wm.Network.Pipes.Create()
# print(p)
# p.Input.Diameter = 1.0
# print(f"Diameter {p.Input.Diameter}")

# OpenFlowsWater.EndSession()

# The following is to use the OFW Python wrapper not yet released into p4 and only available locally
# --------------------------------------------------------------------------------------------------

# Set this path to the locally built version of WaterGEMS OR the installation folder of WaterGEMS (x64 folder)
# Make sure that OpenFlows.dll, OpenFlows.Water.dll and OpenFlows.Water.Python.dll are in that location.
sys.path.append('D:\\p4v\\Teton\\WTRG1035\\Aspen\\Products\\WaterGEMS\\Output\\_Starter\\x64\\Debug')
clr.AddReference('OpenFlows.Water.Python')

from OpenFlows.Water.Python import OpenFlowsWaterPython 

OpenFlowsWaterPython.StartWaterGEMSSession()

filename = "D:\\p4v\\Aspen\\Products\\WaterGEMS\\Development\\Runtime\\Samples\\Example1.wtg"
wm = OpenFlowsWaterPython.OpenModel(filename)
p = wm.Network.Pipes.Elements()[0]

print(f"Diameter: {p.Input.Diameter}")
p.Input.Diameter = 1.0
print(f"Diameter: {p.Input.Diameter}")

OpenFlowsWaterPython.EndSession()