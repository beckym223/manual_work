#!/bin/bash

CURRENT_BRANCH=$(git branch --show-current)

# Generate a unique branch name
BRANCH_NAME="pipeline-run-$(date +'%Y%m%d%H%M%S')"

# Create and switch to the new branch, setting the upstream to the current branch
git checkout -b "$BRANCH_NAME" --track "$CURRENT_BRANCH"
