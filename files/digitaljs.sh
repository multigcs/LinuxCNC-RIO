#!/bin/sh
#
#

#
# cd /usr/src/
# git clone https://github.com/tilk/yosys2digitaljs.git
# cd yosys2digitaljs
# npm install
#
# wget -O files/digitaljs.js https://tilk.github.io/digitaljs/main.js
#

VERILOG_FILE=$1
VERILOG_DIR=`dirname $1`
VERILOG_NAME=`basename $1 | sed "s|\.v$||g"`

SCRIPT_DIR=`dirname $0`

echo "## $VERILOG_DIR $VERILOG_NAME"


/usr/src/yosys2digitaljs/process.js "$VERILOG_FILE" > "$VERILOG_DIR/$VERILOG_NAME.json"

cat <<EOF > "$VERILOG_DIR/$VERILOG_NAME.html"
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
cat "$VERILOG_DIR/$VERILOG_NAME.json" >> "$VERILOG_DIR/$VERILOG_NAME.html"
cat <<EOF >> "$VERILOG_DIR/$VERILOG_NAME.html"
          ) });
    </script>
  </body>
</html>
EOF

cp "$SCRIPT_DIR/digitaljs.js" "$VERILOG_DIR"

