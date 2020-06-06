import json
with open('base.json') as file:
	data = json.load(file)

rutaEnc=[]

carpEnc=[]

AxV=[]

carpSig=[]
	
def primeroAnchura(Carpeta,Archivo):
	print("------------------------------------------")
	if carpSig:
			contX=0
			print("Faltan por comprobar (Carpetas)")
			print(carpSig)
			for s in carpSig:
				contX = contX +1 
			if contX > 1:
				print("Ubicacion Actual")
				print(carpSig[0])
				del carpSig[0]
				
				
		
	if AxV:
		del AxV[:]
	if Carpeta == Archivo:
		return Archivo

	for d in data:
		if d[0] == Carpeta:
			print(d[0]+"/"+d[1])
			AxV.append(d[0])
			carpSig.append(d[1])
			if d[1] == Archivo:
				arch = primeroAnchura(d[1],Archivo)
				if arch:
					return arch
	
	
	carpEnc.append(list(set(AxV)))
	if carpEnc:
		print("Ruta Recorrida "+str(carpEnc))
		print("Siguiente Carpeta ")
		print(carpSig[0])
		rutaEnc.append(carpSig[0])
		print("-----------------------")
		return primeroAnchura(carpSig[0],Archivo)


	
arch=primeroAnchura("C:","MonasChinasOnline.exe")
print("Se encontro el archivo  UwU")
print(arch)
rt = []
if arch:
	for r in rutaEnc:
			if r not in rt:
				rt.append(r)
	print("Carpetas")
	print(rt)
else:
	print("No existe")