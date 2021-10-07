class Dinosaur:
    def __init__(self, name, attack_power, h_p):
        self.name = name
        self.attack_power = attack_power
        self.health = h_p
  
    def attack_damage():
        import random
        attack_power = random.randint(30, 60)
        return attack_power

    def attack(self, robot):
        robot.health -= self.attack_damage()
        print(f"you did damage")
        
        




    
    
