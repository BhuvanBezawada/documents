
# Scope

The scope of this work has been summarised already [[1]] :
> Keeping Horace interface would allow smooth transfer experience for all current Horace users and easy comparison of new and old well verified results, so it is suggested to keep Horace interface with only minor reasonable modifications. 

**This design document is to keep an incremental, running design on new phases of a mantid-horace syntax. It is NOT intended to detail (at time of writing) the complete set of mantid-horace commands, although that is the eventual aim.**

This document is intended to finally pull together contributions from several authors into a workable design document. Where possible the source of the syntax
will be referenced. The primary sources for this document have been:

* [Detailed Horace notes][1]
* [Horace][2]
* [Horace notes for Mantid implementation][3]
* [Horace style Plotting][4]

[2]: http://horace.isis.rl.ac.uk
[3]: https://github.com/mantidproject/documents/blob/master/Design/VATES/MantidHorace/horace-notes.md
[1]: https://github.com/mantidproject/documents/blob/master/Design/VATES/MantidHorace/horace-notes-horace-methods.docx
[4]: https://github.com/mantidproject/documents/blob/master/Design/VATES/MantidHorace/plot-commands.doc

# Contributors

These are people who have provided groundwork for the proposed syntax.

| Contributor        | Facility           |
| ------------- |:-------------:|
| Andrei Savici | SNS      |
| Stuart Campbell | SNS      |
| Alex Buts     | ISIS     |
| Owen Arnold     | ISIS |
| Toby Perring     | ISIS |
| Russell Ewings     | ISIS |
| Nick Draper | ISIS |

# Terminology

Mantid has it's own analogues to Horace objects. Mantid *MDHistoWorkspaces* are equivalent to Horace *DND* objects. Mantid *MDEventWorkspaces* are equivalent to Horace *SQW* objects. One major difference highlighted [[1]] is that a *SQW* object is a *DND* object, where as *MDHistoWorkspaces* and *MDEventWorkspaces* are fundamentally different types. The do share some properties, and where the type of the Mantid n-d workspace is of no importance; we refer to them in a generic way as *MDWorkspaces*.

# Syntax

The following commands will form part of the python CLI (command line interface). The majority of the work is targeted for Mantid python algorithms, but there will need to be modifications made to support the Horace style projections to other areas of Mantid.

## CutMD

This is know as **cut_sqw** in Horace [[2]], but has been named **CutMD** since this fits better with Mantid, where *sqw* is not the generally used term for n-dimensional datasets. **CutMD** will be implemented as a python algorithm. It will have an alias of **cut_md**.


### Arguments and Function Signature

***cut = CutMD (data_source, proj, (p1_bin, p2_bin, p3_bin,
p4_bin), nopix, out_filename)***

* The returned object *cut* will be a Mantid *IMDWorkspace*. This will be either a *MDEventWorkspace* or an *MDHistoWorkspace* depending upon the *nopix* option
* *data_source* could be either an MDEventWorkspace, or iterable collection of workspaces, or, file, or iterative collection of files of type *.sqw, or *.nxs. Consideration could be given to allowing a mix of such input types in the same collection
* The *proj* object will be a slightly modified Mantid TableWorkspace. More detail below. [[3]]
* *out_filename* is optional. If provided then the results will be saved to
this location. [[3]]
* *p1_bin* will be provided as per the Horace syntax [[2]]. However, to allow for n-dimensions, they will be grouped as a tuple (see example)
syntax. These can either be a single value step, or an integration
range. The function will accept these either as a python tuple or list
    * **CutMD now supports the horace syntax for bins, however it's passed to the `PBins` parameter, not `p1_bin`.**
    * See the [trac ticket](http://trac.mantidproject.org/mantid/ticket/11353) and [pull request](https://github.com/mantidproject/mantid/pull/396)
* To keep consistency with Horace, *nopix* option OFF by default [[3]]
* cutMD() should be a public member function of and MDEventWorkspace so that the dimensionality can be automatically determined in addition to the functional implementation above.


#### Internal Step 1. Generate the Projections

We need a new algorithm to generate projections **GenerateSQWProj** [[1]], [[3]]

* Output should be a Mantid TableWorkspace
* We can generate a *Projection* from an algorithm, something like **proj=GenerateSQWProj(arguments)**. If no arguments given, we will use sensible defaults. [[1]], [[3]]
* A data type for a *Projection* could be added to Mantid and exposed to python, but we would not yet consider adding this as a type of property
* Any *Projection* type should be convertible to and from an ITableWorkspace
* The python bindings will allow Horace syntax like proj.u= “1,1,1” [[3]]
* A further addition will be to add proj.w, the third projection axis, since we can do non-orthogonal axes. If not given *proj.w* is calculated as the cross product of *proj.u* and *proj.v* [[3]] 

#### Internal Step 2. Performing the cut

* This will be a wrapper around Mantid **BinMD/SliceMD** algorithms. The *nopix* option would be used to specify the output type *MDHistoWorkspace*, or* MDEventWorkspace* [[1]], [[3]]
* Projections must be full formed either as a Projection type or Projection TableWorkspace (see above), this will avoid an explosion of arguments for **CutMD**
* Inputs should either be full-formed to represent the reciprocal lattice
* We could later add options to complete the transform to HKL if the UB and goniometer information is present
* Andrei will provide transformations to go from reciprocal lattice units to inverse Angstroms. These will be dictated by the projection.
* If projections are not axis aligned, we must prevent the SCD normalisation routines from processing them (at time of writing)

#### Examples
These examples have been generated from examples given for Horace [[1]]

```python

proj.u=[1,1,0]; proj.v=[-1,1,0]; proj.uoffset=[0,0,0]; proj.type='rrr'

proj_table = proj.toWorkspace()


my_vol = cut_md(my_ws, proj_table, ([0,0.1,8], [2,0.05,6], [-2,-1], [0,10,1000]), nopix=True, out_filename='cut.nxs')# Makes a Q,Q,E volume plot

```

## CreateMD

This is known as **gen_sqw** in Horace [[2]], but has been named **CreateMD** since this fits better with Mantid. **CreateMD** will be implemented as a python algorithm. It will have an alias **create_sqw** to fit with the existing lower case Horace scripting.

As highlighted by Toby/Alex, it is important to have a file-backed mode for this operation [[1]]

### Arguments and Function signature

***out_ws = CreateMD ([data_source, ws_name], efix, emode, alatt, angdeg, u, v, psi,
omega, dpsi, gl, gs, out_filename)***

* *out_ws* is the combined MDWorkspace, for file-based workspaces
* *out_filename* is optional. If provided then the results will be saved to
this location, and the processing will be conducted on disk rather than in-memory
* *data_source* could be a number of things. *data_source* can either be a file or a workspace (*.nxspe, *.nxs) *ws_name* is optional [[1]]
* *alatt*, *angdeg*, *u*, *v* are used to set the UB matrix. One can set the UB 
matrix before. If not empty, it will override and set the UB again [[3]]
* *omega*, *dpsi*, *gl*, *gs* are angles for goniometer settings. This should be
in principle set on the input workspaces beforehand. If omega is set, it
should override the individual goniometer settings for each individual
workspace. Dpsi, gl, and gs are additional goniometer rotations. [[3]]

**If omega is not set, do we use
dpsi, gl, and gs?**

#### Internal Steps

* For each set of inputs, Mantid algorithms **SetUB** and **SetGoniometer** may be called if inputs are provided in the script. Same holds for setting *efix*
* Internally, this Mantid algorithm will use **ConvertToMD** to perform the operations on individual sets of inputs
* Results can be merged using either **MergeMD** or **MergeMDFiles** [[1]]
* Individual workspaces will not be deleted and will be named as specified by the *ws_name* [[1]]

#### Examples

These examples have been generated from examples given for Horace [[1]]

```python
input_files = ['data1.nxs', 'data2.nxs', 'data3.nxs' ]

efix = [400, 500, 600] # set incident energy

emode = 'Direct'

alatt=[3,4,5] # Lattice parameters (Angstroms)

angdeg=[120,90,90] # lattice angles (degrees)

u=[1,0,0]; v=[0,1,0] # specify scattering plane, where u is the crystal direction to ki when psi=0, v is another vector so that with u it specifies the equatorial plane

omega=0; dpsi=0; gl=0; gs=0 # goniometer offsets for the sample (usually all zero)

ws = CreateMD (input_files, efix, emode, alatt, angdeg, u, v, psi, omega, dpsi, gl, gs)

```

## SmoothMD

This function takes the same name in Horace[[2]] [Smooth](http://horace.isis.rl.ac.uk/Reshaping_etc#smooth). The Mantid Algorithm should be exactly the same. Like Horace, this operation will only work on DND objects (MDHistoWorkspaces).

#### Examples
```Python

mdhw = CreateMDHistoWorkspace(SignalInput=range(0,16), ErrorInput=[0]*16, Dimensionality=2, Extents='0,1,0,1', NumberOfBins=[4,4], Names='A,B', Units='U,U',)

# Specify all width elements
width_vector = [3, 1] # Specify width per axis
smoothed=SmoothMD(mdhw,[width_vector])

# Single width element
width_vector = [3] # Same for all axes
smoothed=SmoothMD(mdhw,[width_vector])

# Overriding the default smooth_function (which is Hat)
width_vector = [3] # Same for all axes
smooth_function = 'Gaussian'
smoothed=SmoothMD(InputWorkspace=mdhw, WidthVector=width_vector, SmoothFunction=smooth_function)

```

## CompactMD

This function takes the same name in Horace [Compact](http://horace.isis.rl.ac.uk/Reshaping_etc#compact). To achieve the same functionality as Compact, CompactMD should crop an MDHistoWorkspace based on the first non-zero signals found in each dimension.

#### Arguments and Function signature

***OutputWorkspace = ReplicateMD(InputWorkspace)***

* *InputWorkspace* must be an IMDHistoWorkspace.

#### Examples

```python

# Create a 4 by 4 workspace with signal values:
# 0  0  0  0
# 0  1  0  0
# 0  0  1  0
# 0  0  0  0
mdhw = CreateMDHistoWorkspace(SignalInput=[0]*16, ErrorInput=[0]*16, Dimensionality=2, Extents='0,1,0,1', NumberOfBins=[4,4], Names='A,B', Units='U,U',)
mdhw.setSignalAt(6, 1.0)
mdhw.setSignalAt(9, 1.0)

# Use CompactMD algorithm
compacted_mdhw = CompactMD(mdhw)

# Resultant workspace is 2 by 2 with values:
# 1  0 
# 0  1 

```

## ReplicateMD

This function also takes the same name as in Horace [Replicate](http://horace.isis.rl.ac.uk/Reshaping_etc#replicate). ReplicateMD should increase the dimensionality of an MDWorkspace by replicating it along a particular dimension.

#### Arguments and Function signature

***OutputWorkspace = ReplicateMD(ShapeWorkspace, DataWorkspace)***

* *ShapeWorkspace* is an MDWorkspace with the shape of the output workspace.
* *DataWorkspace* is the MDWorkspace to replicate.

#### Examples

```python

# Create workspace to replicate
mdhw_data = CreateMDHistoWorkspace(SignalInput=range(0,16), ErrorInput=[0]*16, Dimensionality=2, Extents='0,1,0,1', NumberOfBins=[4,4], Names='A,B', Units='U,U',)

# Create workspace with desired shape of output workspace
mdhw_shape = CreateMDHistoWorkspace(SignalInput=[0]*48, ErrorInput=[0]*48, Dimensionality=3, Extents='0,1,0,1,0,1', NumberOfBins=[4,4,3], Names='A,B,C', Units='U,U,U',)

outWs = ReplicateMD(mdhw_shape, mdhw_data)

```

## TransposeMD

The TransposeMD algorithm corresponds to Horace's [Permute](http://horace.isis.rl.ac.uk/Reshaping_etc#permute) function. TransposeMD will also have the alias PermuteMD. Inputs of TransposeMD should be equivalent to those of Permute but note that axes are zero indexed in Mantid.

#### Arguments and Function signature

***OutputWorkspace = ReplicateMD(InputWorkspace, Axes)***

* *InputWorkspace* must be an IMDHistoWorkspace.
* *Axes* list of axes indices, zero indexed.

#### Examples

```python

# Create an MDHistoWorkspace
mdhw = CreateMDHistoWorkspace(SignalInput=range(0, 48), ErrorInput=[0]*48, Dimensionality=3, Extents='0,1,0,1,0,1', NumberOfBins=[4,4,3], Names='A,B,C', Units='U,U,U',)

# Swap the first and last axes of the MDWorkspace, note that they are zero indexed.
mdhwOut = TransposeMD(mdhw, [2, 1, 0])

```

## AccumulateMD

This function takes the same name in Horace [Accumulate](http://horace.isis.rl.ac.uk/Generating_SQW_files#accumulate_sqw), and will append new data to an existing MDWorkspace.

#### Arguments and Function signature

***OutputWorkspace = AccumulateMD(DataSources, InputWorkspace, EFix, Emode, Alatt, Angdeg, u, v, Psi, Gl, Gs, Clean)***

* *OutputWorkspace* is a MDWorkspace containing the data of the InputWorkspace and new data from DataSources appended.
* *DataSources* can be a list of files or of workspaces (*.nxspe, *.nxs).
* *EFix* is a list of datasource energy values in meV
* *Emode* is 'Elastic', 'Direct' or 'Indirect'
* *InputWorkspace* is the MDWorkspace to append data to.
* *Alatt*, *Angdeg*, *u*, *v* are used to set the UB matrix.
* *Psi*, *Gl*, *Gs* are angles for goniometer settings.
* *Clean* is a boolean value, if true a fresh MDWorkspace is created, optional and default is false.


#### Examples

```python

# Not all of these files need to exist yet
input_files = ['data1.nxs', 'data2.nxs', 'data3.nxs' , 'data4.nxs' , 'data5.nxs' ]

psi=[0:2:180 1:2:179]  # list of anticipated scan angles

efix=100  # incident energy

emode = 'Direct'

alatt=[5.7,5.7,5.7]  # lattice parameters

angdeg=[90,90,90]  # lattice angles

u=[1,0,0]; v=[0,1,0]  # specify scattering plane, where u is the crystal direction to ki when psi=0, v is another vector so that with u it specifies the equatorial plane

omega=0; dpsi=0; gl=0; gs=0  # goniometer offsets for the sample

# Any new data in input_files is appended to workspace ws
ws = AccumulateMD(input_files, ws, efix, emode, alatt, angdeg, u, v, psi, omega, dpsi, gl, gs)

# OR use "Clean=True" to recreate the workspace from fresh
ws = AccumulateMD(input_files, ws, efix, emode, alatt, angdeg, u, v, psi, omega, dpsi, gl, gs, Clean=True)

```
