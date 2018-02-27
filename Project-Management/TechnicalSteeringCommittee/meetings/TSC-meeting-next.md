Agenda
======

Pinned Topics
-------------
* Review any outstanding external pull request or issues? (Lamar)
* Any updates to [tracking design table](https://github.com/mantidproject/documents/blob/master/Project-Management/TechnicalSteeringCommittee/reports/TSC-TrackingDesignProposals.md)?

New Items
---------
* PyCifRW is now required. Should this be optional?
* Adding [sphinxcontrib-bibtex](https://sphinxcontrib-bibtex.readthedocs.io) to the list of dependencies
* Nexus reference frame vs IDFs. Do we do anything about this? (Lamar)
* Major [changes](https://github.com/mantidproject/mantid/pull/21881) to Instrument View code imminent. (Lamar)
* Set the minimum C++ std version to 14 by end of maintenance? (Martyn)
* [An issue with distributions and dimensionless units](https://github.com/mantidproject/documents/blob/fix-divide-distribution/Design/DistributionsAndDimensionlessData.md) and [Multiplication and division rules for histograms](https://github.com/mantidproject/documents/pull/25)
* Should we use GTest? See https://github.com/mantidproject/mantid/pull/21671.


Minutes
-------

Attendance: Moore, Gigg, Whitfield, Savici, Hahn, Vardanyan

* PyCifRW should be a hard dependency (Gigg)
  * Add to developer package
  * Fail at unit test level if not present

