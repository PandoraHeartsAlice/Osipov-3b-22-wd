class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self._level = level
        self._health = health
        self._attack = attack
        self._defense = defense

    def apply_damage(self, damage):
        self._health -= damage

    def level_up(self):
        self._level += 1
        self._health *= 1.1
        self._attack *= 1.1

    def print_stats(self):
        print(f"Name: {self.name}")
        print(f"Level: {self._level}")
        print(f"Health: {self._health}")
        print(f"Attack: {self._attack}")
        print(f"Defense: {self._defense}")


character = Character("Character", 5, 100, 10, 5)
character.print_stats()
character.level_up()
character.print_stats()
