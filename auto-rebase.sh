#!/bin/bash

set -x

export GIT_TRUNK=/home/landshark/sean.wilson/git/origin/trunk
export SVN_TRUNK="/home/landshark/sean.wilson/rtostrunk"
export TMPDIR="`mktemp -d`"

cleanup() {
  set +e
  cd "$GIT_TRUNK"
  git worktree remove "$TMPDIR"
  git branch -D updater
}

update_trunk() {
  set -e
  pushd "$SVN_TRUNK"
  svn up
  popd
}

reset_baselines() {
  set -e
  cd "$GIT_TRUNK"

  git checkout gitignore
  git worktree add -b updater "$TMPDIR"

  cp -ra "$SVN_TRUNK/.svn" "$TMPDIR"
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

update_trunk
reset_baselines
cleanup
