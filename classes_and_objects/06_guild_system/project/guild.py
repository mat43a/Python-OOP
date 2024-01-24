from typing import List

from project import player
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {self.name} is already in the guild."
        if player.guild != "Unffailited":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name in self.players:
            if player.name == player_name:
                self.players.remove(player_name)
                player.guild = "Unffailited"
                return f"Player {player_name} has been removed from the guild."
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        info = [f"Guild Name: {self.name}"]
        for player in self.players:
            info.append(player.player_info())
        return "\n".join(info)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
