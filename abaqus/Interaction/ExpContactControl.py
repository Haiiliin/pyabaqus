from abaqusConstants import *
from .ContactControl import ContactControl


class ExpContactControl(ContactControl):
    """The ExpContactControl object is used in Abaqus/Explicit analyses to specify optional
    solution controls for problems involving contact between bodies. 
    The ExpContactControl object is derived from the ContactControl object. 

    Notes
    -----
    This object can be accessed by:

    .. code-block:: python

        import interaction
        mdb.models[name].contactControls[name]

    Corresponding analysis keywords
    -------------------------------
        - CONTACT CONTROLS

    """

    def __init__(self, name: str, globTrkChoice: SymbolicConstant = DEFAULT, globTrkInc: int = None,
                 fastLocalTrk: Boolean = ON, scalePenalty: float = 1, warpCheckPeriod: int = 20,
                 warpCutoff: float = 20):
        """This method creates an ExpContactControl object.

        Notes
        -----
        This function can be accessed by:

        .. code-block:: python

            mdb.models[name].ExpContactControl
        
        Parameters
        ----------
        name
            A String specifying the contact controls repository key. 
        globTrkChoice
            A SymbolicConstant specifying whether or not the default value will be used for the 
            maximum number of increments between global contact searches. Possible values are 
            DEFAULT and SPECIFY. The default value is DEFAULT. 
        globTrkInc
            An Int specifying the maximum number of increments between global contact searches. The 
            *globTrkInc* argument applies only when *globTrkChoice*=SPECIFY. The default value is 
            100 for surface-to-surface contact and 4 for self-contact. 
        fastLocalTrk
            A Boolean specifying whether to use the more computationally efficient local tracking 
            method. The default value is ON. 
        scalePenalty
            A Float specifying the factor by which Abaqus/Explicit will scale the default penalty 
            stiffness to obtain the stiffnesses used for the penalty contact pairs. The default 
            value is 1.0. 
        warpCheckPeriod
            An Int specifying the number of increments between checks for highly warped facets on 
            main surfaces. The default value is 20. 
        warpCutoff
            A Float specifying the out-of-plane warping angle (in degrees), at which a facet will be 
            considered to be highly warped. The default value is 20.0. 

        Returns
        -------
            An ExpContactControl object. 

        Raises
        ------
            RangeError. 
        """
        super().__init__()
        pass

    def setValues(self, globTrkChoice: SymbolicConstant = DEFAULT, globTrkInc: int = None,
                  fastLocalTrk: Boolean = ON, scalePenalty: float = 1, warpCheckPeriod: int = 20,
                  warpCutoff: float = 20):
        """This method modifies the ExpContactControl object.
        
        Parameters
        ----------
        globTrkChoice
            A SymbolicConstant specifying whether or not the default value will be used for the 
            maximum number of increments between global contact searches. Possible values are 
            DEFAULT and SPECIFY. The default value is DEFAULT. 
        globTrkInc
            An Int specifying the maximum number of increments between global contact searches. The 
            *globTrkInc* argument applies only when *globTrkChoice*=SPECIFY. The default value is 
            100 for surface-to-surface contact and 4 for self-contact. 
        fastLocalTrk
            A Boolean specifying whether to use the more computationally efficient local tracking 
            method. The default value is ON. 
        scalePenalty
            A Float specifying the factor by which Abaqus/Explicit will scale the default penalty 
            stiffness to obtain the stiffnesses used for the penalty contact pairs. The default 
            value is 1.0. 
        warpCheckPeriod
            An Int specifying the number of increments between checks for highly warped facets on 
            main surfaces. The default value is 20. 
        warpCutoff
            A Float specifying the out-of-plane warping angle (in degrees), at which a facet will be 
            considered to be highly warped. The default value is 20.0.

        Raises
        ------
            RangeError. 
        """
        pass
