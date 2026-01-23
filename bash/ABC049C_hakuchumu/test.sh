read S
T=$(echo "$S" | grep -E '^(dreamer|eraser|dream|erase)+$')
if [[ "$S" == "$T" ]]; then echo "YES"; else echo "NO"; fi
