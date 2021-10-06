import sys
import clr

# TestAssemblyNET48

sys.path.append(r'D:\repos\assembly-crawler\Output\TestAssemblyNET48\bin\Debug')
clr.AddReference('TestAssemblyNET48')
from TestAssemblyNET48.Water import OpenFlowsWater

print("Demonstration using TestAssemblyNET48.  Import the module from the package then start and end a session.")

print("OpenFlowsWater.StartSession()")
OpenFlowsWater.StartSession()

print("OpenFlowsWater.EndSession")
OpenFlowsWater.EndSession()
