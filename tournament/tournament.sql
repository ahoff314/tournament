
CREATE TABLE players (id SERIAL primary key,
                      name TEXT);

CREATE TABLE matches (id SERIAL primary key,
                     winner INTEGER references players(id),
                     loser INTEGER references players(id));

-- creates standings view (name, id, wins, total matches)
CREATE VIEW standings AS
SELECT  players.id, players.name,
(SELECT count(matches.winner) FROM matches WHERE players.id = matches.winner) AS wins,
(SELECT count(matches.id) FROM matches WHERE players.id = matches.winner OR players.id = matches.loser) as total_matches
FROM players ORDER BY wins DESC, total_matches DESC;

