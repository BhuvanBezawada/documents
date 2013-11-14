#Here we aim to write a small algorithm that performs a reduction and conversion to energy transfer of some raw data. This is essentially a snippet of the proper reduction done for the direct-geometry inelastic instruments.
#
# Write an algorithm called <code>ConvertToEnergy</code>
# The algorithm should have 4 properties:
#  - Filename: A FileProperty for a file to load (ignore extensions )
#  - Ei: A FloatProperty for the incident energy with a validator to check that it is positive and non-zero
#  - BinParams: A FloatArrayProperty that will contain the binning of the final workspace
#  - OutputWorkspace: An output MatrixWorkspaceProperty to hold the final result.
#
#
# The steps the algorithm should perform are:
#  - Use the Load algorithm to load the file to a workspace
#  - Run the ConvertUnits algorithm on the previous workspace and put the output in the same workspace. Use Target='DeltaE', EMode=Direct, EFixed=value of Ei property
#  - Run the Rebin algorithm on the previous workspace and put the output in the same workspace. Use Params=value of the BinParams property
#  - Create a new workspace that is the sum of all of the spectra in the output from Rebin (Hint: Use the WorkspaceFactory and create a workspace that uses the existing one a template but with one row).
#  - Set the X values on the new worksapace to the X values from first row of the existing workspace
#  - Loop over the existing workspace and sum up the values and put them in the new workspace.  
#  - Delete the temporary workspace using DeleteWorkspace
#  - Set the new workspace to the <code>OutputWorkspace</code> property
#
# To test the algorithm, execute the file that contains the algorithm to register it with Mantid. It will then show up in the list of algorithms. Use the following inputs:
#  - Filename: MAR11001.raw
#  - Ei: 12.9729
#  - BinParams: -11,0.01,11
#  - OutputWorkspace: DeltaE

from mantid.kernel import *
from mantid.api import *

import numpy as np
 
# Class definition
class ConvertToEnergy(PythonAlgorithm):
 
    def PyInit(self):
        # 3 input properties
        self.declareProperty(FileProperty(name="Filename", defaultValue="",action=FileAction.Load),doc="TOF data filename")
        # Setting the default to -1 requires a user to enter a value as it does not satisfy the validator
        self.declareProperty(name="Ei", defaultValue=-1.0, validator=FloatBoundedValidator(lower=0.0001), doc="Incident energy of neutron")
        self.declareProperty(FloatArrayProperty(name="BinParams"), doc="Bin parameters for the final workspace in units of DeltaE")

        # 1 Output property
        self.declareProperty(MatrixWorkspaceProperty(name="OutputWorkspace", defaultValue="", direction=Direction.Output))

    def PyExec(self):
        from mantid.simpleapi import Load, ConvertUnits, Rebin, DeleteWorkspace
        
        # Load file to workspace
        __tmpws = Load(Filename=self.getPropertyValue("Filename"))
        
        # Convert to units to DeltaE
        ei = self.getProperty("Ei").value
        __tmpws = ConvertUnits(InputWorkspace=__tmpws,Target="DeltaE",EMode="Direct",EFixed=ei)
        
        # Rebin to requested units
        bins = self.getProperty("BinParams").value
        __tmpws = Rebin(InputWorkspace=__tmpws,Params=bins)
        
        # Create the new output workspace
        summed = WorkspaceFactory.create(__tmpws,NVectors=1)
        # Set the X values for the new workspace
        summed.setX(0, __tmpws.readX(0))

        # Sum the rows to a single row. Two methods demonstrated:

        #----- 1: Direct workspace access -----
        # Uses less memory as it avoids a copy of the data

        # readY returns read only array. dataY returns an array we can modify on the new workspace
        sumy = summed.dataY(0)
        for i in range(__tmpws.getNumberHistograms()):
            sumy += __tmpws.readY(i)

        #----- 2: Extract to numpy and sum ----
        # Uses more memory as extract copies to data (uncomment to see working)
        #yin = __tmpsws.extractY()
        #npsum = numpy.sum(yin,axis=0) # Axis 0 = summing down the columns
        # and put the data to the workspace
        #summed.setY(0, npsum)

        DeleteWorkspace(__tmpws)
        self.setProperty("OutputWorkspace", summed)

# Register algorithm with Mantid
AlgorithmFactory.subscribe(ConvertToEnergy)


