from .ConstrainedSketchConstraint import ConstrainedSketchConstraint
from .ConstrainedSketchDimension.ConstrainedSketchDimension import ConstrainedSketchDimension
from .ConstrainedSketchOptions.ConstrainedSketchImageOptions import ConstrainedSketchImageOptions
from .ConstrainedSketchOptions.ConstrainedSketchOptions import ConstrainedSketchOptions
from .ConstrainedSketchParameter.ConstrainedSketchParameter import ConstrainedSketchParameter
from .ConstrainedSketchVertex.ConstrainedSketchVertexArray import ConstrainedSketchVertexArray
from ..Amplitude.ConstrainedSketchGeometryArray import ConstrainedSketchGeometryArray
from ..UtilityAndView.Repository import Repository


class ConstrainedSketchBase:
    """A ConstrainedSketch object contains the entities that are used to create a sketch. The
    objects include ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository,
    such as Line, Arc, and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and ConstrainedSketchParameter objects are
    contained in their respective repositories. 

    Access
    ------
        - import sketch
        - mdb.models[name].sketches[name]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    # A repository of ConstrainedSketchConstraint objects. 
    constraints: Repository[str, ConstrainedSketchConstraint] = Repository[str, ConstrainedSketchConstraint]()

    # A repository of ConstrainedSketchDimension objects. 
    dimensions: Repository[str, ConstrainedSketchDimension] = Repository[str, ConstrainedSketchDimension]()

    # A ConstrainedSketchGeometryArray object specifying the sketch geometry, such as lines, 
    # arcs, circles, and splines. 
    geometry: ConstrainedSketchGeometryArray = ConstrainedSketchGeometryArray()

    # A repository of ConstrainedSketchParameter objects specifying sketch parameters, which 
    # may be associated with dimensions. 
    parameters: Repository[str, ConstrainedSketchParameter] = Repository[str, ConstrainedSketchParameter]()

    # A ConstrainedSketchOptions object specifying the sketch option settings. 
    sketchOptions: ConstrainedSketchOptions = ConstrainedSketchOptions()

    # A ConstrainedSketchVertexArray object. 
    vertices: ConstrainedSketchVertexArray = ConstrainedSketchVertexArray()

    # A ConstrainedSketchImageOptions object. 
    imageOptions: ConstrainedSketchImageOptions = ConstrainedSketchImageOptions()