Think About
===========

* Think about ways to improve my workflow when tracing code - a lot of hopping around the terminal with ag.
  Also I'd like to keep track of the jumplist probably or make notes about certain lines.


TODO
====

* Split up editor command functionality into different argument groups.
    * Send command to editor
    * Open editor/new tab in editor

* Add a command for getting all files in a changelist. (without their change attributes.)

* Vim cleanupwhitespace command should work on a selection

* Open up a new terminal in the current working directory with i3:
    Use a bash command to save the cwd for every terminal.
    When opening a terminal in i3 check the currently active window and lookup its working directory.

* Add a wrapper around svn patch for a single file so I don't have to manually edit the patch files.
  i.e. This type of interface::

    svn patch patchfile --files <list of files to patch>

Log Script
==========

* Modify the log python script to optionally take a vim buffer instead and have it modify the buffer.
  (This way the addition of today's log is only added once the log is saved.)
* Change the log command so it doesn't make me press enter every time to clear the python command output
* Modify the log command so it doesn't leave an open buffer if it's on a ``[No Name]`` buffer.
* Modify the log script to have a prepend a blank line if one doesn't exist before the header entry.

Vim Tag Log
===========

Log which saves jumpable points to a file as well as optional notes which are displayed in a 'jump-bar' buffer as the line is hovered over.
The jump-bar buffer can also be scrolled through and the previous window will jump to the tag.

To-do Log
=========

* Todo add a todo log with due dates to get notifications. Look online at the todo.txt tool or similar alternatives.

* Create a todolist parser for log.txt file.
  Parse the log logging for items under todo.
  Append metadata to each todo item.
  Create various status outputs to manage their status and due dates.

SVN + GIT Workflow
==================

TODO
^^^^

* Use tags rather than branches for the setup and additions types.
* Change auto-rebase script to only run if svn commits were made.
* auto-rebase script should always move forward - not rebase.
