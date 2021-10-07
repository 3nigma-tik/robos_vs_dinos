from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        return 
    
    def create_herd(self):
        dino_one = Dinosaur("Chucky Chomper", 55, 300)
        dino_two = Dinosaur("Sally Spikes", 45, 500)
        dino_three = Dinosaur("Timmy Teeth", 50, 250)
        dino_four = Dinosaur("Doug", 30, 250)
        return dino_one and dino_two and dino_three and dino_four
    