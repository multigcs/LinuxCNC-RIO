#!/bin/bash
#
#

echo ""
echo "## Plugins:"
echo ""

TitleCaseConverter() {
    sed 's/.*/\L&/; s/[a-z]*/\u&/g' <<<"$1"    
}

echo "| Type | Name | Description |"
echo "| --- | --- | --- |"


for S in joint vin vout din dout expansion interface
do
    for P in plugins/${S}_*
    do
        NAME=`echo "$P" | sed "s|^plugins/${S}_||g"`
        DESC=`head -n 3 $P/README.md | tail -n1`
        echo "| $S | $NAME | $DESC |"
    done
done


exit 0

for S in joint vin vout din dout expansion interface:
do
    echo "### `TitleCaseConverter $S`:"
    echo ""
    for P in plugins/${S}_*
    do
        NAME=`echo "$P" | sed "s|^plugins/${S}_||g"`
        echo "#### `TitleCaseConverter $NAME`:"
        echo ""
        head -n 3 $P/README.md | tail -n1
        echo ""
    done
done
