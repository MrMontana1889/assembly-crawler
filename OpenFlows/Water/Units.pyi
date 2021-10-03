from OpenFlows.Units import INetworkUnits, IComponentUnits

class INetworkElementUnits(INetworkUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Pump(self) -> IPumpUnits:
		"""
		Returns:
			IPumpUnits: No Description
		"""
		pass

	@property
	def VSPBUnits(self) -> IVariableSpeedPumpBatteryUnits:
		"""
		Returns:
			IVariableSpeedPumpBatteryUnits: No Description
		"""
		pass

	@property
	def FCV(self) -> IFlowControlValveUnits:
		"""
		Returns:
			IFlowControlValveUnits: No Description
		"""
		pass

	@property
	def GPV(self) -> IGeneralPurposeValveUnits:
		"""
		Returns:
			IGeneralPurposeValveUnits: No Description
		"""
		pass

	@property
	def PBV(self) -> IPressureBreakingValveUnits:
		"""
		Returns:
			IPressureBreakingValveUnits: No Description
		"""
		pass

	@property
	def PRV(self) -> IPressureReducingValveUnits:
		"""
		Returns:
			IPressureReducingValveUnits: No Description
		"""
		pass

	@property
	def PSV(self) -> IPressureSustainingValveUnits:
		"""
		Returns:
			IPressureSustainingValveUnits: No Description
		"""
		pass

	@property
	def TCV(self) -> IThrottleControlValveUnits:
		"""
		Returns:
			IThrottleControlValveUnits: No Description
		"""
		pass

	@property
	def Pipe(self) -> IPipeUnits:
		"""
		Returns:
			IPipeUnits: No Description
		"""
		pass

	@property
	def Lateral(self) -> IBaseLinkUnits:
		"""
		Returns:
			IBaseLinkUnits: No Description
		"""
		pass

	@property
	def Junction(self) -> IJunctionUnits:
		"""
		Returns:
			IJunctionUnits: No Description
		"""
		pass

	@property
	def Hydrant(self) -> IHydrantUnits:
		"""
		Returns:
			IHydrantUnits: No Description
		"""
		pass

	@property
	def Tank(self) -> ITankUnits:
		"""
		Returns:
			ITankUnits: No Description
		"""
		pass

	@property
	def CustomerMeter(self) -> ICustomerMeterUnits:
		"""
		Returns:
			ICustomerMeterUnits: No Description
		"""
		pass

	@property
	def Reservoir(self) -> IReservoirUnits:
		"""
		Returns:
			IReservoirUnits: No Description
		"""
		pass

	@property
	def SCADAElement(self) -> IGeometryUnits:
		"""
		Returns:
			IGeometryUnits: No Description
		"""
		pass

	@property
	def Tap(self) -> IGeometryUnits:
		"""
		Returns:
			IGeometryUnits: No Description
		"""
		pass

	@property
	def SpotElevation(self) -> ISpotElevationUnits:
		"""
		Returns:
			ISpotElevationUnits: No Description
		"""
		pass

	@property
	def ValveWithLinearAreaChange(self) -> IValveWithLinearAreaChangeUnits:
		"""
		Returns:
			IValveWithLinearAreaChangeUnits: No Description
		"""
		pass

	@property
	def PeriodicHeadFlow(self) -> IPeriodicHeadFlowUnits:
		"""
		Returns:
			IPeriodicHeadFlowUnits: No Description
		"""
		pass

	@property
	def AirValve(self) -> IAirValveUnits:
		"""
		Returns:
			IAirValveUnits: No Description
		"""
		pass

	@property
	def OrificeBetweenTwoPipes(self) -> IOrificeBetweenTwoPipesUnits:
		"""
		Returns:
			IOrificeBetweenTwoPipesUnits: No Description
		"""
		pass

	@property
	def SurgeValve(self) -> ISurgeValveUnits:
		"""
		Returns:
			ISurgeValveUnits: No Description
		"""
		pass

	@property
	def DischargeToAtmosphere(self) -> IDischargeToAtmosphereUnits:
		"""
		Returns:
			IDischargeToAtmosphereUnits: No Description
		"""
		pass

	@property
	def RuptureDisk(self) -> IRuptureDiskUnits:
		"""
		Returns:
			IRuptureDiskUnits: No Description
		"""
		pass

	@property
	def Turbine(self) -> ITurbineUnits:
		"""
		Returns:
			ITurbineUnits: No Description
		"""
		pass

	@property
	def SurgeTank(self) -> ISurgeTankUnits:
		"""
		Returns:
			ISurgeTankUnits: No Description
		"""
		pass

	@property
	def HydropneumaticTank(self) -> IHydropneumaticTankUnits:
		"""
		Returns:
			IHydropneumaticTankUnits: No Description
		"""
		pass

	@property
	def IsolationValve(self) -> IIsolationValveUnits:
		"""
		Returns:
			IIsolationValveUnits: No Description
		"""
		pass

	@property
	def PumpStation(self) -> IPumpStationUnits:
		"""
		Returns:
			IPumpStationUnits: No Description
		"""
		pass

	@property
	def CheckValve(self) -> ICheckValveUnits:
		"""
		Returns:
			ICheckValveUnits: No Description
		"""
		pass

class IComponentElementUnits(IComponentUnits):

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

	@property
	def Constituent(self) -> IConstituentUnits:
		"""
		Returns:
			IConstituentUnits: No Description
		"""
		pass

	@property
	def Condition(self) -> IControlConditionUnits:
		"""
		Returns:
			IControlConditionUnits: No Description
		"""
		pass

	@property
	def Action(self) -> IControlActionUnits:
		"""
		Returns:
			IControlActionUnits: No Description
		"""
		pass

	@property
	def Pattern(self) -> IPatternUnits:
		"""
		Returns:
			IPatternUnits: No Description
		"""
		pass

	@property
	def PumpDefinition(self) -> IPumpDefinitionUnits:
		"""
		Returns:
			IPumpDefinitionUnits: No Description
		"""
		pass

	@property
	def UnitDemandLoad(self) -> IUnitDemandLoadUnits:
		"""
		Returns:
			IUnitDemandLoadUnits: No Description
		"""
		pass

	@property
	def AirFlowCurve(self) -> IAirFlowCurveUnits:
		"""
		Returns:
			IAirFlowCurveUnits: No Description
		"""
		pass

	@property
	def GPVHeadlossCurve(self) -> IGPVHeadlossUnits:
		"""
		Returns:
			IGPVHeadlossUnits: No Description
		"""
		pass

	@property
	def ValveCharacteristic(self) -> IValveCharacteristicUnits:
		"""
		Returns:
			IValveCharacteristicUnits: No Description
		"""
		pass

	@property
	def MinorLossCoefficient(self) -> IMinorLossCoefficientUnits:
		"""
		Returns:
			IMinorLossCoefficientUnits: No Description
		"""
		pass

class IWaterUnitsManager:

	def __init__(self) -> None:
		"""Creating a new Instance of this class is not allowed


		Raises:
			Exception: if this class is instanciated
		"""
		raise Exception("Creating a new Instance of this class is not allowed")
		pass

