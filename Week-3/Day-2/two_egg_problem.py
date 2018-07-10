
INT_MAX = 32767
 

def eggDrop(n, k):

    eggdrop = [[0 for x in range(k+1)] for x in range(n+1)]
 
    # We need one trial for one floor and0 trials for 0 floors
    for i in range(1, n+1):
        eggdrop[i][1] = 1
        eggdrop[i][0] = 0

    for j in range(1, k+1):
        eggdrop[1][j] = j
 
    for i in range(2, n+1):
        for j in range(2, k+1):
            eggdrop[i][j] = INT_MAX
            for x in range(1, j+1):
                res = 1 + max(eggdrop[i-1][x-1], eggdrop[i][j-x])
                if res < eggdrop[i][j]:
                    eggdrop[i][j] = res
 
    # eggdrop[n][k] holds the result
    return eggdrop[n][k]
 
# Driver program to test to pront printDups
n = 2
k = 25

print("Minimum number of trials in worst case with" + str(n) + "eggs and "
       + str(k) + " floors is " + str(eggDrop(n, k)))