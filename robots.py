from weapons import Weapon

class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapons = Weapon(weapon[0])
        return 

    
    def attack_damage():
        import random
        attack_power = random.randint(30, 60)
        return attack_power

    
    def attack(self, dinosaur):
        dinosaur.health -= self.attack_damage()
        print(f"you did damage")





   
