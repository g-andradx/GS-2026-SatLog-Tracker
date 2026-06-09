import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import streamlit as st



df = pd.read_csv("satlog_data.csv")
print(df.head())
print(df.info())

duplicates = df.duplicated().sum()
print("numero de dados duplicados", duplicates)
#primeiro é necessario verificar se existem duplicatas no code
#verificar a presença de outliers
plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.title("boxplot, para detectar outliers")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='tipo_carga', data=df)
plt.title("Distribuição das cargas")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='risco', data=df)
plt.title("Distribuição dos riscos")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='sinal_satelite', data=df)
plt.title("Distribuição do sinal do satelite")
plt.xticks(rotation=45)
plt.show()

media = df["atraso_horas"].mean()

sns.barplot(
    x=["atraso_horas"],
    y=[media]
)

plt.title("Média de atrasps")
plt.show()

 #Correlação entre as features numéricas
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
#aqui na parte de cima faz considerar como numéricas todas as colunas que sejam inteiras ou decimais
plt.figure(figsize=(12, 8))
sns.heatmap(df.select_dtypes(include=numerics).corr(), annot=True, cmap='coolwarm')
plt.title("Matriz de Correlação")
plt.show()

# Separando features e labels
X = df.drop(columns=['risco',"carga_id"])
y = df['risco']

# Label Encoder para a variável alvo
le = LabelEncoder()
y = le.fit_transform(y)

# Lista de colunas categóricas e aplicação de One-Hot Encoding
categorical_cols = ['status_rota', 'sinal_satelite','tipo_carga']
ohe = OneHotEncoder(handle_unknown='ignore')
X_encoded = pd.DataFrame(ohe.fit_transform(X[categorical_cols]).toarray())
X_encoded = X_encoded.add_prefix('OHE_')

# Removendo colunas categóricas originais
X = X.drop(categorical_cols, axis=1)

# Concatenando features numéricas + categóricas codificadas
X = pd.concat([X, X_encoded], axis=1)

# Dividindo treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Normalização
scaler = MinMaxScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Random Forest
rf = RandomForestClassifier(n_estimators=25)
rf.fit(X_train_scaled, y_train)
y_pred_rf = rf.predict(X_test_scaled)
print("Acurácia Random Forest:", accuracy_score(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))

# Criando matriz de confusão
cm = confusion_matrix(y_test, y_pred_rf)

# Plotando heatmap
plt.figure(figsize=(6,5))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=le.classes_,
    yticklabels=le.classes_
)

plt.xlabel("Previsto")
plt.ylabel("Real")
plt.title("Matriz de Confusão - Random Forest")
plt.show()

#DASHBOARD
st.title("SatLog Tracker — Monitoramento de Cargas por Satélite")
st.write("sistema que analisa dados de GPS, satélite e sensores para prever o risco logístico das cargas.")

total_cargas = df["carga_id"].nunique()
cargas_risco_alto = df[df["risco"] == "Alto"].shape[0]
media_atraso = df["atraso_horas"].mean()
temperatura_media = df["temperatura_carga"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Cargas monitorados", total_cargas)
col2.metric("Cargas com risco alto", cargas_risco_alto)
col3.metric("Media de atraso",f"{media_atraso:.1f}H")
col4.metric("Temperatura Média das carga", f"{temperatura_media:.1f}C")

st.sidebar.header("Filtros")

filtro_carga = st.sidebar.multiselect(
    "Tipo de Carga",
    df["tipo_carga"].unique(),
    default=df["tipo_carga"].unique()
)

filtro_risco = st.sidebar.multiselect(
    "Risco",
    df["risco"].unique(),
    default=df["risco"].unique()
)

filtro_status = st.sidebar.multiselect(
    "status da rota",
    df["status_rota"].unique(),
    default=df["status_rota"].unique())

filtro_sinal = st.sidebar.multiselect(
    "sinal de satelite",
    df["sinal_satelite"].unique(),
    default=df["sinal_satelite"].unique()
)
df_filtrado = df[
    (df["tipo_carga"].isin(filtro_carga)) &
    (df["risco"].isin(filtro_risco)) &
    (df["status_rota"].isin(filtro_status)) &
    (df["sinal_satelite"].isin(filtro_sinal))]

import plotly.express as px

# =========================
# GRÁFICO 1 - RISCO
# =========================

fig = px.histogram(
    df_filtrado,
    x="risco",
    color="risco",
    title="Quantidade de Cargas por Nível de Risco",
    text_auto=True
)

fig.update_layout(
    xaxis_title="Nível de Risco",
    yaxis_title="Quantidade de Cargas",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# GRÁFICO 2 - TIPO DE CARGA
# =========================

fig = px.histogram(
    df_filtrado,
    x="tipo_carga",
    color="risco",
    barmode="group",
    title="Distribuição de Risco por Tipo de Carga",
    text_auto=True
)

fig.update_layout(
    xaxis_title="Tipo de Carga",
    yaxis_title="Quantidade",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# =========================
# GRÁFICO 3 - ATRASO MÉDIO
# =========================

atraso_medio = (
    df_filtrado
    .groupby("risco", as_index=False)["atraso_horas"]
    .mean()
)

fig = px.bar(
    atraso_medio,
    x="risco",
    y="atraso_horas",
    color="risco",
    title="Atraso Médio por Nível de Risco",
    text="atraso_horas"
)

fig.update_traces(
    texttemplate="%{text:.2f}h",
    textposition="outside"
)

fig.update_layout(
    xaxis_title="Nível de Risco",
    yaxis_title="Atraso Médio (Horas)",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

df_dash = df.drop(columns=["temperatura_carga","velocidade_media_kmh","distancia_destino_km"])
st.title("DADOS DAS CARGAS")
st.write(df_dash)

st.title("PREVER DADOS DE RISCO")
st.write("insira dados para que nossa machine learning treinada possa prever o seu risco")
temperatura_carga = st.number_input("Temperatura da carga")
velocidade_media_kmh = st.number_input("velocidade media em KMH")
distancia_destino_km = st.number_input("Distancia do Destino em Km")
atraso_horas = st.number_input("Atraso em horas")
status_rota = st.selectbox(
    "status da rota",
    ["Parado", "Desvio", "Normal"])
sinal_satelite = st.selectbox(
    "Sinal do satelite",
    ["Medio","Fraco","Forte"])
tipo_carga = st.selectbox(
    "tipo da carga",
    ["Medicamento","eletronico","Alimento"])

if st.button("Prever"):

    dados_numericos = pd.DataFrame({
        "temperatura_carga": [temperatura_carga],
        "velocidade_media_kmh": [velocidade_media_kmh],
        "distancia_destino_km": [distancia_destino_km],
        "atraso_horas": [atraso_horas]
    })

    dados_categoricos = pd.DataFrame({
        "status_rota": [status_rota],
        "sinal_satelite": [sinal_satelite],
        "tipo_carga": [tipo_carga]
    })

    dados_ohe = ohe.transform(dados_categoricos).toarray()

    dados_ohe_df = pd.DataFrame(
        dados_ohe,
        columns=[f"OHE_{i}" for i in range(dados_ohe.shape[1])]
    )
    input_df = pd.concat(
        [dados_numericos, dados_ohe_df],
        axis=1
    )

    input_scaled = scaler.transform(input_df)

    pred = rf.predict(input_scaled)

    resultado = le.inverse_transform(pred)

    if resultado[0] == "Alto":
        st.error("Risco Alto")
    elif resultado[0] == "Medio":
        st.warning("Risco Médio")
    else:
        st.success("Risco Baixo")

