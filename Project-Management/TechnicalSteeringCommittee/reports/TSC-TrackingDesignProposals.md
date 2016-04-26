# Requirements and design documents discussed at TSC meetings


## Requirements documents
| Name | date | Status|
| :------------ |:---------------|:-------|
| [Geometry 2.0](https://github.com/mantidproject/documents/blob/master/Design/Instrument-2.0/requirements-v2.md) | [2016-01-22](https://github.com/mantidproject/documents/blob/master/Project-Management/TechnicalSteeringCommittee/meetings/2016/TSC-meeting-2016-01-22.md) | First draft approved in Mantid annual meetings 2016 |


## Design proposals

For design document guidelines see [here]( http://www.mantidproject.org/Design_Document_Guidelines).

Designs currently being proposed/reviewed via [design document pull requests](https://github.com/mantidproject/documents/pulls).

| Name  | date | Status |
| :------------ |:---------------|:-------|
| [Generic Shape Absorption Corrections](https://github.com/mantidproject/documents/pull/15) | [2016-04-26](/Project-Management/TechnicalSteeringCommittee/meetings/2016/TSC-meeting-2016-04-26.md) | Approved. |
| [Histogram type](https://github.com/mantidproject/documents/pull/14) | 2016-04-12 | TBD. |
| [Spectrum Number and Workspace Index Abstraction Design](https://github.com/mantidproject/documents/pull/13) | [2016-03-29](/Project-Management/TechnicalSteeringCommittee/meetings/2016/TSC-meeting-2016-03-29.md) | Approved. |
| [Live listener customisation](https://github.com/mantidproject/documents/pull/7) | [2016-03-29](/Project-Management/TechnicalSteeringCommittee/meetings/2016/TSC-meeting-2016-03-29.md) | Assign to a developer from PSI. |
| [Data Processing User Interface](/Design/DataProcessorAlgorithmUI/DataProcessingUserInterface.md) | [2015-12-09](/Project-Management/TechnicalSteeringCommittee/meetings/2015/TSC-meeting-2015-12-09.md) | In progress. [14732](https://github.com/mantidproject/mantid/issues/14732), [14921](https://github.com/mantidproject/mantid/issues/14921)  |
| [MD Image Format](/Design/Imaging_IMAT/Workspace_type_for_stacks_of_images.md) | [2015-10-28](/Project-Management/TechnicalSteeringCommittee/meetings/2015/TSC-meeting-2015-10-28.md). | In progress.  [15437](https://github.com/mantidproject/mantid/issues/15437), [14165](https://github.com/mantidproject/mantid/issues/14165), [15418](https://github.com/mantidproject/mantid/issues/15418), [15419](https://github.com/mantidproject/mantid/issues/15419).|
| [Workflow Caching Design](/Design/WorkflowCaching.md) | [2015-09-30](/Project-Management/TechnicalSteeringCommittee/meetings/2015/TSC-meeting-2015-09-30.md) | In progress. ~~[14716](https://github.com/mantidproject/mantid/issues/14716)~~ ~~[14717](https://github.com/mantidproject/mantid/issues/14717)~~. **Next tickets?** |
| [AlignDetectors Redesign](/Design/AlignDetectors_rework.md) | [2015-06-09](/Project-Management/TechnicalSteeringCommittee/meetings/2015/TSC-meeting-2015-06-09.md) | In progress: ~~[844](https://github.com/mantidproject/mantid/pull/844)~~, ~~[12794](https://github.com/mantidproject/mantid/pull/12794)~~, [14676](https://github.com/mantidproject/mantid/issues/14676) |
| [pythonAlgorithmsForMDEvents](/Design/pythonAlgorithmsForMDEvents.rst)     | [2015-04-21](/Project-Management/TechnicalSteeringCommittee/meetings/2015/TSC-meeting-2015-04-21.md)  | **Under reconsideration**. |
| [automatic differentiation](/Design/IntegratingAdept.md) | [2014-11-11](/Project-Management/TechnicalSteeringCommittee/meetings/2014/TSC-meeting-2014-11-11.md) | In progress, "almost there". [10624](https://github.com/mantidproject/mantid/issues/10624) |

Designs from 2015 that were approved and implemented:

| Name  | date | Status |
| :------------ |:---------------|:-------|
| [Algorithm Usage Statistics](/Design/Usage/AlgorithmUsageStatistics.md) | [2015-12-09](/Project-Management/TechnicalSteeringCommittee/meetings/2015/TSC-meeting-2015-12-09.md) | Done.  ~~[12041](https://github.com/mantidproject/mantid/issues/12041)~~.|
| [IMDDimensionUpdate](/Design/VATES/IMDDimensionUpdate.md)     | [2015-06-23](/Project-Management/TechnicalSteeringCommittee/meetings/2015/TSC-meeting-2015-06-23.md) | Done. ~~[12185](https://github.com/mantidproject/mantid/issues/12185)~~ |
| [IDFLoadOrder](/Design/IDFLoadOrder.md) | [2015-06-09](/Project-Management/TechnicalSteeringCommittee/meetings/2015/TSC-meeting-2015-06-09.md) | Done. ~~[12656](https://github.com/mantidproject/mantid/issues/12656)~~ |
| [PocoStringTokenizer](/Design/PocoStringTokenizer.md)  | [2015-02-17](/Project-Management/TechnicalSteeringCommittee/meetings/2015/TSC-meeting-2015-02-17.md)  | Done. ~~[11815](https://github.com/mantidproject/mantid/issues/11815)~~, ~~[PR15366](https://github.com/mantidproject/mantid/pull/15366)~~ |

Designs from 2014 that were approved and implemented:

| Name  | date | Status |
| :------------ |:---------------|:-------|
| [determining usage statistics](/Design/MeasureUsageStatistics.md) |[2014-11-11](/Project-Management/TechnicalSteeringCommittee/meetings/2014/TSC-meeting-2014-11-11.md) | done. ~~[11401](https://github.com/mantidproject/mantid/issues/11401)~~ |
| [New plotting CLI](/Design/Plotting/plotting_cli.md) | [2014-09-02](/Project-Management/TechnicalSteeringCommittee/meetings/2014/TSC-meeting-2014-09-02.md) | done. ~~[9780](https://github.com/mantidproject/mantid/issues/9780)~~, ~~[11395](https://github.com/mantidproject/mantid/issues/11395)~~, ~~[12380](https://github.com/mantidproject/mantid/issues/12380)~~ |
| [EmbeddedInstrumentInfoNexus](/Design/EmbeddedInstrumentInfoNexus.md)     | [2014-08-27](/Project-Management/TechnicalSteeringCommittee/meetings/2014/TSC-meeting-2014-08-27.md) | done. ~~[12255](https://github.com/mantidproject/mantid/issues/12255)~~ |
| [Monitors in Live Data](/Design/MonitorsInLiveData.md) | [2014-05-21](/Project-Management/TechnicalSteeringCommittee/meetings/2014/TSC-meeting-2014-05-21.md) | done. ~~[10384](https://github.com/mantidproject/mantid/issues/10384)~~, ~~[10383](https://github.com/mantidproject/mantid/issues/10383)~~ |
| [Instrument downloading proposal](/Design/InstrumentFetching.md) | [2014-04-22](/Project-Management/TechnicalSteeringCommittee/meetings/2014/TSC-meeting-2014-04-22.md) | done. ~~[9767](https://github.com/mantidproject/mantid/issues/9767)~~, ~~[10489](http://trac.mantidproject.org/mantid/ticket/10489)~~ |
| [Workspace history proposal](/Design/Nested%20History%20Detailed%20Design%20Document.docx) | [2014-04-11](/Project-Management/TechnicalSteeringCommittee/meetings/2014/TSC-meeting-2014-04-11.md) | done. ~~[9756](https://github.com/mantidproject/mantid/issues/9756)~~,  ~~[10212](https://github.com/mantidproject/mantid/issues/10212)~~, ~~[10213](https://github.com/mantidproject/mantid/issues/10213)~~ |


