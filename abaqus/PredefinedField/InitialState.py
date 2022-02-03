from abaqusConstants import *
from .PredefinedField import PredefinedField
from ..Assembly.PartInstanceArray import PartInstanceArray


class InitialState(PredefinedField):
    """The InitialState object stores the data for an initial state predefined field.
    The InitialState object is derived from the PredefinedField object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import load
        mdb.models[name].predefinedFields[name]

    Corresponding analysis keywords
    -------------------------------
        - INSTANCE

    """

    def __init__(self, name: str, instances: PartInstanceArray, fileName: str,
                 endStep: SymbolicConstant = LAST_STEP, endIncrement: SymbolicConstant = STEP_END,
                 updateReferenceConfiguration: Boolean = OFF):
        """This method creates an InitialState predefined field object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].InitialState
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        instances
            A PartInstanceArray object specifying the instances to which the predefined field is 
            applied. 
        fileName
            A String specifying the name of the job that generated the initial state data. 
        endStep
            The SymbolicConstant LAST_STEP or an Int specifying the step from which the initial 
            state values are to be read or the SymbolicConstant LAST_STEP. The default value is 
            LAST_STEP. 
        endIncrement
            The SymbolicConstant STEP_END or an Int specifying the increment, interval or iteration 
            of the step set in *endStep* or the SymbolicConstant STEP_END. The default value is 
            STEP_END. 
        updateReferenceConfiguration
            A Boolean specifying whether to update the reference configuration based on the import 
            data. The default value is OFF. 

        Returns
        -------
            An InitialState object. . 
        """
        super().__init__()
        pass

    def setValues(self, endStep: SymbolicConstant = LAST_STEP, endIncrement: SymbolicConstant = STEP_END,
                  updateReferenceConfiguration: Boolean = OFF):
        """This method modifies the InitialState object.
        
        Parameters
        ----------
        endStep
            The SymbolicConstant LAST_STEP or an Int specifying the step from which the initial 
            state values are to be read or the SymbolicConstant LAST_STEP. The default value is 
            LAST_STEP. 
        endIncrement
            The SymbolicConstant STEP_END or an Int specifying the increment, interval or iteration 
            of the step set in *endStep* or the SymbolicConstant STEP_END. The default value is 
            STEP_END. 
        updateReferenceConfiguration
            A Boolean specifying whether to update the reference configuration based on the import 
            data. The default value is OFF. 
        """
        pass
