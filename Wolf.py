class Animal :
    def __init__(self, energy, position):
        self.energy = energy
        self.pos = position
        self.age = 0
    
    def upgrade_energy(self):
        self.age += 1
        self.energy -= 1


class Wolf(Animal) :
    def move(self):
        s = get_sheep()
        if s!= (0,0,0,0):
            M = s[0]
            i_max=0
            for i in range(1, 4):
                if s[i]>M:
                    M = s[i]
                    i_max = i
                elif s[i]==M:
                    i_max = rd.choice(i_max, i)
            if i_max==0:
                self.pos[1]+=1
            elif i_max==1:
                self.pos[1]-=1
            elif i_max==2:
                self.pos[0]-=1
            elif i_max==3:
                self.pos[0]+=1
            #(top, down, left, right)
            #grass[i]=-inf si hors de la map
        else :
            if self.pos[0] == 0 :
                n = rd.randint(1,3)
            elif self.pos[0] == 49 :
                n = rd.choice([0,2,3])
            elif self.pos[1] == 0 :
                n = rd.choice([0,1,3])
            elif self.pos[1] == 49 :
                n = rd.randint(0, 2)
            else :
                n = rd.randint(0, 3)
            if n==0:
                if self.pos[0]<dim-1:
                    self.pos[1]+=1
            elif n==1:
                if self.pos[0]>0:
                    self.pos[1]-=1
            elif n==2:
                if self.pos[1]>0:
                    self.pos[0]-=1
            elif n==3:
                if self.pos[1]<dim-1:
                    self.pos[0]+=1