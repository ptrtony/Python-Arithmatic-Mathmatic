
print("this line will be printed")
name = "john"
age = 23
astring ="hello word"
print(astring.index("o"))
print(astring.count("l"))
# 左闭右开
print(astring[3:7])
print(len(astring))
primes = [2,3,4,5,6,7,8,3,3,2,31,323,12,32]
for prime in primes:
    print(prime)


if __name__ == '__main__':
    print("%s is %d years old." % (name, age))