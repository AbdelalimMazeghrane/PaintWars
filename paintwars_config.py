# Nicolas
# 2021-03-31

# Arena
import paintwars_arena_G3
get_arena = paintwars_arena_G3.get_arena
arenaIndexSelector = 1 # numéro de l'arène, entre 0 et 4

# Starting position
invertStartingPosition = False # True: red commence à gauche. Sinon, commence à droite.

# Red team
import paintwars_team_sara # importer votre code
get_name_red_team = paintwars_team_sara.get_team_name # mettre ici votre fonction get_team_name
step_red_team = paintwars_team_sara.step # mettre ici votre fonction step

# Blue team
import paintwars_team_Elyes_Abdou
get_name_blue_team = paintwars_team_Elyes_Abdou.get_team_name
step_blue_team = paintwars_team_Elyes_Abdou.step

# Simulation mode: realtime=0, fast=1, super_fast_no_render=2
simulation_mode = 0
