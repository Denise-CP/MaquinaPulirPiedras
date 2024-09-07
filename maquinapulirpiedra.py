class maquinapulirpiedra:
   def __init__ (self , piedra ,pulido) :
       self.piedra = piedra
       self.pulido = pulido
       self.comezado = False
   def comenzar (self):
       self.comenzado = True
       print ("El" , self.piedra ,self.pulido ,"comenzo a pulirse")

   def terminar (self) :
       self.comenzado = False
       print ("El" , self.piedra ,self.pulido ,"termino de pulirse")   

marmol = maquinapulirpiedra ("marmol","1")
granito = maquinapulirpiedra ("granito" ,"2")

print (type(marmol))
print (type(granito))
    
print (marmol.piedra ,marmol.pulido)
print (granito.piedra ,granito.pulido)

marmol.comenzar ()
granito.comenzar ()

print (marmol.comenzado)
print (granito.comenzado)


marmol.terminar ()
granito.terminar ()

print (marmol.terminar)
print (granito.terminar)















