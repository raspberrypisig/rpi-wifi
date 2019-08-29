#!/usr/bin/env bash
set -x
mkdir -p build dist
./install-prerequisites.sh
./install-fpm.sh
./build-elf.sh
./createdeb.sh
