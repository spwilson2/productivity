
export GIT_TRUNK=/home/landshark/sean.wilson/git/origin/trunk

git clone "$GIT_TRUNK" $1
cp -ra "$GIT_TRUNK/.svn" $1
cd $1
git checkout svn/additions
svn up
