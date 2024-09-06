class MaquinaPulirPiedras:
    def __init__(self):
        self.encendida = False
        self.piedras_pulidas = 0

    def encender(self):
        self.encendida = True
        print("La máquina está encendida.")

    def pulir_piedra(self, tipo_piedra):
        if not self.encendida:
            raise Exception("La máquina está apagada. Enciéndela primero.")
        
        nivel_pulido = {"granito": 3, "mármol": 5, "cuarzo": 7}
        if tipo_piedra not in nivel_pulido:
            raise ValueError("Tipo de piedra no reconocido.")
        
        self.piedras_pulidas += 1
        return f"Piedra de {tipo_piedra} pulida al nivel {nivel_pulido[tipo_piedra]}."

    def apagar(self):
        self.encendida = False
        print("La máquina está apagada.")

    def __str__(self):
        estado = "encendida" if self.encendida else "apagada"
        return f"Máquina de pulir piedras - Estado: {estado}, Piedras pulidas: {self.piedras_pulidas}"

if __name__ == "__main__":
    maquina = MaquinaPulirPiedras()
    maquina.encender()
    print(maquina.pulir_piedra("granito"))
    maquina.apagar()
    print(maquina)








    

