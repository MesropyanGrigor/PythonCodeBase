#! /bin/sh
usage()
{
  cat<<EOF
    usage: mkcvsroot [-s] <projectTopDir> -group <group>
        -s option suppresses progress messages (optional)
        -group change project directory group ownership (required)
EOF
}
group=''
silent=''
projdir=''
while [ $# -ne 0 ]; do
    case $1 in
        -s)         silent=1;;
        -group)     group=$2; shift;;
        -h)         usage; exit 1;;
        *)          projdir=$1;;
        #*)          echo "$1: Unsupported option was used"; usage; exit 1;;
    esac
    shift
done
if [ -z $group ]; then
    echo "-- ERROR: Option -group should be provided"
    exit 1
fi
echo "GROUP", $group # TODO delete
projTopDir=`canon $projdir`
echo "Project Dir: " $projTopDir
if [ ! -d $projTopDir ]; then
    echo "-- ERROR: Porject path doesn't exist"
    exit 1
fi
CVSROOT=$projTopDir/.cvsroot
echo "CVSROOT: " $CVSROOT
export CVSROOT
if [ ! -d $CVSROOT ]; then
  tmpDir=/tmp/mkcvsroot$$
  echo "TmpDir: " $tmpDir 
  mkdir -p $tmpDir
  cd $tmpDir
  [ -z "$silent" ] && echo "-- initializing CVS repository $CVSROOT ..."
  cvs init;
  cvs checkout CVSROOT/cvswrappers >/dev/null
  cat >> CVSROOT/cvswrappers <<EOF
*.gz	    -k 'b'
*.tgz	    -k 'b'
*.gif	    -k 'b'
*.jpg	    -k 'b'
*.gds	    -k 'b'
*.pdf	    -k 'b'
*.db	    -k 'b'
*.pdb	    -k 'b'
*.sdb	    -k 'b'
*.cdb	    -k 'b'
*:1	    -k 'b'
*.lava	    -k 'b'
*.brava	    -k 'b'
lib	    -k 'b'
lib_1	    -k 'o'
master.tag  -k 'o'
prop.xx	    -k 'b'
EOF
  cvs commit -m "Added standard binary types." CVSROOT/cvswrappers >/dev/null
  echo y | cvs release -d CVSROOT >/dev/null
fi

if [ ! -d $CVSROOT/libs ]; then
  [ -z "$silent" ] && echo "-- initializing $projTopDir/rev_ctrl/libs ..."
  mkdir $CVSROOT/libs
  if [ -d $projTopDir/rev_ctrl/libs ]; then
    echo "-- ERROR: $projTopDir/rev_ctrl/libs already exists ..."
  else
    if [ ! -d $projTopDir/rev_ctrl ]; then mkdir -p $projTopDir/rev_ctrl; fi
    cd $projTopDir/rev_ctrl
    cvs checkout libs >/dev/null 2>&1
  fi
fi

if [ ! -z $group ]; then
    echo "-- Changing mods of $projTopDir directory"
    chgrp $group $projTopDir -R;
    chmod o-w $projTopDir -R;
    chmod g+s $projTopDir -R;
fi
