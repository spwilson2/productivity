
TODO
====
* Split up editor command functionality into different argument groups.
    * Send command to editor
    * Open editor/new tab in editor

* Add a wrapper around svn patch for a single file so I don't have to manually edit the patch files.
  i.e. This type of interface::

  svn patch patchfile --files <list of files to patch>

* Add a command for getting all files in a changelist. (without their change attributes.)

* Prototype git+svn workflow rather than using svn patches.

* Open up a new terminal in the current working directory with i3:
    Use a bash command to save the cwd for every terminal.
    When opening a terminal in i3 check the currently active window and lookup its working directory.

Complete
========

* Add blocking support into the python based editor script
* Create a single file daily log.
* Forward arguments from editor script to gvim.
* Add a backup script + cronjob for the log directory.
