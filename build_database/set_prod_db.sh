#!/bin/bash

scp prod_database.db daniel@192.168.1.123:website-volume/database/database.db
rm prod_database.db