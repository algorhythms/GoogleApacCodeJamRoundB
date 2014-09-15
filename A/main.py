__author__ = 'Danyang'
# global
def factorial(n):
    factorial = 1
    for i in range(n):
        factorial *= i+1
    return factorial

def comb(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))
class Solution:
    def solve(self, cipher):
        """

        """
        M, N = cipher
        M = int(M)
        N = int(N)
        result = M**N
        for i in xrange(1, M):
            result = (result +(-1)**(i)*comb(M, M-i)*(M-i)**N)%(10**9+7)
        return result




if __name__=="__main__":
    f = open("p2.in", "r")
    o = open("out.out", "w")

    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher =  f.readline().strip().split(' ')

        # solve
        s = "Case #%d: %s\n"%(t+1, Solution().solve(cipher))
        print s,
        o.write(s)
