# SHERMAN OAKS OPEN 2016

## Clone the repo

`git clone https://github.com/ahoff314/tournament.git golf`

`cd golf`

## Make sure VirtualBox and Vagrant are installed

`vagrant up`

`vagrant ssh`

## Navigate to tournament database

`psql tournament`

`\q` to exit

## Or create the database if necessary

`psql`

`CREATE DATABASE tournament;`

`\i tournament.sql`

## Test

`cd tournament`

`python tournament_test.py`


