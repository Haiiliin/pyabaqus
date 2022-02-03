from abaqusConstants import *


class Face:
    """Faces are two-dimensional regions of geometry.

    Attributes
    ----------
    index: int
        An Int specifying the index of the face in the FaceArray.
    isReferenceRep: Boolean
        A Boolean specifying whether the face belongs to the reference representation of the
        Part or Instance.
    pointOn: float
        A tuple of tuples of Floats specifying the coordinates. For a face of a shell **pointOn**
        specifies the **X**-, **Y**-, and **Z**-coordinates of a point located on the face and the
        **X**-, **Y**-, and **Z**-components of the normal to the face.For a face of a solid **pointOn**
        specifies the **X**-, **Y**-, and **Z**-coordinates of a point located on the face.
    featureName: float
        A tuple of Floats specifying the name of the feature that created this face.
    instanceName: float
        A tuple of Floats specifying the name of the part instance for this face (if
        applicable).

    Notes
    -----
        This object can be accessed by:
        - import part
        - mdb.models[name].parts[name].allInternalSets[name].faces[i]
        - mdb.models[name].parts[name].allInternalSurfaces[name].faces[i]
        - mdb.models[name].parts[name].allSets[name].faces[i]
        - mdb.models[name].parts[name].allSurfaces[name].faces[i]
        - mdb.models[name].parts[name].faces[i]
        - mdb.models[name].parts[name].sets[name].faces[i]
        - mdb.models[name].parts[name].surfaces[name].faces[i]
        - import assembly
        - mdb.models[name].rootAssembly.allInstances[name].faces[i]
        - mdb.models[name].rootAssembly.allInstances[name].sets[name].faces[i]
        - mdb.models[name].rootAssembly.allInstances[name].surfaces[name].faces[i]
        - mdb.models[name].rootAssembly.allInternalSets[name].faces[i]
        - mdb.models[name].rootAssembly.allInternalSurfaces[name].faces[i]
        - mdb.models[name].rootAssembly.allSets[name].faces[i]
        - mdb.models[name].rootAssembly.allSurfaces[name].faces[i]
        - mdb.models[name].rootAssembly.instances[name].faces[i]
        - mdb.models[name].rootAssembly.instances[name].sets[name].faces[i]
        - mdb.models[name].rootAssembly.instances[name].surfaces[name].faces[i]
        - mdb.models[name].rootAssembly.modelInstances[i].sets[name].faces[i]
        - mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].faces[i]
        - mdb.models[name].rootAssembly.sets[name].faces[i]
        - mdb.models[name].rootAssembly.surfaces[name].faces[i]

    """

    # An Int specifying the index of the face in the FaceArray. 
    index: int = None

    # A Boolean specifying whether the face belongs to the reference representation of the 
    # Part or Instance. 
    isReferenceRep: Boolean = OFF

    # A tuple of tuples of Floats specifying the coordinates. For a face of a shell *pointOn* 
    # specifies the *X*-, *Y*-, and *Z*-coordinates of a point located on the face and the 
    # *X*-, *Y*-, and *Z*-components of the normal to the face.For a face of a solid *pointOn* 
    # specifies the *X*-, *Y*-, and *Z*-coordinates of a point located on the face. 
    pointOn: float = None

    # A tuple of Floats specifying the name of the feature that created this face. 
    featureName: float = None

    # A tuple of Floats specifying the name of the part instance for this face (if 
    # applicable). 
    instanceName: float = None

    def getCentroid(self):
        """This method returns the centroid of a face.

        Returns
        -------
            A sequence of Floats specifying the *X*-, *Y*-, and *Z*-coordinates of the centroid of 
            the face. . 
            !img 
        """
        pass

    def getCurvature(self, point: tuple, uParam: float, vParam: float):
        """This method returns information about the curvature at a location on the face.
        
        Parameters
        ----------
        point
            A tuple specifying the *X*-, *Y*-, and *Z* coordinates of the point where the curvature 
            is desired. If the *point* does not lie on the face it will be projected onto the face. 
            This argument and *uParam* and *vParam* are mutually exclusive. 
        uParam
            A Float specifying the normalized *U* parameter value at which the curvature is to be 
            computed. This value must lie between (0,1). *vParam* must also be specified. This 
            argument is mutually exclusive with *point*. 
        vParam
            A Float specifying the normalized *V* parameter value at which the curvature is to be 
            computed. This value must lie between (0,1). 

        Returns
        -------
            A dictionary with keys 'evaluationPoint', 'principalAxis1', 'principalAxis2', 
            'curvature1', 'curvature2' and 'gaussianCurvature'. Where the evaluationPoint specifies 
            the location at which the curvature was evaluated. 'principalAxis1' and 'principalAxis2' 
            refer to the vectors specifying the two principal axes of the face. 'curvature1' and 
            'curvature2' specify the curvatures along the two principal axes. . 
            !img 
        """
        pass

    def getElements(self):
        """This method returns an array of element objects that are associated with the face.

        Returns
        -------
            A MeshElementArray object which is a sequence of MeshElement objects. . 
            !img 
        """
        pass

    def getElementFaces(self, faceSide: SymbolicConstant = BOTH_SIDES):
        """This method returns an array of mesh face objects. Each mesh face object contains the
        element label and the side of the element that lies on the geometric face.
        
        Parameters
        ----------
        faceSide
            A symbolic constant specifying the side of the geometric face of a solid from which the 
            element faces should be retrieved. Possible values are *SIDE1*, *SIDE2*, and 
            *BOTH_SIDES*. The default value is *BOTH_SIDES*. For shell faces this option is ignored. 

        Returns
        -------
            A MeshFaceArray object which is a sequence of MeshFace objects. . 
            !img 
        """
        pass

    def getNodes(self, faceSide: SymbolicConstant = BOTH_SIDES):
        """This method returns an array of mesh node objects. Each mesh node object contains the
        label of the node that lies on the geometric face.
        
        Parameters
        ----------
        faceSide
            A symbolic constant specifying the side of the geometric face of a solid from which the 
            nodes should be retrieved. Possible values are xo*SIDE1*, *SIDE2*, and *BOTH_SIDES*. The 
            default value is *BOTH_SIDES*. For shell faces and for faces with compatible meshes on 
            either sides this option is ignored. Otherwise, the nodes on the specified side(s) of 
            the face are output. 

        Returns
        -------
            A MeshNodeArray object which is a sequence of MeshNode objects. . 
            !img 
        """
        pass

    def getNormal(self, point: tuple = ()):
        """This method returns the normal to a face at the location specified by the *pointOn*
        member. The normal at a different location on the face can be obtained by specifying the
        optional *point* argument.
        
        Parameters
        ----------
        point
            A tuple specifying the *X*-, *Y*-, and *Z* coordinates of the point where the normal to 
            the face is desired. If the *point* does not lie on the face it will be projected onto 
            the face. 

        Returns
        -------
            A sequence of Floats specifying the *X*-, *Y*-, and *Z*-components of the normal to the 
            face. 

        Raises
        ------
            An exception is raised if the optional argument *point* is provided but the point cannot 
            be projected onto the face. 
            !img 
        """
        pass

    def getSize(self, printResults: str = True):
        """This method returns a Float indicating the area of the face.
        
        Parameters
        ----------
        printResults
            A Bool specifying whether verbose output is printed. The default value is True. 

        Returns
        -------
            A Float. . 
            !img 
        """
        pass

    def getEdges(self):
        """This method returns a sequence consisting of the edge ids of the edges on the face.

        Returns
        -------
            A tuple of integers. . 
            !img 
        """
        pass

    def getVertices(self):
        """This method returns a sequence consisting of the vertex ids of the vertices of the face.

        Returns
        -------
            A tuple of integers. . 
            !img 
        """
        pass

    def getCells(self):
        """This method returns a sequence consisting of the cell ids of the cells to which this
        face belongs.

        Returns
        -------
            A tuple of integers. . 
            !img 
        """
        pass

    def getAdjacentFaces(self):
        """This method returns an array of face objects that share at least one edge of the face.

        Returns
        -------
            A FaceArray object which is a sequence of Face objects. . 
            !img 
        """
        pass

    def getFacesByFaceAngle(self, angle: str):
        """This method returns an array of Face objects that are obtained by recursively finding
        adjacent faces that are at an angle of less than or equal to the specified angle.
        
        Parameters
        ----------
        angle
            A float specifying the value of the face angle. 

        Returns
        -------
            A FaceArray object, which is a sequence of Face objects. . 
            !img 
        """
        pass

    def getFacesByCurvature(self):
        """This method returns an array of Face objects that are obtained by recursively finding
        adjacent faces that share the same curvature.

        Returns
        -------
            A FaceArray object, which is a sequence of Face objects. . 
            !img 
        """
        pass

    def isNormalFlipped(self):
        """This method determines whether the normal to the face is flipped from its default
        direction by the use of the flipNormal method on a Part object.

        Returns
        -------
            A Boolean value of True if the normal is flipped and False if not. . 
            !img 
        """
        pass

    def getCADAttributes(self):
        """This method returns an array of CAD attribute strings associated with the Face when the
        part was created from CAD data.

        Returns
        -------
            An array of String . 
            !img 
        """
        pass
