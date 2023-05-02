import random as rd
import matplotlib.pyplot as plt
import math

'''# nombre de "couche" de bruit 
octave = 12

# nombre de "detail" a chaque octave (couche)
persistence = 2

# taille de la map/image
scale = 100'''


def r_seed(lenth, r_max = 1):
    return [rd.random()/r_max for _ in range(lenth**2)]

 
def perlin_noise(size, seed, octaves, persistence, out = 2):

    # out = 1 -> return 1D array
    # out = 2 -> return 2D array

    if 2**(octaves - 1) > size:
        # si l'octave est trop grande
        # on la reduit a la taille max

        octaves = int(math.log2(size)) + 1
        print("========================================")
        print("Attention: ")
        print("votre octave est trop grande et a donc ete reduite a", octaves)
        print("========================================")


    output = [0 for _ in range(size**2)]

    for x in range(size):
        for y in range(size):

            noise = 0.0
            scale = 1.0 # importance du pixel a la couche actuelle
            scaleAcc = 0.0 # total de couche avec leur importance (1 + 1/2 + 1/4 + 1/8...) 

            for i in range(octaves):
                
                # pitch = distance entre les points
                # >> deplace les bits a droite : 0100 >> 1 = 0010
                pitch = size >> i

                sampleX1 = int(x / pitch) * pitch
                sampleY1 = int(y / pitch) * pitch

                sampleX2 = (sampleX1 + pitch) % size
                sampleY2 = (sampleY1 + pitch) % size

                # distance entre ce point et le point de reference
                blendX = (x - sampleX1) / pitch
                blendY = (y - sampleY1) / pitch

                # interpolation
                sampleT = (1.0 - blendX) * seed[sampleY1 * size + sampleX1] + blendX * seed[sampleY1 * size + sampleX2]
                sampleB = (1.0 - blendX) * seed[sampleY2 * size + sampleX1] + blendX * seed[sampleY2 * size + sampleX2]

                scaleAcc += scale
                noise += (blendY * (sampleB - sampleT) + sampleT) * scale
                scale = scale / persistence

            output[y * size + x] = noise / scaleAcc

    if out == 1:
        return output
    else:
        out = []
        
        for i in range(size):
            tempn = []
            for y in range(size):
                tempn.append(output[i*size + y])
            out.append(tempn)

        return out


