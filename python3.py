

print("Complex Number Calculator")

real1 = float(input("Enter real part of first complex number: "))
imag1 = float(input("Enter imaginary part of first complex number: "))

real2 = float(input("Enter real part of second complex number: "))
imag2 = float(input("Enter imaginary part of second complex number: "))

num1 = complex(real1, imag1)
num2 = complex(real2, imag2)

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2


print("\nFirst Complex Number:", num1)
print("Second Complex Number:", num2)

print("\nResults:")
print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)

print("\nExtra Information:")
print("Real part of first number:", num1.real)
print("Imaginary part of first number:", num1.imag)
print("Real part of second number:", num2.real)
print("Imaginary part of second number:", num2.imag)