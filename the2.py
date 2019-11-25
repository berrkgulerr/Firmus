def is_firmus(c1, c2):
    if (c2[1]+c2[3]) - (c1[1]+c1[3]) > 0.00000001 :
        if 0.001 >= min(c1[1], c1[3]) >= -0.001 and 0.001 >= min(c2[1], c2[3]) - max(c1[1], c1[3]) >= -0.001:
            if ((c2[0] + c2[2]) / 2.0) - min(c1[0], c1[2]) >= -0.001 and max(c1[2], c1[0]) - ((c2[0] + c2[2]) / 2.0) >= -0.001 :
                return ['FIRMUS', abs(c1[2]-c1[0]) * abs(c1[1]-c1[3]) + abs(c2[2]-c2[0]) * abs(c2[1]-c2[3])]

            else:
                if min(c1[0], c1[2]) - ((c2[0] + c2[2]) / 2.0) > 0.001 :
                    a = 2.0 * min(c1[0], c1[2]) - min(c2[0],c2[2])
                    
                    return ['ADDENDUM', [max(c2[0], c2[2]), c2[1], a, c2[3]]]

                if ((c2[0] + c2[2]) / 2.0) - max(c1[2], c1[0]) > 0.001:
                     a = 2.0 * max(c1[0], c1[2]) - max(c2[0],c2[2])
                     
                     return ['ADDENDUM', [a, c2[1], min(c2[0], c2[2]), c2[3]]]
		
        else:
                k = 0
                m = 2
                c3 = [1, 1, 1, 1, 1]

                if min(c1[1], c1[3]) < min(c2[1], c2[3]) < max(c1[1], c1[3]):
                    k += 1
                    c3[k] = min(c2[1], c2[3])

                if min(c1[1], c1[3]) < max(c2[1], c2[3]) < max(c1[1], c1[3]):
                    k += 1
                    c3[k] = max(c2[1], c2[3])

                if min(c2[1], c2[3]) < min(c1[1], c1[3]) < max(c2[1], c2[3]):
                    k += 1
                    c3[k] = min(c1[1], c1[3])

                if min(c2[1], c2[3]) < max(c1[1], c1[3]) < max(c2[1], c2[3]):
                    k += 1
                    c3[k] = max(c1[1], c1[3])

                if min(c1[0], c1[2]) < min(c2[0], c2[2]) < max(c1[0], c1[2]):
                    m += 1
                    c3[m] = min(c2[0], c2[2])

                if min(c1[0], c1[2]) < max(c2[0], c2[2]) < max(c1[0], c1[2]):
                    m += 1
                    c3[m] = max(c2[0], c2[2])

                if min(c2[0], c2[2]) < min(c1[0], c1[2]) < max(c2[0], c2[2]):
                    m += 1
                    c3[m] = min(c1[0], c1[2])

                if min(c2[0], c2[2]) < max(c1[0], c1[2]) < max(c2[0], c2[2]):
                    m += 1
                    c3[m] = max(c1[0], c1[2])
                if min(c1[1], c1[3]) == min(c2[1], c2[3]):
                    k += 1
                    c3[k] = min(c2[1], c2[3])

                if max(c2[1], c2[3]) == max(c1[1], c1[3]):
                    k += 1
                    c3[k] = max(c1[1], c1[3])

                if min(c1[0], c1[2]) == min(c2[0], c2[2]):
                    m += 1
                    c3[m] = min(c2[0], c2[2])

                if max(c2[0], c2[2]) == max(c1[0], c1[2]):
                    m += 1
                    c3[m] = max(c1[0], c1[2])

                if m == 4 and k == 2:

                    return ["DAMNARE", abs(c1[1] - c1[3]) * abs(c1[0] - c1[2]) + abs(c2[1] - c2[3]) * abs(c2[0] - c2[2]) - abs(
                            c3[1] - c3[2]) * abs(c3[3] - c3[4])]
                else:
                    return ["DAMNARE", abs(c1[1] - c1[3]) * abs(c1[0] - c1[2]) + abs(c2[1] - c2[3]) * abs(c2[0] - c2[2])]



    elif (c1[1] + c1[3]) - (c2[1] + c2[3]) > 0.00000001 :
        if 0.001 >= min(c2[1], c2[3]) >= -0.001 and 0.001 >= min(c1[1], c1[3]) - max(c2[1], c2[3]) >= -0.001:
            if ((c1[0]+c1[2]) / 2.0) - min(c2[0], c2[2]) >= -0.001 and  max(c2[2], c2[0]) - ((c1[0]+c1[2]) / 2.0) >= -0.001 :
                return ['FIRMUS', abs(c2[2] - c2[0]) * abs(c2[1] - c2[3]) + abs(c1[2] - c1[0]) * abs(c1[1] - c1[3])]

            else:
                if min(c2[0], c2[2]) - (c1[0] + c1[2]) / 2.0 > 0.001 :
                    a = 2.0 * min(c2[0], c2[2]) - min(c1[0],c1[2])
                    
                    return ['ADDENDUM', [max(c1[0], c1[2]), c1[1], a, c1[3]]]

                if (c1[0] + c1[2]) / 2.0 - max(c2[2], c2[0]) > 0.001 :
                    a = 2.0 * max(c2[0], c2[2]) - max(c1[0],c1[2])
                    
                    return ['ADDENDUM', [min(c1[0], c1[2]), c1[1], a, c1[3]]]
		
        else:
                k = 0
                m = 2
                c3 = [1, 1, 1, 1, 1]

                if min(c1[1], c1[3]) < min(c2[1], c2[3]) < max(c1[1], c1[3]):
                    k += 1
                    c3[k] = min(c2[1], c2[3])

                if min(c1[1], c1[3]) < max(c2[1], c2[3]) < max(c1[1], c1[3]):
                    k += 1
                    c3[k] = max(c2[1], c2[3])

                if min(c2[1], c2[3]) < min(c1[1], c1[3]) < max(c2[1], c2[3]):
                    k += 1
                    c3[k] = min(c1[1], c1[3])

                if min(c2[1], c2[3]) < max(c1[1], c1[3]) < max(c2[1], c2[3]):
                    k += 1
                    c3[k] = max(c1[1], c1[3])

                if min(c1[0], c1[2]) < min(c2[0], c2[2]) < max(c1[0], c1[2]):
                    m += 1
                    c3[m] = min(c2[0], c2[2])

                if min(c1[0], c1[2]) < max(c2[0], c2[2]) < max(c1[0], c1[2]):
                    m += 1
                    c3[m] = max(c2[0], c2[2])

                if min(c2[0], c2[2]) < min(c1[0], c1[2]) < max(c2[0], c2[2]):
                    m += 1
                    c3[m] = min(c1[0], c1[2])

                if min(c2[0], c2[2]) < max(c1[0], c1[2]) < max(c2[0], c2[2]):
                    m += 1
                    c3[m] = max(c1[0], c1[2])
                if min(c1[1], c1[3]) == min(c2[1], c2[3]):
                    k += 1
                    c3[k] = min(c2[1], c2[3])

                if max(c2[1], c2[3]) == max(c1[1], c1[3]):
                    k += 1
                    c3[k] = max(c1[1], c1[3])

                if min(c1[0], c1[2]) == min(c2[0], c2[2]):
                    m += 1
                    c3[m] = min(c2[0], c2[2])

                if max(c2[0], c2[2]) == max(c1[0], c1[2]):
                    m += 1
                    c3[m] = max(c1[0], c1[2])

                if m == 4 and k == 2:

                    return ["DAMNARE", abs(c1[1] - c1[3]) * abs(c1[0] - c1[2]) + abs(c2[1] - c2[3]) * abs(c2[0] - c2[2]) - abs(
                            c3[1] - c3[2]) * abs(c3[3] - c3[4])]
                else:
                    return ["DAMNARE", abs(c1[1] - c1[3]) * abs(c1[0] - c1[2]) + abs(c2[1] - c2[3]) * abs(c2[0] - c2[2])]
    else:
	return "None"
