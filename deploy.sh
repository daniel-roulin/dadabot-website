#!/bin/bash

printf "Using local context...\n"
docker context use default

printf "\nBuilding images...\n"
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

printf "\nPulling frontend...\n"
while ! docker compose pull frontend
do
  printf "Pulling frontend failed, trying again...\n"
done
printf "\nPulling backend...\n"
while ! docker compose pull backend
do
  printf "Pulling backend failed, trying again...\n"
done
printf "\nPulling proxy...\n"
while ! docker compose pull proxy
do
  printf "Pulling proxy failed, trying again...\n"
done

printf "\nWARNING: About to start new containers. If you need to modifiy the production database, do it NOW!\n"
printf "Press enter when ready to continue:\n"
read

printf "\nStarting containers...\n"
docker compose up -d

printf "\nResetting context...\n"
docker context use default

printf "\nDone!\n"