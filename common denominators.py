import math
import functools

def convertFracts(lst):
    lcm = lambda a, b : abs(a*b) // math.gcd(a, b)
    tmp_list = list(map(lambda x : x[1] ,list(lst)))
    lcm_num = functools.reduce(lcm,tmp_list)
    return list(map(lambda x : [x[0] * lcm_num // x[1], lcm_num] , list(lst)))
