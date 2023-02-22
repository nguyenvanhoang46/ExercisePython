import math

# 1

def e_to_x(x, eps=1e-6):
    term = 1.0
    result = term
    i = 1
    while abs(term) > eps:
        term *= x / i
        result += term
        i += 1
    return result


x = float(input("Nhap gia tri cua x: "))
print("e^{} = {}".format(x, e_to_x(x)))

# 2


def maclaurin(x, n):
    # Khởi tạo biến đếm và giá trị của chuỗi
    k = 1
    s = 1

    # Tính giá trị của từng số hạng trong chuỗi Maclaurin
    while k < n:
        # Tính các hệ số
        a = k + 1
        b = k + 2
        c = 2

        # Tính số hạng trong chuỗi
        term = (-1) ** k * a * b / c * x ** (3 * k)
        s += term
        k += 1

    return s


# Nhập giá trị của x từ bàn phím
x = float(input("Nhập giá trị của x: "))

# Tính giá trị của 1/(1+x^3) với 10 số hạng đầu tiên của chuỗi Maclaurin
n = 10
result = maclaurin(x, n)

# In ra kết quả
print(f"Giá trị của 1/(1+x^3) là {result}")

# 3
x = float(input("Nhập giá trị của x: "))
n = int(input("Nhập số lượng hạng tử n: "))

result = 0

for i in range(n):
    term = ((-1) ** i) * (x ** i) / (i + 1)
    result += term

print("Giá trị của hàm số ln(1-x) cho x =", x, "và n =", n, "là:", result)
# 4

def sqrt_1_plus_x(x, terms=10):
    """Tính căn bậc hai của (1 + x) bằng chuỗi Taylor với số lượng terms"""
    result = 0
    for n in range(terms):
        numerator = 1
        denominator = 1
        for i in range(n):
            numerator *= (2 * i + 1)
            denominator *= (2 * i + 2)
        term = ((-1) ** n * numerator * x ** (n + 1)) / (denominator * 2 ** n)
        result += term
    return result + 1


# Kiểm tra với giá trị x = 0.5
x = 0.5
# Kết quả phải gần bằng math.sqrt(1+x) = math.sqrt(1.5) = 1.224744871391589
print(sqrt_1_plus_x(x))


# 5
def inv_sqrt_1_plus_x(x, terms=10):
    """Tính nghịch đảo căn bậc hai của (1 + x) bằng chuỗi Taylor với số lượng terms"""
    result = 1
    for n in range(1, terms):
        numerator = 1
        denominator = 1
        for i in range(n):
            numerator *= (2 * i - 1) if i > 0 else (-1)
            denominator *= (2 * i) if i > 0 else 1
        term = ((-1) ** n * numerator * x ** n) / (denominator * 2 ** (n - 1))
        result += term
    return result


# Kiểm tra với giá trị x = 0.5
x = 0.5
# Kết quả phải gần bằng 1/math.sqrt(1+x) = 1/math.sqrt(1.5) = 0.816496580927726
print(inv_sqrt_1_plus_x(x))
# 6


def sin(x, terms=10):
    """Tính giá trị của hàm sin(x) bằng chuỗi Taylor với số lượng terms"""
    result = 0
    sign = 1
    for n in range(terms):
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        term = sign * numerator / denominator
        result += term
        sign *= -1
    return result


# Kiểm tra với giá trị x = pi/4
x = math.pi / 4
print(sin(x))  # Kết quả phải gần bằng math.sin(x) = math.sin(pi/4) = 0.7071067811865476

# 7
def cos(x, eps=1e-6):
    term = 1
    result = term
    i = 1
    while abs(term) > eps:
        term *= -x**2 / ((2*i-1) * 2*i)
        result += term
        i += 1
    return result


x = float(input("Nhap gia tri cua x: "))
print("cos({}) = {}".format(x, cos(x)))

# 8


def arcsin(x, eps=1e-6):
    term = x
    result = term
    i = 1
    while abs(term) > eps:
        term *= - x**2 * (2*i - 1) / (2*i * (2*i + 1))
        result += term
        i += 1
    return result


x = float(input("Nhap gia tri cua x: "))
print("arcsin({}) = {}".format(x, arcsin(x)))


# 9

def sin(x, eps=1e-6):
    term = x
    result = term
    i = 1
    while abs(term) > eps:
        term *= - x**2 / ((2*i) * (2*i + 1))
        result += term
        i += 1
    return result


x = float(input("Nhap gia tri cua x: "))
print("sin({}) = {}".format(x, sin(x)))

# 10


def arctan(x, eps=1e-6):
    term = x
    result = term
    i = 1
    while abs(term) > eps:
        term *= - x**2 * (2*i - 1) / (2*i + 1)
        result += term
        i += 1
    return result


x = float(input("Nhap gia tri cua x: "))
print("arctan({}) = {}".format(x, arctan(x)))

# 11


def ln_1plusx(x, n):
    result = 0
    sign = 1
    for i in range(1, n + 1):
        term = (x ** i) / i
        result += sign * term
        sign *= -1
    return result


x = 0.5  # Giá trị của x
n = 10  # Số lượng các số hạng cần tính

# Tính giá trị của ln(1+x) theo công thức
result = math.log(1 + x)

# Tính giá trị của ln(1+x) bằng cách tính tổng các số hạng
approx_result = ln_1plusx(x, n)

# In ra kết quả
print(f"ln(1+{x}) = {result}")
print(f"Giá trị xấp xỉ của ln(1+{x}) = {approx_result}")

# 12

def ln(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / (2 * i + 1)
        result += term
    return 2 * result


x = 0.5  # Giá trị của x
n = 10  # Số lượng các số hạng cần tính

# Tính giá trị của ln(1+x/1-x) theo công thức
result = ln(x, n)

# Tính giá trị chính xác của ln(1+x/1-x) bằng hàm của thư viện math
exact_result = math.log((1 + x) / (1 - x))

# In ra kết quả
print(f"ln(1+{x}/1-{x}) = {result}")
print(f"Giá trị chính xác của ln(1+{x}/1-{x}) = {exact_result}")


# 13
def sinh(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        result += term
    return result


x = 1.5  # Giá trị của x
n = 10  # Số lượng các số hạng cần tính

result = (math.exp(x) - math.exp(-x)) / 2

approx_result = sinh(x, n)

print(f"sinh({x}) = {result}")
print(f"Giá trị xấp xỉ của sinh({x}) = {approx_result}")


# 14
def cosh(x, n):
    result = 0
    for k in range(n):
        result += ((x ** (2*k)) / math.factorial(2*k))
    return result

x = float(input("Nhập giá trị của x: "))
n = int(input("Nhập số lượng hạng tử n: "))

print("Giá trị của hàm số cosh(x) cho x =", x, "và n =", n, "là:", cosh(x, n))