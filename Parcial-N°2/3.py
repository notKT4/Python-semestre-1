# Definir los dos sets de precios
set1 = {100, 250, 300, 1000}
set2 = {150, 250, 500, 1000}

# A) Verificar si el valor 100 está en ambos sets
valor_100_en_ambos = 100 in set1 and 100 in set2

# B) Comprobar si al menos el valor 500 o 700 está en alguno de los sets
valor_500_o_700_en_alguno = 500 in set1 or 500 in set2 or 700 in set1 or 700 in set2

# C) Elevar a 3 todos los valores dentro de los sets
set1 = {precio ** 3 for precio in set1}
set2 = {precio ** 3 for precio in set2}

# D) Unir ambos sets en uno solo
set_unido = set1.union(set2)

# Imprimir los resultados
print("A) ¿El valor 100 está en ambos sets?:", valor_100_en_ambos)
print("B) ¿El valor 500 o 700 está en alguno de los sets?:", valor_500_o_700_en_alguno)
print("C) Set 1 elevado a 3:", set1)
print("   Set 2 elevado a 3:", set2)
print("D) Set unido:", set_unido)

