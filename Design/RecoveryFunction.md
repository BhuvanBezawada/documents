# Introducing a Recovery function

## Motivation

Several users have commented that it would be very useful if Mantid could recover the final state after a crash. The motivation for this is quite clear. However, there are also some additional benefits that could arise from such a functionality.
* The history used for recovery could provide useful diagnostics of crash instances
* The history used for recovery could also be used to re-load workflows, rather than saving data, which is quicker for data-intensive users, such as single crystal diffraction

## Requirements

The recovery function should generate a script, this should:
* Be capable of recreating all workspaces present when it was last generated
* Be automatically generated at regular intervals
* Result in as efficient a re-load process as possible
* Have minimal overhead for running
* Allow some level of user choice of how much of the history to re-run

## Implementation possibilities

Currently the preferred option is to have a script that can amalgamate the workspace histories in the current instance of Mantid and generate a single script. This can be done by comparing time/date-stamps, algorithm names and input parameters.

## Open questions

* How much overlap would this functionality have with Project Saving? 
* Should the functionality be in MantidPlot or Framework?

## Actions

Keith to work on prototyping and testing the proposed implementation. (30 May 2018)
