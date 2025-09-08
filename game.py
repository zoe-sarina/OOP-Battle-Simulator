import random
from goblin import Goblin
from hero import Hero
from robot import ChatGPT

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Bruce Wayne")
    

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "blue") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    total_damage = 0
    rounds = 0

    # Battle Loop and Phase 1: Goblin Fight
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        rounds += 1
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)
        total_damage += damage

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
                total_damage += damage

    # Determine outcome of goblin fight
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
        # Final tally of goblins defeated
        print(f"\nTotal damage dealt: {total_damage}")
        print(f"Total rounds fought: {rounds}")
        print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
        return # ends game is hero is dead

    # after goblins are defeated but before boss fight
    hero.health = min(hero.health + 50, 150)
    print(f"\n{hero.name} recovers 50 health before the boss fight! Current health: {hero.health} 🩹") 

    # PHASE 2: Boss Fight
    print("\n Boss Fight Time!")
    boss = ChatGPT("Bob")
    print(f"\n Boss {boss.name} enters the battlefield with {boss.health} health! 😨")


    while hero.is_alive() and boss.is_alive():
        print("\n--- Boss Battle Round ---")

        # hero attacks boss
        damage = hero.strike()
        print(f"\nHero attacks {boss.name} for {damage} damage!")
        boss.take_damage(damage)
        total_damage += damage

        # boss attacks hero if still alive
        if boss.is_alive():
            damage = boss.attack()
            print(f"\n{boss.name} attacks hero for {damage} damage!")
            hero.receive_damage(damage)
            total_damage += damage

    # outcome of boss fight
    if hero.is_alive():
        print(f"\n The hero has defeated the boss {boss.name} and won the game!🏆")
    else:
        print(f"\n The hero was defeated by {boss.name}. Game Over. ☠️")
   
    # Final tally 
    print(f"\nTotal damage dealt: {total_damage}")
    print(f"Total rounds fought: {rounds}")
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
