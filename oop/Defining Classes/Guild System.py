class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for key, val in self.skills.items():
            result += f'==={key} – {val}\n'
        return result


class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player not in self.list_of_players and player.guild == "Unaffiliated":
            self.list_of_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"
        elif player in self.list_of_players:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player):
        if player in self.list_of_players:
            player.guild = "Unaffiliated"
            self.list_of_players.remove(player)
            return f"Player {player.name} has been removed from the guild."
        return f"Player {player.name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {guild.name}\n"
        for p in self.list_of_players:
            result += p.player_info()
        return result


