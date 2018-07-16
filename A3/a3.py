import time
import random
import sys

n = 100
sys.path.append('../../ch50')
from ch50 import p50

sys.path.append('../../A33')
from A33 import a33

'''The following function finds the maximal element in an array
' Takes:  
'     3n + k operations to find the max (its complexity is 3n + k )
'     k operations before loop  +  3 op in the loop  repeated n times 
'     This is a polynomial where the fastest growing term is a factor of n, so it is O(n).
'     Time complexity Big-O :  O(n)
'''


def vacum():
    import sqlite3
    conn = sqlite3.connect('../../git/numeri.db')
    conn.execute("VACUUM")
    conn.close()


def find_max(array):
    maxi = -sys.maxsize - 1
    el = 0
    arend = len(array)
    while el < arend:
        if maxi < array[el]:
            maxi = array[el]
        el += 1

    return maxi


'''
' Function checks if an array has any duplicates
' the inner loop are run n^2 times
' The complexity will be something like an^2 + bn + c , and since the highest term is n^2 , 
' the O notation is O(n^2)
'''


def contains_duplicates(array):
    eloop1 = 0
    arend = len(array) - 1
    while eloop1 < arend:
        eloop2 = 1
        while eloop2 <= arend:
            if eloop2 != eloop1 and array[eloop1] == array[eloop2]:
                return True
            eloop2 += 1
        eloop1 += 1
    return False


'''
' Function checks if an array has any duplicates
' the inner loop body is run 1 + 2 + ... + n - 1 = n(n-1)/2 times
' The complexity will be something like an^2 + bn + c , and since the highest term is n^2 , 
' the Big-O class is still O(n^2)  
'''


def fast_contains_duplicates(array):
    eloop1 = 0
    arend = len(array) - 1
    while eloop1 < arend:
        eloop2 = eloop1 + 1
        while eloop2 <= arend:
            if array[eloop1] == array[eloop2]:
                return True
            eloop2 += 1
        eloop1 += 1
    return False


def obig_class(fnz):
    print('The %s function Time complexity Big-O class is : O(1) O(n) 0(n^2) ?' % fnz)

    reg = 10

    d = {}
    # 10000001
    while reg < n + 1:
        listaNum = p50.numerirandom(reg)
        ticinizio = time.time()
        print(reg, fnz(listaNum))
        d[reg] = time.time() - ticinizio
        reg *= 10

    for key in d:
        print('\t\tTooks: %.4fs %s Milli secondi ' % (d[key] * 1000, key))
    print('******************\n')


# obig_class(find_max)
# obig_class(contains_duplicates)
# obig_class(fast_contains_duplicates)
# obig_class(a33.quicksort)
# obig_class(a33.quicksort_fast)
vacum()
