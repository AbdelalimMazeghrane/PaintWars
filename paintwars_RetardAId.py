# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: David Lin 21131699
#  Prénom Nom: Nabil Battata 28727210

def get_team_name():
    return "RetardAId"

def step(robotId, sensors):
    import random
    rotation = 0
    translation = 1
   
   # comportement éviter obstacles
    if sensors["sensor_front_right"]["distance"] == sensors["sensor_front_left"]["distance"] and sensors["sensor_front_right"]["distance"] != 1:
        rotation = 1
    elif sensors["sensor_front_right"]["isRobot"] == False and sensors["sensor_front_right"]["distance"] != 1:
        rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]
    elif sensors["sensor_front_left"]["isRobot"] == False and sensors["sensor_front_left"]["distance"] != 1:
        rotation = (1) * sensors["sensor_front_right"]["distance"] + (-1) * sensors["sensor_front_left"]["distance"]
    elif sensors["sensor_front"]["isRobot"] == False and sensors["sensor_front"]["distance"] != 1:
        rotation = random.choice([-0.1, 0.1])

    # comportement éviter robot allié
    elif sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["distance"] != 1 and sensors["sensor_front_right"]["isSameTeam"] == True:
        rotation = (-1) * sensors["sensor_front_left"]["distance"] + (1) * sensors["sensor_front_right"]["distance"]
    elif sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["distance"] != 1 and sensors["sensor_front_left"]["isSameTeam"] == True:
        rotation = (1) * sensors["sensor_front_right"]["distance"] + (-1) * sensors["sensor_front_left"]["distance"]
    elif sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["distance"] != 1 and sensors["sensor_front_left"]["isSameTeam"] == True:
        rotation = -1 if robotId % 2 == 0 else 1

    # comportement perdre robot ennemi
    elif (sensors["sensor_back"]["isRobot"] and sensors["sensor_back"]["isSameTeam"] == False) or (sensors["sensor_back_right"]["isRobot"] and sensors["sensor_back_right"]["isSameTeam"] == False):
        rotation = -1
    elif (sensors["sensor_back_left"]["isRobot"] and sensors["sensor_back_left"]["isSameTeam"] == False):
        rotation = 1

    elif (robotId%8) in [0, 1, 2, 3, 4, 5, 6, 7]:

        # comportement suivre robot ennemi
        if (robotId%8) in [1, 2, 5, 6]:
            if (sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False and sensors["sensor_front_right"]["distance"] != 1) or (sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False and sensors["sensor_front_left"]["distance"] != 1):
                rotation = (-1) * sensors["sensor_front_right"]["distance"] + (1) * sensors["sensor_front_left"]["distance"]
        
        # comportement éviter robot ennemi
        if (robotId%8) not in [1, 2, 5, 6]:
            if any(sensors[key]["isRobot"] for key in ["sensor_front", "sensor_front_left", "sensor_front_right"]):
                if any(sensors[key]["isSameTeam"] == False for key in ["sensor_front", "sensor_front_left", "sensor_front_right"]):
                    if (sensors["sensor_front"]["distance"]!=1) or (sensors["sensor_front_right"]["distance"]!=1) or (sensors["sensor_front_left"]["distance"]!=1):
                        rotation = -1 if robotId % 2 == 0 else 1
        
        # comportement suivre mur
        if (robotId%8) in [0, 7]:
            if (sensors["sensor_right"]["isRobot"] == False and sensors["sensor_right"]["distance"] != 1):
                if (random.randint(1, 100) <= 5):
                    rotation = -1
                else:
                    rotation = 0.5
            elif (sensors["sensor_left"]["isRobot"] == False and sensors["sensor_left"]["distance"] != 1):
                if (random.randint(1, 100) <= 5):
                    rotation = 1
                else:
                    rotation = -0.5

    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))

    return translation, rotation
