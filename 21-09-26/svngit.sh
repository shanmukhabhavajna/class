#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: bash svngit.sh <filename>"
    exit 1
fi

FILE="$1"
COMMIT_MSG="${2:-Update $FILE}"

git add "$FILE"
git commit -m "$COMMIT_MSG"
git push

REPO_URL=$(git config --get remote.origin.url | sed 's/\.git$//')
BRANCH=$(git branch --show-current)
PREFIX=$(git rev-parse --show-prefix)

echo "=================================================="
echo "Direct Link:"
echo "${REPO_URL}/blob/${BRANCH}/${PREFIX}${FILE}"
echo "=================================================="
