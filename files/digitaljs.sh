#!/bin/sh
#
#

#
# wget -O files/digitaljs.js https://tilk.github.io/digitaljs/main.js
#
# cd /usr/src/
# git clone https://github.com/tilk/yosys2digitaljs.git
# cd yosys2digitaljs
# npm install
#

if test "$1" = "all"
then

    mkdir -p HTML-SIMULATION
    rm -rf HTML-SIMULATION/*

    cat <<EOF > HTML-SIMULATION/index.html
<html>
  <frameset cols="300, *">
    <frame src="menu.html" name="nav">
    <frame src="vout_pwm.html" name="main">
  </frameset>
</html>
EOF
    
    echo "<h3>RIO-Plugins</h3>" > HTML-SIMULATION/menu.html
   
    for P in `ls plugins/*/*_*.v`
    do
        P_DIR=`dirname $P`
        P_NAME=`basename $P | sed "s|\.v$||g"`
        echo "<a target='main' href='$P_NAME.html'>$P_NAME</a><br/>" >> HTML-SIMULATION/menu.html
        sh $0 $P HTML-SIMULATION
    done
    echo "" >> HTML-SIMULATION/menu.html



    cat HTML-SIMULATION/index.html

    exit 0
fi

VERILOG_FILE=$1
VERILOG_DIR=`dirname $1`
VERILOG_NAME=`basename $1 | sed "s|\.v$||g"`
SCRIPT_DIR=`dirname $0`
OUTPUT=$VERILOG_DIR

if test "$2" != ""
then
    OUTPUT="$2"
fi

echo "generating: $OUTPUT/$VERILOG_NAME.html"

/usr/src/yosys2digitaljs/process.js "$VERILOG_FILE" > "$OUTPUT/$VERILOG_NAME.json"

cat <<EOF > "$OUTPUT/$VERILOG_NAME.html"
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
    <title>$VERILOG_NAME</title>
  <script type="text/javascript" src="digitaljs.js"></script></head>
  <body>
    <div>
        <button name="start" type="button">▶️</button>
        <button name="stop" type="button">⏹️</button>
    </div>
    <div id="paper">
    </div>
    <div>
        <input name="fixed" type="checkbox">Fixed Mode</input>
        <button name="json" type="button">Serialize and Reload</button>
        <input name="layout" type="checkbox">Include layout information</button>
    </div>
    <div>
        <button name="ppt_up" type="button">+</button><button name="ppt_down">-</button><button name="left">&lt;</button><button name="right">&gt;</button><button name="live">live</button>
    </div>
    <div id="monitor">
    </div>
    <div id="iopanel">
    </div>
    <script>
      var circuit, monitor, monitorview, iopanel, paper;
      var start = \$('button[name=start]');
      var stop = \$('button[name=stop]');
      var papers = {};
      const fixed = function (fixed) {
        Object.values(papers).forEach(p => p.fixed(fixed));
      }
      const loadCircuit = function (json) {
        circuit = new digitaljs.Circuit(json);
        monitor = new digitaljs.Monitor(circuit);
        monitorview = new digitaljs.MonitorView({model: monitor, el: \$('#monitor') });
        iopanel = new digitaljs.IOPanelView({model: circuit, el: \$('#iopanel') });
        circuit.on('new:paper', function(paper) {
          paper.fixed(\$('input[name=fixed]').prop('checked'));
          papers[paper.cid] = paper;
          paper.on('element:pointerdblclick', (cellView) => {
            window.digitaljsCell = cellView.model;
            console.info('You can now access the doubly clicked gate as digitaljsCell in your WebBrowser console!');
          });
        });
        circuit.on('changeRunning', () => {
          if (circuit.running) {
            start.prop('disabled', true);
            stop.prop('disabled', false);
          } else {
            start.prop('disabled', false);
            stop.prop('disabled', true);
          }
        });
        paper = circuit.displayOn(\$('#paper'));
        fixed(\$('input[name=fixed]').prop('checked'));
        circuit.on('remove:paper', function(paper) {
          delete papers[paper.cid];
        });
        circuit.start();
      }
      start.on('click', (e) => { circuit.start(); });
      stop.on('click', (e) => { circuit.stop(); });
      \$('button[name=json]').on('click', (e) => {
        monitorview.shutdown();
        iopanel.shutdown();
        circuit.stop();
        const json = circuit.toJSON(\$('input[name=layout]').prop('checked'));
        console.log(json);
        loadCircuit(json);
      });
      \$('input[name=fixed]').change(function () {
        fixed(\$(this).prop('checked'));
      });
      \$('button[name=ppt_up]').on('click', (e) => { monitorview.pixelsPerTick *= 2; });
      \$('button[name=ppt_down]').on('click', (e) => { monitorview.pixelsPerTick /= 2; });
      \$('button[name=left]').on('click', (e) => { monitorview.live = false; monitorview.start -= monitorview._width / monitorview.pixelsPerTick / 4; });
      \$('button[name=right]').on('click', (e) => { monitorview.live = false; monitorview.start += monitorview._width / monitorview.pixelsPerTick / 4; });
      \$('button[name=live]').on('click', (e) => { monitorview.live = true; });
      \$(window).ready(function () { loadCircuit(
EOF
cat "$OUTPUT/$VERILOG_NAME.json" >> "$OUTPUT/$VERILOG_NAME.html"
cat <<EOF >> "$OUTPUT/$VERILOG_NAME.html"
          ) });
    </script>
  </body>
</html>
EOF

cp "$SCRIPT_DIR/digitaljs.js" "$OUTPUT"

