import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 1. Criando datas mensais

datas = pd.date_range(start="2020-01-01", end="2022-12-31", freq='MS')  # 'MS' = mês de início


# 2. Gerar dados de vendas

np.random.seed(42)

n = len(datas)
tendencia = np.linspace(100, 280, n)  # crescimento ao longo do tempo
sazonalidade = 20 * np.sin(2 * np.pi * (np.arange(n) % 12) / 12)  # ciclo anual
ruido = np.random.normal(0, 10, n)  # variação aleatória

vendas = tendencia + sazonalidade + ruido
vendas = np.clip(vendas, a_min=0, a_max=None)  # evita valores negativos


# 3. Criar DataFrame

df = pd.DataFrame({
    "Data": datas,
    "Vendas_R$": vendas.round(2)
})


# 4. Salvar como CSV

nome_arquivo = "vendas_mensais_com_sazonalidade.csv"
df.to_csv(nome_arquivo, index=False)
print(f"Arquivo salvo com sucesso: {nome_arquivo}")

# 5. Plotar

plt.figure(figsize=(12, 6))
plt.plot(df["Data"], df["Vendas_R$"], label="Vendas", color="steelblue")
plt.xlabel("Data")
plt.ylabel("Vendas (R$)")
plt.title("Vendas Mensais com Sazonalidade (2020–2022)")
plt.grid(True)
plt.tight_layout()
plt.show()
