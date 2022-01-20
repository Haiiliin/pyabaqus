from abaqusConstants import *


class Potential:
    """The Potential object defines an anisotropic yield/creep model.

    Access
    ------
        - import material
        - mdb.models[name].materials[name].creep.potential
        - mdb.models[name].materials[name].Plastic.potential
        - mdb.models[name].materials[name].viscous.potential
        - import odbMaterial
        - session.odbs[name].materials[name].creep.potential
        - session.odbs[name].materials[name].Plastic.potential
        - session.odbs[name].materials[name].viscous.potential

    Table Data
    ----------
        - R11.
        - R22.
        - R33.
        - R12.
        - R13.
        - R23.
        - Temperature, if the data depend on temperature.
        - Value of the first field variable, if the data depend on field variables.
        - Value of the second field variable.
        - Etc.

    Corresponding analysis keywords
    -------------------------------
        - POTENTIAL

    """

    def __init__(self, table: tuple, temperatureDependency: Boolean = OFF, dependencies: int = 0):
        """This method creates a Potential object.

        Path
        ----
            - mdb.models[name].materials[name].creep.Potential
            - mdb.models[name].materials[name].Plastic.Potential
            - mdb.models[name].materials[name].viscous.Potential
            - session.odbs[name].materials[name].creep.Potential
            - session.odbs[name].materials[name].Plastic.Potential
            - session.odbs[name].materials[name].viscous.Potential

        Parameters
        ----------
        table
            A sequence of sequences of Floats specifying the items described below. 
        temperatureDependency
            A Boolean specifying whether the data depend on temperature. The default value is OFF. 
        dependencies
            An Int specifying the number of field variable dependencies. The default value is 0. 

        Returns
        -------
            A Potential object. 

        Exceptions
        ----------
            RangeError. 
        """
        pass

    def setValues(self):
        """This method modifies the Potential object.

        Parameters
        ----------

        Returns
        -------
            None. 

        Exceptions
        ----------
            RangeError. 
        """
        pass