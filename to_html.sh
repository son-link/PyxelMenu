#!/bin/bash

declare -A example0=(
    [file]='001-default.py'
	[extras]=null
)

declare -A example1=(
    [file]='002-colors.py'
	[extras]=
)

declare -A example2=(
    [file]='003-cursor.py'
	[extras]=
)

declare -A example4=(
    [file]='004-cursor-img.py'
	[extras]='assets.pyxres'
)

declare -A example5=(
    [file]='005-highlight.py'
	[extras]=
)

declare -A example6=(
    [file]='006-submenu.py'
	[extras]=
)

declare -n example
for example in ${!example@}; do
    echo "File: ${example[file]}"

    number=$(echo "${example[file]}" | cut -d '-' -f 1)
    name=$(echo "${example[file]}" | cut -d '.' -f 1)

    build_dir="tmp/${name}"
    mkdir -p $build_dir
    cp "./examples/${example[file]}" pyxel_menu.py $build_dir

    if [ -n "${example[extras]}" ]; then
        echo "Extra: ${example[extras]}"
        cp "./examples/${example[extras]}" $build_dir
    fi

    pushd $build_dir
    pyxel package . "${example[file]}"
    pyxel app2html "${name}.pyxapp"
    popd
    mv "${build_dir}/${name}.html" docs/examples/play/
    #rm -r $build_dir
done