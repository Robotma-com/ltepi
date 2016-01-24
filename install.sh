#!/bin/bash

VERSION=0.9.5

RECORD="./files.txt"
if [ -n "$1" ]; then
  RECORD=$1
fi

function assert_root {
  if [[ $EUID -ne 0 ]]; then
     echo "This script must be run as root" 
     exit 1
  fi
}

function install {
  cp -f PKG-INFO.txt PKG-INFO
  sed -i -e "s/%VERSION%/${VERSION//\//\\/}/g" PKG-INFO
  cp -f setup.py.txt setup.py
  sed -i -e "s/%VERSION%/${VERSION//\//\\/}/g" setup.py
  python ./setup.py install --record ${RECORD}
}

assert_root
install
