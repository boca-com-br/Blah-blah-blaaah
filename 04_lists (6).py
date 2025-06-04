# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=10872

### Lists ###

# Definición

my_listita = list()
my_other_listita = []

print(len(my_listita))

my_listita = [35, 24, 62, 52, 30, 30, 17]

print(my_listita)
print(len(my_listita))

my_other_listita = [35, 1.77, "Brais", "Moure"]

print(type(my_listita))
print(type(my_other_listita))

# Acceso a elementos y búsqueda

print(my_other_listita[0])
print(my_other_listita[1])
print(my_other_listita[-1])
print(my_other_listita[-4])
print(my_listita.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_listita.index("Brais"))

age, height, name, surname = my_other_listita
print(name)

name, height, age, surname = my_other_listita[2], my_other_listita[1], my_other_listita[0], my_other_listita[3]
print(age)

# Concatenación

print(my_listita + my_other_listita)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_listita.append("MoureDev")
print(my_other_listita)

my_other_listita.insert(1, "Rojo")
print(my_other_listita)

my_other_listita[1] = "Azul"
print(my_other_listita)

my_other_listita.remove("Azul")
print(my_other_listita)

my_listita.remove(30)
print(my_listita)

print(my_listita.pop())
print(my_listita)

my_pop_element = my_listita.pop(2)
print(my_pop_element)
print(my_listita)

del my_listita[2]
print(my_listita)

# Operaciones con listas

my_new_listita = my_listita.copy()

my_listita.clear()
print(my_listita)
print(my_new_listita)

my_new_listita.reverse()
print(my_new_listita)

my_new_list.sort()
print(my_new_listita)

# Sublistas

print(my_new_listita[1:3])

# Cambio de tipo

my_listita = "Hola Python"
print(my_listita)
print(type(my_listita))
