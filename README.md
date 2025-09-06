# 📊 Graph API - API de Gráficos Analíticos

Uma API desenvolvida em Python usando **FastAPI**, que permite gerar gráficos analíticos, calcular estatísticas básicas e manipular arquivos CSV. Ideal para integrar em diferentes projetos, aplicativos ou dashboards.

---

## 🛠 Funcionalidades Atuais

### 1. Gráficos (`chart_service`)
- Tipos suportados:
  - `line` → gráfico de linha
  - `column` → gráfico de colunas verticais
  - `bar` → barras horizontais
  - `scatter` → gráfico de dispersão
  - `pie` → gráfico de pizza
  - `area` → gráfico de área preenchida
- Personalizações básicas: título, nomes de eixos.
- Retorno em **base64**, pronto para uso em qualquer frontend ou app.

### 2. Estatísticas (`stats_service`)
- Calcula estatísticas simples a partir de uma lista de números:
  - Média, mediana
  - Mínimo, máximo
  - Desvio padrão

### 3. Arquivos (`file_service`)
- Upload de arquivos CSV (ou Excel futuramente)
- Leitura e conversão em DataFrame para uso nos gráficos e estatísticas
- Retorna metadados do arquivo (nome, tamanho)

---

## 🗂 Estrutura do Projeto

graph-api/
├── main.py
├── app/
│   ├── routes/
│   │   ├── charts.py
│   │   ├── stats.py
│   │   └── files.py
│   ├── services/
│   │   ├── chart\_service.py
│   │   ├── stats\_service.py
│   │   └── file\_service.py
│   ├── models/
│   │   ├── chart\_models.py
│   │   ├── stats\_models.py
│   │   └── file\_models.py
│   └── utils/
├── examples/
│   └── sample.csv
└── requirements.txt

````

---

## ⚡ Como Rodar

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/graph-api.git
cd graph-api
````

2. **Crie e ative um ambiente virtual**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Rodar a API**

```bash
uvicorn main:app --reload
```

> A API estará disponível em: `http://127.0.0.1:8000`
> A documentação automática estará em: `http://127.0.0.1:8000/docs`

---

## 📌 Exemplos de Uso

### 1. Gerar Gráfico (POST /charts/generate)

```json
POST /charts/generate
{
  "x": ["Jan", "Feb", "Mar"],
  "y": [100, 200, 150],
  "chart_type": "column",
  "title": "Vendas Mensais",
  "xlabel": "Mês",
  "ylabel": "Vendas"
}
```

Retorno:

```json
{
  "image_base64": "iVBORw0K..."
}
```

### 2. Calcular Estatísticas (POST /stats/calculate)

```json
POST /stats/calculate
{
  "values": [10, 20, 30, 40]
}
```

Retorno:

```json
{
  "mean": 25,
  "median": 25,
  "min": 10,
  "max": 40,
  "stdev": 12.909944487358056
}
```

### 3. Upload de Arquivo (POST /files/upload)

Envie um arquivo CSV via multipart/form-data:

```bash
curl -F "file=@sample.csv" http://127.0.0.1:8000/files/upload
```

Retorno:

```json
{
  "filename": "sample.csv",
  "size": 1234,
  "message": "Upload concluído com sucesso"
}
```

---

## 📝 Observações

* Todos os endpoints usam **Pydantic Models**, garantindo validação e documentação automática.
* Serviços (`chart_service`, `stats_service`, `file_service`) são separados da API para **reuso e testes**.

```
