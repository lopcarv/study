'''
# metodo sort() ordena em alfabetica
cars = ['bmw', 'audi', 'toyota','subaru']
cars.sort() 
print(cars)

# metodo sort() ordena inverso
cars = ['bmw', 'audi', 'toyota','subaru']
cars.sort(reverse=True) 
print(cars)

# metodo ordenar temporariamente sorted()
cars = ['bmw', 'audi', 'toyota','subaru']
print("Esta lista é a original: ")
print(cars)
print(sorted(cars))
print("\nEsta é a lista original de novo: ")
print(cars)

# metodo ordenar reversamente
cars = ['bmw', 'audi', 'toyota','subaru']
print(cars)
cars.reverse()
print(cars)
'''
# descobrindo o tamanho da lista
cars = ['bmw', 'audi', 'toyota','subaru']
len(cars)