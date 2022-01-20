from abaqus.Sketcher.ConstrainedSketchBase import ConstrainedSketchBase
from abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry import ConstrainedSketchGeometry
from abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex import ConstrainedSketchVertex
from abaqusConstants import *


class ConstrainedSketchDimensionModel(ConstrainedSketchBase):
    """The ConstrainedSketchDimension object stores the dimensions associated with a sketch.

    Access
    ------
        - import sketch
        - mdb.models[name].sketches[name].dimensions[i]

    Table Data
    ----------

    Corresponding analysis keywords
    -------------------------------

    """

    def AngularDimension(self, line1: ConstrainedSketchGeometry, line2: ConstrainedSketchGeometry,
                         textPoint: tuple[float], value: float = None, reference: Boolean = OFF):
        """This method constructs a ConstrainedSketchDimension object between two
        ConstrainedSketchGeometry objects, with the given angle between them.

        Path
        ----
            - mdb.models[name].sketches[name].AngularDimension

        Parameters
        ----------
        line1
            A ConstrainedSketchGeometry object specifying the first line.
        line2
            A ConstrainedSketchGeometry object specifying the second line.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float specifying the angle between the two lines.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the angle between two lines.

        Returns
        -------
            A ConstrainedSketchDimension object (None if the dimension cannot be created).

        Exceptions
        ----------
            None.
            !img
        """
        pass

    def HorizontalDimension(self, vertex1: ConstrainedSketchVertex, vertex2: ConstrainedSketchVertex,
                            textPoint: tuple[float], value: float = None, reference: Boolean = OFF):
        """This method constructs a ConstrainedSketchDimension object between two vertices. A
        horizontal dimension indicates the horizontal distance along the *X*-axis between two
        vertices.

        Path
        ----
            - mdb.models[name].sketches[name].HorizontalDimension

        Parameters
        ----------
        vertex1
            A ConstrainedSketchVertex object specifying the first endpoint.
        vertex2
            A ConstrainedSketchVertex object specifying the second endpoint.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float distance between the two vertices.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the distance between the two vertices.

        Returns
        -------
            A ConstrainedSketchDimension object (None if the dimension cannot be created).

        Exceptions
        ----------
            None.
            !img
        """
        pass

    def ObliqueDimension(self, vertex1: ConstrainedSketchVertex, vertex2: ConstrainedSketchVertex,
                         textPoint: tuple[float], value: float = None, reference: Boolean = OFF):
        """This method constructs a ConstrainedSketchDimension object between two vertices. An
        oblique dimension indicates the distance between two vertices.

        Path
        ----
            - mdb.models[name].sketches[name].ObliqueDimension

        Parameters
        ----------
        vertex1
            A ConstrainedSketchVertex object specifying the first endpoint.
        vertex2
            A ConstrainedSketchVertex object specifying the second endpoint.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float specifying the distance between the two ConstrainedSketchVertex objects.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the distance between the two vertices.

        Returns
        -------
            A ConstrainedSketchDimension object (None if the dimension cannot be created).

        Exceptions
        ----------
            None.
            !img
        """
        pass

    def RadialDimension(self, curve: ConstrainedSketchGeometry, textPoint: tuple[float], value: float = None,
                        reference: Boolean = OFF, majorRadius: float = None, minorRadius: float = None):
        """This method constructs a ConstrainedSketchDimension object on a circular or elliptical
        arc. A radial dimension indicates the radius of an arc or circle or the major or minor
        radius of an ellipse.

        Path
        ----
            - mdb.models[name].sketches[name].RadialDimension

        Parameters
        ----------
        curve
            A ConstrainedSketchGeometry object specifying the circular or elliptical arc.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float specifying the radius of the arc, circle or ellipse.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the angle between two lines.
        majorRadius
            A Float specifying the major Radius if *curve* is an ellipse. This is mutually exclusive
            with *value* and *minorRadius*.
        minorRadius
            A Float specifying the minor Radius if *curve* is an ellipse. This is mutually exclusive
            with *value* and *majorRadius*.

        Returns
        -------
            A ConstrainedSketchDimension object (None if the dimension cannot be created).

        Exceptions
        ----------
            None.
            !img
        """
        pass

    def VerticalDimension(self, vertex1: ConstrainedSketchVertex, vertex2: ConstrainedSketchVertex,
                          textPoint: tuple[float], value: float = None, reference: Boolean = OFF):
        """This method constructs a ConstrainedSketchDimension between two vertices. A vertical
        dimension controls the vertical distance along the *Y*-axis between two vertices.

        Path
        ----
            - mdb.models[name].sketches[name].VerticalDimension

        Parameters
        ----------
        vertex1
            A ConstrainedSketchVertex object specifying the first endpoint.
        vertex2
            A ConstrainedSketchVertex object specifying the second endpoint.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float specifying the angle between the two lines.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the angle between two lines.

        Returns
        -------
            A ConstrainedSketchDimension object (None if the dimension cannot be created).

        Exceptions
        ----------
            None.
            !img
        """
        pass

    def DistanceDimension(self, entity1: ConstrainedSketchVertex, entity2: ConstrainedSketchVertex,
                          textPoint: tuple[float], value: float = None, reference: Boolean = OFF):
        """This method constructs a ConstrainedSketchDimension object between two
        ConstrainedSketchGeometry, or aConstrainedSketchVertex and ConstrainedSketchGeometry
        object. A distance dimension specifies the shortest distance between two entities.

        Path
        ----
            - mdb.models[name].sketches[name].DistanceDimension

        Parameters
        ----------
        entity1
            A ConstrainedSketchVertex object or ConstrainedSketchGeometry object.
        entity2
            A ConstrainedSketchVertex object or ConstrainedSketchGeometry object.
        textPoint
            A pair of Floats specifying the location of the dimension text.
        value
            A Float specifying the angle between the two lines.
        reference
            A Boolean specifying whether the created dimension enforces the above value or if it
            simply measures the angle between two lines.

        Returns
        -------
            A ConstrainedSketchDimension object (None if the dimension cannot be created).

        Exceptions
        ----------
            None.
            !img
        """
        pass