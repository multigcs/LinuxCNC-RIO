#!/bin/sh
#
#

if test "$1" = "all"
then

    for P in `ls plugins/*/*_*.v`
    do
        P_DIR=`dirname $P`
        P_NAME=`basename $P | sed "s|\.v$||g"`
        sh $0 $P
    done
    exit 0
fi

VERILOG_FILE=$1
VERILOG_DIR=`dirname $1`
VERILOG_NAME=`basename $1 | sed "s|\.v$||g"`
SCRIPT_DIR=`dirname $0`

echo "generating: $OUTPUT/$VERILOG_NAME.dot,  $OUTPUT/$VERILOG_NAME.svg"

cd $VERILOG_DIR
yosys -p "read_verilog $VERILOG_NAME.v"  -p "hierarchy -check"  -p "proc; opt; fsm; opt; memory; opt"  -p "show -prefix $VERILOG_NAME -notitle -colors 2 -width -format dot"

dot -Tsvg $VERILOG_NAME.dot -o $VERILOG_NAME.svg

if test -e README.md && ! grep -s -q $VERILOG_NAME.svg README.md
then
    echo "" >> README.md
    echo "# $VERILOG_NAME.v" >> README.md
    echo "![graphviz](./$VERILOG_NAME.svg)" >> README.md
    echo "" >> README.md
fi

