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

for CONFIG in $CONFIGS
do
    rm -rf Output/*
    echo $CONFIG
    STAMP1=`date +%s`
    if ! python3 buildtool.py $CONFIG
    then
        echo "ERROR building for $CONFIG"
        exit 1
    fi
    (
        cd Output/*/Firmware/
        if ! make
        then
            echo "ERROR building bitfile for $CONFIG"
            exit 1
        fi
    )
    STAMP2=`date +%s`
    echo "`expr $STAMP2 - $STAMP1`s: $CONFIG" >> build-testall.log
done


