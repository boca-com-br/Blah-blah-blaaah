# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### Operadores Aritméticos ###

# Operaciones con enteros
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)
print(2 ** 3 + 3 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("HALLO " + "Python " + "¿Qué tal?")
print("HALLO " + str(5))

# Operaciones mixtas
print("HALLO " * 5)
print("HALLO " * (2 ** 3))

my_float = 2.5 * 2
print("HALLO " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("HALLO" > "Python")
print("HALLO" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("HALLO" <= "Python")
print("HALLO" == "HOLA")
print("HALLO" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "HALLO" > "Python")
print(3 > 4 or "HALLO" > "Python")
print(3 < 4 and "HALLO" < "Python")
print(3 < 4 or "HALLO" > "Python")
print(3 < 4 or ("HALLO" > "Python" and 4 == 4))
print(not (3 > 4))
