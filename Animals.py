
class Animal :
    def __init__(self, energy, position):
        self.energy = energy
        self.pos = position
        self.age = 0
        self.compteur = 0
    
    def upgrade_energy(self):
        self.compteur += 1

        if (self.compteur == 20 or self.compteur == 40) and self.age < 3:
            self.age += 1
        
        if self.compteur == 20:
            self.energy -= 10
    
    def move(self, target):
        target_near = is_target_near()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        if target_near != (0, 0, 0, 0):
            m = max(target_near)
            indices_max = [i for i, val in enumerate(target_near) if val == m]
            n = rd.choice(indices_max)
        else:
            possibles = []
            if self.pos[1] < 49: possibles.append(0) # Top
            if self.pos[1] > 0:  possibles.append(1) # Down
            if self.pos[0] > 0:  possibles.append(2) # Left
            if self.pos[0] < 49: possibles.append(3) # Right
            n = rd.choice(possibles)

        # Application du mouvement
        dx, dy = directions[n]
        self.pos[1] += dy
        self.pos[0] += dx

class Sheep(Animal):

    def eat_grass(self, grass):
        self.energy += grass.age * 10
        grass.ate()
    
    def move_wolf(self):
        super().move('grass')
    
    def sheep_ate(self):
        pass

class Wolf(Animal) :
    
    def eat_sheep(self):
        self.energy += 10
    
    def move_wolf(self):
        super().move('sheep')