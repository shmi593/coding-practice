#!/bin/bash

# match
all_keys=$(cat input.json | jq -r '.[].key' | sort)

pattern="192.168.1.1"
matched_keys=$(cat input.json | jq --arg pattern "${pattern}" '.[] | select(.value[] // empty | test($pattern)) ' | jq -r '.key' | sort)

diff_keys=$(diff -y --suppress-common-lines <(cat <<< "${all_keys}") <(cat <<< "${matched_keys}") | cut -c 1)

cat <<< "${diff_keys}" | xargs -I {} echo "diff is {}."