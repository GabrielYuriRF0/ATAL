class Solution(object):
    def maximum69Number(self, num):
        def listToNumber(list):
            stringNumber = ''
            for element in list:
                stringNumber += str(element)
            return int(stringNumber)
        """
        :type num: int
        :rtype: int
        """
        formattedNum = [int(x) for x in str(num)]
        n = len(formattedNum)
        solution = formattedNum[:]

        for i in range(0, n):
            parcialSolution = formattedNum[:]
            if formattedNum[i] == 6:
                parcialSolution[i] = 9
            else:
                parcialSolution[i] = 6

            if  listToNumber(parcialSolution) > listToNumber(solution):
                solution = parcialSolution[:]

        return listToNumber(solution)
    