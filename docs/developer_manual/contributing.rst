============
Contributing
============

Before submitting a pull request, please take a look at the following points:

- To submit a pull request (PR), you will need to fork the repository. Then, it is
  recommended to create a new branch in your fork dedicated to your bug fix or
  new feature. Once the PR has been accepted, the content of the branch will be
  squashed into a single commit on the master branch. Afterward, the branch can
  be deleted (or forgotten).

- For simple modifications (e.g. typos) the whole process above can be done
  automatically by Github by using its edition functionality (the pencil icon
  on the top left of Github's file viewer).

- See the :doc:`testing` section of the documentation for details on how to
  test the code.
  Before submitting a change of the code, make sure that all tests are passing.
  If you'd like to add a feature, please add the relevant tests to the `pytest`
  directory.

- All modifications of the code are listed in the ``docs/changelog.rst``.
  If you submit a bug fix or a new feature, please add a line in the changelog.

- New features should also be documented in the user manual (``docs/user_manual/``).
  Please add a short documentation of the feature in the relevant page.

- The code follows the `PEP8`_ guidelines for code style.
  Indentation is done with four spaces.
  Try to avoid trailing whitespaces whenever possible.

.. _`PEP8`: https://pep8.org/


The whole of Capytaine is currently licensed under the terms of the General
Public License (GPL). In the future, some modules might be extracted and
released with another free software license, such as the Apache License. If
your contribution cannot be released under another license (because it includes
code from another GPL package or just because you don't want to), please tell
us explicitly.
