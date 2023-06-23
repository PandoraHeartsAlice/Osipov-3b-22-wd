class Character:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        damage_taken = damage - self.defense
        if damage_taken > 0:
            self.health -= damage_taken

    def attack_enemy(self, enemy):
        damage_dealt = self.attack - enemy.defense
        if damage_dealt > 0:
            enemy.take_damage(damage_dealt)


character1 = Character("Character 1", 10, 150, 20, 10)
character2 = Character("Character 2", 15, 150, 15, 5)

for i in range(3):
    print(f"Round {i+1}:")
    print(f"{character1.name} attacks {character2.name}")
    character1.attack_enemy(character2)
    print(f"{character2.name} has left {character2.health} health")
    print(f"{character2.name} attacks {character1.name}")
    character2.attack_enemy(character1)
    print(f"{character1.name} has left {character1.health} health")

if character1.health > character2.health:
    print(f"{character1.name} won!")
elif character2.health > character1.health:
    print(f"{character2.name} won!")
else:
    print("Draw!")
