class Soldier:
    def __init__(self, level: int, name: str):
        self.level = level
        self.name = name

    def attack(self):
        return self.level * 1


class Jedi:
    def __init__(self, level: int):
        self.level = level

    def attackWithSaber(self):
        return self.level * 100


class JediAdapter:
    def __init__(self, jedi, name: str):
        self.jedi = jedi
        self.name = name

    def attack(self):
        return self.jedi.attackWithSaber()


class StarWarsGame:
    def __init__(self, character):
        self.character = character

    def fight_enemy(self):
        print(
            f'{self.character.name} caused {self.character.attack()} of damage to the enemy')


StarWarsGame(Soldier(5, 'Soldier')).fight_enemy()
StarWarsGame(JediAdapter(Jedi(20), 'Jedi')).fight_enemy()
