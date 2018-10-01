# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
"""1.0.02
Improved documentation to use shorter import forms.

Also bumped version number.

Also planning to tag this with a version to see whether that encourages
readthedocs to add the version properly.

29.05.2018 1.0.03
Add pushv (for maintainer use only) and this CHANGES.py file.

29.05.2018 1.0.04
Correctly cast strings to native strings in check_shell_output.

29.05.2018 1.0.05
Tests for feather are now ignored if pmmif/feather are not installed.

29.05.2018 1.0.06
Windows fixes.

31.05.2018 1.0.07
Fix for UTF-8 encoding in subprocesses on Windows.

Also added documentation on setting up fonts on Windows to display
ticks and crosses correctly.

6.06.2018 1.0.08
Improved metadata in TDDA files.

11.06.2018 1.0.09
Add support for postloadhook and postdicthook.

25.07.2018 1.0.10
Minor bug fixes.

 - Fuzzy verification of 'min' constraint was printing out the type of the col.
 - Typo in documentation of the properties available in a Verification result.
 - Verification of 'rex' constraint was not checking that the field exists.

26.07.2018 1.0.11
Fixed bug in pandas detect; it wasn't detecting min/max length constraints.

Also fixed issue with pandas CSV file reader; it has problems reading files
that have stuttered quotes and which also have escaped content. It now
notices if that has gone wrong, and has another try.

26.07.2018 1.0.12
minor refactoring and comments

1.08.2018 1.0.13
Now accepts 'false' as a valid specification value for no-duplicates.

Also improved the error message you get if you provide invalid specifications.
Also suppressed pandas warning about nanoseconds on conversion.

1.08.2018 1.0.14
Ignore epsilon for date min/max (rather than crashing).

This probably isn't ideal, but to make it better we'd need to decide
on what epsilon should mean for dates, which is not obvious.

13.08.2018 1.0.15
Change use of re.U (UNICODE) to re.UNICODE | re.DOTALL.

This means that dot actually matches any character.
The Python documentation claims that without this any character except
newline is matched, but it appears that some other characters are
also not matched without re.DOTALL, including a non-breaking space (0x80).

18.09.2018 1.0.16
referencetest class now exports TaggedTestLoader for convenience.

18.09.2018 1.0.17
TestLoader now takes an optional 'printer' parameter to control how -0 works.

18.09.2018 1.0.18
Renamed tdda.referencetest method assertFileCorrect -> assertTextFileCorrect.

The original name is still available for backwards compatibility, but
is deprecated.

19.09.2018 1.0.19
Added tdda.referencetest method assertBinaryFileCorrect.
Also fixed some issues with tdda.referencetest ignore_patterns method.

19.09.2018 1.0.20
Added test files so that all the new tests will pass.

--------------------------- branch gentest -------------------------------
Add initial code for automatically generating reference tests.

Change location of reference files from $(pwd)/ref to $(pwd)/ref/NAME
where NAME is the base name of the test script (without 'test_' and '.py').
This is to allow multiple tests to co-exist in the same directory
without conflict, and also means that the reference files can be
named STDOUT and STDERR rather than more convoluted names.

Also changed the command-line syntax to use STDOUT and STDERR (in any case)
for those streams, and to default not to use them. This means that any
behaviour specifiable from the wizard can now also be specified on the
command line, and reduces the complexity of the logic.

Check exit status, and require to be zero by default.

Allow NONZEROEXIT to specify that a non-zero exit status is OK on command line,
and add question to wizard for this.

Warn if any of the files specified are not available for copying, but
still generated the test script.

Remove existing reference files and script before generating, if they exist.

Handle multiple reference files with the same name.

Disambiguate reference files that differ only in case so that things
are more likely to work on case-insensitive filesystems.

Clearer reporting after generating test script.

Also test script now includes (equivalent) command used to generate it.

Added shell script that generates the first test for gentest.
(The shell script uses tdda gentest to generate itself.)

Add default values to gentest wizard.

Allow directories as files to check and default to checking new files
created under $(pwd).

Allow glob patterns in reference file specifications.

Add timing information to output from gentest.

Add some tests generated by gentest! Quite circular.
(Will only work for njr at the moment, because of paths in the test
output, but we should be able to fix this soon.)

Add flag handling and use new -r option in tests.

This means tests should work for other people.

Get rid of TDDA_CWD and use os.dirname(__file__).

Added support for multiple runs (default 2). This will be used to look
for variation in output between runs, to generate exclusions etc.

Started to generate exclusions automatically based on the difference
between two runs. Removed some of the boilerplate as a result and instead
use a function to generate all the variable tests.

Started adding code for over-specific lines (paths, timestamps etc.)

The two hand-generated specific gentest tests are now producing
what seem to be the correct results, starting to give some confidence
that we're generating the intended exclusion patterns.

----------------------- end of branch gentest ---------------------------

------------------------- dev branch -------------------------
Refactored reporting of differences for files and strings, to take
better account of 'ignore' and 'remove' parameters. It now builds a 'diff'
that will only appear 'different' for lines that are REALLY different, after
any removals and ignores have been collapsed. That diff can also include an
embedded 'raw' diff, which will show ALL the differences, but the main focus
is on showing 'what is different that should not be'.

Also improved reporting of differences when there are different numbers
of lines. It now says what line at which the (effective) differences start
(taking into account removals and ignores).

The ignore_patterns parameter is now treated slightly more strictly than
before, and has had its documentation improved. If you provide an unanchored
regular expression pattern, it now requires that both sides match that
pattern, but it ALSO now requires that the remaining parts, to the left and
right of where the pattern matched, be 'equivalent' if the line is to be
ignored. The two 'left parts' must be equivalent, and the two 'right parts'
must also be equivalent. This 'equivalence' is checked by (recursively)
applying the same logic to these sub-parts.

The ignore_substrings parameter is now treated slightly more strictly than
before. Previously, a line was ignored if it contained any of the ignorable
substrings, in either the actual or the expected. That meant that lines in
the actual data might be being unexpectedly ignored if they start to include
such strings, which probably was not the intent of the test at all. Now,
ignorable substrings only refer to the *expected* data (which is fixed for
the test, and you know exactly what is in it and what is not).

------------------------- end of dev branch -------------------------
"""
