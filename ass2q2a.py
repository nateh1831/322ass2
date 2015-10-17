dom = {1,2,3,4}
fails = 0

for A in dom:
    for B in dom:
        for C in dom:
            for D in dom:
                if C !=D:
                    for E in dom:
                        if E != C and E < (D - 1):
                            for F in dom:
                                if abs(F - B) == 1 and F != C and F != D and abs(E - F) % 2 == 1:
                                    for G in dom:
                                        if A > G and abs(G - C) == 1 and D > G and G != F:
                                            for H in dom:
                                                if A <= H and (H - C) % 2 == 0 and H != D and H - 2 != E and H != F and G < H:
                                                    print(A, B, C, D, E, F, G, H, "solution")
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

