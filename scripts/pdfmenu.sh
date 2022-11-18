#!/usr/bin/env bash

set -eu
cd "$(dirname "${BASH_SOURCE[0]}")"
sed 's/\&/+/g' ../data/menu_data.json > ./menu_data.json.tmp
chevron -d ./menu_data.json.tmp ./menu.tex.mustache > ./menu.tex
lualatex menu.tex
