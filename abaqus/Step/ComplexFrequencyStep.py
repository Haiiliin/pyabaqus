from abaqusConstants import *
from .AnalysisStep import AnalysisStep
from ..Adaptivity.AdaptiveMeshConstraintState import AdaptiveMeshConstraintState
from ..Adaptivity.AdaptiveMeshDomain import AdaptiveMeshDomain
from ..BoundaryCondition.BoundaryConditionState import BoundaryConditionState
from ..LoadAndLoadCase.LoadCase import LoadCase
from ..LoadAndLoadCase.LoadState import LoadState
from ..PredefinedField.PredefinedFieldState import PredefinedFieldState
from ..StepMiscellaneous.Control import Control
from ..StepMiscellaneous.SolverControl import SolverControl
from ..StepOutput.DiagnosticPrint import DiagnosticPrint
from ..StepOutput.FieldOutputRequestState import FieldOutputRequestState
from ..StepOutput.HistoryOutputRequestState import HistoryOutputRequestState
from ..StepOutput.Monitor import Monitor
from ..StepOutput.Restart import Restart


class ComplexFrequencyStep(AnalysisStep):
    """The ComplexFrequencyStep object is used to perform eigenvalue extraction to calculate
    the complex eigenvalues and corresponding complex mode shapes of a system. 
    The ComplexFrequencyStep object is derived from the AnalysisStep object. 

    Attributes
    ----------
    name: str
        A String specifying the repository key.
    numEigen: SymbolicConstant
        The SymbolicConstant ALL or an Int specifying the number of complex eigenmodes to be
        calculated or a SymbolicConstant ALL. The default value is ALL.
    shift: float
        None or a Float specifying the shift point in cycles per time. The default value is
        None.
    frictionDamping: Boolean
        A Boolean specifying whether to add to the damping matrix contributions due to friction
        effects. The default value is OFF.
    matrixStorage: SymbolicConstant
        A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC,
        UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT.
    minEigen: float
        None or a Float specifying the minimum frequency of interest in cycles per time. The
        default value is None.
    maxEigen: float
        None or a Float specifying the maximum frequency of interest in cycles per time. The
        default value is None.
    propertyEvaluationFrequency: float
        None or a Float specifying the frequency at which to evaluate frequency-dependent
        properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction.
        If the value is None, the analysis product will evaluate the stiffness associated with
        frequency-dependent springs and dashpots at zero frequency and will not consider the
        stiffness contributions from frequency-domain viscoelasticity in the step. The default
        value is None.
    previous: str
        A String specifying the name of the previous step. The new step appears after this step
        in the list of analysis steps.
    description: str
        A String specifying a description of the new step. The default value is an empty string.
    explicit: SymbolicConstant
        A SymbolicConstant specifying whether the step has an explicit procedure type
        (**procedureType=ANNEAL**, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).
    perturbation: Boolean
        A Boolean specifying whether the step has a perturbation procedure type.
    nonmechanical: Boolean
        A Boolean specifying whether the step has a mechanical procedure type.
    procedureType: SymbolicConstant
        A SymbolicConstant specifying the Abaqus procedure. Possible values are:
        - ANNEAL
        - BUCKLE
        - COMPLEX_FREQUENCY
        - COUPLED_TEMP_DISPLACEMENT
        - COUPLED_THERMAL_ELECTRIC
        - DIRECT_CYCLIC
        - DYNAMIC_IMPLICIT
        - DYNAMIC_EXPLICIT
        - DYNAMIC_SUBSPACE
        - DYNAMIC_TEMP_DISPLACEMENT
        - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL
        - FREQUENCY
        - GEOSTATIC
        - HEAT_TRANSFER
        - MASS_DIFFUSION
        - MODAL_DYNAMICS
        - RANDOM_RESPONSE
        - RESPONSE_SPECTRUM
        - SOILS
        - STATIC_GENERAL
        - STATIC_LINEAR_PERTURBATION
        - STATIC_RIKS
        - STEADY_STATE_DIRECT
        - STEADY_STATE_MODAL
        - STEADY_STATE_SUBSPACE
        - VISCO
    suppressed: Boolean
        A Boolean specifying whether the step is suppressed or not. The default value is OFF.
    fieldOutputRequestState: dict[str, FieldOutputRequestState]
        A repository of :py:class:`~abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState` objects.
    historyOutputRequestState: dict[str, HistoryOutputRequestState]
        A repository of :py:class:`~abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState` objects.
    diagnosticPrint: DiagnosticPrint
        A :py:class:`~abaqus.StepOutput.DiagnosticPrint.DiagnosticPrint` object.
    monitor: Monitor
        A :py:class:`~abaqus.StepOutput.Monitor.Monitor` object.
    restart: Restart
        A :py:class:`~abaqus.StepOutput.Restart.Restart` object.
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshConstraintState.AdaptiveMeshConstraintState` objects.
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain]
        A repository of :py:class:`~abaqus.Adaptivity.AdaptiveMeshDomain.AdaptiveMeshDomain` objects.
    control: Control
        A :py:class:`~abaqus.StepMiscellaneous.Control.Control` object.
    solverControl: SolverControl
        A :py:class:`~abaqus.StepMiscellaneous.SolverControl.SolverControl` object.
    boundaryConditionStates: dict[str, BoundaryConditionState]
        A repository of :py:class:`~abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState` objects.
    interactionStates: int
        A repository of :py:class:`~abaqus.Interaction.InteractionState.InteractionState` objects.
    loadStates: dict[str, LoadState]
        A repository of :py:class:`~abaqus.LoadAndLoadCase.LoadState.LoadState` objects.
    loadCases: dict[str, LoadCase]
        A repository of :py:class:`~abaqus.LoadAndLoadCase.LoadCase.LoadCase` objects.
    predefinedFieldStates: dict[str, PredefinedFieldState]
        A repository of :py:class:`~abaqus.PredefinedField.PredefinedFieldState.PredefinedFieldState` objects.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import step
        mdb.models[name].steps[name]

    Corresponding analysis keywords
    -------------------------------
        - COMPLEX FREQUENCY
        - STEP

    """

    # A String specifying the repository key. 
    name: str = ''

    # The SymbolicConstant ALL or an Int specifying the number of complex eigenmodes to be 
    # calculated or a SymbolicConstant ALL. The default value is ALL. 
    numEigen: SymbolicConstant = ALL

    # None or a Float specifying the shift point in cycles per time. The default value is 
    # None. 
    shift: float = None

    # A Boolean specifying whether to add to the damping matrix contributions due to friction 
    # effects. The default value is OFF. 
    frictionDamping: Boolean = OFF

    # A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
    # UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
    matrixStorage: SymbolicConstant = SOLVER_DEFAULT

    # None or a Float specifying the minimum frequency of interest in cycles per time. The 
    # default value is None. 
    minEigen: float = None

    # None or a Float specifying the maximum frequency of interest in cycles per time. The 
    # default value is None. 
    maxEigen: float = None

    # None or a Float specifying the frequency at which to evaluate frequency-dependent 
    # properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. 
    # If the value is None, the analysis product will evaluate the stiffness associated with 
    # frequency-dependent springs and dashpots at zero frequency and will not consider the 
    # stiffness contributions from frequency-domain viscoelasticity in the step. The default 
    # value is None. 
    propertyEvaluationFrequency: float = None

    # A String specifying the name of the previous step. The new step appears after this step 
    # in the list of analysis steps. 
    previous: str = ''

    # A String specifying a description of the new step. The default value is an empty string. 
    description: str = ''

    # A SymbolicConstant specifying whether the step has an explicit procedure type 
    # (*procedureType*=ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT). 
    explicit: SymbolicConstant = None

    # A Boolean specifying whether the step has a perturbation procedure type. 
    perturbation: Boolean = OFF

    # A Boolean specifying whether the step has a mechanical procedure type. 
    nonmechanical: Boolean = OFF

    # A SymbolicConstant specifying the Abaqus procedure. Possible values are: 
    # - ANNEAL 
    # - BUCKLE 
    # - COMPLEX_FREQUENCY 
    # - COUPLED_TEMP_DISPLACEMENT 
    # - COUPLED_THERMAL_ELECTRIC 
    # - DIRECT_CYCLIC 
    # - DYNAMIC_IMPLICIT 
    # - DYNAMIC_EXPLICIT 
    # - DYNAMIC_SUBSPACE 
    # - DYNAMIC_TEMP_DISPLACEMENT 
    # - COUPLED_THERMAL_ELECTRICAL_STRUCTURAL 
    # - FREQUENCY 
    # - GEOSTATIC 
    # - HEAT_TRANSFER 
    # - MASS_DIFFUSION 
    # - MODAL_DYNAMICS 
    # - RANDOM_RESPONSE 
    # - RESPONSE_SPECTRUM 
    # - SOILS 
    # - STATIC_GENERAL 
    # - STATIC_LINEAR_PERTURBATION 
    # - STATIC_RIKS 
    # - STEADY_STATE_DIRECT 
    # - STEADY_STATE_MODAL 
    # - STEADY_STATE_SUBSPACE 
    # - VISCO 
    procedureType: SymbolicConstant = None

    # A Boolean specifying whether the step is suppressed or not. The default value is OFF. 
    suppressed: Boolean = OFF

    # A repository of FieldOutputRequestState objects. 
    fieldOutputRequestState: dict[str, FieldOutputRequestState] = dict[str, FieldOutputRequestState]()

    # A repository of HistoryOutputRequestState objects. 
    historyOutputRequestState: dict[str, HistoryOutputRequestState] = dict[str, HistoryOutputRequestState]()

    # A DiagnosticPrint object. 
    diagnosticPrint: DiagnosticPrint = DiagnosticPrint()

    # A Monitor object. 
    monitor: Monitor = None

    # A Restart object. 
    restart: Restart = Restart()

    # A repository of AdaptiveMeshConstraintState objects. 
    adaptiveMeshConstraintStates: dict[str, AdaptiveMeshConstraintState] = dict[
        str, AdaptiveMeshConstraintState]()

    # A repository of AdaptiveMeshDomain objects. 
    adaptiveMeshDomains: dict[str, AdaptiveMeshDomain] = dict[str, AdaptiveMeshDomain]()

    # A Control object. 
    control: Control = Control()

    # A SolverControl object. 
    solverControl: SolverControl = SolverControl()

    # A repository of BoundaryConditionState objects. 
    boundaryConditionStates: dict[str, BoundaryConditionState] = dict[str, BoundaryConditionState]()

    # A repository of InteractionState objects. 
    interactionStates: int = None

    # A repository of LoadState objects. 
    loadStates: dict[str, LoadState] = dict[str, LoadState]()

    # A repository of LoadCase objects. 
    loadCases: dict[str, LoadCase] = dict[str, LoadCase]()

    # A repository of PredefinedFieldState objects. 
    predefinedFieldStates: dict[str, PredefinedFieldState] = dict[str, PredefinedFieldState]()

    def __init__(self, name: str, previous: str, numEigen: SymbolicConstant = ALL, description: str = '',
                 shift: float = None, frictionDamping: Boolean = OFF,
                 matrixStorage: SymbolicConstant = SOLVER_DEFAULT, maintainAttributes: Boolean = False,
                 minEigen: float = None, maxEigen: float = None,
                 propertyEvaluationFrequency: float = None):
        """This method creates a ComplexFrequencyStep object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ComplexFrequencyStep
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        previous
            A String specifying the name of the previous step. The new step appears after this step 
            in the list of analysis steps. 
        numEigen
            The SymbolicConstant ALL or an Int specifying the number of complex eigenmodes to be 
            calculated or a SymbolicConstant ALL. The default value is ALL. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        shift
            None or a Float specifying the shift point in cycles per time. The default value is 
            None. 
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction 
            effects. The default value is OFF. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        maintainAttributes
            A Boolean specifying whether to retain attributes from an existing step with the same 
            name. The default value is False. 
        minEigen
            None or a Float specifying the minimum frequency of interest in cycles per time. The 
            default value is None. 
        maxEigen
            None or a Float specifying the maximum frequency of interest in cycles per time. The 
            default value is None. 
        propertyEvaluationFrequency
            None or a Float specifying the frequency at which to evaluate frequency-dependent 
            properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. 
            If the value is None, the analysis product will evaluate the stiffness associated with 
            frequency-dependent springs and dashpots at zero frequency and will not consider the 
            stiffness contributions from frequency-domain viscoelasticity in the step. The default 
            value is None. 

        Returns
        -------
            A ComplexFrequencyStep object. 

        Raises
        ------
            RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, numEigen: SymbolicConstant = ALL, description: str = '', shift: float = None,
                  frictionDamping: Boolean = OFF, matrixStorage: SymbolicConstant = SOLVER_DEFAULT,
                  minEigen: float = None, maxEigen: float = None,
                  propertyEvaluationFrequency: float = None):
        """This method modifies the ComplexFrequencyStep object.
        
        Parameters
        ----------
        numEigen
            The SymbolicConstant ALL or an Int specifying the number of complex eigenmodes to be 
            calculated or a SymbolicConstant ALL. The default value is ALL. 
        description
            A String specifying a description of the new step. The default value is an empty string. 
        shift
            None or a Float specifying the shift point in cycles per time. The default value is 
            None. 
        frictionDamping
            A Boolean specifying whether to add to the damping matrix contributions due to friction 
            effects. The default value is OFF. 
        matrixStorage
            A SymbolicConstant specifying the type of matrix storage. Possible values are SYMMETRIC, 
            UNSYMMETRIC, and SOLVER_DEFAULT. The default value is SOLVER_DEFAULT. 
        minEigen
            None or a Float specifying the minimum frequency of interest in cycles per time. The 
            default value is None. 
        maxEigen
            None or a Float specifying the maximum frequency of interest in cycles per time. The 
            default value is None. 
        propertyEvaluationFrequency
            None or a Float specifying the frequency at which to evaluate frequency-dependent 
            properties for viscoelasticity, springs, and dashpots during the eigenvalue extraction. 
            If the value is None, the analysis product will evaluate the stiffness associated with 
            frequency-dependent springs and dashpots at zero frequency and will not consider the 
            stiffness contributions from frequency-domain viscoelasticity in the step. The default 
            value is None.

        Raises
        ------
            RangeError. 
        """
        pass
