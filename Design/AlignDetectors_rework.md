Motivation
==========
With the NOMAD instrument there is a consistent issue with figuring out which instrument geometry a given calibration file
was created with. Since the offsets are relative, using the wrong geometry makes the calibration (potentially) useless. In
addition, the instrument team has determined that adding additional TOF dependant calibration parameters (`DIFA` and `TZERO`)
yield better focused data. This design will address both of these issues.

Select Additional Requirements
==============================
1. The information needs to be stored in a file that can be read/written quickly and with accuracy. There is a performance issue with SNAP which has 18x256x256 pixels.
2. The parameters need to be somewhat flexible since the specific calibration parameters used change over time.
3. Which instrument (e.g. name and date) the parameters are valid for is useful for diagnosing/debugging purposes.

Proposed Solution
=================

Algorithms
----------
* Create a AlignDetectors v2 ([v1](http://docs.mantidproject.org/nightly/algorithms/AlignDetectors-v1.html)) which no longer reads in the calibration file, and takes in a new workspace with the (extensible) calibration information.
* Update [AlignAndFocusPowder](http://docs.mantidproject.org/nightly/algorithms/AlignAndFocusPowder-v1.html) to use the new calibration information.
* Create read/write algorithms for the calibration information.
* (later) Update [GetDetOffsetsMultiPeaks](http://docs.mantidproject.org/nightly/algorithms/GetDetOffsetsMultiPeaks-v1.html) to determine additional parameters.

Calibration workspace
---------------------
The calibration will be stored in memory as a [TableWorkspace](http://docs.mantidproject.org/nightly/api/python/mantid/api/ITableWorkspace.html). The columns will be labeled, in order, `detid` (int32), `difc` (double), `difa` (double), and `tzero` (double). The order of the rows and columns will not matter to algorithms that use the workspace. Algorithms that create the TableWorkspace will use this column order with the rows sorted by `detid` (smallest first). Any missing column, other than `detid`, will be assumed to be all zeros.

Calibration file
----------------
The data will be stored using HDF5 using as simple a format as possible to allow for external programs to read/write them without excessive effort. Missing values will be assumed to be zero. The data will be stored as multiple parallel 1-dimensional arrays `difc` (double), `difa` (double), `tzero` (double), `detid` (int32), and `group` (int32, with 1 being smallest number, 0 will set to not use). In addition there will be sufficient information to denote which instrument geometry file to use. This geometry will only be used for plotting the various parameters on an instrument view.
