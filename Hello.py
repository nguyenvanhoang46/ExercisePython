
import math

eps = 0.00001 #Sai số

# bài 1
def baimot(x):
    k = 0
    s = 1
    term = 1

    while abs(term) > 1e-8:
        k += 1
        term *= x / k
        s += term

    return s


# Kiểm tra với giá trị x = 7
print(f"Kết quả bài 1: {baimot(float(7)):.8f}")

# bài 2
def baihai(x):
    i = 1 
    first = 1
    second = first - ( (((i+1) * (i+2))/2)*x**i )

    while(abs(first - second) >  eps):
        i += 1
        first = second 

        if(i % 2 == 0): 
            second = first + ( (((i+1) * (i+2))/2)*x**i )
        else:
            second = first - ( (((i+1) * (i+2))/2)*x**i )
            
    return first


# Kiểm tra với giá trị x = 0.5
print(f"Kết quả bài 2: {baihai(0.5)}")

# bài 3
def baiba(x):
    i = 1
    first = -x
    second = first - ((x**(i+1))/(i+1))
    
    while(abs(second - first) > 0.0001):
        i += 1
        first = second
        second = first - ((x**(i+1))/(i+1))
        
    return first


print(f"Kết quả bài 3: {baiba(float(-1))}")

# bài 4
def baibon(x):
    i = 1
    first = 1
    tuSo = 1
    mauSo = 2
    
    second = first + (tuSo / mauSo)*x
    tuSoStep = 1
    mauSoStep = 4
        
    while(abs(first - second) > eps):
        i += 1
        first = second
        
        
        tuSo *= tuSoStep
        mauSo *= mauSoStep
        
        tuSoStep += 2
        mauSoStep += 2
        
        if (i % 2 == 0):
            second -= (tuSo / mauSo)*x**i
        else:
            second += (tuSo / mauSo)*x**i
        
    return first

print(f"Kết quả bài 4: {baibon(float(0.5))}")

# bài 5
def bainam(x):
    i = 1
    first = 1
    tuSo = 1
    mauSo = 2
    tuSoStep = 3
    mauSoStep = 4
    
    second = first - (tuSo / mauSo)*x
    while(abs(first - second) > eps):
        i += 1
        tuSo *= tuSoStep
        mauSo *= mauSoStep
        
        tuSoStep += 2
        mauSoStep += 2
        first = second
        
        if (i % 2 == 0):
            second += (tuSo / mauSo)*x**i
        else:
            second -= (tuSo / mauSo)*x**i
    
    return first

# Kiểm tra với giá trị x = 0.5
print(f"Kết quả bài 5: {bainam(0.5)}")


# bài 6
def baisau(x):
    i = 3
    
    first = 1
    second = 1 - (x**(i))/math.factorial(i)
    y = 0

    while(abs(first - second) > eps):
        i += 2
        y += 1
        
        first = second
        
        if (i % 2 == 0):
            second -= x**i/math.factorial(i)
        else:
            second += x**i/math.factorial(i)  
        
    return first

print(f"Kết quả bài 6: {baisau(1)}")


# bài 7
def baibay(x):
    i = 2
    
    first = 1
    second = 1 - (x**(i))/math.factorial(i)
    y = 0

    while(abs(first - second) > eps):
        y += 1
        i += 2
        
        first = second
        
        if (i % 2 != 0):
            second -= x**i/math.factorial(i)
        else:
            second += x**i/math.factorial(i)  
        
    return first


print(f"Kết quả bài 7: {baibay(1)}")


# bài 8
def baitam(x):
    i = 3
    first = x
    tuSo = 1
    mauSo = 2
    second = first + ( (tuSo/mauSo) * (x**i)/i )  
    while(abs(first - second) > eps):
        i += 2
        tuSo = tuSo * (i - 2)
        mauSo = mauSo * ( i - 1)

        first = second
        second = first + ( (tuSo/mauSo) * (x**i)/i )
    return first

# Kiểm tra kết quả với x = 0.5
print(f"Kết quả bài 8: {baitam(0.5)}")


# bài 9
def baichin(x):
    step = 2
    i = 0
    first = 1
    second = (first - x**step / math.factorial(step+1))

    while abs(first - second) > eps:
        step += 2
        i += 1
        first = second
        if (i % 2 != 0):
            second = first + x**step / math.factorial(step+1)
        else:
            second = first - x**step / math.factorial(step+1)
    return first

# Kiểm tra kết quả với x = 1 và n = 5
print(f"Kết quả bài 9: {baichin(1)}")


# bài 10
def baimuoi(x):
    step = 3
    i = 0
    first = x
    second = (first - x**step / step)

    while abs(first - second) > eps:
        step += 2
        i += 1
        first = second
        if (i % 2 != 0):
            second = first + x**step / step
        else:
            second = first - x**step / step

    return first

# Kiểm tra kết quả với x = 0.5 
print(f"Kết quả bài 10: {baimuoi(0.5)}")


# bài 11
def baimuoimot(x):
    step = 3
    first = x
    second = first + x**step / step

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x**step / step
    return first

# Kiểm tra kết quả với x = 0.5
print(f"Kết quả bài 11: {baimuoimot(0.5)}")


# bài 12
def baimuoihai(x):
    step = 3
    first = x
    second = first + x**step / step

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x**step / step
    return first

# Kiểm tra kết quả với x = 0.5 
print(f"Kết quả bài 12: {baimuoihai(0.5)}")


# bài 13
def baimuoiba(x):
    step = 3
    first = x
    second = first + x**step / math.factorial(step)

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x**step / math.factorial(step)
    return first


# Kiểm tra kết quả với x = 0.5
print(f"Kết quả bài 13: {baimuoiba(0.5)}")


# bài 14
def baimuoibon(x):
    step = 2
    first = x
    second = first + x**step / math.factorial(step)

    while abs(first - second) > eps:
        step += 2
        first = second
        second = first + x**step / math.factorial(step)
    return first

# Kiểm tra kết quả với x = 0.5
print(f"Kết quả bài 14: {baimuoibon(0.5)}")