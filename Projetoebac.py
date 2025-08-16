import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de visualização
pd.set_option('display.max_columns', None)
sns.set(style="whitegrid", palette="pastel")

# Carregar o dataset
df = pd.read_csv("The impact of artificial intelligence on society.csv", encoding="latin1")

# Informações básicas
print("\n Informações gerais do dataset:")
print(df.info())

print("\n Primeiras 5 linhas:")
print(df.head())
    
# Verificar valores ausentes
print("\n Valores nulos por coluna:")
print(df.isnull().sum())

df["What is your occupation? (optional)"] = df["What is your occupation? (optional)"].fillna("Não respondido")

# Padronizar os valores da coluna de ocupação
df["What is your occupation? (optional)"] = df["What is your occupation? (optional)"].str.strip()   # remove espaços extras
df["What is your occupation? (optional)"] = df["What is your occupation? (optional)"].str.lower()   # coloca tudo em minúsculo
df["What is your occupation? (optional)"] = df["What is your occupation? (optional)"].str.title()   # primeira letra maiúscula

# Conferir valores únicos após padronização
print(df["What is your occupation? (optional)"].unique())

# Refazer a contagem
ocupacoes = df["What is your occupation? (optional)"].value_counts()
print(ocupacoes)
 
# Conferindo se ainda existem nulos
print(df["What is your occupation? (optional)"].isnull().sum())

# Estatísticas descritivas
print("\n Estatísticas descritivas (todas as variáveis):")
print(df.describe(include="all"))

# Distribuição por variáveis categóricas
cat_cols = df.select_dtypes(include=["object"]).columns

for col in cat_cols:
    plt.figure(figsize=(8, 4))
    df[col].value_counts(dropna=False).plot(kind='bar', color='skyblue')
    plt.title(f"Distribuição de {col}")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Frequência")
    plt.tight_layout()
    plt.show()

# Geração de insights básicos
print("\n INSIGHTS AUTOMÁTICOS:")

idade_top = df["What is your age range?"].value_counts().idxmax()
idade_freq = df["What is your age range?"].value_counts().max()
print(f"- Faixa etária mais comum: {idade_top} ({idade_freq} respondentes)")

genero_top = df["What is your gender?"].value_counts().idxmax()
genero_freq = df["What is your gender?"].value_counts().max()
print(f"- Gênero predominante: {genero_top} ({genero_freq} respondentes)")

educ_top = df["What is your education level?"].value_counts().idxmax()
print(f"- Escolaridade mais comum: {educ_top}")

prof_top = df["What is your occupation? (optional)"].value_counts().idxmax()
print(f"- Ocupação mais citada: {prof_top}")

uso_top = df["How often do you use technological devices?"].value_counts().idxmax()
print(f"- Uso mais frequente de dispositivos tecnológicos: {uso_top}")

conhecimento_top = df["How much knowledge do you have about artificial intelligence (AI) technologies?"].value_counts().idxmax()
print(f"- Nível de conhecimento sobre IA mais comum: {conhecimento_top}")

media_uso_ai = df["Please rate how actively you use AI-powered products in your daily life on a scale from 1 to 5."].mean()
print(f"- Média de uso de produtos com IA: {media_uso_ai:.2f} (escala de 1 a 5)")

conf_top = df["Do you generally trust artificial intelligence (AI)?"].value_counts().idxmax()
print(f"- Confiança predominante na IA: {conf_top}")

impacto_top = df["Do you think artificial intelligence (AI) will be generally beneficial or harmful to humanity?"].value_counts().idxmax()
print(f"- Opinião mais comum sobre impacto da IA: {impacto_top}")

etica_top = df["Do you believe that artificial intelligence (AI) should be limited by ethical rules?"].value_counts().idxmax()
print(f"- Posição mais comum sobre limites éticos: {etica_top}")

nao_ia_top = df["Which of the following do you think is NOT an artificial intelligence (AI) application?"].value_counts().idxmax()
print(f"- Aplicação mais citada como não sendo IA: {nao_ia_top}")

chatgpt_top = df["The artificial intelligence application called 'ChatGPT' is an example of which type of AI system?"].value_counts().idxmax()
print(f"- Tipo mais atribuído ao ChatGPT (certo ou errado): {chatgpt_top}")

print("\n Fim da análise automática.")

# Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv("The impact of artificial intelligence on society EDA realizado 01.csv", index=False, encoding="latin1")
