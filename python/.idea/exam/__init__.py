def f(w, s, n):
    if s == 0:
        return True
    elif (s < 0) or (s > 0 and n < 1):
        return False
    elif f(w, s - w[n - 1], n - 1):
        print(w[n - 1])
        return True
    else:
        return f(w, s, n - 1)
w=[5,7,9,8,6]
print(f(w,9,2))