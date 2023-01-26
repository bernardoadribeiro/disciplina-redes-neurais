from ex1_fit_model_iris import modelo_treinado


"""
    Features: ['SepalLengthCm' 'SepalWidthCm' 'PetalLengthCm' 'PetalWidthCm']
"""

modelo = modelo_treinado

#print(modelo_treinado.feature_names_in_)

SepalLengthCm = float(input("Comprimento da Sepala (cm): "))
SepalWidthCm  = float(input("Largura da Sepala (cm): "))
PetalLengthCm = float(input("Comprimento da Petala (cm): "))
PetalWidthCm = float(input("Largura da Petala (cm): "))

predicao = modelo.predict([[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]])

print(f"Categoria da Flor: ", predicao)
