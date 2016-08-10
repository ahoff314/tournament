#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("TRUNCATE TABLE matches RESTART IDENTITY;")
    DB.commit()
    DB.close()


def deletePlayers():
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("TRUNCATE TABLE players RESTART IDENTITY CASCADE;")  # cascades to matches table first, restarts id at 1
    DB.commit()
    DB.close()


def countPlayers():
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("SELECT count(*)from players as player_count;")
    player_count = c.fetchone()[0]
    DB.close()
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("SELECT * from standings;")
    matches = c.fetchall()
    DB.close()
    return matches


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("INSERT INTO matches (id, winner, loser) VALUES (default, %s, %s);", (winner, loser))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("SELECT id, name FROM standings ORDER BY total_matches desc;")
    standings = c.fetchall()
    DB.close()

    if len(standings) % 2 == 0:
        i = 0
        pair = []
        while i < len(standings):
            player1_id = standings[i][0]
            player1_name = standings[i][1]
            player2_id = standings[i + 1][0]
            player2_name = standings[i + 1][1]
            pair.append((player1_id, player1_name, player2_id, player2_name))
            i += 2

        return pair
    else:
        print "Odd number of players in the Sherman Oaks Open 2016!"
