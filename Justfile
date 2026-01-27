# List available recipes
default:
    @just --list

solve-py problem test_site="atcoder":
    #!/usr/bin/env bash

    readonly dir="{{ test_site }}/python/{{ problem }}"
    if [ ! -d "${dir}" ]; then
        echo "Error: Directory ${dir} does not exist."
        exit 1
    fi
    uv run "${dir}/test.py" < "${dir}/input.txt"
