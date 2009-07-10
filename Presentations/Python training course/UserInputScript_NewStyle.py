# --------------------------------------------------------------------------------------------------------------------------------------
#  Python Training Exercise 2 Solution with syntax style
# A generalized script
#  Changes:
# 		- Uses new parameter names. All parameters now have a consistent naming style. 
#		- Numbers, lists can be used directly without conversion to strings
#              - Dialog functions have new arguments, enable and disable which can be
#                use to explicity enable or disable a control when the dialog is raised
#-----------------------------------------------------------------------------------------------------------------------------------------

# Load the monitor spectrum, asking the  user for file
loadalg = LoadRawDialog(OutputWorkspace="Monitor",SpectrumMin=2,SpectrumMax=2,message="Enter the raw file you want to process", disable="SpectrumList")

# Retrieve the file that was loaded
file = loadalg.getPropertyValue("Filename")
# Load the main data bank (same file)
LoadRaw(Filename=file,OutputWorkspace="Small_Angle",SpectrumMin=130, SpectrumMax=16130)

# Remove the prompt pulse from the monitor
RemoveBins(InputWorkspace="Monitor",OutputWorkspace="Monitor",XMin=19900,XMax=20500,Interpolation='Linear')

# Correct monitor for a flat background
FlatBackground(InputWorkspace="Monitor",OutputWorkspace="Monitor",SpectrumIndexList=0,StartX=31000,EndX=39000)

# Convert monitor to wavelength
ConvertUnits(InputWorkspace="Monitor",OutputWorkspace="Monitor",Target="Wavelength")

# Rebin with a suggested set of parameters
# The list of parameters [2.2,-0.035,10] can also be given as a '2.2,-0.035,10'
rebinalg = RebinDialog(InputWorkspace="Monitor",OutputWorkspace="Monitor",Params=[2.2,-0.035,10],message="Enter the binning you want to use, in wavelength", enable="Params")
rebinparam = rebinalg.getPropertyValue("params")

# Convert data to wavelength
ConvertUnits(InputWorkspace="Small_Angle",OutputWorkspace="Small_Angle",Target="Wavelength")

# Rebin the small angle workspace with the same parameters as the previous Rebin
Rebin(InputWorkspace="Small_Angle",OutputWorkspace="Small_Angle",Params=rebinparam)

# Finally, correct for incident beam monitor
Divide(LHSWorkspace="Small_Angle", RHSWorkspace="Monitor",OutputWorkspace="Corrected data")
