from django.db import models

# Create your models here.


class Seasons(models.Model):
    year = models.IntegerField(max_length=4)


class Users(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    wins = models.IntegerField()
    losses = models.IntegerField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Games(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    winning_p1 = models.CharField(max_length=255)
    winning_p2 = models.CharField(max_length=255)
    lossing_p1 = models.CharField(max_length=255)
    lossing_p2 = models.CharField(max_length=255)
    lossing_score = models.IntegerField()
    season = models.IntegerField()
    windspeed = models.IntegerField()


class Groups(models.Model):
    player = models.CharField(max_length=255)

# CREATE TABLE "seasons"(
#     "season_id" INTEGER NULL,
#     "year" INTEGER NOT NULL,
#     "season_name" VARCHAR(255) NOT NULL
# );
# ALTER TABLE
#     "seasons" ADD PRIMARY KEY("season_id");
# CREATE TABLE "players"(
#     "player_id" INTEGER NULL,
#     "player_name" VARCHAR(255) NOT NULL,
#     "wins" INTEGER NOT NULL,
#     "loses" INTEGER NOT NULL,
#     "username" VARCHAR(255) NOT NULL,
#     "password" VARCHAR(255) NOT NULL,
#     "email" VARCHAR(255) NOT NULL
# );
# ALTER TABLE
#     "players" ADD PRIMARY KEY("player_id");
# CREATE TABLE "games"(
#     "game_id" INTEGER NULL,
#     "date" DATE NOT NULL,
#     "winning_P1" INTEGER NULL,
#     "winning_P2" INTEGER NULL,
#     "losing_P1" INTEGER NULL,
#     "losing_P2" INTEGER NULL,
#     "winning_score" INTEGER NOT NULL,
#     "losing_score" INTEGER NOT NULL,
#     "season_id" INTEGER NULL,
#     "windspeed" INTEGER NOT NULL
# );
# ALTER TABLE
#     "games" ADD PRIMARY KEY("game_id");
# CREATE TABLE "Groups"("group_id" INTEGER NULL);
# ALTER TABLE
#     "Groups" ADD PRIMARY KEY("group_id");
# ALTER TABLE
#     "games" ADD CONSTRAINT "games_winning_p2_foreign" FOREIGN KEY("winning_P2") REFERENCES "players"("player_id");
# ALTER TABLE
#     "games" ADD CONSTRAINT "games_winning_p1_foreign" FOREIGN KEY("winning_P1") REFERENCES "players"("player_id");
# ALTER TABLE
#     "games" ADD CONSTRAINT "games_season_id_foreign" FOREIGN KEY("season_id") REFERENCES "seasons"("season_id");
# ALTER TABLE
#     "games" ADD CONSTRAINT "games_losing_p1_foreign" FOREIGN KEY("losing_P1") REFERENCES "players"("player_id");
# ALTER TABLE
#     "games" ADD CONSTRAINT "games_losing_p2_foreign" FOREIGN KEY("losing_P2") REFERENCES "players"("player_id");
# ALTER TABLE
#     "players" ADD CONSTRAINT "players_player_id_foreign" FOREIGN KEY("player_id") REFERENCES "Groups"("group_id");
