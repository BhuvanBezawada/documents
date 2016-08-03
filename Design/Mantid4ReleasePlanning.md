Release Planning for Mantid version 4.0
=======================================

Motivation
----------

We have a number of desired changes that will break backward compatibility for users scripts, and potentially ways of working with 
Mantid and Mantidplot.  Following the rules of Semantic versioning (http://semver.org/) this means we need to increase the major version number. While we can make these kind of changes in a planned way with carefull communication, we cannot follow that up
with other breaking changes soon afterwards.

In order to decide on the changes to make it into this major release, and to align them to deliver together we will document the planned changes
to include here.

Timing of Mantid 4.0
--------------------

The timing for Mantid 4.0 is not determined by the current version numbering, that is to say there is no reason that 4.0 should follow 3.9, we could perfectly well have version 3.10 and so on.
The determinating step for Mantid 4.0 is the list of breaking changes below.  If we decide all of them are to remain in this release, then the latest to deliver will determine the timng of Mantid 4.0.

User Expectations of Mantid 4.0
-------------------------------

We have not raised the concept of Mantid 4.0 with our users, so we have not made any commitment about what it may contain.  However we should be aware that while it is  not defined in Semantic versioning (http://semver.org/), the users will expect some significant improvements in order to justify the version change, and to act as a carrot to entice them to upgrade and overcome the discomfort of the breaking changes we are introducing.  Some of the breaking changes themselves will bring significant advantages, but the benefits of others are less visible.  It is worth considering other significant improvements that can be aligned with Mantid 4.0 to encourage enthusiastic adoption of these changes.

List of breaking changes 
------------------------

1. Change from qwt5 graphs to ? [3 people 1-3m]
1. Move to Python 3 on all platforms [1 person 2m]
1. Sanitise Algorithm and property names (including merging) [Plan - 1 person 2w, Impl 3 people 1-3m]
1. Removing InOut workspace usage [1 person 2w]
1. ?Moving the Python API from the SimpleAPI (the impacts of this need further consideration) [????????]

List of other changes
---------------------

These changes are not bound to be included in this release, but being significant changes it would be good to include them together if
the timing and resource allows.

1. Instrument 2.0 [2p 4m]
2. Upgrade to Qt5 [2p 2m]

The guestimates provided in [ ] are included at present only to propose a starting point for further conversation. 

Easing the pain of user adoption
--------------------------------

With such a collection of changes we will nedd to plan to ensure we communicate the changes well, and have approaches in place to ease the migration of user scripts to work with the new version of Mantid. The following straw man is proposed for discussion:

1. Once the Plan is agreed
 - Inform all users about the upcoming changes and migration plans

1. At the preceeding release (~4 months till release)
 - Remind all users about the upcoming changes
 - Implement a "Future" API layer, that will allows scripts to be migrated in advance
 - Deprecate the existing API functionality that will be broken in Mantid 4.0, leaving it functional, but sending warning messages to the log.
   - ? Send emails to a special email account on usage of deprecated fn, or store in DB? This would allow us to track down scripts that need changing.
 - Development team to update all scripts in the script repository to the "future" api
 - Provide a deadline for all users to submit scripts by email for them to be update by the dev team
 - Run Script update drop in sessions (once/twice per month?, with cake?)

1. At the release of Mantid 4.0
 - During Beta Testing (or earlier) ensure all instruemnts can operate on Mantid 4.0
 - Remove deprecated functionality
 - Merge Future API to main API
