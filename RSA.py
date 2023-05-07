#funcion para establecer numeros primos 
def verifica_primo(n):
	c=0
	x=2
	if n>=2:
		while x<=n/2:
			if n%x==0:
				c=c+1
				x=x+1
			else:
				x=x+1
		if c==0:
			return True
		else:
			return False
	else:
		return False
#funcion para generar numeros primos
def genera_primos(n):
	lp=[]
	x=2
	while n!=0:
		if verifica_primo(x)==True:
			lp.append(x)
			x=x+1
			n=n-1
		else:
			x=x+1
	return lp
def pyq():
	
	p=int(input("\tValor de (p)="))
	while verifica_primo(p)==False:
		print("\t(p) tiene que ser un numero primo !!!")
		p=int(input("\tValor de (p)="))
	q=int(input("\tValor de (q)="))
	while verifica_primo(q)==False or q==p:
		print("\t(q) tiene que ser un numero primo diferente de (p) !!!")
		q=int(input("\tValor de (q)="))
	lpq=[p,q]
	return lpq
#funcion para calcular e
def calculae(ø):
	e=2
	le=[]
	while e>1 and e<ø :
		if mcd(e,ø)==1:
			le.append(e)
			e=e+1
		else:
			e=e+1
	print("\nVALORES PARA (e)="+str(le))
	e=int(input("\n\tValor de (e)="))
	while mcd(e,ø)!=1:
		print("\n\tEliga un valor de la lista !!!")
		e=int(input("\n\tValor de (e)="))
	return e

def mcd(e,ø):
	m=ø%e
	while m!=0:
		ø=e
		e=m
		m=ø%e
	return e
#funcion para indentificar el numero de rango para e
def congruente(e,ø):
	k=1
	m=(1+(k)*(ø))%(e)
	while m!=0:
		k=k+1
		m=(1+(k)*(ø))%(e)
	d=int((1+(k)*(ø))/(e))
	return d
#funcion para definir insertar el cifrado a cada letra de la palabra
def cifrarmensaje(msj,key):
	msj=msj.upper()
	lm=msj.split(" ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=cifrarpalabra(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc
#funcion para sustituir cada letra por palabra para cifrar
def cifrarpalabra(m,k):
	lpc=[]
	lp=[]
	n,e=k
	cpc=""
	for i in m:
		x=buscarpos(i)
		lp.append(x)
	for j in lp:
		c=(j**e)%n
		lpc.append(c)
	for k in lpc:
		cpc=cpc+str(k)+" "
	return cpc	
# funcion para buscar posicion de cada lera por metodo append
def buscarpos(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==i:
			return c
		else:
			c=c+1	
#funcion para descifrar mensaje
def descifrarmensaje(msj,key):
	msj=msj.upper()
	lm=msj.split("  ")
	cmc=""
	lmc=[]
	for i in lm:
		pal=descifrarnumero(i,key)
		lmc.append(pal)
	for j in lmc:
		cmc=cmc+str(j)+" "
	return cmc
#funcion para descifrar cada numero y convertir a letra
def descifrarnumero(m,k):
	lnc=[]
	ln=[]
	n,d=k
	cnc=""
	men=m.split(" ")
	for i in men:
		x=int(i)
		ln.append(x)
	for j in ln:
		m=(j**d)%n
		lnc.append(m)
	for k in lnc:
		l=buscarlet(k)
		cnc=cnc+str(l)
	return cnc
#funcion para buscar el equivalente al numero de la letra
def buscarlet(x):
	alf="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
	c=0
	for i in alf:
		if x==c:
			return i
		else:
			c=c+1	
#ingresar valores para variable p y q
print("\n Elige valores para las variables (p) y (q) DEBEN DE SER PRIMOS Y NO REPETIDOS ")
lista_primos=genera_primos(50)

p,q=pyq()
print("\t(p)="+str(p)+"\n\t(q)="+str(q))

n=p*q

ø=(p-1)*(q-1)

#Se calcula e

e=calculae(ø)

#se calcula la congruencia de datos

d=congruente(e,ø)
#generacion de llave publica y privada
key_public=[n,e]
key_private=[n,d]
print("\n\tLLAVE PUBLICA="+str(key_public)+"\n\tLLAVE PRIVADA="+str(key_private))

print("\n Encryptar mensaje por metodo RSA")
mensaje=input("\n\tMensaje : ")
mensaje_cifrado=cifrarmensaje(mensaje,key_public)
print("\tMensaje Cifrado : "+str(mensaje_cifrado))
#se muestra el resultado de la desencriptacion
print("\n Descifrar mensaje por metodo RSA")
mensaje_cifrado=input("\n\tMensaje Cifrado : ")
mensaje_descifrado=descifrarmensaje(mensaje_cifrado,key_private)
print("\tMensaje Descifrado : "+str(mensaje_descifrado))