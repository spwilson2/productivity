#!/bin/bash

#name=${PPID}
#name=$(pwd)
name="${vserv:-gvim}"

block() {
  read -p "Press enter when done. "
}

if [ $# -eq 0 ] ; then
    gvim --servername "${name}" --remote-send ":tabnew" || gvim --servername "${name}"
    if ! [ "$async_editor" = "true" ] ; then
      block
    fi
else
    gvim --servername "${name}" --remote-tab $@
    if ! [ "$async_editor" = "true" ] ; then
      block
    fi
fi

#xfce4-terminal -x vim $@
