#!/bin/bash
pyrcc4.exe feedpy.qrc > feedpy_rc.py
pyuic4.sh diag.ui -o diag.py
pyuic4.sh untitled.ui -o untitled.py
pyuic4.sh filters.ui -o filters.py

