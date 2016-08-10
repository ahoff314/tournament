# Clone the repo

`git clone https://github.com/ahoff314/tournament.git`

`cd \vagrant\tournament\`

# Make sure VirtualBox and Vagrant are installed

`vagrant up`

# Create Tournament Database

`psql`

`CREATE DATABASE tournament;`

# Import SQL Schema

`\i tournament.sql`

`\q` to exit

# Test

`python tournament_test.py`


