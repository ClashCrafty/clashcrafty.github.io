from faker import Faker
from PIL import Image, ImageDraw
import random as rd

import numpy as np
import json

#coloration_type = input("type de l'île :")

def coloration(noise, h = 0, coloration_type = "continentale"):
    
    size = len(noise)
    image = Image.new(mode = "RGB", size = (size, size))
    h = h / 100

    fake = Faker()

    deep_sea = (58, 95, 205)
    sea = (24, 116, 205)
    shallow = (0, 154, 205)

    if coloration_type == "continentale":
        couleur_4 = (240, 210, 172)
        couleur_5 = (34, 139 , 34)
        couleur_6 = (0, 128, 0)
        couleur_7 = (0, 100, 0)
        couleur_8 = (140, 140, 140)
        couleur_9 = (130, 130, 130)
        couleur_10 = (250, 250, 250)
        habitation = (94, 38, 18)
    
    elif coloration_type == "iceberg":
        couleur_4 = (240, 255, 255)
        couleur_5 = (240, 255, 255)
        couleur_6 = (240, 255, 255)
        couleur_7 = (240, 255, 255)
        couleur_8 = (240, 255, 255)
        couleur_9 = (240, 255, 255)
        couleur_10 = (240, 255, 255)
        habitation = (193, 205, 205)

    elif coloration_type == "volcanique":
        couleur_4 = (99, 99, 99)
        couleur_5 = (97, 97, 97)
        couleur_6 = (94, 94, 94)
        couleur_7 = (92, 92, 92)
        couleur_8 = (89, 89, 89)
        couleur_9 = (128, 0, 0) # lave 1
        couleur_10 = (238, 0, 0) # lave 2
        habitation = (132, 132, 132)

    print("ajout couleur")

    for i in range(size):
        habitation_formation = rd.randint(1, 60)   #probabilité d'avoir une habitation

        for j in range(size):
            noise_value = (noise[i][j]) # je met le contraste max pour avoir tt les couleurs
            if noise_value < 0.2 - h:
                image.putpixel((i, j), deep_sea)
            elif noise_value < 0.32 - h:
                image.putpixel((i, j), sea)
            elif noise_value < 0.5 - h:
                image.putpixel((i, j), shallow)
            elif noise_value < 0.55 - h:
                image.putpixel((i, j), couleur_4) # entre .5 et .55

            elif noise_value < 0.6 - h:
                image.putpixel((i, j), couleur_5) # entre .55 et .6
                if 0.585 - h < noise_value < 0.59 - h and habitation_formation == 1:   # ajout d'habitations
                    image.putpixel((i, j), habitation)

            elif noise_value < 0.65 - h:
                image.putpixel((i, j), couleur_6)
            elif noise_value < 0.75 - h:
                image.putpixel((i, j), couleur_7)
            elif noise_value < 0.85 - h:
                image.putpixel((i, j), couleur_8)
            elif noise_value < 0.9 - h:
                image.putpixel((i, j), couleur_9)
            else:
                image.putpixel((i, j), couleur_10)

    print("couleur ajoutée")

    text = fake.local_latlng(country_code = 'NO')
    draw = ImageDraw.Draw(image)
    draw.text((50, 50), "lat: {lat}; long: {long}; nom: {nom}; pays: {pays}".format(lat = text[0], long = text[1], nom = text[2], pays = text[3]), fill = (255, 255, 255))

    return image