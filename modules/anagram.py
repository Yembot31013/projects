from pakage import *

writelines(""" 
      _________________________________________________________________________________________
      |0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|//
      |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
      |0|    |O|      0|0|0     |0|     |O|      0|0|0    0|0|0     |O|      0|0|0| |0|0|0  |0|
      |0|  |0| |0|   0|0| |0|  0|0|   |0| |0|   |0       |0|      |0| |0|   |0|0| |0| |0|0| |0|
      |0| 0|0|0|0|0  0|0|  0| |0|0|  0|0|0|0|0  |0   0|0 |0|     0|0|0|0|0  |0|0|  0  |0|0| |0|
      |0||0|     |0| 0|0|  0|0|0|0| |0|     |0|  0|0|0|  |0|    |0|     |0| |0|0|     |0|0| |0|
      |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
      |0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0|//
      _______________________________________________________________________________________//
      """)
pletter('\n\n')

pword("Two strings are anagrams if they're made of the same character with the same frequencies", times=0.8)
writelines("""
      for an example___
                      ||
                      \/

    INPUT:
     S1 = "danger"
     s2 = "garden"
    OUTPUT: True

    EXPLANATION:                                                 ____
                |o|0|0       |O|      |0|0|     |0|  0|0|0     0|       0|0|0  
                |0|   |0   |0| |0|   0|0| |0|  0|0| |0        |0|____  |0|
                |0|   |0  0|0|0|0|0  0|0|  0| |0|0| |0   0|0  |0|      |0|
                |0|0|0   |0|     |0| 0|0|  0|0|0|0|  0|0|0|    0|_____ |0|
                            |0|                                 
                            |o|
                            |0|                                
                            |0|
                            |0|
                            |0|
                                                        ____
                 0|0|0       |O|      0|0|0 |o|0|0    0|       |0|0|     |0|
                |0         |0| |0|   |0|    |0|   |0 |0|____  0|0| |0|  0|0|
                |0   0|0  0|0|0|0|0  |0|    |0|   |0 |0|      0|0|  0| |0|0|
                 0|0|0|  |0|     |0| |0|    |0|0|0    0|____  0|0|  0|0|0|0| 
""")

s1 = input("enter the first value to compare: ")
s2 = input("enter the second value to compare: ")


pletter('\n\n\n\n')


def sort(s):
    arr = []
    for n in range(len(s)):
        arr.append(s[n])
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
    return ''.join(arr)


def anagram(s1, s2):
    value1 = sort(s1)

    value2 = sort(s2)

    if value1 == value2:
        pletter('[*] there are anagrams', times=0.5)
    else:
        pletter('[-] sorry, there are not anagrams', times=0.5)


anagram(s1, s2)
