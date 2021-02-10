class New(int):
    def __gt__(self,other):
        if other==999999: return True
        else: return self.__int()>other.__int__()

a=New(0)

print(type(a))

print(a==a**2)
print(a==a*2)
print(a>999999)