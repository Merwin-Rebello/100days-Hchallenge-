# number of senior citizens in the given array

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for item in details:
            age = int(item[11]+item[12]) # also  age=int(item[11:13])
            if age > 60:
                count +=1
        return count