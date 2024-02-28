# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Oudam-dara LIM
#  Prénom Nom: Yonan KOH

def get_team_name():
    return "Wonderful ColorBlast" # à compléter (comme vous voulez)

def step(robotId, sensors):
    
    #Comportement par défaut(Sans obstacle)
    translation = 1  #Vitesse de translation initiale
    rotation = 0  #Vitesse de rotation initiale
	
    if robotId == 0:
        rotation = -0.05
    
    if robotId == 1:
        rotation = -0.025
    
    if robotId == 2:
        rotation = -0.005
     
    if robotId == 5:
    	rotation = 0.005
    
    if robotId == 6:
        rotation = 0.025
     
    if robotId == 7:
    	rotation = 0.05

    #Détection d'un robot adverse avec les capteurs frontaux et latéraux (Comportement suiveur)
    robot_in_front = (sensors["sensor_front"]["isRobot"] == True) and (sensors["sensor_front"]["isSameTeam"] == False)
    robot_on_left = sensors["sensor_left"]["isRobot"] and not sensors["sensor_left"]["isSameTeam"]
    robot_on_right = sensors["sensor_right"]["isRobot"] and not sensors["sensor_right"]["isSameTeam"]
    robot_behind = (sensors["sensor_back"]["isRobot"] == True) and (sensors["sensor_back"]["isSameTeam"] == False)
    robot_behind_left = sensors["sensor_back_left"]["isRobot"] and not sensors["sensor_back_left"]["isSameTeam"]
    robot_behind_right = sensors["sensor_back_right"]["isRobot"] and not sensors["sensor_back_right"]["isSameTeam"]
    robot_on_wall = (sensors["sensor_front"]["isRobot"] == False) and (sensors["sensor_front"]["isSameTeam"] == False)
    
    #Détection d'un robot adverse avec le capteur avant
    if robot_in_front:
        if sensors["sensor_front_left"]["distance"] < sensors["sensor_front_right"]["distance"]:
            rotation = -0.5 #Tourne à gauche
            #Si un robot obstacle est détecté
            if sensors["sensor_front_left"]["distance"] < 0.05:
                translation = -1
                rotation = 1
        else:
            rotation = 0.5 #Tourne à droite
            #Si un robot obstacle est détecté
            if sensors["sensor_front_right"]["distance"] < 0.05:
                translation = -1
                rotation = -1
            
    elif robot_on_left:
        #Si un robot est détecté à gauche uniquement, tourne légèrement à droite pour le suivre
        rotation = -1
        #Si un robot obstacle est détecté
        if sensors["sensor_left"]["distance"] < 0.05:
            translation = -1
            rotation = 1

    elif robot_on_right:
        #Si un robot est détecté à droite uniquement, tourne légèrement à gauche pour le suivre
        rotation = 1
        #Si un robot allié est détecté
        if sensors["sensor_right"]["distance"] < 0.05:
            translation = -1
            rotation = -1
        
    elif robot_behind:
        translation = 0.5  #Ralentir pour se rapprocher
        
        #Tourne pour se repositionner face au robot
        if robot_behind_left:
            rotation = 0.5
        else:
            rotation = -0.5  
    elif (robot_on_wall) and (robotId == 3) and (robotId == 4):
        if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
            rotation = 0.2  #Rotation vers la droite pour aller vers l'obstacle
        elif sensors["sensor_front_right"]["distance"] < 1:
            rotation = -0.2  #Rotation vers la gauche pour aller vers l'obstacle
        elif sensors["sensor_front"]["distance"] < 0.1:
            rotation = -0.5
        elif sensors["sensor_front_right"]["distance"] < 0.1:
            rotation = 0.5
        
    else:
        #Comportement normal(Evite obstacle) si aucun robot adverse n'est détecté devant
        if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1:
            rotation = 0.7  #Rotation vers la droite pour éviter l'obstacle
        elif sensors["sensor_front_right"]["distance"] < 1:
            rotation = -0.7  #Rotation vers la gauche pour éviter l'obstacle
        
       

    # limite les valeurs de sortie entre -1 et +1
    translation = max(-1,min(translation,1))
    rotation = max(-1, min(rotation, 1))

    return translation, rotation

    
