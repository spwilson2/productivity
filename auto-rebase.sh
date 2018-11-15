#!/bin/bash

set -e

export GIT_TRUNK=/home/landshark/sean.wilson/git/origin/trunk
export SVN_TRUNK=""
export TMPDIR="`mktemp -d`"

cleanup() {
  cd "$GIT_TRUNK"
  git worktree remove "$TMPDIR"
  git branch -D updater
  #rm -rf "$TMPDIR"
}

reset_baselines() {
  set -x

  git checkout gitignore
  git worktree add -b updater "$TMPDIR"


  cp -ra .svn "$TMPDIR"
  cd "$TMPDIR"
  svn up
  git add -A
  revision="`svn info | grep Revision: | sed "s/.* //"`"
  git commit -m "svn: $revision"


  git checkout svn/clean --force
  git reset --hard updater

  git checkout svn/setup
  git reset --hard svn/clean
  ./setup
  git add -A
  git commit -m "Run setup script"


  git checkout svn/additions
  git reset --hard svn/setup
  ./products/integrity_additions_bto.sh
  git add -A 
  git commit -m "Run additions script"
  git checkout updater
}


cd "$GIT_TRUNK"
reset_baselines
cleanup
