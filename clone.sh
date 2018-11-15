set -xe

export GIT_TRUNK=/home/landshark/sean.wilson/git/origin/trunk
export SVN_TRUNK="/home/landshark/sean.wilson/rtostrunk"

git clone "$GIT_TRUNK" $1
cp -ra "$SVN_TRUNK/.svn" $1
cd $1
git checkout svn/additions
