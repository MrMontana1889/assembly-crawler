import sys
import clr

print("Uses OpenFlows.Water.Python wrapper and the OpenFlowsWaterPythong class to start a session, open a model, do some stuff and end the sssion")

sys.path.append('D:\\p4\\Glacier\\Products\\WaterGEMS\\Output\\_Starter\\x64\\Debug')
clr.AddReference('OpenFlows.Water.Python')

from OpenFlows.Water.Python import OpenFlowsWaterPython

OpenFlowsWaterPython.StartWaterGEMSSession()

filename = "D:\\p4\\Glacier\\Products\\WaterGEMS\\Development\\Runtime\\Samples\\Example1.wtg"
wm = OpenFlowsWaterPython.OpenModel(filename)
p = wm.Network.Pipes.Elements()[0]

junction = wm.Network.Junctions.Elements()[0]
print(junction.Label)

wm.RunActiveScenario()
print(junction.Results.Demand())

demands = junction.Input.DemandCollection.Get()
print(demands.Count)
demands.Add(2.5, None)

junction.Input.DemandCollection.Set(demands)
print(junction.Input.DemandCollection.Count)

wm.RunActiveScenario()

print(junction.Results.Demand())

wm.RunActiveScenario()

print(f"Diameter: {p.Input.Diameter}")
p.Input.Diameter = 1.0
print(f"Diameter: {p.Input.Diameter}")

OpenFlowsWaterPython.EndSession()