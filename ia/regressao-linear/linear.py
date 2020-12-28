from matplotlib import pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from math import sqrt

# Criando na variável df um dataset baseado na leitura do csv.
df = pd.read_csv("FuelConsumptionCo2.csv")

# Mostrando os 5 primeiros elementos desse dataset
print(df.head())

# Exibe o resumo do dataset
print(df.describe())

# Selecionando apenas as features dos motores e emissão de CO2 dos carros datados.
motores = df[['ENGINESIZE']]
co2 = df[['CO2EMISSIONS']]

# Mostrandos os 5 primeiros elementos de cada variável.
print(motores.head())
print(co2.head())

# Dividindo as variáveis de motores e co2 em 4 bases de dados: treino para motores, teste para motores...
motores_treino, motores_test, co2_treino, co2_teste = train_test_split(
    motores, co2, test_size=0.2, random_state=42)
print(motores_treino)

# Plotando o gráfico com as co-relações entre motores e emissão de CO2. X = Motor, Y = Emissão de CO2
plt.scatter(motores_treino, co2_treino, color='blue')
plt.xlabel("Motor")
plt.ylabel("Emissão de CO2")
plt.show()

# Definindo o tipo de modelo
modelo = linear_model.LinearRegression()

# Treinando o modelo utilizando o dataset de treino para encontrar o valor de A e B da fórmula: Y = A + BX
# FIT = TREINAMENTO
modelo.fit(motores_treino, co2_treino)

# Mostrando os coeficientes encontrados dos valores de A e B
print('(A) Intercepto: ', modelo.intercept_)
print('(B) Inclinação: ', modelo.coef_)

# MOSTRANDO EM GRÁFICO A REGRESSÃO LINEAR FEITA PELO TREINAMENTO
plt.scatter(motores_treino, co2_treino, color='blue')
plt.plot(motores_treino, modelo.coef_[
         0][0]*motores_treino + modelo.intercept_[0], '-r')
plt.ylabel("Emissão de C02")
plt.xlabel("Motores")
plt.show()

# Fazendo as predições no modelo de teste
predicoesCo2 = modelo.predict(motores_test)

# Reta de regressão linear do dataset de teste
plt.scatter(motores_test, co2_teste, color='blue')
plt.plot(motores_test, modelo.coef_[0][0]
         * motores_test + modelo.intercept_[0], '-r')
plt.ylabel("Emissão de C02")
plt.xlabel("Motores")
plt.show()

# Mostrando todas as métricas obtidas através dos testes
print("Soma dos Erros ao Quadrado (SSE): %.2f " %
      np.sum((predicoesCo2 - co2_teste)**2))
print("Erro Quadrático Médio (MSE): %.2f" %
      mean_squared_error(co2_teste, predicoesCo2))
print("Erro Médio Absoluto (MAE): %.2f" %
      mean_absolute_error(co2_teste, predicoesCo2))
print("Raiz do Erro Quadrático Médio (RMSE): %.2f " %
      sqrt(mean_squared_error(co2_teste, predicoesCo2)))
print("R2-score: %.2f" % r2_score(co2_teste, predicoesCo2))
