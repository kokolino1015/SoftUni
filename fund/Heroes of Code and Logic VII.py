class Heroes:
    def __init__(self):
        self.heroes = {}
        self.spins = int(input())
        self.adding_heroes()

    def adding_heroes(self):
        for i in range(self.spins):
            command = input().split(" ")
            heroes_name = command[0]
            hp = command[1]
            mp = command[2]
            self.heroes[heroes_name] = [heroes_name, hp, mp]
        self.solve()

    def solve(self):
        command = input()
        while not command == 'End':
            token = command.split(' - ')
            if token[0] == "Heal":
                self.heal(token[1], int(token[2]))
            elif token[0] == "CastSpell":
                self.cast_spell(token[1], int(token[2]), token[3])
            elif token[0] == "TakeDamage":
                self.take_damage(token[1], int(token[2]), token[3])
            elif token[0] == "Recharge":
                self.recharge(token[1], int(token[2]))
            command = input()
        self.print()

    def heal(self, hero_name, amount):
        value = self.heroes[hero_name]
        hp = int(value[1])
        health = 0
        new_hp = 0
        if hp + amount > 100:
            health += 100 - hp
            new_hp += 100
        elif hp + amount <= 100:
            health += amount
            new_hp += hp + amount
        self.heroes[hero_name] = [hero_name, new_hp, value[2]]
        print(f"{hero_name} healed for {health} HP!")
        self.solve()

    def cast_spell(self, hero_name, mp_needed, spell_name):
        value = self.heroes[hero_name]
        mp = int(value[2])
        if mp >= mp_needed:
            mp -= mp_needed
            self.heroes[hero_name] = [value[0], value[1], mp]
            print(f"{hero_name} has successfully cast {spell_name} and now has {mp} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        self.solve()

    def take_damage(self, hero_name, damage, attacker):
        value = self.heroes[hero_name]
        hp = int(value[1])
        if hp > damage:
            hp -= damage
            self.heroes[hero_name] = [hero_name, hp, value[2]]
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hp} HP left!")
        else:
            self.heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
        self.solve()

    def recharge(self, hero_name, amount):
        value = self.heroes[hero_name]
        mp = int(value[2])
        mp_gain = 0
        new_mp = 0
        if mp + amount > 200:
            mp_gain += 200 - mp
            new_mp += 200
        elif mp + amount <= 200:
            mp_gain += amount
            new_mp += mp + amount
        self.heroes[hero_name] = [hero_name, value[1], new_mp]
        print(f"{hero_name} recharged for {mp_gain} MP!")
        self.solve()

    def print(self):
        dictionary = sorted(self.heroes.values(), key=lambda x: (-int(x[1]), x[0]))
        for i in dictionary:
            print(f"{i[0]}\n HP: {i[1]}\n MP: {i[2]}")
        quit()


res = Heroes()
