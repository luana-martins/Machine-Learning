# Pre-processamento de dados não estruturados

import numpy as np # array and vector manipulation
import pandas as pd # data manipulation

testsmells_class_data = pd.read_csv("../Dados/rxJava/testsmells-class.csv")
class_data = pd.read_csv("../Dados/rxJava/class.csv")

# Removendo instâncias $Anonymous
class_data.drop(class_data[class_data["type"] == "anonymous"].index, inplace=True)
# Obtendo tamanho atual das linhas
class_data_lines = class_data.shape[0]

# Mantendo somente os nomes das classes
for i in range(class_data_lines):
  class_data.iat[i, 1] = class_data.iat[i, 1].split('.').pop()

# Removendo instâncias de classes de produção
class_data.drop(class_data[~class_data["class"].str.contains("Test")].index, inplace=True)

# Renomeando coluna de nomes de classes do testsmells_class_data
testsmells_class_data = testsmells_class_data.rename(columns={'TestFileName': 'class'})
# Removendo coluna App
testsmells_class_data = testsmells_class_data.drop(['App'], axis=1)

# Unindo dados das duas tabelas
joined_data = pd.merge(class_data, testsmells_class_data, on="class")

print(joined_data)