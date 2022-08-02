import typing

from abaqusConstants import *
from .ConstrainedSketchConstraint.ConstrainedSketchConstraintModel import (
    ConstrainedSketchConstraintModel,
)
from .ConstrainedSketchDimension.ConstrainedSketchDimensionModel import (
    ConstrainedSketchDimensionModel,
)
from .ConstrainedSketchGeometry.ConstrainedSketchGeometry import (
    ConstrainedSketchGeometry,
)
from .ConstrainedSketchGeometry.ConstrainedSketchGeometryModel import (
    ConstrainedSketchGeometryModel,
)
from .ConstrainedSketchParameter.ConstrainedSketchParameterModel import (
    ConstrainedSketchParameterModel,
)
from .ConstrainedSketchVertex.ConstrainedSketchVertex import ConstrainedSketchVertex
from .ConstrainedSketchVertex.ConstrainedSketchVertexModel import (
    ConstrainedSketchVertexModel,
)
from ..Part.AcisFile import AcisFile


class ConstrainedSketch(
    ConstrainedSketchConstraintModel,
    ConstrainedSketchDimensionModel,
    ConstrainedSketchGeometryModel,
    ConstrainedSketchParameterModel,
    ConstrainedSketchVertexModel,
):
    @typing.overload
    def __init__(
        self,
        name: str,
        sheetSize: float,
        gridSpacing: float = None,
        transform: tuple = (),
    ):
        """This method creates a ConstrainedSketch object. If the sketch cannot be created, the
        method returns None.

        Notes
        -----
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ConstrainedSketch

        Parameters
        ----------
        name
            A String specifying the repository key.
        sheetSize
            A Float specifying the sheet size.
        gridSpacing
            A Float specifying the spacing between gridlines. Possible values are Floats >> 0. The
            default value is approximately 2 percent of *sheetSize*.
        transform
            A sequence of sequences of Floats specifying the three-dimensional orientation of the
            sketch. The sequence is a 3 × 4 transformation matrix specifying the axis of rotation
            and the translation vector. Possible values are any Floats.The default value for the
            axis of rotation is the identity matrix`(1.0, 0.0, 0.0),  (0.0, 1.0, 0.0),  (0.0, 0.0,
            1.0)`The default value for the translation vector is`(0.0, 0.0, 0.0)`The default values
            position the sketch on the *X–Y* plane centered at the origin.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    @typing.overload
    def __init__(self, name: str, objectToCopy: "ConstrainedSketch"):
        """This method copies one ConstrainedSketch object to a new ConstrainedSketch object. Note:
        If the name of the sketch to be copied to is __edit__, Abaqus creates an exact copy that
        contains both reference geometry and a non-identity transform matrix. Otherwise, the
        Sketch copy constructor strips the reference geometry from the copied sketch and sets
        the transform matrix to identity, creating a standalone copy.

        Notes
        -----
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ConstrainedSketch

        Parameters
        ----------
        name
            A String specifying the repository key.
        objectToCopy
            A ConstrainedSketch object to be copied.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def __init__(self, *args, **kwargs):
        pass

    def ConstrainedSketchFromGeometryFile(self, name: str, geometryFile: AcisFile):
        """This method creates a ConstrainedSketch object and places it in the sketches repository.

        Notes
        -----
            This function can be accessed by:

            .. code-block:: python

                mdb.models[name].ConstrainedSketchFromGeometryFile

        Parameters
        ----------
        name
            A String specifying the repository key.
        geometryFile
            An AcisFile object specifying a file containing geometry. The geometry in the file is
            converted to two-dimensional sketch geometry in the *X–Y* plane.

        Returns
        -------
        sketch: ConstrainedSketch
            A ConstrainedSketch object
        """
        pass

    def print(self):
        """This method prints the following statistics about a sketch:
        - The sketch Id (a positive integer).
        - The number of geometry curves (the number of ConstrainedSketchGeometry objects).
        - The number of dimensions (the number of ConstrainedSketchDimension objects).
        - The number of vertices (the number of ConstrainedSketchVertex objects).
        """
        pass

    def assignCenterline(self, line: ConstrainedSketchGeometry):
        """This method indicates the construction line that will be used as a centerline for
        revolved features.

        Parameters
        ----------
        line
            A ConstrainedSketchGeometry object specifying a construction line that indicates the
            centerline of revolved features.
        """
        pass

    def assignCenterOfTwist(self, point: ConstrainedSketchVertex):
        """This method indicates the isolated point that will be used as the center of twist when
        an extruded feature is created with twist.

        Parameters
        ----------
        point
            A ConstrainedSketchVertex object specifying an isolated point that indicates the center
            of twist for extruded features that use a twist angle.
        """
        pass

    def autoDimension(self, objectList: tuple):
        """This method applies dimensions to the selected ConstrainedSketchGeometry objects in an
        effort to make the ConstrainedSketch well defined.

        Parameters
        ----------
        objectList
            A sequence specifying the ConstrainedSketchGeometry objects to dimension.
        """
        pass

    def autoTrimCurve(self, curve1: str, point1: tuple[float], parameter1: float):
        """This method automatically trims a selected ConstrainedSketchGeometry object at the
        specified location. If the object does not intersect other ConstrainedSketchGeometry
        objects, the entire selected object will be deleted.

        Parameters
        ----------
        curve1
            The ConstrainedSketchGeometry object to be trimmed.
        point1
            A pair of Floats specifying the location on ConstrainedSketchGeometry where the trimming
            should be applied. *point1* and *parameter1* are mutually exclusive.
        parameter1
            A Float specifying the parameter location on the ConstrainedSketchGeometry where the
            trimming should be applied. *point1* and *parameter1* are mutually exclusive.
        """
        pass

    def breakCurve(
        self,
        curve1: ConstrainedSketchGeometry,
        point1: tuple[float],
        curve2: ConstrainedSketchGeometry,
        point2: tuple[float],
    ):
        """This method breaks a specified ConstrainedSketchGeometry object (*curve1*) using another
        specified ConstrainedSketchGeometry object (*curve2*). If the selected
        ConstrainedSketchGeometry objects intersect, then only *curve1* will be broken; *curve2*
        is not affected by the operation. The location for the break is determined by the
        specified point values.

        Parameters
        ----------
        curve1
            A ConstrainedSketchGeometry object specifying the object to be broken.
        point1
            A pair of Floats specifying the location on *curve1* near where the break should be
            applied.
        curve2
            A ConstrainedSketchGeometry object specifying where *curve1* should be broken.
        point2
            A pair of Floats specifying the location on *curve2* near where *curve1* should be
            broken.
        """
        pass

    def copyMirror(
        self,
        mirrorLine: ConstrainedSketchGeometry,
        objectList: tuple[ConstrainedSketchGeometry],
    ):
        """This method creates copies of the given ConstrainedSketchGeometry objects, mirrors them
        about a selected line, and inserts them into the appropriate repositories of the
        ConstrainedSketch object.

        Parameters
        ----------
        mirrorLine
            A ConstrainedSketchGeometry object specifying the line about which Abaqus will mirror
            the sketch.
        objectList
            A sequence of ConstrainedSketchGeometry objects specifying the sketch to be copied and
            mirrored.
        """
        pass

    def copyMove(self, vector: tuple, objectList: tuple[ConstrainedSketchGeometry]):
        """This method creates copies of the given ConstrainedSketchGeometry objects, moves them
        from their original position, and inserts them into the appropriate repositories of the
        ConstrainedSketch object.

        Parameters
        ----------
        vector
            A sequence of two Floats specifying the translation vector.
        objectList
            A sequence of ConstrainedSketchGeometry objects to be copied and moved.
        """
        pass

    def copyRotate(
        self,
        centerPoint: tuple[float],
        angle: float,
        objectList: tuple[ConstrainedSketchGeometry],
    ):
        """This method creates copies of the given ConstrainedSketchGeometry objects, rotates them,
        and inserts them into the appropriate repositories of the ConstrainedSketch object.

        Parameters
        ----------
        centerPoint
            A pair of Floats specifying the center of rotation.
        angle
            A Float specifying the angle of rotation in degrees.
        objectList
            A sequence of ConstrainedSketchGeometry objects to be copied and moved.
        """
        pass

    def copyScale(
        self,
        scaleValue: float,
        scaleCenter: tuple[float],
        objectList: tuple[ConstrainedSketchGeometry],
    ):
        """This method creates copies of the given ConstrainedSketchGeometry objects, scales them
        by the specified value about a selected point, and inserts them into the appropriate
        repositories of the ConstrainedSketch object.

        Parameters
        ----------
        scaleValue
            A Float specifying the value for scaling.
        scaleCenter
            A pair of Floats specifying the center of scaling.
        objectList
            A sequence of ConstrainedSketchGeometry objects to be copied and scaled.
        """
        pass

    def delete(self, objectList: tuple):
        """This method deletes the given ConstrainedSketchGeometry, ConstrainedSketchDimension, or
        ConstrainedSketchConstraint objects.

        Parameters
        ----------
        objectList
            A sequence of ConstrainedSketchGeometry, ConstrainedSketchDimension, or
            ConstrainedSketchConstraint objects to be deleted.
        """
        pass

    def deleteParameter(self, name: str):
        """The command deletes a specified parameter.

        Parameters
        ----------
        name
            A String specifying the name of the parameter to delete.
        """
        pass

    def dragEntity(self, entity: str, points: tuple):
        """This method drags a specified ConstrainedSketchGeometry or ConstrainedSketchVertex
        object to a specific location.

        Parameters
        ----------
        entity
            A ConstrainedSketchGeometry or ConstrainedSketchVertex object specifying the object to
            drag.
        points
            A sequence of sequences of three Floats specifying a sequence of points along which to
            drag the entity. The order of points in the sequence defines a path that determines the
            solution.
        """
        pass

    def linearPattern(
        self,
        number1: int,
        spacing1: float,
        angle1: float,
        vertexList: tuple[ConstrainedSketchVertex] = (),
        geomList: tuple[ConstrainedSketchGeometry] = (),
        number2: str = 1,
        spacing2: float = None,
        angle2: float = None,
    ):
        """This method copies ConstrainedSketchGeometry objects in a linear pattern along one or
        two directions. This method also copies any associated dimension or constraint objects
        that exist between the given objects.

        Parameters
        ----------
        number1
            An Integer specifying the total number of copies, including the original objects, that
            appear along the first direction in the pattern. Possible values are 1 ≤≤ *number1* ≤≤
            1000.
        spacing1
            A Float specifying the spacing between copies along the first direction in the pattern.
            Possible values are 0.0 ≤≤ *spacing1* .
        angle1
            A Float specifying the angle in degrees of the first direction in the pattern. Possible
            values are –360.0 ≤≤ *angle1* ≤≤ 360.0.
        vertexList
            A sequence of ConstrainedSketchVertex objects to copy.
        geomList
            A sequence of ConstrainedSketchGeometry objects to copy.
        number2
            An integer specifying the total number of copies, including the original objects, that
            appear along the second direction in the pattern. Possible values are 1 ≤≤ *number2* ≤≤
            1000. The default value is 1. The value of either *number1* or *number2* must be greater
            than one.
        spacing2
            A Float specifying the spacing between copies along the first direction in the pattern.
            Possible values are 0.0 ≤≤ *spacing2*. The default value is *spacing1*.
        angle2
            A Float specifying the angle in degrees of the first direction in the pattern. Possible
            values are –360.0 ≤≤ *angle2* ≤≤ 360.0. The default value is 90° beyond the value of
            *angle1*.

        Returns
        -------
            None.

        Raises
        ------
            - AbaqusException
              Number must be greater than 1 for at least one direction
            !img
        """
        pass

    def mergeVertices(self, value: float, vertexList: tuple[ConstrainedSketchVertex]):
        """This method merges the ConstrainedSketchVertex objects that lie within the specified
        distance of each other. If only one ConstrainedSketchVertex object is selected, it will
        merge all ConstrainedSketchVertex objects that lie within the specified distance of that
        vertex. If more than one vertex is selected, the search will be restricted to only the
        selected ConstrainedSketchVertex objects.

        Parameters
        ----------
        value
            A Float specifying the search radius.
        vertexList
            A sequence of ConstrainedSketchVertex objects to be merged.
        """
        pass

    def move(self, vector: tuple, objectList: tuple[ConstrainedSketchGeometry]):
        """This method translates the given ConstrainedSketchGeometry objects by the given vector.

        Parameters
        ----------
        vector
            A sequence of two Floats specifying the translation vector.
        objectList
            A sequence of ConstrainedSketchGeometry objects specifying the objects to be translated.
        """
        pass

    def offset(
        self,
        distance: float,
        objectList: tuple[ConstrainedSketchGeometry],
        side: SymbolicConstant,
        filletCorners: Boolean = OFF,
    ):
        """This method creates copies of the selected ConstrainedSketchGeometry objects, offsets
        them by the specified distance in the specified direction, and inserts them into the
        ConstrainedSketch object's appropriate repositories. If connected objects are selected,
        trim or extend is carried out to complete the offset.

        Parameters
        ----------
        distance
            A Float specifying the distance to be offset.
        objectList
            A sequence of ConstrainedSketchGeometry objects to be copied and offset.
        side
            A SymbolicConstant specifying which side the offset should occur. Possible values are
            LEFT and RIGHT.
        filletCorners
            A Boolean specifying whether the corners need to be rounded instead of being extended.
        """
        pass

    def radialPattern(
        self,
        number: int,
        totalAngle: float,
        centerPoint: tuple[float],
        vertexList: tuple[ConstrainedSketchVertex] = (),
        geomList: tuple[ConstrainedSketchGeometry] = (),
    ):
        """This method copies ConstrainedSketchGeometry objects in a radial pattern about a
        specified center point.

        Parameters
        ----------
        number
            An Int specifying the total number of copies, including the original objects, that
            appear in the radial pattern. Possible values are 2 ≤≤ *number2* ≤≤ 1000.
        totalAngle
            A Float specifying the total angle in degrees between the first and last instance in the
            pattern. A positive angle corresponds to a counter-clockwise direction. The values 360°
            and -360° represent a special case where the pattern makes a full circle. In this case,
            because the copy would overlay the original, the copy is not placed at the last
            position. Possible values are –360.0 ≤≤ *totalAngle* ≤≤ 360.0.
        centerPoint
            A pair of Floats specifying the center of the radial pattern.
        vertexList
            A sequence of ConstrainedSketchVertex objects to copy.
        geomList
            A sequence of ConstrainedSketchGeometry objects to copy.
        """
        pass

    def resetView(self):
        """This method resets the view to be perpendicular to the sketching plane."""
        pass

    def rectangle(self, point1: tuple[float,float], point2: tuple[float,float]):
        """This method creates four lines that form a rectangle with diagonal corners defined by
        the given points and inserts them into the geometry repository of the ConstrainedSketch
        object.

        Parameters
        ----------
        point1
            A pair of Floats specifying the first corner of the rectangle.
        point2
            A pair of Floats specifying the second corner of the rectangle.

        Returns
        -------
        success: int
            An Int specifying the success or failure of the method. A value of 0 indicates failure
        """
        pass

    def removeGapsAndOverlaps(
        self, tolerance: str, geomList: tuple[ConstrainedSketchGeometry]
    ):
        """This method removes gaps and overlaps between sketch geometries specified by the user.
        This method is particularly useful when cleaning up imported sketches

        Parameters
        ----------
        tolerance
            A float value which specifies the largest size of the gap or overlap between entities
            that is to be removed. Typically this value is small and is used to close gaps and
            overlaps which may not exist in the originating program but exist in the sketch because
            of mismatched tolerances between the two programs.
        geomList
            A sequence of ConstrainedSketchGeometry objects where the gaps and overlaps are to be
            removed.
        """
        pass

    def repairShortEdges(
        self, geomList: tuple[ConstrainedSketchGeometry], tolerance: str = ""
    ):
        """This method deletes the short edges specified, optionally selecting only those short
        edges whose lengths are smaller than the specified tolerance and healing the resultant
        gap in the sketch. This method is particularly useful in conjunction with
        removeGapsAndOverlap when cleaning up imported sketches.

        Parameters
        ----------
        geomList
            A sequence of ConstrainedSketchGeometry objects where the short edges are to be removed.
        tolerance
            A float value that is used to select and delete only those edges specified in *geomList*
            whose lengths are smaller than the given value. The default value is –1.0. This value
            implies that all edges specified in *geomList* will be removed and the sketch healed to
            remove gaps left by their removal.
        """
        pass

    def retrieveSketch(self, sketch: "ConstrainedSketch"):
        """This method copies all ConstrainedSketchGeometry, ConstrainedSketchDimension,
        ConstrainedSketchConstraint, and ConstrainedSketchParameter objects from the specified
        ConstrainedSketch object. The new objects are added to the existing objects (if any).
        The objects in the specified ConstrainedSketch object are not modified by the retrieve
        operation.

        Parameters
        ----------
        sketch
            A ConstrainedSketch object specifying the object from which to copy.
        """
        pass

    def rotate(self, centerPoint: tuple[float], angle: float, objectList: tuple):
        """This method rotates the given ConstrainedSketchGeometry objects by the given angle and
        about the given point.

        Parameters
        ----------
        centerPoint
            A pair of Floats specifying the center of rotation.
        angle
            A Float specifying the angle of rotation in degrees.
        objectList
            A sequence of ConstrainedSketchGeometry specifying the objects to be rotated.
        """
        pass

    def scale(
        self,
        scaleValue: float,
        scaleCenter: tuple[float],
        objectList: tuple[ConstrainedSketchGeometry],
    ):
        """This method scales the given ConstrainedSketchGeometry objects by the given scale factor
        and about the given point.

        Parameters
        ----------
        scaleValue
            A Float specifying the value of scale.
        scaleCenter
            A pair of Floats specifying the center of scale.
        objectList
            A sequence of ConstrainedSketchGeometry objects specifying the objects to be scaled.
        """
        pass

    def setPrimaryObject(self, option: SymbolicConstant):
        """This method makes the ConstrainedSketch object the primary object in the current
        viewport. The sketch remains the primary object in the current viewport until an
        unsetPrimaryobject command is issued.

        Parameters
        ----------
        option
            A SymbolicConstant specifying how the sketch is displayed. Possible values
            are:STANDALONE: Indicates a new stand-alone sketch. The current viewport is cleared and
            is replaced by the stand-alone sketch. The view direction is set to −ZZ.SUPERIMPOSE:
            Indicates that the sketch is superimposed on the current viewport. The view direction is
            changed to be perpendicular to the sketch plane. The change is effected smoothly as an
            animated sequence of many small viewing steps.
        """
        pass

    def trimExtendCurve(
        self, curve1: str, point1: tuple[float], curve2: str, point2: tuple[float]
    ):
        """This method trims or extends a specified ConstrainedSketchGeometry object (*curve1*)
        using another specified ConstrainedSketchGeometry object (*curve2*). *curve2* is not
        affected by the operation. The location for the trim or extend is determined by the
        specified point values.

        Parameters
        ----------
        curve1
            The ConstrainedSketchGeometry object specifying the object to be trimmed or extended.
        point1
            A pair of Floats specifying the location on *curve1* where trim or extend should be
            applied.
        curve2
            The ConstrainedSketchGeometry object specifying the object to which *curve1* is trimmed
            or extended. *curve2* is not trimmed or extended.
        point2
            A pair of Floats specifying the location on *curve2* near where *curve1* should be
            trimmed or extended.
        """
        pass

    def undo(self):
        """This method undoes the effects of the last ConstrainedSketch object method."""
        pass

    def unsetPrimaryObject(self):
        """This method removes the ConstrainedSketch object from the current viewport, reversing
        the effects of the setPrimaryobject command. If the *option* argument was set to
        SUPERIMPOSE, the viewport will be returned to the view orientation that was in place
        when the setPrimaryobject command was issued. If the *option* argument was set to
        STANDALONE, the viewport will be left empty.
        """
        pass

    def writeAcisFile(self, fileName: str, version: float = None):
        """This method exports the geometry of the sketch to a named file in ACIS format.

        Parameters
        ----------
        fileName
            A String specifying the file name.
        version
            A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS
            Version 12.0. The default value is the current version of ACIS.
        """
        pass

    def writeIgesFile(self, filename: str, flavor: SymbolicConstant = None):
        """This method exports the geometry of the sketch to a named file in IGES format.

        Parameters
        ----------
        filename
            A String specifying the file name.
        flavor
            A SymbolicConstant specifying a particular flavor of IGES to export. Possible values
            areSTANDARD, AUTOCAD, SOLIDWORKS, JAMA, and MSBO.
        """
        pass
