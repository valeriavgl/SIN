from utils import descolocadas # FIXME! Asume que has llamado "descolocadas" a la función.

assert descolocadas("123804765") == 0  # no hay ninguna pieza descolocada 
assert descolocadas("123840765") == 1  # hay una pieza descolocada
assert descolocadas("123847065") == 2  # hay dos piezas descolocadas
assert descolocadas("123847605") == 3  # hay tres piezas descolocadas
assert descolocadas("123847650") == 4  # hay cuatro piezas descolocadas
assert descolocadas("123487650") == 5  # hay cinco piezas descolocadas
assert descolocadas("124387650") == 6  # hay seis piezas descolocadas
assert descolocadas("142387650") == 7  # hay siete piezas descolocadas 
assert descolocadas("567048321") == 8  # todas las piezas están descolocadas

print("TODO OK!")