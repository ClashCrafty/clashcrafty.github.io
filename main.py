# import modules
import numpy as np
import math
from PIL import Image

# imports fichiers
import perlinNoise as pn
import coloration_deco as cd
import detourage_principal


# taille de l'image
size = 512

def generation_ile(size, i = 0):

    if math.log2(size).is_integer() ==  False:

        # si la taille n'est pas une puissance de 2
        # elle est arrondi a la puissance de 2 superieur

        size = 2**(math.ceil(math.log2(size)))

        print("========================================")
        print("Attention: ")
        print("votre taille n'est pas une puissance de 2 et a donc ete augmente a", size)
        print("========================================")


    seed = pn.r_seed(size) # creation d'une seed
    noise = pn.perlin_noise(size, seed, 9, 2, out = 1) # creation du bruit de perlin
    print("bruit de perlin cree")

    noise = np.array(noise).reshape(size, size) # transformation de la liste du bruit en matrice

    # contraste du bruit
    min_p = np.amin(noise) 
    max_p = np.amax(noise)

    noise = [[(i - min_p) / (max_p - min_p) for i in j] for j in noise]

    image, image_det = Image.new(mode = "RGB", size = (size, size)), Image.new(mode = "RGB", size = (size, size))

    image = cd.coloration(noise)

    noise = detourage_principal.detourage(noise)

    image_det = cd.coloration(noise)

    # image.save("image/ile_initial{i}.png".format(i = i))

    return image, image_det
