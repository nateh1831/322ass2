__author__ = 'Nathan'
dom = {1,2,3,4}
fails = 0

for H in dom:
    for F in dom:
        if H != F:
            for G in dom:
                if G < H and G != F:
                    for D in dom:
                        if H != D and  F != D and  D > G:
                            for C in dom:
                                if (H - C) % 2 == 0 and F != C and abs(G - C) == 1 and C !=D:
                                    for E in dom:
                                        if H - 2 != E and abs(E - F) % 2 == 1 and  E < (D - 1) and E != C:
                                            for A in dom:
                                                if A <= H and A > G:
                                                    for B in dom:
                                                        if abs(F - B) == 1:
                                                            print(A, B, C, D, E, F, G, H, "solution")
                                                        else:
                                                            fails += 1
                                                else:
                                                    fails +=1
                                        else:
                                            fails += 1
                                else:
                                    fails += 1
                        else:
                            fails += 1
                else:
                    fails += 1
        else:
            fails += 1

print("number of failures:",fails)