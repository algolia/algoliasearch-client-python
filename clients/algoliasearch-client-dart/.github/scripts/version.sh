#!/bin/bash

current_commit=$(git rev-parse HEAD)
previous_commit=$(git rev-parse HEAD^)

declare -A packages=(
  ["client_core"]="core"
  ["client_search"]="search"
  ["client_insights"]="insights"
  ["algoliasearch"]="algoliasearch"
)

git config --global user.email "accounts+algolia-api-client-bot@algolia.com"
git config --global user.name "algolia-bot"

for package_dir in "${!packages[@]}"; do
    tag_prefix="${packages[$package_dir]}"
    diff_output=$(git diff -U0 "$previous_commit" "$current_commit" -- packages/"$package_dir"/pubspec.yaml)
    if echo "$diff_output" | grep -q "^+version:"; then
        echo "Version was updated in $package_dir."
        new_version=$(echo "$diff_output" | grep "^+version:" | cut -d " " -f 2)
        echo "New version is: $new_version"
        echo "Creating new tag..."
        git tag "$tag_prefix-$new_version"
        git push origin "$tag_prefix-$new_version"
        echo "$tag_prefix=true" >> "$GITHUB_OUTPUT"
    else
        echo "Version was not updated in $package_dir."
    fi
done
