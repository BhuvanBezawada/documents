# ----------------------------------------------------------------------------------------------------
#  Python Training Exercise 1 Solution using the new syntax style
#  Removing the HRPD prompt pulse
#  Changes:
# 		- Uses new parameter names. All parameters now have a consistent naming style. 
#		- Numbers, lists can be used directly without conversion to strings
#------------------------------------------------------

# The input data set
inputData = "HRP39182"
# The path to the data (this may have to be change based upon your setup
path = "C:/Mantid/Test/Data/"
# Load the file
LoadRaw(Filename=path+inputData+".RAW",OutputWorkspace=inputData,Cache="If Slow")

# First do the analysis without prompt pulse removal so that we can compare the difference
# Align the detectors (incoporates unit conversion to d-Spacing)
cal_file = "hrpd_new_072_01.cal"
AlignDetectors(InputWorkspace=inputData,OutputWorkspace="aligned-withpulse",CalibrationFile=path + cal_file)
# Focus the data
DiffractionFocussing(InputWorkspace="aligned-withpulse",OutputWorkspace="focussed-withpulse",GroupingFileName=path+cal_file)

# Plot a spectrum. As each pulse is removed below, the graph will update
plotSpectrum(inputData,0)

# Remove the prompt pulse, which occurs at at 20,000 microsecond intervals. The bin width comes from a quick look at the data
for i in range(0,5):
  min = 19990 + (i*20000)
  max = 20040 + (i*20000)
  MaskBins(InputWorkspace=inputData,OutputWorkspace=inputData,XMin=min,XMax=max)

# Align the detectors (on the data with the pulse removed incoporates unit conversion to d-Spacing)
AlignDetectors(InputWorkspace=inputData,OutputWorkspace="aligned-withoutpulse",CalibrationFile=path + cal_file)
# Focus the data
DiffractionFocussing(InputWorkspace="aligned-withoutpulse",OutputWorkspace="focussed-withoutpulse",GroupingFileName=path + cal_file)

# Now plot a focussed spectrum with and without prompt peak removal so that you can see the difference
mergePlots(plotSpectrum("focussed-withoutpulse",0),plotSpectrum("focussed-withpulse",0))
