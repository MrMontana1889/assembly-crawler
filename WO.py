# test python file trying to use direct WO.NET APi to open a sqlite database
# really a proof of concept attempt

import clr
import sys

sys.path.append('D:\\p4v\\Teton\\WTRG1035\\Aspen\\Products\\WaterGEMS\\Output\\_Starter\\x64\\Debug')
filename = "D:\\OneDrive - Bentley Systems, Inc\\Documents\\Bentley\\WaterGEMS\\Samples_1040\\Example1.wtg.sqlite"

clr.AddReference('Haestad.Domain')
clr.AddReference('Haestad.Domain.ModelingObjects.Water')
clr.AddReference('Haestad.Support')
clr.AddReference('Haestad.LicensingFacade')
clr.AddReference('System')
clr.AddReference('Haestad.Calculations.Pressure.Domain')

from Haestad.Domain.ModelingObjects.Water import IdahoDataSource
from Haestad.Domain import ConnectionProperty, ConnectionType, StandardFieldName, StandardAlternativeName, StandardCalculationOptionFieldName, ModelingElementCollection
from Haestad.Support.Units import UnitConversionManager
from Haestad.LicensingFacade import License, ProductRelease, ProductId
from System import IntPtr

dataSource = IdahoDataSource()
dataSource.SetConnectionProperty(ConnectionProperty.FileName, filename)
dataSource.SetConnectionProperty(ConnectionProperty.ConnectionType, ConnectionType.Sqlite)
dataSource.SetConnectionProperty(ConnectionProperty.EnableSchemaUpdate, False)
dataSource.SetConnectionProperty(ConnectionProperty.ShouldUpdateCounters, False)
dataSource.SetConnectionProperty(ConnectionProperty.EnableCoreSchemaUpdate, False)
dataSource.SetConnectionProperty(ConnectionProperty.CheckSuccessfulCloseFlag, False)

dataSource.Open()

domainDataSet = dataSource.DomainDataSetManager.DomainDataSet(1)
pipeManager = domainDataSet.DomainElementManager(69)

field = pipeManager.DomainElementField(StandardFieldName.Physical_PipeDiameter, StandardAlternativeName.Physical)
id = pipeManager.ElementIDs()[0]

workingUnit = UnitConversionManager.Current.UnitAt(field.WorkingUnitIndex)
print(f"{field.GetValue(id)} {workingUnit.Label}")

field.WorkingUnitIndex = UnitConversionManager.UnitIndex.Inches
workingUnit = UnitConversionManager.Current.UnitAt(field.WorkingUnitIndex)

print(f"{field.GetValue(id)} {workingUnit}")

pr = ProductRelease(ProductId.Bentley_WaterGEMS, "10.03.05.05")
license = License.Default(pr, IntPtr.Zero, None)
license.Initialize()
license.StartDesktop()

scenarioManager = domainDataSet.ScenarioManager
scenario = scenarioManager.Element(scenarioManager.ActiveScenarioID)
mec = ModelingElementCollection()
mec.Add(scenario)

engine = domainDataSet.NumericalEngine(StandardCalculationOptionFieldName.EpaNetEngine)
engine.SetLicensingInfo(license)

engine.Run(mec)

license.StopDesktop

dataSource.Close()