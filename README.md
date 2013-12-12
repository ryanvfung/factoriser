Integer Factoriser for Python
=============================

Introduction
------------

The integer factoriser checks for the factors of an integer, and returns a list of factors while providing transcript of successful factor discoveries.

Use version 4 for quick access through a console, or use version 3 for direct access through an IDE

**Author**: Ryan Fung

**Created**: 2013-10-18

**Last Modified**: 2013-11-28

### Method
It checks prime factors up to the square root, while timing the operation and pausing to prevent processing overload on the CPU. Works by checking directly prime factors from 2 to 29, then checks factors in batches of 30.


Upcoming Features to be Implemented
-----------------------------------
None


Change log
----------
### 2013-10-15 Version 0.1
* Initial release - basic factoriser function defined

### 2013-10-15 Version 0.2
* Implemented factorisation process duration, allows aborts after interval time

### 2013-10-15 Version 0.3
* Modified process duration check, allows user to change duration before next abort prompt

### 2013-11-28 Version 0.4
* Deprecated f(n) as shorthand
* Added code to allow factoriser function to run immediately following loading on a console
