#!/bin/bash

printf "Using local context...\n"
docker context use default

printf "\nBuilding images with no cache...\n"
# docker compose build --no-cache
docker compose build

printf "\nPushing images...\n"
docker compose push

printf "\nSwitching context to dadaserver...\n"
docker context use dadaserver

printf "\nRemoving old containers...\n"
while ! docker compose down
do
  printf "\nRemoving failed, trying again...\n"
done

printf "\nPulling images...\n"
while ! docker compose pull
do
  printf "\Pulling failed, trying again...\n"
done

printf "\nWARNING: About to start new container. If you need to modifiy the production database, do it NOW!\n"
printf "Press enter when ready to continue:\n"
read

printf "\nStarting containers...\n"
docker compose up -d

printf "\nResetting context...\n"
docker context use default

printf "\nDone!\n"