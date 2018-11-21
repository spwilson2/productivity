set -xe

if [ $# -ne 2 ] ; then
  echo "$0 <source-repo> <new-repo>"
  exit 1
fi

#GIT_TRUNK="/home/landshark/sean.wilson/git/origin/trunk"
GIT_TRUNK="$1"
NEW_REPO="$2"

SVN_TRUNK="`cd $GIT_TRUNK && svn info --show-item url`"
REVISION="`git -C "$GIT_TRUNK" svn log --limit 1 | head -n 2| ag "r\d+" -o`"

git clone "$GIT_TRUNK" "$NEW_REPO"
cd "$NEW_REPO"
git fetch origin git-svn:refs/remotes/git-svn
cp -r "$GIT_TRUNK/.svn" .
svn revert -R .
svn update -r "$REVISION"

git svn init "$SVN_TRUNK"
git checkout --force
git svn fetch
