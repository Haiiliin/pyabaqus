from abaqusConstants import *
from .Leaf import Leaf


class LeafFromOdbNodePick(Leaf):

    """The LeafFromOdbNodePick object can be used whenever a Leaf object is expected as an 
    argument. Leaf objects are used to specify the items in a display group. Leaf objects 
    are constructed as temporary objects, which are then used as arguments to DisplayGroup 
    commands. 
    The LeafFromOdbNodePick object is derived from the Leaf object. 

    Access
    ------
        - import displayGroupOdbToolset

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the leaf type. Possible values are EMPTY_LEAF, 
    # DEFAULT_MODEL, ALL_ELEMENTS, ALL_NODES, and ALL_SURFACES. 
    leafType: SymbolicConstant = None

    def __init__(self, nodePick: tuple):
        """This method creates a Leaf object from a tuple containing machine readable, compact
        strings defining the nodes picked for each part instance. Leaf objects specify the items
        in a display group.

        Path
        ----
            - LeafFromOdbNodePick

        Parameters
        ----------
        nodePick
            A sequence of tuples of the form [part name, entity count, machine readable pick 
            strings]. 

        Returns
        -------
            A LeafFromOdbNodePick object. 

        Exceptions
        ----------
            None. 
        """
        super().__init__(DEFAULT_MODEL)
        pass

