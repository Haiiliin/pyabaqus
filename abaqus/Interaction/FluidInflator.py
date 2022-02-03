from .Interaction import Interaction


class FluidInflator(Interaction):
    """The FluidInflator object is used to define a fluid inflator to model deployment of an
    airbag. 
    The FluidInflator object is derived from the Interaction object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].interactions[name]

    Corresponding analysis keywords
    -------------------------------
        - FLUID INFLATOR

    """

    def __init__(self, name: str, createStepName: str, cavity: str, interactionProperty: str,
                 inflationTimeAmplitude: str = '', massFlowAmplitude: str = ''):
        """This method creates a FluidInflator object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].FluidInflator
        
        Parameters
        ----------
        name
            A String specifying the repository key. 
        createStepName
            A String specifying the name of the step in which the FluidInflator object is created. 
        cavity
            A String specifying the first FluidCavity object associated with this interaction. 
        interactionProperty
            A String specifying the FluidInflatorProperty object associated with this interaction. 
        inflationTimeAmplitude
            A string specifying the name of the amplitude curve defining a mapping between the 
            inflation time and the actual time. 
        massFlowAmplitude
            A string specifying the name of the amplitude curve by which to modify the mass flow 
            rate. 

        Returns
        -------
            A FluidInflator object. . 
        """
        super().__init__()
        pass

    def setValues(self, inflationTimeAmplitude: str = '', massFlowAmplitude: str = ''):
        """This method modifies the FluidInflator object.
        
        Parameters
        ----------
        inflationTimeAmplitude
            A string specifying the name of the amplitude curve defining a mapping between the 
            inflation time and the actual time. 
        massFlowAmplitude
            A string specifying the name of the amplitude curve by which to modify the mass flow 
            rate. 
        """
        pass
