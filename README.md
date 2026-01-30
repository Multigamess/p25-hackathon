# p25-hackathon
Pour lancer la simulation, il faut simplement run le fichier game-engine.py

Les paramètres réglables sont les suivants:
GRID_SIZE: la taille de la grille
PIXEL_SIZE: la taille des cases
INITIAL_SHEEPS: le nombre de moutons initial
INITIAL_WOLVES: le nombre de loup initial
INITIAL_GRASS_COVERAGE: pourcentage de recouvrement initial d'herbe
SHEEP_INITIAL_ENERGY: énergie initiale des moutons
WOLF_INITIAL_ENERGY: énergie initiale des loups
SHEEP_ENERGY_LOSS_PER_TURN: perte d'énergie par pas de simu pour les moutons
WOLF_ENERGY_LOSS_PER_TURN: perte d'énergie par pas de simu pour les loups
GRASS_REGROWTH_TIME: période de repousse de l'herbe

Les règles implémentées sont les suivantes:
-les moutons mangent de l'hebre pour gagner de l'énergie
-les moutons 