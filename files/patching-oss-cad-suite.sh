#!/bin/bash
#
#

# https://github.com/YosysHQ/oss-cad-suite-build/releases/download/2023-07-20/oss-cad-suite-linux-x64-20230720.tgz


OSS=$1
AVERSION="Apycula-0.8.2a2.dev1+g8e31050-py3.8.egg"

if ! test -e "$OSS/lib/python3.8/site-packages"
then
    echo "ERROR: $OSS/lib/python3.8/site-packages/ not found"
    echo "please add PATH to your oss-cad-suite"
    echo ""
    echo "    $0 PATH_TO_OSS_CAD_SUITE"
    echo ""
    exit 1
fi

if ! test -e "$OSS/lib/python3.8/site-packages/$AVERSION"
then
    echo "ERROR: $AVERSION not found in $OSS/lib/python3.8/site-packages/"
    echo "please user the right version of oss-cad-suite: 2023-07-20"
    exit 1
fi

if test -f "$OSS/lib/python3.8/site-packages/$AVERSION/apycula/gowin_pack.py"
then
    echo "allready patched"
    exit 0
fi


cd $OSS/lib/python3.8/site-packages/

mv $AVERSION $AVERSION.zip
mkdir -p $AVERSION
cd $AVERSION
unzip ../$AVERSION.zip

sed -i "s|import importlib.resources|from importlib_resources import files|g" apycula/gowin_pack.py
sed -i "s|importlib.resources.files|files|g" apycula/gowin_pack.py


