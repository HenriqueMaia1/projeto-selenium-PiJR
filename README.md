# 🛒 Web Scraping no Swag Labs com SeleniumBase

Projeto prático de automação e web scraping em um e-commerce de testes (Swag Labs), utilizando **SeleniumBase** com Python.

---

## 🚀 Objetivo

Este script automatiza as seguintes etapas no site [Swag Labs](https://www.saucedemo.com):

- Login automatizado com credenciais padrão
- Extração de todos os produtos disponíveis (nome, descrição e preço)
- Adição de todos os produtos ao carrinho
- Preenchimento automático do formulário de checkout
- Raspagem das informações finais da compra
- Verificação da mensagem de confirmação
- Salvamento dos dados em arquivos `.json`

---

## 📂 Estrutura do Projeto

```bash
web-scraping-swaglabs/
├── data/
│ ├── produtos.json # Dados extraídos dos produtos
│ └── checkout_info.json # Informações finais do pedido
├── src/
│ └── swaglabs_scraper.py # Código principal da automação
├── .gitignore
├── requirements.txt
├── README.md
```
---

## 🧪 Como executar

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/web-scraping-swaglabs.git
cd web-scraping-swaglabs
```
---

2. Ative seu ambiente virtual e instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o teste com SeleniumBase:

```bash
pytest src/swaglabs_scraper.py
```
---

⚠️ É necessário ter o Google Chrome instalado.

---

📄 Requisitos Técnicos:

- Python 3.8+

- SeleniumBase

- pytest

---

