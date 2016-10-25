## Test Scenarios for Workspace Dock Widget 
![Dock1](ScenariosScreenshots/MantidDock.png)
Concepts:
 - [Workspace](http://docs.mantidproject.org/nightly/concepts/Workspace.html)
 - [Algorithm](http://docs.mantidproject.org/nightly/concepts/Algorithm.html)
 
<link href="ScenariosScreenshots/style.css" type="text/css" rel="stylesheet" />
 
1. **Load button in Workspace Dock**
 * **s1** - Load button used to launch load dialog, user selects valid data file and hits Run. Workspace loaded into the displayed workspace list (DWL) and the workspace name is added to the workspace dock. <img src="ScenariosScreenshots/Load1-1.png" width="300"/> ![Load1-2](ScenariosScreenshots/Load1-2.png)
 * **s2** - Load button used to launch load dialog, user selects multiple files from the file open dialog and clicks the Run button. A group workspace is created called MultipleFiles which contains the selected workspaces. ![Load2-1](ScenariosScreenshots/Load2-1.png) ![Load2-2](ScenariosScreenshots/Load2-2.png) ![Load2-3](ScenariosScreenshots/Load2-3.png)
 * **s3** - Load button used to launch load dialog, user cancels load (Close). No interaction with DWL or workspace dock.
 * **s4** - Load button used to launch load dialog, workspace is not set by user. User selects Run. User presented with a dialog which states that one or more invalid properties (filename) have been set.
 * **s5** - User runs Load algorithm outside of workspace dock with valid data file. Workspace loaded into DWL and the workspace name is added to the workspace dock. ![Load5-1](ScenariosScreenshots/Load5-1.png) ![Load5-2](ScenariosScreenshots/Load5-2.png) ![Load5-3](ScenariosScreenshots/Load5-3.png)
2. **Group Button**
 * **s6** - User selects multiple workspaces within the workspace dock and clicks the Group button.  A group workspace called NewGroup is created which contains the selected workspaces. The workspaces are no longer displayed independently of the group. ![Group1-1](ScenariosScreenshots/Group1-1.png) ![Group1-2](ScenariosScreenshots/Group1-2.png) ![Group1-3](ScenariosScreenshots/Group1-3.png)
 * **s7** - User selects a workspace group within the workspace dock and clicks the UnGroup button. The workspace group is removed and the individual constituent workspaces are listed in the workspace dock. ![Group2-1](ScenariosScreenshots/Group2-1.png) ![Group2-2](ScenariosScreenshots/Group2-2.png)
 * **s8** - User selects a group workspace and a free workspace within the workspace dock and clicks the Group button. A group workspace called NewGroup is created which contains all of the workspaces in the previous group and the free workspace. There are no subgroups. Just one new group. ![Group3-1](ScenariosScreenshots/Group3-1.png) ![Group3-2](ScenariosScreenshots/Group3-2.png) ![Group3-3](ScenariosScreenshots/Group3-3.png)
3. **Sort Button**
 * **s9** - User clicks the Sort button, then selects ascending from drop-down menu with name selected. The workspaces in the dock are sorted by name ascending. ![Sort1-1](ScenariosScreenshots/Sort1-1.png) ![Sort1-2](ScenariosScreenshots/Sort1-2.png)
 * **s10** - User clicks the Sort button, then selects descending from drop-down menu with name selected. The workspaces in the dock are sorted by name descending. ![Sort2-1](ScenariosScreenshots/Sort2-1.png) ![Sort2-2](ScenariosScreenshots/Sort2-2.png)
 * **s11** - User clicks the Sort button, then selects ascending from drop-down menu with last modified selected. The workspaces in the dock are sorted by last modified ascending.
 * **s12** - User clicks the Sort button, then selects descending from drop-down menu with last modified selected. The workspaces in the dock are sorted by last modified descending.
4. **Delete Button in Workspace Dock**
 * **s13** - User selects works valid workspace in workspace dock and clicks the delete button. The user is presented with a Yes/No confirmation dialog. User selects Yes. Workspace is removed from workspace dock. ![Delete1-1](ScenariosScreenshots/Delete1-1.png) ![Delete1-2](ScenariosScreenshots/Delete1-2.png)
 * **s14** - User selects works valid workspace in workspace dock and clicks the delete button. The user is presented with a Yes/No confirmation dialog. User selects No. Selected workspace is not deleted from the dock. ![Delete2-1](ScenariosScreenshots/Delete2-1.png) ![Delete2-2](ScenariosScreenshots/Delete2-2.png)
 * **s15** - User selects multiple workspaces in workspace dock and clicks the delete button. The user is presented with a Yes/No confirmation dialog. User selects Yes. All selected workspaces are removed from the workspace dock. ![Delete3-1](ScenariosScreenshots/Delete3-1.png) ![Delete3-2](ScenariosScreenshots/Delete3-2.png)
 * **s16** - User selects a workspace which is a member of a workspace group and clicks the delete button. The user is presented with a Yes/No confirmation dialog. User selects Yes. The selected workspace is deleted from the group. The group remains but with one less workspace. ![Delete4-1](ScenariosScreenshots/Delete4-1.png) ![Delete4-2](ScenariosScreenshots/Delete4-2.png)
 * **s17** - User selects the workspace in a workspace group which only contains one workspace and clicks the delete button. The user is presented with a Yes/No confirmation dialog. User selects Yes. The selected workspace and the parent group are removed from the workspace dock. ![Delete5-1](ScenariosScreenshots/Delete5-1.png) ![Delete5-2](ScenariosScreenshots/Delete5-2.png)
 * **s18** - User selects a workspace from the workspace tree and an additional workspace which exists within a workspace group and clicks the Delete button. The user is presented with a Yes/No confirmation dialog. User selects Yes. The selected workspace names are removed from the workspace dock. ![Delete6-1](ScenariosScreenshots/Delete6-1.png) ![Delete6-2](ScenariosScreenshots/Delete6-2.png)
5. **Save Button**
 * **s19** - With a single workspace selected, the user clicks the save button. A dropdown list appears which allows the user to select an output file type. User selects an output file type and a save file dialog is launched.
 * **s20** - With multiple workspaces selected, the user clicks the save button. A save file dialog is immediately launched.
6. **Load button for Live Data**
 * **s21** - User clicks Load Button and a dropdown list appears with the options File and Live Data. User selects Live Data and the Start Live dialog is launched.
7. **Other Actions**
 * **s22** - User right clicks workspace/group in workspace dock and selects Rename. A rename dialog is launched which prompts for the new workspace name. User enters a valid workspace name. The workspace name is updated in the DWL and the workspace dock. ![Other1-1](ScenariosScreenshots/Other1-1.png) ![Other1-2](ScenariosScreenshots/Other1-2.png) ![Other1-3](ScenariosScreenshots/Other1-3.png)
 * **s23** - User right clicks workspace/group in workspace dock and selects Rename. A Yes/No confirmation dialog is launched. The user selects Yes. The workspace is removed from the workspace dock and DWL. ![Other2-1](ScenariosScreenshots/Other2-1.png) ![Other2-2](ScenariosScreenshots/Other2-2.png) ![Other2-3](ScenariosScreenshots/Other2-3.png)
 
