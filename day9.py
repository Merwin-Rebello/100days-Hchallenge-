class Solution:
 def intToRoman(self, num:int)->str:
    values={
           "I" : 1,
            "IV": 4,
            "V" : 5,
            "IX": 9,
            "X" : 10,
            "XL": 40,
            "L" : 50,
            "XC": 90,
            "C" : 100,
            "CD": 400,
            "D" : 500,
            "CM": 900,
            "M" : 1000,
    }
    output=[]
    for key , val in reversed(values.items()):
      while num > 0:
        if val<= num:
          output.append(key)
          num-=val
        else:
          break
    return "".join(output)      
