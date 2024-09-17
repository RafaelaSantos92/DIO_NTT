class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando...")
        print("Bicicleta parada.")
    
    def correr(self):
        print("Correndo...")

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"


'''bicicleta_01 = bicicleta("vermelha", "caloi", 2024, 899)
bicicleta_01.buzinar()
bicicleta_01.correr()
bicicleta_01.parar()



print(bicicleta_01.modelo, bicicleta_01.cor, bicicleta_01.ano, bicicleta_01.valor)
'''

bicicleta_02 = bicicleta("verde","Monarka", 2023, 599)
print(bicicleta_02)  
