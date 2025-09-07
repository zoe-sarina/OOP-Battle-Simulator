import random
from enemy import Enemy

class ChatGPT(Enemy):
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.base_attack_power = 20 # base poer
        self.crit_hit_chance = 0.2 # 20% chance for a critical hit
        self.crit_multiplier = 2 # critical hits deal double the damage

        self.crit_hit_power = random.randint(1, 20)

    def attack(self):
        missing_health = 200 - self.health
        bonus = missing_health // 20 # plus 1 poer for every 20 missing health
        attack = self.base_attack_power + bonus
        # critical hit
        if random.random() < self.crit_hit_chance:
            attack *= self.crit_mulitplier
            print(f" Critical Hit by {self.name}!")

    def take_damage(self, damage):
        self.health -= damage
        self.health = max(0, self.health)
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
    


