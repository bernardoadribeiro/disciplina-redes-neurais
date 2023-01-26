"""Gera modelo de classificacao para a base de dados Iris (especificamente)"""

# Separar colunas de atributos e coluna alvo
def separar_features_target(df):
    print(f"Separando as features do target")

    X = df.drop(columns=['Species']) # Atributos
    y = df['Species'] # Target (alvo)

    return X, y


# Separar em dados de Treino e testes
def separar_treino_test(df):
    from sklearn.model_selection import train_test_split

    X, y = separar_features_target(df)
    test_size = 0.3

    print(f"Separando em dados de treino e teste. test_size={test_size}")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    return X_train, X_test, y_train, y_test


# Treinamento e teste do modelo
def gerar_modelo(df):
    from sklearn.neural_network import MLPClassifier

    X_train, X_test, y_train, y_test = separar_treino_test(df)

    print(f"Treinando modelo")
    modelo = MLPClassifier()
    modelo.fit(X_train, y_train)     # Treina modelo com dados de Treino

    y_pred = modelo.predict(X_test)  # Realiza uma predição com os dados de Teste para testar modelo
    
    from sklearn.metrics import classification_report
    #print(f"MÉTRICAS\n", classification_report(y_test,y_pred)) # Mostra as métricas do modelo

    return modelo


import pandas as pd
df = pd.read_csv('exercicios\lista_aula_3\Iris.csv')

df = df.drop(columns=['Id'])

modelo_treinado = gerar_modelo(df)
