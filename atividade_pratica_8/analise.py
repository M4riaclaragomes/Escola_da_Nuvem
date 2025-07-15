# Importar bibliotecas necessárias
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o conjunto de dados de câncer de mama
# Este dataset é comumente usado para problemas de classificação binária.
# A variável 'data' contém as características e 'target' contém os rótulos (0 para maligno, 1 para benigno).
cancer = load_breast_cancer()
X = cancer.data  # Características
y = cancer.target  # Variável target (0: maligno, 1: benigno)

# Dividir o conjunto de dados em treino e teste
# 70% dos dados serão usados para treino e 30% para teste.
# 'random_state' garante que a divisão seja a mesma cada vez que o código for executado.
# 'stratify=y' garante que a proporção das classes (maligno/benigno) seja mantida tanto no treino quanto no teste.
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Inicializar e treinar o modelo Random Forest
# O Random Forest é um algoritmo de ensemble que constrói múltiplas árvores de decisão
# e as combina para obter uma previsão mais precisa e estável.
modelo_rf = RandomForestClassifier(random_state=42) # Usamos random_state para reprodutibilidade
modelo_rf.fit(X_treino, y_treino)

# Fazer previsões no conjunto de teste
# 'y_pred' são as previsões das classes (0 ou 1)
# 'y_pred_proba' são as probabilidades de cada classe, necessárias para calcular a AUC-ROC
y_pred = modelo_rf.predict(X_teste)
y_pred_proba = modelo_rf.predict_proba(X_teste)[:, 1] # Probabilidade da classe positiva (benigno)

# Calcular as métricas de classificação

# Precisão (Precision): Proporção de verdadeiros positivos entre todos os resultados classificados como positivos.
# É importante quando o custo de um falso positivo é alto.
precisao = precision_score(y_teste, y_pred)

# Recall (Sensibilidade): Proporção de verdadeiros positivos entre todos os casos positivos reais.
# É importante quando o custo de um falso negativo é alto (neste caso, não detectar um câncer).
recall = recall_score(y_teste, y_pred)

# F1-Score: Média harmônica da Precisão e do Recall.
# É uma boa métrica quando você precisa de um equilíbrio entre Precisão e Recall.
f1 = f1_score(y_teste, y_pred)

# AUC-ROC (Area Under the Receiver Operating Characteristic Curve):
# Mede a capacidade do modelo de distinguir entre classes.
# Um valor próximo de 1 indica um modelo com excelente poder de discriminação.
auc_roc = roc_auc_score(y_teste, y_pred_proba)

# Imprimir as métricas calculadas
print(f"Métricas de Classificação do Modelo Random Forest:")
print(f"--------------------------------------------------")
print(f"Precisão (Precision): {precisao:.4f}")
print(f"Recall (Sensibilidade): {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print(f"AUC-ROC: {auc_roc:.4f}")
print(f"--------------------------------------------------")

# Gerar e exibir a Matriz de Confusão
# A Matriz de Confusão mostra o número de previsões corretas e incorretas.
# Verdadeiro Negativo (TN): Previu 0, era 0
# Falso Positivo (FP): Previu 1, era 0
# Falso Negativo (FN): Previu 0, era 1
# Verdadeiro Positivo (TP): Previu 1, era 1
cm = confusion_matrix(y_teste, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=cancer.target_names, yticklabels=cancer.target_names)
plt.xlabel('Previsão')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusão')
plt.show()

