from abaqusConstants import *


class ElectricalConductivity:
    """The ElectricalConductivity object specifies electrical conductivity.

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import material
        mdb.models[name].materials[name].electricalConductivity
        import odbMaterial
        session.odbs[name].materials[name].electricalConductivity

    The table data for this object are:

    - If *type*=ISOTROPIC, the table data specify the following:
        - Electrical conductivity.
        - Frequency, if the data depend on frequency.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If *type*=ORTHOTROPIC, the table data specify the following:
        - σE1E.
        - σE2E.
        - σE3E.
        - Frequency, if the data depend on frequency.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.
    - If *type*=ANISOTROPIC, the table data specify the following:
        - σ11E.
        - σ12E.
        - σE2E.
        - σE3E.
        - σE3E.
        - σE3E.
        - Frequency, if the data depend on frequency.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    The corresponding analysis keywords are:

    - ELECTRICAL CONDUCTIVITY

    """

    def __init__(self, table: tuple, type: SymbolicConstant = ISOTROPIC, frequencyDependency: Boolean = OFF,
                 temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates an ElectricalConductivity object.

        Notes
        -----
            This function can be accessed by:
            
            .. code-block:: python
            
                mdb.models[name].materials[name].ElectricalConductivity
                session.odbs[name].materials[name].ElectricalConductivity
        
        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        type
            A SymbolicConstant specifying the type of electrical conductivity. Possible values are 
            ISOTROPIC, ORTHOTROPIC, and ANISOTROPIC. The default value is ISOTROPIC. 
        frequencyDependency
            A Boolean specifying whether the data depend on frequency. The default value is OFF. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            An ElectricalConductivity object. 

        Raises
        ------
        RangeError
        """
        pass

    def setValues(self):
        """This method modifies the ElectricalConductivity object.

        Raises
        ------
        RangeError
        """
        pass