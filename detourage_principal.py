import numpy as np
import detourage_spe as ds


def detourage(noise):

    size = len(noise)

    # 0 = mer; 1 = ile

    ile = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
    ile_inv = ((1, 1, 1), (1, 0, 1), (1, 1, 1))

    droite = ((0, 0, 0), (1, 1, 1), (0, 0, 0))
    droite_tourne = ((0, 1, 0), (0, 1, 0), (0, 1, 0))
    droite_inv = ((1, 1, 1), (0, 0, 0), (1, 1, 1))
    droite_tourne_inv = ((1, 0, 1), (1, 0, 1), (1, 0, 1))

    double_c = ((1, 0, 1), (1, 1, 1), (1, 0, 1))
    double_c_tourne = ((1, 1, 1), (0, 1, 0), (1, 1, 1))
    double_c_inv = ((0, 1, 0), (0, 0, 0), (0, 1, 0))
    double_c_tourne_inv = ((0, 0, 0), (1, 0, 1), (0, 0, 0))

    coin = ((1, 0, 1), (0, 0, 0), (1, 0, 1))
    coin_inv = ((0, 1, 0), (1, 1, 1), (0, 1, 0))

    croix = ((1, 0, 1), (0, 1, 0), (1, 0, 1))
    croix_inv = ((0, 1, 0), (1, 0, 1), (0, 1, 0))


    # check des points: milieu des cotes, coints et centre
    check_points = ((noise[0][0], noise[0][size//2], noise[0][-1]),(noise[size//2][0], noise[size//2][size//2], noise[size//2][-1]),(noise[-1][0], noise[-1][size//2], noise[-1][-1]))
    print(check_points)
    # si les points sont > 0.5, ils sont considérés comme de la terre (1), sinon ils sont considérés comme de l'eau (0)
    check_points = tuple([tuple([1 if i >= 0.5 else 0 for i in j]) for j in check_points])

    print(check_points)

    if check_points == ile:
        noise = ds.ile(noise)
        print("ile")

    elif check_points == ile_inv:
        noise = [[1 - i for i in j] for j in noise]
        noise = ds.ile(noise)
        print("ile_inv")

    elif check_points == droite:
        noise = ds.detour_droite(noise)
        print("droite")

    elif check_points == droite_tourne:
        noise = np.rot90(noise, 1)
        noise = ds.detour_droite(noise)
        print("droite_tourne")

    elif check_points == droite_inv:
        noise = [[1 - i for i in j] for j in noise]
        noise = ds.detour_droite(noise)
        print("droite_inv")

    elif check_points == droite_tourne_inv: 
        noise = [[1 - i for i in j] for j in noise]
        noise = np.rot90(noise, 1)
        noise = ds.detour_droite(noise)
        print("droite_tourne_inv")


    elif check_points == double_c:
        noise = [[1 - i for i in j] for j in noise]
        noise = ds.detour_double_c(noise)
        print("double_c")

    elif check_points == double_c_tourne:
        noise = [[1 - i for i in j] for j in noise]
        noise = np.rot90(noise, 1)
        noise = ds.detour_double_c(noise)
        print("double_c_tourne")

    elif check_points == double_c_inv:
        noise = ds.detour_double_c(noise)
        print("double_c_inv")
        
    elif check_points == double_c_tourne_inv:
        noise = np.rot90(noise, 1)
        noise = ds.detour_double_c(noise)
        print("double_c_tourne_inv")


    elif check_points == coin:
        noise = ds.coin(noise)
        print("coint")

    elif check_points == coin_inv:
        noise = [[1 - i for i in j] for j in noise]
        noise = ds.coin(noise)
        print("coint_inv")

    elif check_points == croix:
        noise = [[1 - i for i in j] for j in noise]
        noise = ds.detour_croix(noise)
        print("croix")

    elif check_points == croix_inv:
        noise = ds.detour_croix(noise)
        print("croix_inv")

    else:
        noise = ds.ile(noise)
        print("unknown pattern")
    
    return noise
