'''
1.Math
    eg.+,-,*,/
    (1)** 指數
    (2)% 餘數
    (3)// 取商數（整數除法）
    a 是 b的因數 -> b % a = 0
    print(2**5)
    print(10 % 3)
    print(10 // 3)
2.Strings
    (1)+
    eg.print('abc'+'efg') -> 'abcefg'
    (2)*
    eg.print('abc'*2) -> 'abcabc'
3.Boolean
    (1)not 反閘
        周杰倫：哎呦不錯喔 -> True
        錯   -> False
        不(not)錯(False) -> True
        行  -> True
        不(not)行(True) -> False
    (2)or 或閘
        math or english -> 3000
        T       F           T
        F       T           T
        T       T           T
        F       F           F (真值表truth table)
    (3)and 且閘
        HW and 打掃 -> :)
        T       F      F
        F       T      F
        T       T      T
        F       F      F
    (4)xor(excursive or) 斥或閘
        珍奶 xor 烏龍拿鐵 -> :)
        T       F           T
        F       T           T
        T       T           F
        F       F           F

        [1] not or and
            a, b
            (a or b) and not(a and b)
        [2] binary ^
        a = 3
        b = 5
        print((a or b) and not(a and b))
        print(a^b)
        
4.List
    (1)+
        print([1]+[2])  
    (2)*
        print([1]*3)

5.關係 num op num -> bool
>, <, >=, <=, ==(equal), !=(not equal)
'''