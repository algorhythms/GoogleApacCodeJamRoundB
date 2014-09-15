__author__ = 'Danyang'


class Solution:
    def generateParenthesisDfs(self, result, cur, left, right):
        """
        DFS
        Catalan Number
        :param result: result list
        :param cur: currently processing string
        :param left: number of left parenthesis remaining
        :param right: number of right parenthesis remaining
        """
        # trivial
        if left==0 and right==0:
            result.append(cur)
            return
            # add left parenthesis
        if left>0:
            self.generateParenthesisDfs(result, cur+"(", left-1, right)
            # add right parenthesis
        if right>left:
            self.generateParenthesisDfs(result, cur+")", left, right-1)

    def catalan(self, n):
        """
        number of unique binary search tree
        Catalan Number

        C_n = {2n\choose n} - {2n\choose n+1}
        Proof: http://en.wikipedia.org/wiki/Catalan_number#Second_proof
        :param n: integer
        :return: integer
        """
        return self.factorial(2*n)/(self.factorial(n)*self.factorial(n))-self.factorial(2*n)/(
            self.factorial(n+1)*self.factorial(n-1))

    def factorial(self, n):
        factorial = 1
        for i in range(n):
            factorial *= i+1
        return factorial

    def solve_small(self, cipher):
        """

        """
        n, k= cipher
        n = int(n)
        k = int(k)

        result = []
        self.generateParenthesisDfs(result, "", n, n)
        try:
            return result[k-1]
        except IndexError:
            return "Doesn't Exist!"

    def solve(self, cipher):
        """

        """
        n, k = cipher
        n = int(n)
        k = int(k)

        if k>self.catalan(n):
            return "Doesn't Exist!"












if __name__=="__main__":
    f = open("1.in", "r")
    o = open("out.out", "w")

    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher =  f.readline().strip().split(' ')

        # solve
        s = "Case #%d: %s\n"%(t+1, Solution().solve_small(cipher))
        print s,
        o.write(s)
