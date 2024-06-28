
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# removendo com dell

del motorcycles[1] #indice 1
print(motorcycles)

#pop = o resultado é que separamos a ultima e expomos
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motocyles = motorcycles.pop()
print(motorcycles)
print(popped_motocyles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'pop']
last_owned = motorcycles.pop()
print("a ultima moto que eu comprei foi uma " + last_owned.title() + ".")


# removendo intem de qualquer posição usando o pop

motorcycles = ['honda', 'yamaha', 'suzuki', 'pop']
last_owned = motorcycles.pop() # o indice que se quer retirar
print("a primeira moto que eu comprei foi uma " + last_owned.title() + ".")

# Mostrar o que esta sendo removido da lista
motorcycles = ['honda', 'yamaha', 'suzuki', 'pop', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print("\nA " +too_expensive.title() + " é muito cara pra mim.")