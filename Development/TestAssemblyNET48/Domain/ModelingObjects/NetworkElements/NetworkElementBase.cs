using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TestAssemblyNET48.Water.Domain.ModelingObjects;
using TestAssemblyNET48.Water.Domain.ModelingObjects.NetworkElements;

namespace TestAssemblyNET48.Domain.ModelingObjects.NetworkElements
{
    internal abstract class NetworkElementBase<TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType,
        TModelComponentType, TComponentElementType, TComponentElementTypeEnum, TNetworkUnitsType, TComponentUnitsType>
        : ModelingElementBase<TElementManagerType, TElementType, TElementTypeEnum, TNetworkUnitsType, TComponentUnitsType>, IActiveElementInput,
        IModelingElementFieldManager, INetworkElement<TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
        where TElementManagerType : class, INetworkElements<TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
        where TElementType : class, INetworkElement<TElementManagerType, TElementType, TUnitsType, TElementTypeEnum, TElementInputType, TElementResultsType, TElementsInputType, TElementsResultsType>
        where TUnitsType : class, IElementUnits
        where TElementTypeEnum : Enum
        where TElementInputType : class, IActiveElementInput
        where TElementResultsType : class, IElementResults
        where TElementsInputType : class, IActiveElementsInput
        where TElementsResultsType : class, IElementsResults
        where TComponentElementType : class, IElement
        where TComponentElementTypeEnum : Enum
        where TModelComponentType : class, IModelComponents<TComponentElementType, TComponentElementTypeEnum>
        where TNetworkUnitsType : class, INetworkUnits
        where TComponentUnitsType : class, IComponentUnits
    {
        #region Constructor
        public NetworkElementBase(int id, TElementManagerType manager, IDomainModel domainModel,
            TModelComponentType modelComponents, IModelElementManager model, IUnitsEx<TNetworkUnitsType, TComponentUnitsType> units)
            : base(id, manager, domainModel, model, units)
        {
            ModelComponents = modelComponents;
        }
        #endregion

        #region Public Methods
        public IField NetworkElementField(string fieldName)
        {
            return NetworkElementManager.NetworkElementField(fieldName);
        }
        public IField NetworkElementField(string fieldName, string alternativeTypeName)
        {
            return NetworkElementManager.NetworkElementField(fieldName, alternativeTypeName);
        }
        public TResultFieldType ResultField<TResultFieldType>(string fieldName, string resultRecordTypeName) where TResultFieldType : class, IResultField
        {
            return NetworkElementManager.ResultField<TResultFieldType>(fieldName, resultRecordTypeName);
        }
        public TResultFieldType ResultField<TResultFieldType>(string fieldName, string numericalEngineTypeName, string resultRecordTypeName) where TResultFieldType : class, IResultField
        {
            return NetworkElementManager.ResultField<TResultFieldType>(fieldName, numericalEngineTypeName, resultRecordTypeName);
        }
        #endregion

        #region Public Properties
        public abstract TUnitsType Units { get; }
        public abstract TElementInputType Input { get; }
        public abstract TElementResultsType Results { get; }
        public override ModelElementType ModelElementType => ModelElementType.NetworkElement;
        public IFieldManager InputFields => Manager.InputFields;
        public IFieldManager ResultFields => Manager.ResultFields;
        public bool IsActive
        {
            get => GetFieldValue<bool>(NetworkElementField(StandardFieldName.HMIActiveTopologyIsActive, StandardAlternativeName.HmiActiveTopology));
            set => SetFieldValue(NetworkElementField(StandardFieldName.HMIActiveTopologyIsActive, StandardAlternativeName.HmiActiveTopology), value);
        }
        #endregion

        #region Protected Methods
        protected bool HasResults()
        {
            string mainNumericalEngineTypeName = DomainModel.DomainDataSet.DomainDataSetType().GetMainNumericalEngineTypeName();
            INumericalEngine numericalEngine = DomainModel.DomainDataSet.NumericalEngine(mainNumericalEngineTypeName);
            return numericalEngine.ResultDataConnection.HasResults(DomainModel.DomainDataSet.ScenarioManager.ActiveScenarioID);
        }
        protected void OpenResultsIfNeeded()
        {
            if (HasResults())
            {
                string mainNumericalEngineTypeName = DomainModel.DomainDataSet.DomainDataSetType().GetMainNumericalEngineTypeName();
                INumericalEngine numericalEngine = DomainModel.DomainDataSet.NumericalEngine(mainNumericalEngineTypeName);
                if (!numericalEngine.ResultDataConnection.IsActive(DomainModel.DomainDataSet.ScenarioManager.ActiveScenarioID))
                    numericalEngine.ResultDataConnection.Open(DomainModel.DomainDataSet.ScenarioManager.ActiveScenarioID);
            }
        }
        protected abstract bool HasElementResults();
        /// <summary>
        /// Determine if the active solver supports the provided result field.
        /// By default, returns true.
        /// </summary>
        /// <param name="field">The field to determine if supported by the active solver</param>
        /// <returns>True if supported, otherwise false.</returns>
        protected virtual bool ActiveSolverSupportsField(IResultField field)
        {
            if (field is IDomainField domainField)
            {
                if (domainField.FieldType is IFieldTypeUI fieldTypeUI)
                {
                    string activeSolver = ActiveEngineLibrary.GetActiveNumericalEngineName(DomainModel.DomainDataSet,
                        DomainModel.DomainDataSet.ScenarioManager.ActiveScenarioID);
                    var solvers = fieldTypeUI.GetFilteringByNumericalEngineType();

                    // If not filtered for any solvers or the solver count is 0, then assume supported.
                    if (solvers == null || solvers.Count == 0) return true;

                    // Determine if the active solver is in the list of solvers returned.
                    return (solvers.IndexOf(activeSolver) > -1);
                }
            }

            return true;
        }
        protected IResultTimeVariantField TimeVariantResultField(string fieldName, string resultRecordTypeName)
        {
            return ResultField<IResultTimeVariantField>(fieldName, resultRecordTypeName) as IResultTimeVariantField;
        }
        protected TReturnType GetResultFieldValue<TReturnType>(IField field)
        {
            if (!ActiveSolverSupportsField(field as IResultField))
            {
                string activeSolver = ActiveEngineLibrary.GetActiveNumericalEngineName(DomainModel.DomainDataSet, ActiveScenarioID);
                throw new FieldNotSupportedByActiveSolver($"The field {field.Name} is not supported by the active solver {activeSolver}");
            }

            if (!HasElementResults())
            {
                if (Nullable.GetUnderlyingType(typeof(TReturnType)) != null)
                    return default;

                throw new NoElementResultsAvailableExceptions();
            }

            return GetFieldValue<TReturnType>(field);
        }
        protected TReturnType GetTimeVariantResult<TReturnType>(IResultTimeVariantField field, int timeStepIndex)
        {
            if (!ActiveSolverSupportsField(field))
            {
                string activeSolver = ActiveEngineLibrary.GetActiveNumericalEngineName(DomainModel.DomainDataSet, ActiveScenarioID);
                throw new FieldNotSupportedByActiveSolver($"The field {field.Name} is not supported by the active solver {activeSolver}");
            }

            if (!HasElementResults())
            {
                if (Nullable.GetUnderlyingType(typeof(TReturnType)) != null)
                    return default;

                throw new NoElementResultsAvailableExceptions();
            }

            SetWorkingUnit(field);
            int scenarioID = DomainModel.DomainDataSet.ScenarioManager.ActiveScenarioID;
            return (TReturnType)field.GetValue(Id, scenarioID, timeStepIndex);
        }
        protected TReturnType[] GetTimeVariantResultsOverTime<TReturnType>(IResultTimeVariantField field)
        {
            if (!ActiveSolverSupportsField(field))
            {
                string activeSolver = ActiveEngineLibrary.GetActiveNumericalEngineName(DomainModel.DomainDataSet, ActiveScenarioID);
                throw new FieldNotSupportedByActiveSolver($"The field {field.Name} is not supported by the active solver {activeSolver}");
            }

            if (!HasElementResults())
            {
                if (Nullable.GetUnderlyingType(typeof(TReturnType)) != null)
                    return default;

                throw new NoElementResultsAvailableExceptions();
            }

            SetWorkingUnit(field);
            int scenarioID = DomainModel.DomainDataSet.ScenarioManager.ActiveScenarioID;

            if (Nullable.GetUnderlyingType(typeof(TReturnType)) == null)
                return (TReturnType[])field.GetValuesOverTime(Id, scenarioID);
            else
            {
                Array retVal = field.GetValuesOverTime(Id, scenarioID);
                var results = new TReturnType[retVal.Length];
                for (int i = 0; i < retVal.Length; ++i)
                    results[i] = (TReturnType)retVal.GetValue(i);
                return results;
            }
        }
        protected int GetActiveTimeStepIndex()
        {
            IDScenario scenario = (IDScenario)DomainModel.DomainDataSet.ScenarioManager.Element(ActiveScenarioID);
            return scenario.ActiveTimeStep;
        }
        protected IUnit FieldFormatterFor(string formatterName)
        {
            return FieldUnit.New(UnitsEx.NumericFormatterFor(formatterName));
        }
        protected IUnit FieldFormatterFor(StandardNumericFormatters formatter)
        {
            return FieldFormatterFor(NumericFormatterLibrary.GetNumericFormatterName(formatter));
        }
        protected IUnit GetFieldUnit(string fieldName, string alternativeTypeName)
        {
            IDomainField field = NetworkElementField(fieldName, alternativeTypeName) as IDomainField;
            return FieldUnit.New(UnitsEx.NumericFormatterFor(field.FieldType.NumericFormatterName));
        }
        protected IUnit GetFieldUnit(string fieldName)
        {
            IDomainField field = NetworkElementField(fieldName) as IDomainField;
            return FieldUnit.New(UnitsEx.NumericFormatterFor(field.FieldType.NumericFormatterName));
        }
        protected IUnit GetResultFieldUnit(string fieldName, string resultRecordTypeName)
        {
            IDomainField field = ResultField<IResultField>(fieldName, resultRecordTypeName) as IDomainField;
            return FieldUnit.New(UnitsEx.NumericFormatterFor(field.FieldType.NumericFormatterName));
        }
        protected ICollectionField GetCollectionField(string fieldName, string alternativeTypeName)
        {
            return NetworkElementField(fieldName, alternativeTypeName) as ICollectionField;
        }
        protected IField GetCollectionCountField(string fieldName, string alternativeTypeName)
        {
            return NetworkElementField(fieldName, alternativeTypeName);
        }
        #endregion

        #region Protected Properties
        protected INetworkElementFieldManager NetworkElementManager => Manager as INetworkElementFieldManager;
        protected int ActiveScenarioID => DomainModel.DomainDataSet.ScenarioManager.ActiveScenarioID;
        protected TModelComponentType ModelComponents { get; }
        #endregion
    }
}
