import sys
from typing import List

import clr
import pathlib

# For python, you must append to the path the location of the OpenFlows assemblies.
# This is typically the installation folder for WaterGEMS, the x64 folder in particular.
sys.path.append('D:\\p4\\Glacier\\Products\\WaterGEMS\\Output\\_Starter\\x64\\Debug')
clr.AddReference('OpenFlows.Water')

# Import the OpenFlowsWater module
from OpenFlows.Water import OpenFlowsWater, WaterProductLicenseType

print("Initializing session of OpenFlows.Water...")
OpenFlowsWater.StartSession(WaterProductLicenseType.WaterGEMS)

print("Opening model...")
projectFilename1:str = r'D:\p4\Glacier\Products\WaterGEMS\Development\Runtime\Samples\Example1.wtg'
projectFilename2 = r'D:\p4\Glacier\Products\WaterGEMS\Development\Runtime\Samples\Example5.wtg'
projectFilename3 = r'D:\p4\Glacier\Products\WaterGEMS\Development\Runtime\Samples\Example2.wtg'

OpenFlowsWater.SetMaxProjects(2)

firstModel = OpenFlowsWater.Open(projectFilename1)
print(f"Model successfully open ({pathlib.Path(projectFilename1).name}")

secondModel = OpenFlowsWater.Open(projectFilename2)
filename = pathlib.Path(projectFilename2).name

print(f"Model successfully open ({filename}")
print(f"{secondModel.ModelInfo.Filename}")
print(f"Title: {secondModel.ModelInfo.Title}")
print(f"Engineer: {secondModel.ModelInfo.Engineer}")
print(f"Company: {secondModel.ModelInfo.Company}")
print(f"Notes: {secondModel.ModelInfo.Notes}")

secondModel.Scenarios.Elements()[0].MakeCurrent()
print(f"Scenario {secondModel.ActiveScenario.Label} now current in {filename}")

scenario = firstModel.Scenarios.Elements("Y2000 - Age Analysis")[0]
print(f"Setting {scenario.Label} as the active scenario")
firstModel.SetActiveScenario(scenario)

print(f"Number of Pipes: {firstModel.Network.Pipes.Count}")

tank = firstModel.Network.Tanks.Element("T-215")
tank.Input.Elevation = 915.0

print("Calculating model...")
firstModel.RunActiveScenario()

OpenFlowsWater.EndSession()