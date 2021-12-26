from abaqusConstants import *
from .OdbInstance import OdbInstance
from .SectionPoint import SectionPoint


class FieldValue:

    """The FieldValue object represents the field data at a point. The FieldValue object has no 
    constructor; it is created by the Odb object when data are added to the FieldOutput 
    object using the addData method. For faster, bulk-data access, see Using bulk data 
    access to an output database. 

    Access
    ------
        - import odbAccess
        - session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A SymbolicConstant specifying the position of the output in the element. Possible values 
    # are: 
    # - NODAL, specifying the values calculated at the nodes. 
    # - INTEGRATION_POINT, specifying the values calculated at the integration points. 
    # - ELEMENT_NODAL, specifying the values obtained by extrapolating results calculated at 
    # the integration points. 
    # - ELEMENT_FACE, specifying the results obtained for surface variables such as cavity 
    # radiation that are defined for the surface facets of an element. 
    # - CENTROID, specifying the value at the centroid obtained by extrapolating results 
    # calculated at the integration points. 
    position: SymbolicConstant = None

    # A SymbolicConstant specifying the precision of the output in the element. Possible 
    # values are: 
    # - SINGLE_PRECISION, specifying that the output values are in single precision. 
    # - DOUBLE_PRECISION, specifying that the output values are in double precision. 
    precision: SymbolicConstant = None

    # An Int specifying the element label of the element containing the location. 
    # *elementLabel* is available only if *position*=INTEGRATION_POINT, CENTROID, 
    # ELEMENT_NODAL, or ELEMENT_FACE. 
    elementLabel: int = None

    # An Int specifying the node label of the node containing the location. *nodelabel* is 
    # available only if *position*=ELEMENT_NODAL or NODAL. 
    nodeLabel: int = None

    # An Int specifying the integration point in the element. *integrationPoint* is available 
    # only if *position*=INTEGRATION_POINT. 
    integrationPoint: int = None

    # A SymbolicConstant specifying the face of the element. *face* is available only if 
    # *position*=ELEMENT_FACE. 
    face: SymbolicConstant = None

    # A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR, 
    # TENSOR_3D_FULL, TENSOR_3D_PLANAR, TENSOR_3D_SURFACE, TENSOR_2D_PLANAR, and 
    # TENSOR_2D_SURFACE. 
    type: SymbolicConstant = None

    # A Float specifying the length or magnitude of the vector. *magnitude* is valid only when 
    # *type*=VECTOR. 
    magnitude: float = None

    # A Float specifying the calculated von Mises stress. The value is valid only when the 
    # *validInvariants* member includes MISES; otherwise, the value is indeterminate. 
    # Conjugate data will be ignored in invariant calculation. 
    mises: float = None

    # A Float specifying the calculated Tresca stress. The value is valid only when the 
    # *validInvariants* member includes TRESCA; otherwise, the value is indeterminate. 
    # Conjugate data will be ignored in invariant calculation. 
    tresca: float = None

    # A Float specifying the calculated pressure stress. The value is valid only when the 
    # *validInvariants* member includes PRESS; otherwise, the value is indeterminate. 
    # Conjugate data will be ignored in invariant calculation. 
    press: float = None

    # A Float specifying the calculated third stress invariant. The value is valid only when 
    # the *validInvariants* member includes INV3; otherwise, the value is indeterminate. 
    # Conjugate data will be ignored in invariant calculation. 
    inv3: float = None

    # A Float specifying the calculated maximum principal stress. The value is valid only when 
    # the *validInvariants* member includes MAX_PRINCIPAL; otherwise, the value is 
    # indeterminate. Conjugate data will be ignored in invariant calculation. 
    maxPrincipal: float = None

    # A Float specifying the calculated intermediate principal stress. The value is valid only 
    # when the *validInvariants* member includes MID_PRINCIPAL; otherwise, the value is 
    # indeterminate. Conjugate data will be ignored in invariant calculation. 
    midPrincipal: float = None

    # A Float specifying the minimum principal stress. The value is valid only when the 
    # *validInvariants* member includes MIN_PRINCIPAL; otherwise, the value is indeterminate. 
    # Conjugate data will be ignored in invariant calculation. 
    minPrincipal: float = None

    # A Float specifying the maximum principal in-plane stress. The value is valid only when 
    # the *validInvariants* member includes MAX_INPLANE_PRINCIPAL; otherwise, the value is 
    # indeterminate. Conjugate data will be ignored in invariant calculation. 
    maxInPlanePrincipal: float = None

    # A Float specifying the calculated minimum principal in-plane stress. The value is valid 
    # only when the *validInvariants* member includes MIN_INPLANE_PRINCIPAL; otherwise, the 
    # value is indeterminate. Conjugate data will be ignored in invariant calculation. 
    minInPlanePrincipal: float = None

    # A Float specifying the calculated principal out-of-plane stress. The value is valid only 
    # when the *validInvariants* member includes OUTOFPLANE_PRINCIPAL; otherwise, the value is 
    # indeterminate. Conjugate data will be ignored in invariant calculation. 
    outOfPlanePrincipal: float = None

    # An OdbInstance object specifying the part to which the labels belong. 
    instance: OdbInstance = OdbInstance()

    # A SectionPoint object. 
    sectionPoint: SectionPoint = None

    # A tuple of tuples of Floats specifying the 3 × 3 matrix of Floats specifying the 
    # direction cosines of the local coordinate system (the rotation from global to local). 
    # Each sequence represents a row in the direction cosine matrix. *localCoordSystem* is 
    # available for TENSOR data written in a local coordinate system. It is also available for 
    # VECTOR data for connector element outputs. For connector element outputs the rotation is 
    # from local to global. If the underlying data are in double precision, an exception will 
    # be thrown. 
    localCoordSystem: tuple = ()

    # A tuple of tuples of Floats specifying the 3 × 3 matrix of Doubles specifying the 
    # direction cosines of the local coordinate system (the rotation from global to local). 
    # Each sequence represents a row in the direction cosine matrix. *localCoordSystemDouble* 
    # is available for TENSOR data written in a local coordinate system. It is also available 
    # for VECTOR data for connector element outputs. For connector element outputs the 
    # rotation is from local to global. If the underlying data are in single precision, an 
    # exception will be thrown. 
    localCoordSystemDouble: tuple = ()

    # A tuple of Floats specifying data in the form described by *type*. If *type*=TENSOR or 
    # VECTOR, *data* is a sequence containing the components. If the underlying data are in 
    # double precision an exception will be thrown. 
    data: tuple = ()

    # A tuple of Floats specifying data in the form described by *type*. If *type*=TENSOR or 
    # VECTOR, *data* is a sequence containing the components. If the underlying data are in 
    # single precision, an exception will be thrown. 
    dataDouble: tuple = ()

    # A tuple of Floats specifying data in the form described by *type*. If *type*=TENSOR or 
    # VECTOR, *conjugateData* is a sequence containing the components. If the underlying data 
    # are in double precision, an exception will be thrown. 
    conjugateData: tuple = ()

    # A tuple of Floats specifying data in the form described by *type*. If *type*=TENSOR or 
    # VECTOR, *conjugateData* is a sequence containing the components. If the underlying data 
    # are in single precision, an exception will be thrown. 
    conjugateDataDouble: tuple = ()

