# 🍕 Sistema de Pizzaria

Sistema web desenvolvido em **Django** para gerenciamento de uma pizzaria, permitindo o cadastro e gerenciamento de pizzas e categorias, além de uma funcionalidade de consulta de CEP.

O projeto foi desenvolvido como parte das atividades da **Fábrica de Software 2026.2**.

---

## 📋 Sobre o Projeto

O sistema tem como objetivo facilitar o gerenciamento dos produtos de uma pizzaria, permitindo que o usuário cadastre, visualize, edite e exclua pizzas e suas respectivas categorias.

O sistema também possui integração com a API **ViaCEP**, possibilitando a consulta de endereços através do CEP informado.

---

## 🚀 Funcionalidades

### 🍕 Gerenciamento de Pizzas

* Listagem de pizzas cadastradas
* Cadastro de novas pizzas
* Edição de pizzas
* Exclusão de pizzas
* Cadastro de preço
* Cadastro de descrição
* Associação da pizza a uma categoria
* Upload de imagem da pizza
* Alteração da imagem da pizza

### 🏷️ Gerenciamento de Categorias

* Listagem de categorias
* Cadastro de categorias
* Edição de categorias
* Exclusão de categorias
* Descrição das categorias
* Visualização da quantidade de pizzas associadas

### 📍 Consulta de CEP

* Consulta de CEP utilizando a API ViaCEP
* Retorno dos dados do endereço
* Tratamento de CEP inexistente
* Tratamento de erros de comunicação com a API

### 🎨 Interface

* Layout baseado em `base.html`
* Navegação entre as principais áreas do sistema
* Cards para apresentação das pizzas e categorias
* Botões para ações de cadastro, edição e exclusão
* Interface adaptada para diferentes tamanhos de tela

---

## 🛠️ Tecnologias Utilizadas

### Backend

* Python
* Django
* Django REST Framework

### Banco de Dados

* MySQL

### Frontend

* HTML5
* CSS3
* Django Templates

### API Externa

* ViaCEP

### Ferramentas

* Visual Studio Code
* Git
* GitHub

---

## 📁 Estrutura do Projeto

```text
wsBackendFabricaDeSoftware26.2/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── produtos/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── admin.py
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── pizzas.html
│   ├── nova_pizza.html
│   ├── editar_pizza.html
│   ├── excluir_pizza.html
│   ├── categorias.html
│   ├── nova_categoria.html
│   ├── editar_categoria.html
│   ├── excluir_categoria.html
│   └── consultar_cep.html
│
├── media/
│   └── pizzas/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd wsBackendFabricaDeSoftware26.2
```

### 2. Criar o ambiente virtual

No Windows:

```bash
python -m venv venv
```

Ative o ambiente virtual:

```powershell
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` ainda não exista, ele pode ser gerado utilizando:

```bash
pip freeze > requirements.txt
```

### 4. Configurar o banco de dados

O projeto utiliza **MySQL**.

Crie um banco de dados chamado:

```text
fabrica_software
```

Depois configure as credenciais do banco no arquivo:

```text
config/settings.py
```

Exemplo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fabrica_software',
        'USER': 'root',
        'PASSWORD': 'SUA_SENHA',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Executar as migrações

```bash
python manage.py makemigrations
```

Depois:

```bash
python manage.py migrate
```

### 6. Iniciar o servidor

```bash
python manage.py runserver
```

O sistema estará disponível em:

```text
http://127.0.0.1:8000/
```

---

## 🔗 Principais Rotas

| Página            | URL                         |
| ----------------- | --------------------------- |
| Início            | `/`                         |
| Pizzas            | `/pizzas/`                  |
| Nova Pizza        | `/pizzas/nova/`             |
| Editar Pizza      | `/pizzas/editar/<id>/`      |
| Excluir Pizza     | `/pizzas/excluir/<id>/`     |
| Categorias        | `/categorias/`              |
| Nova Categoria    | `/categorias/nova/`         |
| Editar Categoria  | `/categorias/editar/<id>/`  |
| Excluir Categoria | `/categorias/excluir/<id>/` |
| Consultar CEP     | `/consultar-cep/`           |

---

## 🔌 API REST

O projeto também possui endpoints utilizando **Django REST Framework**.

### Categorias

```text
/api/categorias/
```

### Pizzas

```text
/api/pizzas/
```

### Consulta de CEP

```text
/api/consultar-cep/<cep>/
```

---

## 🗃️ Modelos

### Categoria

O modelo `Categoria` possui:

* `nome`
* `descricao`

### Pizza

O modelo `Pizza` possui:

* `nome`
* `descricao`
* `preco`
* `imagem`
* `categoria`

Cada pizza está relacionada a uma categoria através de uma chave estrangeira.

---

## 🖼️ Upload de Imagens

As imagens das pizzas são armazenadas na pasta:

```text
media/pizzas/
```

O projeto utiliza o `ImageField` do Django para realizar o upload das imagens.

---

## 🌐 ViaCEP

A consulta de CEP utiliza a API pública do **ViaCEP**.

Exemplo de consulta:

```text
https://viacep.com.br/ws/01001000/json/
```

O sistema trata situações como:

* CEP válido
* CEP inexistente
* Falha na comunicação com o serviço

---

## 👨‍💻 Desenvolvimento

Projeto desenvolvido para a **Fábrica de Software 2026.2**.

### Integrante

**Davi Guedes**

---

## 📌 Status do Projeto

🟢 **Concluído para a etapa atual do projeto.**

O sistema possui as principais funcionalidades de gerenciamento de pizzas e categorias, upload de imagens, consulta de CEP e API REST.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos e educacionais.
