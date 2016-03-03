#!/bin/bash

VERSION=0.9.5

PREFIX="."
RECORD="ltepi-files.txt"
if [ -n "$1" ]; then
  PREFIX="$1"
fi
RECORD="${PREFIX}/ltepi-files.txt"

function assert_root {
  if [[ $EUID -ne 0 ]]; then
     echo "This script must be run as root"
     exit 1
  fi
}

function install_pyserial {
  python -c "import serial"
  if [ "$?" == "0" ]; then
    return
  fi
  apt-get update -qq
  apt-get install -y python-serial
}

function install {
  cp -f PKG-INFO.txt PKG-INFO
  sed -i -e "s/%VERSION%/${VERSION//\//\\/}/g" PKG-INFO
  cp -f setup.py.txt setup.py
  sed -i -e "s/%VERSION%/${VERSION//\//\\/}/g" setup.py
  python ./setup.py install --record ${RECORD}
  cp -f uninstall.sh ${PREFIX}/ltepi-uninstall.sh
}

function package {
  rm -f ltepi-*.tgz
  # http://unix.stackexchange.com/a/9865
  COPYFILE_DISABLE=1 tar --exclude="./.*" -zcf ltepi-${VERSION}.tgz *
}

if [ "$1" == "pack" ]; then
  package
  exit 0
fi

assert_root
install_pyserial
install
