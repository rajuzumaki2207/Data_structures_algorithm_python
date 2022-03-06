class Solution:
    def fizzBuzz(self, n: int):
        
        d= {3: 'Fizz', 5: 'Buzz'}
        y =[a for a in d.keys()]
        x =[i for i in range (1, n+1)]

        l=0
        while l<n:
            if x[l] % 15==0:
                x[l] = d[y[0]] + d[y[1]]
                
            elif x[l]% 3 ==0:
                x[l] =d[y[0]]
            elif x[l]% 5 ==0:
                x[l] =d[y[1]]
            else:
                x[l] = str(x[l])
                
            l+=1


        return x
if __name__=="__main__":
    k= Solution()
    print (k.fizzBuzz(15))
