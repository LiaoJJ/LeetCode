'''
very hard
the basic idea is to split the 9 digit num into 3 part
each part below than 1000
than split 1000 into <20, <100, <1000
for <20, every one is unique
for <100, need to plus a tens, some-ty
for <1000, need to plus a hundreds, some Hundred

corner cases:
50, this will output "Fifty  ", solution: deal with num==0
1000001, this should be "One Million One", in this case, should not output thousands where thousands==0
'''

class Solution:
    def numberToWords(self, num):
        def help(num):
            if num==0:
                return ""
            if num<20:
                return below20[num] + " "
            elif num<100:
                return tens[num//10]+ " " + help(num%10)
            else:
                return below20[num//100] + " Hundred " + help(num%100)

        below20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        if num==0: return "Zero"
        res = ""
        i = 0
        while num:
            cur = num % 1000
            if cur!=0:
                res = help(cur) + thousands[i] + " " + res
            num //=1000
            i += 1
        
        res = res.strip()
        return res