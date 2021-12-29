# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2021 replay file
# Internal Version: 2020_03_06-22.50.37 167380
# Run by Hailin on Wed Dec 29 13:49:45 2021
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.16602, 1.16667), width=171.637, 
    height=115.733)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
#: Executing "onCaeStartup()" in the site directory ...
execfile('C:/Users/user/OneDrive/Documents/GitHub/PyAbaqusBase/test-dst.py', 
    __main__.__dict__)
#: Executing "onCaeStartup()" in the site directory ...
#: The interaction property "IntProp-1" has been created.
#: The interaction "Int-1" has been created.
#: Warning: Field output is not requested in the following steps:
#: INITIAL-STRESS
#: 
#: History output is not requested in the following steps:
#: INITIAL-STRESS
#* IOError: C:/Users/Hailin/OneDrive/Documents/GitHub/PyAbaqusBase/tests/dst: 
#* Directory not found
#* File "C:/Users/user/OneDrive/Documents/GitHub/PyAbaqusBase/test-dst.py", 
#* line 168, in <module>
#*     
#* mdb.saveAs('C:\\Users\\Hailin\\OneDrive\\Documents\\GitHub\\PyAbaqusBase\\tests\\dst\\dst.cae')
