# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬(not); ⋁(or); ⋀(and)
x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))
left = not (x or y or z)
right = not x and not y and not z
if left == right:
    print("True")
else:
    print("False")
