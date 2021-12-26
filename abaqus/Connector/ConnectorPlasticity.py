from abaqusConstants import *
from .ConnectorBehaviorOption import ConnectorBehaviorOption
from .ConnectorOptions import ConnectorOptions
from .ConnectorPotentialArray import ConnectorPotentialArray


class ConnectorPlasticity(ConnectorBehaviorOption):

    """The ConnectorPlasticity object defines plastic behavior for one or more components of a 
    connector's relative motion. 
    The ConnectorPlasticity object is derived from the ConnectorBehaviorOption object. 

    Access
    ------
        - import section
        - mdb.models[name].sections[name].behaviorOptions[i]
        - import odbSection
        - session.odbs[name].sections[name].behaviorOptions[i]

    Table Data
    ----------
        Table data for *isotropicTable*:
        If *isotropicType*=TABULAR, then each sequence of the table data specifies the following:
        - Equivalent yield force or moment defining the size of the elastic range.
        - Equivalent relative plastic motion.
        - Equivalent relative plastic motion rate.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *isotropicType*=EXPONENTIAL_LAW, then each sequence of the table data specifies the following:
        - Equivalent force or moment defining the size of the elastic range at zero plastic motion.
        - Isotropic hardening parameter QinfQinf.
        - Isotropic hardening parameter bb.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        Table data for *kinematicTable*:
        If *kinematicType*=HALF_CYCLE, then each sequence of the table data specifies the following:
        - Yield force or moment.
        - Connector relative plastic motion.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *kinematicType*=STABILIZED, then each sequence of the table data specifies the following:
        - Yield force or moment.
        - Connector relative plastic motion.
        - Connector relative constitutive motion range.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
        If *kinematicType*=PARAMETERS, then each sequence of the table data specifies the following:
        - Yield force or moment at zero relative plastic motion.
        - Kinematic hardening parameter CC.
        - Kinematic hardening parameter γγ. Set γγ=0 to specify linear Ziegler kinematic hardening.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - CONNECTOR PLASTICITY
        - CONNECTOR HARDENING
        - CONNECTOR POTENTIAL

    """

    # A ConnectorOptions object specifying the ConnectorOptions used to define tabular options 
    # for the isotropic hardening table. 
    isotropicOptions: ConnectorOptions = ConnectorOptions()

    # A ConnectorOptions object specifying the ConnectorOptions used to define tabular options 
    # for the kinematic hardening table. 
    kinematicOptions: ConnectorOptions = ConnectorOptions()

    def __init__(self, coupling: SymbolicConstant = UNCOUPLED, isotropic: Boolean = ON, 
                 isotropicType: SymbolicConstant = TABULAR, isotropicTemperature: Boolean = OFF, 
                 isotropicDependencies: int = 0, kinematic: Boolean = OFF, 
                 kinematicType: SymbolicConstant = HALF_CYCLE, kinematicTemperature: Boolean = OFF, 
                 kinematicDependencies: int = 0, forcePotentialOperator: SymbolicConstant = SUM, 
                 forcePotentialExponent: float = 2, 
                 connectorPotentials: ConnectorPotentialArray = None,
                 isotropicTable: tuple = (), kinematicTable: tuple = (), components: tuple = ()):
        """This method creates a connector plasticity behavior option for a ConnectorSection
        object.

        Path
        ----
            -           import connectorBehavior
            -           connectorBehavior.ConnectorPlasticity
            -           import odbConnectorBehavior
            -           odbConnectorBehavior.ConnectorPlasticity

        Parameters
        ----------
        coupling
            A SymbolicConstant specifying whether or not the behavior is coupled. Possible values 
            are UNCOUPLED and COUPLED. The default value is UNCOUPLED. 
        isotropic
            A Boolean specifying whether isotropic hardening data will be used. The default value is 
            ON.If *isotropic*=OFF, then *kinematic* must be specified as ON. 
        isotropicType
            A SymbolicConstant specifying the type of isotropic hardening to be specified. Possible 
            values are TABULAR and EXPONENTIAL_LAW. The default value is TABULAR.This argument is 
            applicable only if *isotropic*=ON. 
        isotropicTemperature
            A Boolean specifying whether the isotropic data depend on temperature. The default value 
            is OFF.This argument is applicable only if *isotropic*=ON. 
        isotropicDependencies
            An Int specifying the number of field variable dependencies for the isotropic data. The 
            default value is 0.This argument is applicable only if *isotropic*=ON. 
        kinematic
            A Boolean specifying whether kinematic hardening data will be used. The default value is 
            OFF.If *kinematic*=OFF, then *isotropic* must be specified as ON. 
        kinematicType
            A SymbolicConstant specifying the type of kinematic hardening to be specified. Possible 
            values are HALF_CYCLE, STABILIZED, and PARAMETERS. The default value is HALF_CYCLE.This 
            argument is applicable only if *kinematic*=ON. 
        kinematicTemperature
            A Boolean specifying whether the kinematic data depend on temperature. The default value 
            is OFF.This argument is applicable only if *kinematic*=ON. 
        kinematicDependencies
            An Int specifying the number of field variable dependencies for the kinematic data. The 
            default value is 0.This argument is applicable only if *kinematic*=ON. 
        forcePotentialOperator
            A SymbolicConstant specifying the contribution operator for the force potential 
            contributions. Possible values are SUM and MAXIMUM. The default value is SUM.This 
            argument is applicable only if *coupling*=COUPLED. 
        forcePotentialExponent
            A Float specifying the number equal to the inverse of the overall exponent in the force 
            potential definition. The default value is 2.0.This argument is applicable only if 
            *coupling*=COUPLED and if *forcePotentialOperator*=SUM. 
        connectorPotentials
            A ConnectorPotentialArray object specifying one ConnectorPotential object for each force 
            potential contribution. This member can be specified only if *coupling*=COUPLED. 
        isotropicTable
            A sequence of sequences of Floats specifying isotropic plasticity properties. Items in 
            the *isotropicTable* data are described below. This argument is applicable only if 
            *isotropic*=ON. The default value is an empty sequence. 
        kinematicTable
            A sequence of sequences of Floats specifying kinematic plasticity properties. Items in 
            the *kinematicTable* data are described below. This argument is applicable only if 
            *kinematic*=ON. The default value is an empty sequence. 
        components
            A sequence of Ints specifying the components of relative motion for which the behavior 
            is defined. Possible values are 1 ≤≤ *components* ≤≤ 6. Only available components can be 
            specified. This argument can be specified only if *coupling*=UNCOUPLED. The default 
            value is an empty sequence. 

        Returns
        -------
            A ConnectorPlasticity object. 

        Exceptions
        ----------
            ValueError and TextError. 
        """
        super().__init__()
        pass

    def setValues(self):
        """This method modifies the ConnectorPlasticity object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            ValueError. 
        """
        pass

