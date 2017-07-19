Summary
=======

This document describes the design of the new matplotlib-based workbench that will replace MantidPlot.

Workflow
========

The new workbench will be developed on a long-running feature branch within the main [`mantid`][mantidrepo] repository. The exception to this is the new directory
structure described below for the graphical components. These changes will be made on the `master` branch prior to any work starting on the workbench. This
will minimize the effect of merge conflicts on existing components that are going to be reused.

The advantage here is that we can remove the existing MantidPlot on this branch and reuse the name for the new workbench.


Directory Structure
===================

The following diagram indicates the proposed directory structure for the graphical components.

```
mantid.git
   |-- Framework
   |-- qt
   |   |-- applications
   |   |   |-- mantidplot
   |   |       |-- setup.py
   |   |-- algorithm_dialogs
   |   |-- paraview
   |   |-- scientific_interfaces
   |   |   |-- CMakeLists.txt
   |   |   |-- Diffraction
   |   |   |   |-- PowderDiffractionReduction
   |   |   |   |   |-- Powder_Diffraction_Reduction.py
   |   |   |   |   |-- Powder_Diffraction_Reduction
   |   |   |   |   |   |-- ...
   |   |   |-- Indirect
   |   |   |   |-- Common
   |   |   |   |-- Corrections
   |   |   |   |-- DataAnalysis
   |   |   |-- Muon
   |   |   |   |-- ALC
   |   |   |   |-- DataAnalysis
   |   |   |-- Reflectometry
   |   |   |   |-- ISISReflectometry
   |   |   |   |   |-- ISIS_Reflectometry.py
   |   |   |   |   |-- ISIS_Reflectometry
   |   |   |   |   |   |-- ...
   |   |-- mantidqt # will become the mantidqt python module
   |   |   |-- setup.py
   |   |   |-- pyplot
   |   |   |-- widgets
   |   |   |   |-- common
   |   |   |   |-- reduction_gui # Python reduction gui framework
   |   |   |   |-- instrumentviewer
   |   |   |   |-- spectrumviewer
   |   |   |   |-- sliceviewer
```

Technologies
============

The workbench will be written primarily in Python using:

 - [PyQt5][PyQt5]
 - [matplotlib][matplotlib_org]
 - [IPython][IPython]

`sip` will be used for exporting any required C/C++ to Python.

Python 2/3
----------

Due to the requirement to support RedHat 7 we will continue to write Python 2/3 compatible
code.

PyQt shim
----------

An abstraction layer around `PyQt4`, `PyQt5`, `PySide` will be used to wrap all calls to PyQt functionality. This should reduce
portability concerns in the future when its inevitable that a PyQt6 will come out. The shim should provide a similar layer
of protection as it currently does between `PyQt4` & `PyQt5`.

We could either write our own, use those provided by other dependencies: [matplotlib][matplotlib_qtcompat], [IPython][IPython] or
use a separate package such as [qtpy][qtpy] provided by the [Spyder][Spyder] developers.

Packaging & Deployment
======================

Python
------

The framework package will remain separate and called `mantid`.

The new ui package will be called `mantidui` and have the following submodules:

 - mantidui.plotting: contain custom plotting code based on matplotlib, i.e keep/make current behaviour, custom toolbars, custom figure window
 - mantidui.widgets: contain these set of reusable widgets used to build the workbench & its components

The workbench will be called `mantidplot` and depend on `mantudui` & `mantid`.

Installation
------------

It is proposed that a new package be generated for shipping the new workbench. The reasons for this are:

* it avoids disturbing the production package at all to provide maximal stability for existing users
* Qt5/PyQt5 will need to be shipped on Windows/OSX and this would explode the current package size if we bundled it there
* we may want to experiment with different versions of packages that we already ship and we don't want to disturb the current application
* it can be a starting point for generating the separate packages on Linux (hand-written spec/debian files??).

For Windows/Mac we will use the same installer technology as we do currently. The packages **must** be able to live alongside a current production or nightly version. The package names suggested are:

* Windows/OSX: mantidpreview - A combined package bundling everthing, much as we currently do. Defaults to a different install location than current
* Linux: mantidpreview-framework, mantidpreview-ui, mantidpreview-mantidplot: separate packages to allow just dependencies on widgets etc.


<!-- Link Definitions -->

[mantidrepo]: https://www.github.com/mantidproject/mantid
[matplotlib_org]: https://matplotlib.org/
[matplotlib_qtcompat]: https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/backends/qt_compat.py
[PyQt5]:https://riverbankcomputing.com/software/pyqt/download5
[IPython]: https://ipython.org/
[qtpy]: https://pypi.python.org/pypi/QtPy
[Spyder]: https://github.com/spyder-ide/spyder
[Nsis]: http://nsis.sourceforge.net/Main_Page
[QtInstallerFramework]: http://doc.qt.io/qtinstallerframework/
