function git-clone-aptrunk() {
    ~/projects/productivity/clone.sh /home/landshark/sean.wilson/git/origin/aptrunk "$@" && \
    cd "$@" && ./setup && ./products/integrity_additions_multivisor.sh
}
function git-clone-i11.7() {
  ~/projects/productivity/clone.sh /home/landshark/sean.wilson/git/origin/i11.7 "$@" && \
  cd "$@" && ./setup && ./products/integrity_additions_multivisor.sh
}
function git-clone-trunk() {
  ~/projects/productivity/clone.sh /home/landshark/sean.wilson/git/origin/trunk "$@" && \
  cd "$@" && ./setup && ./products/integrity_additions_bto.sh
}
function git-update-svn() {
  REV="`git svn log --limit 1 | head -n 2| ag "r\d+" -o`"
  svn revert -R . && svn update -r "$REV" --force && git checkout --force
}
