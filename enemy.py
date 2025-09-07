import random

class Enemy:
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name):
        self.name = name
        self.health = 80
        self.attack_power = random.randint(5, 15)

    def attack(self):
        return random.randint(1, 8)

    def take_damage(self, damage):
        self.health -= damage
        # TODO We should prevent the goblins health from going into the NEGATIVE
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0