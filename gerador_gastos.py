import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. Gerando dados aleatórios.

np.random.seed(42) # faz com que os dados sejam os mesmos sempre que o script for excutado 

# Gerarndo 150 idades entre 18 e 65 anos
idades = np.random.randint(18, 66, 150)

# Gerando gastos mensais com medicamentos (gasto aumenta com a idade)
gastos = np.random.normal(loc=idades * 3, scale=25)
gastos = np.clip(gastos, a_min=10, a_max=225)  # não permite valores negativos

# Criar DataFrame (tabela)
df = pd.DataFrame({
    "Idade": idades,
    "Gasto_Mensal_Medicamentos_R$": gastos.round(2)
})


# 2. Salvando como arquivo CSV

nome_do_arquivo = "dados_gastos_medicamentos.csv"
df.to_csv(nome_do_arquivo, index=False)  # index=False evita salvar a coluna de índice
print(f"Arquivo CSV salvo com sucesso: {nome_do_arquivo}")


# 3. Calculando correlação

correlacao = df["Idade"].corr(df["Gasto_Mensal_Medicamentos_R$"])
print(f"Correlação entre idade e gasto: {correlacao:.3f}")


# 4. Gerando o gráfico de dispersão

plt.figure(figsize=(10, 6))
plt.plot(df["Idade"], df["Gasto_Mensal_Medicamentos_R$"], '.', alpha=0.7)
plt.xlabel("Idade")
plt.ylabel("Gasto Mensal com Medicamentos (R$)")
plt.title("Relação entre Idade e Gasto com Medicamentos")
plt.grid(True)
plt.tight_layout()
plt.show()
