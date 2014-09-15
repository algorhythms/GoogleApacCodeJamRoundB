__author__ = 'Danyang'
class Solution:
    smallest = 1<<32
    def dfs(self, seq, K):
        if self.smallest==0:
            return

        length = len(seq)
        self.smallest = min(self.smallest, length)

        if length<3:
            return

        for i in xrange(length-2):
            if seq[i+2]-seq[i+1]==K and seq[i+1]-seq[i]==K:
                self.dfs(seq[:i]+seq[i+3:], K)


    def solve(self, cipher, lst):
        """
        K = 0, greedy
        """
        N, K= cipher
        N = int(N)
        K = int(K)


        while True:
            flag = False
            for i in xrange(len(lst)-2):
                if lst[i+2]-lst[i+1]==K and lst[i+1]-lst[i]==K:
                    lst = lst[:i]+lst[i+3:]
                    flag = True
                    break
            if flag:
                continue
            else:
                break


        return len(lst)




if __name__=="__main__":
    f = open("1.in", "r")
    o = open("out.out", "w")

    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip().split(' ')
        lst = [int(item) for item in f.readline().strip().split(' ')]

        # solve
        s = "Case #%d: %s\n"%(t+1, Solution().solve(cipher, lst))
        print s,
        o.write(s)
