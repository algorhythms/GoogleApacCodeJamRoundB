__author__ = 'Danyang'
def sum_sum(n):
    return (n**3+3*n**2+2*n)/6

class Solution:
    def solve(self, cipher):
        """
        Large Problem Set Not solved
        """
        B, L, N= cipher
        B = int(B)
        L = int(L)
        N = int(N)

        lowest_level = 0
        # 1 is 250, 3 is 750 ml
        n = 1
        while True:
            temp = sum_sum(n)
            temp2 = 3*B
            if sum_sum(n)<3*B<=sum_sum(n+1):
                lowest_level = n+1
                break
            n += 1

        if L<lowest_level:
            return 250
        if L>lowest_level:
            return 0
        else:
            remain = 3*B - sum_sum(lowest_level-1)
            l_1 = 3
            l_2 = (lowest_level-2)*3
            l_3 = (lowest_level*(lowest_level+1)/2)-l_1-l_2

            eff = float(remain)/(l_1+2*l_2+3*l_3)
            eff *= 250.0

            cor3 = sum(range(1, lowest_level+1))
            cor2 = cor3 - lowest_level+1
            if N in (1, cor2, cor3):
                return eff

            border = []
            border += [sum(range(1, i+1)) for i in range(2, lowest_level)]
            border += [sum(range(1, i+1))-i-1 for i in range(2, lowest_level)]
            border += range(cor2+1, cor3)
            if N in border:
                return 2*eff

            return 3*eff









if __name__=="__main__":
    f = open("0.in", "r")
    o = open("out.out", "w")

    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher =  f.readline().strip().split(' ')

        # solve
        s = "Case #%d: %.6f\n"%(t+1, Solution().solve(cipher))
        print s,
        o.write(s)
