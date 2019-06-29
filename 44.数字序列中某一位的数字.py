class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return -1
        len_number = 1
        while True:
            # len_number位的数字有多少个 获取对应的位数
            numbers = 9 * pow(10, len_number-1)
            if n <= numbers*len_number:
                a = (n-1)/len_number
                b = (n-1)%len_number
                num = pow(10, len_number-1)+a
                for i in range(len_number-1-b):
                    num = num/10
                return num%10
            n = n-len_number*numbers
            len_number+=1
            print("n",n)
        return -1
