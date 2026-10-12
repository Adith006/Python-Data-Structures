dict1 = {
    'value':11
}

dict2 = dict1

print("before value is updated")
print("dict1 =",dict1)
print("dict2 = ",dict2)

print("\nnum1 points to:",id(dict1))

print("\nnum2 points to:",id(dict2))

dict2['value'] = 22

print("after value is updated")
print("dict1 =",dict1)
print("dict2 = ",dict2)

print("\nnum1 points to:",id(dict1))

print("\nnum2 points to:",id(dict2))