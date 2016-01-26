#!/bin/bash

RECORD="./ltepi-files.txt"
if [ -n "$1" ]; then
  RECORD="$1/ltepi-files.txt"
fi

function assert_root {
  if [[ $EUID -ne 0 ]]; then
     echo "This script must be run as root" 
     exit 1
  fi
}

function uninstall {
  cat ${RECORD} | xargs rm -rf
}

assert_root
uninstall
