#!/usr/bin/env bash
pyinstaller --specpath build --onefile src/rpiwifigui.py --workpath build/elf --distpath dist/elf
