#!/bin/bash

## Wait for PostgreSQL to be up and running
#until pg_isready -h citus_coordinator -p 5433 -U example_user
#do
#  echo "Waiting for PostgreSQL to be ready..."
#  sleep 2
#done

# Add worker nodes to the coordinator
psql -h citus_coordinator -p 5433 -U example_user -d example_db -c "SELECT master_add_node('worker_1', 5432);"
psql -h citus_coordinator -p 5433 -U example_user -d example_db -c "SELECT master_add_node('worker_2', 5432);"
