#  ...
#  .#.
#  ...

# tout

import numpy as np

def ile(noise):
    size = len(noise)



    # hauteur max sur les cotes
    valeur_max = 0
    for i in range(size):
        if noise[i][0] > valeur_max:
            valeur_max = noise[i][0]
        if noise[i][-1] > valeur_max:
            valeur_max = noise[i][size-1]
        if noise[0][i] > valeur_max:
            valeur_max = noise[0][i]
        if noise[-1][i] > valeur_max:
            valeur_max = noise[-1][i]

    x = size/((-size/2 ) / ((0.5/valeur_max)-1))

    if x < 0.85:
        x = 0.85

    cercle1 = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            cercle1[i][j] = (1- (((i-size/2)**2 + (j-size/2)**2)**0.5 / (size/x)))

    cercle2 = np.zeros((size,size))

    for i in range(size):
        for j in range(size):
            distanceToCenter = ((i-size/2)**2 + (j-(size/2+50))**2)**0.5
    
            if distanceToCenter <= size//4:
                cercle2[i][j] = 1 - ((distanceToCenter / (size//4)))
    
    cercle3 = np.zeros((size,size))

    for i in range(size):
        for j in range(size):
            cercle3[i][j] = cercle1[i][j] if cercle1[i][j] > cercle2[i][j] else cercle2[i][j]
    
    noise = noise * cercle3
 
   
    return(noise)


#  ...
#  ###
#  ...

def detour_droite(noise):
    size = len(noise)

    # max contrast
    min_p = np.amin(noise)
    max_p = np.amax(noise)

    noise = [[(i - min_p) / (max_p - min_p) for i in j] for j in noise]
    noise = [[i if i >= 0.5 else i-0.1 * (1 - i + .03) for i in j] for j in noise]
    print("noise contrasted")


    cercle = []
    for i in range(size):
        for j in range(size):
            cercle.append(1 - ((i-size/2)**2 + (j-size/2)**2)**0.5 / (size/2))

    cercle = [i if i >= 0.5 else i-0.15 for i in cercle]

    cercle = np.array(cercle).reshape(size, size)

    print("cercle created and contrasted")

    # deplace de size//2 vers le haut
    rotate_noise180 = np.roll(noise, size//2, axis=1)
    # tourne de 180° (symetrie centrale)
    rotate_noise180 = np.rot90(rotate_noise180, 2)

    print("noise rotated 180°")
    
    # create rotate_noise from noise
    rotate_noise90 = np.rot90(noise, 1)

    '''    
    fig, ax = plt.subplots(1, 4)
    ax[0].imshow(noise, cmap='gray')
    ax[1].imshow(rotate_noise90, cmap='gray')
    ax[2].imshow(rotate_noise180, cmap='gray')
    ax[3].imshow(cercle, cmap='gray')
    plt.show()
    '''
    
    av_noise = np.zeros((size, size))

    # moyenne des 4 images
    for i in range(size):
        for j in range(size):
            av_noise[i][j] = (noise[i][j] * 0.6 + rotate_noise180[i][j] * 0.4 + rotate_noise90[i][j] * 1.06) /2.06 #  + cercle[i][j] * 0.25) / 2.31


    # hauteur max sur les cotes
    valeur_max = 0
    for i in range(size):
        if av_noise[i][0] > valeur_max:
            valeur_max = av_noise[i][0]
        if av_noise[i][-1] > valeur_max:
            valeur_max = av_noise[i][size-1]
        if av_noise[0][i] > valeur_max:
            valeur_max = av_noise[0][i]
        if av_noise[-1][i] > valeur_max:
            valeur_max = av_noise[-1][i]

    x = size/((-size/2 ) / ((0.5/valeur_max)-1))

    if x < 0.85:
        x = 0.85

    cercle1 = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            cercle1[i][j] = (1- (((i-size/2)**2 + (j-size/2)**2)**0.5 / (size/x)))
    
    cercle2 = np.zeros((size,size))
    
    for i in range(size):
        for j in range(size):
            distanceToCenter = ((i-(size/3))**2 + (j-(size/3))**2)**0.5
            if distanceToCenter <= size//2: 
                cercle2[i][j] = 1 - ((distanceToCenter / (size//1.5))) # taille

    cercle3 = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            cercle3[i][j] = cercle1[i][j] if cercle1[i][j] > cercle2[i][j] else cercle2[i][j]

    av_noise = av_noise * cercle3

    return(av_noise)


#  #.#
#  ###
#  #'#

def detour_double_c(noise):
    size = len(noise)

    # max contrast
    min_p = np.amin(noise)
    max_p = np.amax(noise)

    noise = [[(i - min_p) / (max_p - min_p) for i in j] for j in noise]

    print("noise contrasted")

    # deplace la moitie inferieure de l image en haut
    noise = np.roll(noise, size // 2, axis = 0)

    # hauteur max sur les cotes
    valeur_max = 0
    for i in range(size):
        if noise[i][0] > valeur_max:
            valeur_max = noise[i][0]
        if noise[i][-1] > valeur_max:
            valeur_max = noise[i][size-1]
        if noise[0][i] > valeur_max:
            valeur_max = noise[0][i]
        if noise[-1][i] > valeur_max:
            valeur_max = noise[-1][i]

    x = size/((-size/2 ) / ((0.5/valeur_max)-1))

    if x < 0.85:
        x = 0.85

    cercle1 = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            cercle1[i][j] = (1- (((i-size/2)**2 + (j-size/2)**2)**0.5 / (size/x)))
    
    cercle2 = np.zeros((size,size))
    
    for i in range(size):
        for j in range(size):
            distanceToCenter = ((i-(size/3))**2 + (j-(size/3))**2)**0.5
            if distanceToCenter <= size//2: 
                cercle2[i][j] = 1 - ((distanceToCenter / (size//1.5))) # taille

    cercle3 = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            cercle3[i][j] = cercle1[i][j] if cercle1[i][j] > cercle2[i][j] else cercle2[i][j]

    noise = noise * cercle3

    return(noise)


#  #.#
#  .#.
#  #.#

def detour_croix(noise):
    size = len(noise)

    # max contrast
    min_p = np.amin(noise)
    max_p = np.amax(noise)

    noise = [[(i - min_p) / (max_p - min_p) for i in j] for j in noise]

    print("noise contrasted")

    # deplace l image de size//2 vers le haut (met la moitie suppereure de l image en bas)
    noise = np.roll(noise, size // 2, axis = 0)


    # hauteur max sur les cotes
    valeur_max = 0
    for i in range(size):
        if noise[i][0] > valeur_max:
            valeur_max = noise[i][0]
        if noise[i][-1] > valeur_max:
            valeur_max = noise[i][size-1]
        if noise[0][i] > valeur_max:
            valeur_max = noise[0][i]
        if noise[-1][i] > valeur_max:
            valeur_max = noise[-1][i]

    x = size/((-size/2 ) / ((0.5/valeur_max)-1))

    if x < 0.85:
        x = 0.85

    cercle1 = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            cercle1[i][j] = (1- (((i-size/2)**2 + (j-size/2)**2)**0.5 / (size/x)))
    
    cercle2 = np.zeros((size,size))
    
    for i in range(size):
        for j in range(size):
            distanceToCenter = ((i-(size/3))**2 + (j-(size/3))**2)**0.5
            if distanceToCenter <= size//2: 
                cercle2[i][j] = 1 - ((distanceToCenter / (size//1.5))) # taille

    cercle3 = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            cercle3[i][j] = cercle1[i][j] if cercle1[i][j] > cercle2[i][j] else cercle2[i][j]

    noise = noise * cercle3
    
    return(noise)
    # image.save(image_filepath)


def detour_coin(noise):
    size = len(noise)

    # max contrast
    min_p = np.amin(noise)
    max_p = np.amax(noise)

    noise = [[(i - min_p) / (max_p - min_p) for i in j] for j in noise]

    print("noise contrasted")

    # prend la moitie superieure de l image et la met en bas, puis deplace la moitie gauche de l image a droite
    noise = np.roll(noise, size // 2, axis = 0)
    noise = np.roll(noise, size // 2, axis = 1)

    # hauteur max sur les cotes
    valeur_max = 0
    for i in range(size):
        if noise[i][0] > valeur_max:
            valeur_max = noise[i][0]
        if noise[i][-1] > valeur_max:
            valeur_max = noise[i][size-1]
        if noise[0][i] > valeur_max:
            valeur_max = noise[0][i]
        if noise[-1][i] > valeur_max:
            valeur_max = noise[-1][i]

    x = size/((-size/2 ) / ((0.5/valeur_max)-1))

    if x < 0.85:
        x = 0.85

    cercle1 = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            cercle1[i][j] = (1- (((i-size/2)**2 + (j-size/2)**2)**0.5 / (size/x)))
    
    cercle2 = np.zeros((size,size))
    
    for i in range(size):
        for j in range(size):
            distanceToCenter = ((i-(size/3))**2 + (j-(size/3))**2)**0.5
            if distanceToCenter <= size//2: 
                cercle2[i][j] = 1 - ((distanceToCenter / (size//1.5))) # taille
    
    cercle3 = np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            cercle3[i][j] = cercle1[i][j] if cercle1[i][j] > cercle2[i][j] else cercle2[i][j]

    noise = noise * cercle3

    return(noise)

