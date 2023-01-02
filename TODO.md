- Workflow to build containers locally and push them to dadabot
=> How to work with docker compose file

DO NOT FORGET TO RENAME images: IN DOCkER-COMPOSE.YML => Use docker hub id.

Worflow:
local context:
- docker-compose build
- docker-compose push

server context:
- docker compose pull
- docker compose up

(switch back context)