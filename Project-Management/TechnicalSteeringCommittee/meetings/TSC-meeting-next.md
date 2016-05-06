Agenda
======

Pinned Topics
-------------
* Review any outstanding external pull request or issues? (Owen)
* Any updates to [tracking design table](https://github.com/mantidproject/documents/blob/master/Project-Management/TechnicalSteeringCommittee/reports/TSC-TrackingDesignProposals.md)? (Fede)

New Items
---------
* [Histogram Design](https://github.com/mantidproject/documents/pull/14) (Simon)
* [Absorption Corrections](https://github.com/mantidproject/documents/pull/15) (Martyn)
* Distributing optional Python packages, e.g `LoadCIF` & `PyCifRW` (Martyn) 
* [Py-Qt-MVC](https://github.com/morefigs/Py-Qt-MVC) (Owen)
* Discussion questions:
  1.  Do we move our 1D/2D plotting to use matplotlib directly?
  2.  Do we drop our fitting for scipy’s?
  3.  Do we move TableWorkspace to be a pandas DataFrame [[1](http://stackoverflow.com/questions/21647054/creating-a-pandas-dataframe-with-a-numpy-array-containing-multiple-types)]?
  4.  Do we change Workspace2D (or lower) to use XArray?
  5.  Do we migrate our current underlying geometry to [CombLayer](https://github.com/SAnsell/CombLayer), openCascade[[2](https://blog.kitware.com/designing-nuclear-reactor-core-geometry-and-meshes/), [3](http://dev.opencascade.org/index.php?q=node/1090), [4](http://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__vis.html)] VTK?
