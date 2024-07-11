print (" 1) Letras maiusculas nas iniciais das palavras:")
name = "luis orlando"
print(name.title())

print (" 2) Maiusculas e Minusculas:")
name = "Luis Orlando"
print(name.upper())
print(name.lower())

print (" 3) concatenando")
first_name = "Luis"
last_name = "Orlando"
full_name = first_name + " " + last_name
print(full_name)


print (" 4) Acrescentar espaços em Branco:")
print (" oi mundo")
print ("\t oi mundo") # add uma tabulação

print (" 5) Quebras de linhas:")
print ("Languages: \nPython\nC\nJavaScript") 

print (" 6) Tabulação e Quebras de linhas:")
print ("Languages: \n\tPython\n\tC\n\tJavaScript")

print (" 6) Removendo espaços vazios:")
favorite_language = '  python  '

favorite_language.rstrip() #lado direito

favorite_language.lstrip () #lado esquerdo

favorite_language.strip () #ambos os lado 

print(favorite_language)

print (" 7) Evitando erro de Aspas e sintaxe:")
exemplo = " o de aspas 'simples' se tiver dentro de aspas duplas sem pro! "
print(exemplo)

exemplo = ' o contrario tambem funciona aspas "duplas" se tiver dentro de aspas simples sem pro! '
print(exemplo)


