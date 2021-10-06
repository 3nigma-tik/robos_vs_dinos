class Dinosaur:
    def __init__(self, name, attack_power, h_p):
        self.name = name
        self.attack_power = attack_power
        self.health = h_p
    def attack(self, robot):
        pass



dino_one = Dinosaur("Dr. Teeth", 55, 300)
dino_two = Dinosaur("Chucky Chomper", 40, 200)
dino_three = Dinosaur("Sally Spikes", 45, 500)
dino_four = Dinosaur("Doug", 25, 200)
    
    
print(dino_one.health)