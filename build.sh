#!/usr/bin/env bash
mkdir -p build dist
./install-prerequisites.sh
./install-fpm.sh
./build-elf.sh
./createdeb.sh
