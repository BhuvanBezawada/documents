# Multidimensional Plotting Tasks for Release 3.5

This documents aims to keep track of the required tasks which need to be addressed for the current release (3.5).

This will allow us to have an overview of the status quo and how to channel our efforts. Please add your issues to this document and change priorities if needed. Also if you think that we won't resolve something for this release, then add/move it to the [Resolve later](#resolve-later) section.


## Priority High 

#### GIL compatibility with ParaView for LaTeX style labels
Resolve Python issue with LaTeX in VSI

#### Implement a 2D text filter for Peaks in Splatterplot
Utkarsh has provided us with a demo for displaying 2D text on a 3D rendered environment. This needs to be integrated with the PeaksViewer in Splatterplot mode (Anton has the demo code).

#### Check if items of the Kitware contract have been implemented
Go through the list of deliverables and check if they have been implemented (see contract)

#### Cut then Scale issue
Currently we can scale and then cut, but there is an issue if we reverse the order. See [here.](https://github.com/mantidproject/mantid/issues/12368)

#### Artifacts when changing size
When we change the size of the VSI the rendered view does not update. A similar effect happens when we use the PeaksTable in the Splatterplot mode. The issue is caused by applying the old state xml file when switching views.

#### Slice position
It was discussed that we should have an input field to define the slice position for the ThreeSliceView.

#### Zero Memory copies
Investigate zero memory copies

#### Axes and labels improvement
This will most likely be an umbrella ticket. Some issues are:

* Provide TeX-like features
* In Threeslice Mode provide a sensible text size (Note that this will need a newer version of PV.)

#### CutMD in VSI can come back with zero data in it
See [here](https://github.com/mantidproject/mantid/issues/12554)



## Priority Medium

#### PipelineBrowser + PropertiesWidget mock ups
Create mock ups for a possible replacement of the pipeline browser and the properties widget


## Priority Low

#### Multiple Windows/Instances
Provide multiple VSI instances. See [here](https://github.com/mantidproject/mantid/issues/12395).


## Resolved

* [GIL compatibility with ParaView for LaTeX style labels](#GIL-compatibility-with-ParaView-for-LaTeX-style-labels)


## Resolve later
