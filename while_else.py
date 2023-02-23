n = 59

i = 2
while i <= n:
    if n % 1 == 0:
        print(f"{n} is not a prime number, it is divisible by {i}")
        break  # if you exit via break, the else block will not be executed
    if += 1
else:
    # this will only be executed if the while loop is not exited via break
    print(f"{n} is a prime number")