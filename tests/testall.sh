#!/bin/bash
#
#

export PATH=$PATH:/opt/oss-cad-suite/bin/
export PATH=$PATH:/opt/gowin/IDE/bin/
export PATH=$PATH:/opt/Xilinx/Vivado/2023.1/bin/

CONFIGS=$1
if test "$CONFIGS" = ""
then
    CONFIGS=configs/*/config*.json
fi

echo -n > build-testall.log

rm -rf Output/*
for CONFIG in $CONFIGS
do
    echo $CONFIG
    FOLDER="`cat $CONFIG | jq -r '.name'`"
    
    STAMP1=`date +%s`
    if ! python3 buildtool.py $CONFIG
    then
        echo "ERROR building for $CONFIG"
        exit 1
    fi
    (
        cd Output/$FOLDER/Gateware/
        if grep -s -q gowin_build Makefile
        then
            echo "build gateware: make clean gowin_build"
            if ! make clean gowin_build
            then
                echo "ERROR building bitfile for $CONFIG"
                exit 1
            fi
        else
            echo "build gateware: make clean all"
            if ! make clean all
            then
                echo "ERROR building bitfile for $CONFIG"
                exit 1
            fi
        fi
    )
    STAMP2=`date +%s`
    echo "`expr $STAMP2 - $STAMP1`s: $CONFIG" >> build-testall.log
done


