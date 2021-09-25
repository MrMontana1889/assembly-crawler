import sys
import clr

print(sys.executable)
print ("\n")

# sys.path.append('D:\\p4\\Glacier\\Products\\WaterGEMS\\Output\\_Starter\\x64\\Debug\\')
sys.path.append('D:\\repos\\assembly-crawler\\Output\\TestAssemblyNET48\\bin\\Debug')

# assem = clr.AddReference('OpenFlows.Water.Python')
assem = clr.AddReference('TestAssemblyNEt48')

print(assem)
print(assem.Location)

from TestAssemblyNET48 import Water


Water.EntryPoint.StartSession()
model =  Water.EntryPoint.Open("Test.wtg")
print(model)

tm = Water.EntryPoint.GetModel()
tm2 = Water.EntryPoint.GetModel()

print(tm)
print(tm2)

p = model.Network.Pipes.Create()
print(p)

Water.EntryPoint.EndSession()


# TestAssemblyNET48.EntryPoint.StartSession()

# from OpenFlows.Water.Python import OpenFlowsWaterAPI

# ofw = OpenFlowsWaterAPI()
# print(ofw)

# ofw.StartWaterGEMSSession()

# filename = 'D:\\p4\\Glacier\\Products\\WaterGEMS\\Development\\Runtime\\Samples\\Example1.wtg'
# wm = ofw.OpenModel(filename)
# if wm is None:
#     print("Undefined result")
# else:
#     print("WaterModel successfully retrieved: ", wm)
#     print("ModelInfo:  ", wm.ModelInfo.Filename, wm.ModelInfo.Date)

# if wm is not None:
#     print("Active Scenario Id: ", wm.ActiveScenario.Id, " ", wm.ActiveScenario.Label)

#     print("HasResults: ", wm.ActiveScenario.HasResults)
#     if not wm.ActiveScenario.HasResults:
#         print("Calculating model...")
#         wm.RunActiveScenario()
#         print("Scenario successfully calculated.")

#     if wm.ActiveScenario.HasResults:
#         print("Results found.  Retrieving flow for first available pipe")
#         print("Flow: ",  wm.Network.Pipes.Elements()[0].Results.Flow())

# print("Or I can use the WaterModel property: ", ofw.WaterModel)
# ofw.EndWaterGEMSSession()

