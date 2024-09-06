class MaquinaPulirPiedras:
    def __init__(self):
        self.prendida = False
        self.piedras_pulidas = 0

    def prender(self):
        self.prendida = True
        print("La maquina esta prendida.")

    def pulir_piedra(self, tipo_piedra):
        if not self.prendida:
            raise Exception("La maquina esta apagada. prendela primero.")
        
        nivel_pulido = {"granito": 3, "marmol": 5, "cuarzo": 7}
        if tipo_piedra not in nivel_pulido:
            raise ValueError("Tipo de piedra no reconocido.")
        
        self.piedras_pulidas += 1
        return f"Piedra de {tipo_piedra} pulida al nivel {nivel_pulido[tipo_piedra]}."

    def apagar(self):
        self.encendida = False
        print("La maquina esta apagada.")

    def __str__(self):
        estado = "prendida" if self.prendida else "apagada"
        return f"Maquina de pulir piedras - Estado: {estado}, Piedras pulidas: {self.piedras_pulidas}"

if __name__ == "__main__":
    maquina = MaquinaPulirPiedras()
    maquina.prender()
    print(maquina.pulir_piedra("granito"))
    maquina.apagar()
    print(maquina)





    

