import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = random.randint(15, 20)      
    

    def strike(self):
        return random.randint(10, self.attack_power)
    
    def receive_damage(self, damage):
        reduced = int(damage * 0.75) # reduce damage by 25%
        self.health -= reduced
        if self.health < 0:
            self.health = 0
        print(f"\n{self.name} takes {reduced} damage (reduced from {damage}). Health is now {self.health}.")
    def is_alive(self):
        return self.health > 0
    
