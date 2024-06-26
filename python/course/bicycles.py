'''
# conceitos de lista
bicycles = ['trek', 'cannodale', 'redline', 'specialized','speed', 'magrelinha']
print (bicycles[2].title()) # formatando para iniciar maiuscula
print (bicycles[3].title()) # formatando para iniciar maiuscula
print (bicycles[-1]) # formatando para iniciar maiuscula

message = "minha primeira bicicleta foi a " + bicycles[0].title()+ ", e minha ultima foi a " +bicycles[-1] + "." 
print (message)

# modificando

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0]= 'ducati' # modifica o indice 0 de honda para ducati
print(motocycles)

motocycles.append('Wayady') # acrescenta
print(motocycles)

# criando lista dinamica com append
frutas = []
frutas.append('pera')
frutas.append('uva')
frutas.append('maça')
frutas.append('banana')
print(frutas)
'''
# adicionando elementos em uma lista com metodo insert
cidade = ['natal','belem'] 
cidade.insert(1, 'rio')
print(cidade)