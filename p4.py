'''
------ Logical operators------
Types :
1.Logical AND
2. Logical OR
3.Logical NOT


----------- AND operators-----------
       C1         C2          RESULTS
       T           T             T
       T           F             F
       F           T             F
       F           F             F
       
------------ OR operators -----------
        C1          C2          RESULTS
        T            T             T
        T            F             T
        F            T             T
        F            F             F
        
---------- NOT operators --------------
 opposite to the original output

'''
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))

 '''
a=10
b=20
c=30
 
'''
 
print(a>b and a>c)
print(a<b and a>c)
 print(a<b and a<c)
 
 print(a>b or a>c)
 print(a<b or a>c)
 
 print(a>b)
 print(not(a>b))
 