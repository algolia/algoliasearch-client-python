#!/bin/bash

# treat website as independant yarn project
touch website/yarn.lock

DOCKER=true yarn cli build specs all -s 

# install website deps and build
cd website && yarn install && yarn build
