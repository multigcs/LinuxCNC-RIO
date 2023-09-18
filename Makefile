
#export PATH=$PATH:/opt/oss-cad-suite/bin/

CONFIG ?= configs/Lattice-iCE40HX8K_BOB/config.json
TARGETNAME = $(shell jq -r '.name' < ${CONFIG})

all: build firmware components

build:
	python3 buildtool.py ${CONFIG}

clean:
	rm -rf Output/${TARGETNAME}

format:
	black buildtool.py plugins/*/*.py
	astyle --style=gnu -A4  generators/linuxcnc_component/rio.c

isort:
	isort buildtool.py plugins/*/*.py

flake8:
	flake8 --ignore S605 --max-line-length 200 buildtool.py plugins/*/*.py

mypy:
	mypy buildtool.py generators/firmware/*.py plugins/*/*.py

check: isort flake8 mypy

istyle:
	iStyle plugins/*/*.v

schema: files/schema.svg

files/schema.svg: files/schema.sh
	files/schema.sh > files/schema.svg

firmware:
	(cd Output/${TARGETNAME}/Firmware/ ; make)

components:
	sudo halcompile --install Output/${TARGETNAME}/LinuxCNC/Components/rio.c

jsonlint: configs/*/*.json
	@for file in $^ ; do jq < $${file} > /dev/null || echo "JSON ERROR: $${file}"; done

verilator: plugins/*/*_*.v
	@for file in $^ ; do verilator --lint-only $${file}; done

verilatorWall: plugins/*/*_*.v
	@for file in $^ ; do verilator --lint-only -Wall $${file}; done

unittest:
	python3.9 -m pytest -vv -v tests/test_generator.py
