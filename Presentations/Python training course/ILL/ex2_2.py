#
# Generalizing the Script
#

load_alg = LoadILLDialog(Disable='FilenameVanadium,WorkspaceVanadium',OutputWorkspace='data')

filename = load_alg.getProperty('Filename').value
logger.information("Filename is: " + filename)

Integration(InputWorkspace='data', OutputWorkspace='mon', EndWorkspaceIndex=0)

Divide(LHSWorkspace='data', RHSWorkspace='mon', OutputWorkspace='data_norm')

ConvertUnits(InputWorkspace='data',OutputWorkspace='data_DeltaE',Target='DeltaE',EMode='Direct')

rebin_alg = RebinDialog(Message="Rebin the monitors by providing rebin parameters", InputWorkspace='data_DeltaE', OutputWorkspace='data_E_Rebin',
	Params='-50,0.1,3',  Enable='Params')
			    
params = rebin_alg.getProperty('Params').value
logger.information("Rebinning params: " + str(params)

