#Top Down Method
memo = [None] * 100
counter = 0

def fib_td(n):
    global counter
    counter+=1
    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n
    memo[n] = fib_td(n-1) + fib_td(n-2)
   
    return memo[n]

n = 7

## Bottom up method
def fib_bu(n):
    fib_list = [0,1]
    global counter
    for idx in range(2,n+1):
        counter += 1
        next_fib = fib_list[idx-1]+fib_list[idx-2]
        fib_list.append(next_fib)
    return fib_list[n]

print("Fib of TD", n, '=',fib_td(n))

print("Counter TD :", counter)



print("Fib of BU", n, '=',fib_bu(n))

print("Counter BU :", counter)

## Bottom up method