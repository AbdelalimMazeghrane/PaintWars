# Projet "robotique" IA&Jeux 2024
#
# Binome:
#  Prénom Nom: Bourenane Mohamed Elyes
#  Prénom Nom: Abdou Mazeghrane

def get_team_name():
    return "elyes_abdou" # à compléter (comme vous voulez)

def comportement_1(sensors):
  #### on evite tout obstacles ####
  if (sensors["sensor_front"]["distance"] < 0.2 or sensors["sensor_front_right"]["distance"] < 0.2 or sensors["sensor_front_left"]["distance"] < 0.2
      or sensors["sensor_left"]["distance"] < 0.1 or sensors["sensor_right"]["distance"] < 0.1):
    translation = 0.3
    if (min(sensors["sensor_front_left"]["distance"], sensors["sensor_left"]["distance"]) < min(sensors["sensor_front_right"]["distance"], sensors["sensor_right"]["distance"])):
      rotation = 0.15
    else:
      rotation = -0.15

  ####  si un robot ennemi   nous suit on recule pour s'en debarasser ####
  elif ((sensors["sensor_back"]["isRobot"] and not sensors["sensor_back"]["isSameTeam"]) or (sensors["sensor_back_left"]["isRobot"] and not sensors["sensor_back_left"]["isSameTeam"])
        or (sensors["sensor_back_right"]["isRobot"] and not sensors["sensor_back_right"]["isSameTeam"])):

      translation = -1
      rotation = (1) * sensors["sensor_back_left"]["distance"] + (-1) * sensors["sensor_back_right"]["distance"]


  #### suivre les robots ennemis ####
  elif ((sensors["sensor_front"]["isRobot"] and not sensors["sensor_front"]["isSameTeam"]) or 
        (sensors["sensor_front_left"]["isRobot"] and not sensors["sensor_front_left"]["isSameTeam"]) or 
        (sensors["sensor_front_right"]["isRobot"] and not sensors["sensor_front_right"]["isSameTeam"]) or 
        (sensors["sensor_left"]["isRobot"] and not sensors["sensor_left"]["isSameTeam"]) or
        (sensors["sensor_right"]["isRobot"] and not sensors["sensor_right"]["isSameTeam"])):

    translation = 1
    rotation = (1) * min(sensors["sensor_front_left"]["distance"], sensors["sensor_left"]["distance"]) + (-1) * min(sensors["sensor_front_right"]["distance"], sensors["sensor_right"]["distance"])

  #### on avance et on evite les obstacless ####
  else:

    translation = 1 * sensors["sensor_front"]["distance"]
    rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]

  return (translation, rotation)




def comportement_2(sensors):

  #### on evite les robots qui sont devant nous ####
  if ((sensors["sensor_front"]["isRobot"]) or (sensors["sensor_front_right"]["isRobot"]) or (sensors["sensor_front_left"]["isRobot"])):
    translation = 1
    if (sensors["sensor_front_left"]["distance"] < sensors["sensor_front_right"]["distance"]):
        rotation = 1
    else:
        rotation = -1
  ####  si un robot ennemi   nous suit on recule pour s'en debarasser ####
  elif ((sensors["sensor_back"]["isRobot"] and not sensors["sensor_back"]["isSameTeam"]) or (sensors["sensor_back_left"]["isRobot"] and not sensors["sensor_back_left"]["isSameTeam"])or (sensors["sensor_back_right"]["isRobot"] and not sensors["sensor_back_right"]["isSameTeam"])):


          translation = -1
          rotation = (1) * sensors["sensor_back_left"]["distance"] + (-1) * sensors["sensor_back_right"]["distance"]


  else:

    #### Si il y a un obstable vers l'avant, on l'evite et on se dirige vers un mur #### 
    if (sensors["sensor_front"]["distance"] < 0.3 or sensors["sensor_front_right"]["distance"] < 0.2 or sensors["sensor_front_left"]["distance"] < 0.2 ):
      translation = 0.6
      rotation = 0.3

    #### Sinon si il y a un trou dans le mur, on rentre ####
    elif (sensors["sensor_front_left"]["distance"] == 1 and sensors["sensor_left"]["distance"] == 1 and sensors["sensor_back_left"]["distance"] < 1):
        translation = 0.40
        rotation = -1

    #### on rapproche du mur ####
    elif (((sensors["sensor_left"]["distance"] < 1 ) and (sensors["sensor_left"]["distance"] > 0.35 ) ) or ((sensors["sensor_front_left"]["distance"] < 1 ) and (sensors["sensor_front_left"]["distance"] > 0.45 )) and ((sensors["sensor_back_left"]["distance"] < 1 ) or (sensors["sensor_back_left"]["distance"] > 0.45 ))  ): # trop loin du mur (tourne à gauche, car mur à gauche)
      translation = 1
      rotation = -0.3

    #### si on est trop proche du mur on s'eloigne ####
    elif (sensors["sensor_left"]["distance"] < 0.2  ):  # trop proche du mur (tourne à droite, car mur à gauche)
      translation = 1
      rotation =  0.15	

    #### on tente de trouver un mur ####
    else:
      translation = 1
      rotation = 0

  return translation, rotation




iterations = 0
def step(robotId, sensors):
    global iterations
    if iterations < 1500:
        if (robotId % 8 == 0):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 1):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 2):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 3):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 4):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 5):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 6):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 7):
            translation, rotation = comportement_2(sensors)
    else:
        if (robotId % 8 == 0):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 1):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 2):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 3):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 4):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 5):
            translation, rotation = comportement_1(sensors)
        elif (robotId % 8 == 6):
            translation, rotation = comportement_2(sensors)
        elif (robotId % 8 == 7):
            translation, rotation = comportement_2(sensors)
    
    iterations += 1
    return translation, rotation
        