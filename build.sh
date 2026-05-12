#!/bin/bash

echo "Cleaning previous builds..."

rm -rf build
rm -rf dist
rm -f *.spec

echo "Building JobButler..."

./venv/bin/pyinstaller \
    --windowed \
    --collect-all customtkinter \
    --add-data "templates:templates" \
    --name JobButler \
    --icon=icon.png \
    src/main.py

echo "Build finished."