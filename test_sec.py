from utils import secuencia # FIXME! Asume que has llamado "secuencia" a la función.

assert secuencia("123804765") == 0    # Todas las secuencias son correctas
assert secuencia("123084765") == 15   # Hay dos secuencias incorrectas y el centro
assert secuencia("132467850") == 51   # Todas las secuencias son incorrectas
assert secuencia("812703654") == 0    # Todas correctas, aunque no es el estado final
assert secuencia("283164705") == 33   # El ejemplo del boletín (3*S(n) = 3*11 = 33)


print("TODO OK!")