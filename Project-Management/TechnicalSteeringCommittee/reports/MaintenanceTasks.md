For 3.5 maintenance period
--------------------------
1. Harmonizing external contributions with the rest of mantid (e.g. PSI subpackage)
1. Remove unused tools
   3. mwclient
1. all systemtests at least work on one platform [skipped system tests](http://developer.mantidproject.org/systemtests/)
1. Reducing static analysis issues (discus stewards and soft limits)
   1. [pylint](http://builds.mantidproject.org/job/pylint_master)
   2. [coverity](https://scan.coverity.com/projects/335)
   3. [clang](http://builds.mantidproject.org/job/master_clean-clang/)
   6. header analysis (e.g. [include what you use](http://www.mantidproject.org/IWYU) and CLion) - Limited to 2 man days
   7. Refactoring of specific code areas (load nexus algorithms) - investigate and distribute
   4. ~~CutAndPaste detector~~
   5. ~~gcov (or equivalent)~~
1. Update `class_maker.py` to generate code following current standards
1. Removed by agreement
1. Filling in argument list in python bindings (e.g. "self")
1. Enforcing the [C++ coding standards](http://www.mantidproject.org/C%2B%2B_Coding_Standards) (on Framework)
   1. Re-run `clang-format`
   1. Editing actual variable and class names - investigate the discrepancy of our code with that in [C++ coding standards](http://www.mantidproject.org/C%2B%2B_Coding_Standards) and not covered by `clang-format`, max 1 days effort
1. Generate `.py` from `.ui` files as part of the build
1. Add `LINK_PRIVATE` where possible in CMake
1. Add `f2py` code to the builds - this is an ongoing process, only complex items remain (translating fortran to python and effectively support as python)

Too low benefit/priority for this release
-----------------------------------------
1. Proper rpm and deb packages (see previous item) - is this required
1. Making packages properly external - benefit low, current version is effectively frozen this way which is actually good for us.
   1. ANN
   2. GSoap ?
1. Back-port changes from QTIPlot to MantidPlot - 2 man days to produce a shopping list of functionality, benefits and estimates

   
For a different release
-----------------------
2. Move to CMake 3 [#9362](http://trac.mantidproject.org/mantid/ticket/9362), rework cmake as a whole, re-examine the package structure
2. Move to Qt 5
3. Move to Python 3
4. Move to visual studio 2015 community edition
5. Investigate breaking issues with updated dependencies
    1. [Poco 1.6](http://trac.mantidproject.org/mantid/ticket/10976)
    2. oce 0.17 or OpenCascade 6.8
    3. iPython 3.0
