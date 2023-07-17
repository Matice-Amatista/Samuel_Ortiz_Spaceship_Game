from game.components.enemies.enemy import Enemy

from game.components.enemies.enemy2 import Enemy2

from random import randint



class EnemyManager:
    def __init__(self):   
        self.enemies =[]

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self,screen):
        for enemy in self.enemies:
            enemy.draw(screen)


    def add_enemy(self):
        r = randint(0,1)
        if r >= 0.5 and len(self.enemies) < 2:
            enemy = Enemy()
            self.enemies.append(enemy)
        if r < 0.5 and len(self.enemies) < 2:
            enemy = Enemy2()
            self.enemies.append(enemy)


        print(len(self.enemies))