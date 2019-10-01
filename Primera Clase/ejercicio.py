# Primer metodo
def metodoUno(n):
	return n**2
# Segundo Metodo
def metodoDos(m):
	return m+1
# Tercer metodo
def metodoTres(x):
	return x+100
# Cuarto metodo
def metodoCuatro(y):
	return x*3

# Resultados
print(metodoUno(4))
print(metodoDos(metodoUno(4)))
print(metodoTres(metodoDos(metodoTres(5))))
print(metodoUno(metodoDos(metodoTres(metodoCuatro(2)))))