#!/bin/bash

if [[ "$(uname)" == "Darwin" ]]; then
  sed_arg=('-i' '' '-e')
else
  sed_arg=('-i' '-e')
fi

for dir in packages/*/ ; do
  dir=${dir%/}
  version=$(grep "^version:" "${dir}/pubspec.yaml" | sed 's/version: //')
  sed "${sed_arg[@]}" "s/^const packageVersion = .*;$/const packageVersion = '$version';/" "${dir}/lib/src/version.dart";
done
