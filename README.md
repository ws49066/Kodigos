# Kodigos Estoques
---
## Tecnologias Usadas no Front-End
- Node.js 
- Axios 
- Bootstrap
- Font Awesome
- React.js
- JSX
- CSS
- JavaScript

---

## Tecnologias Usadas no Back-End
- Postgresql - Banco de Dados 
- Python3
---

## Sistema Operacional Linux Ubuntu 20.04 


## Instalação de Ferramentas e inicialização do servidor backend

Postgresql (https://www.postgresql.org/download/)
```sh
 $ sudo apt-get update
 $ sudo apt-get install postgresql postgresql-contrib
```

Acessar o postgresql 
```sh
$ sudo su - postgres
$ psql
```
Crie o Bando de Dados para o nosso projeto
```sh

$ CREATE DATABASE estoque
```

Instalação do python3
```sh
$ sudo apt install python3
```

Instalação de dependencias para rodar o backend com python3
```sh
$ pip install Flask
$ pip install flask_sqlalchemy
$ pip install flask_script
$ pip install flask_migrate
$ pip install psycopg2-binary
```

Acessando a diretorio backend para migrar banco de dados usando Migrate.
```sh
$ python3 produto.py db migrate
$ python3 produto.py db upgrade
```

Acesse Produto.py e altere as entradas de acesso ao banco de dados.
user = 'postgres'
password = '123456'
host = 'localhost'
db = 'estoque'

Inicializar o servidor backend
```sh
$ FLASK_APP=produto.py FLASK_ENV=development flask run -p 3001
```
Com isso o servidor backend vai está rodando em
http://127.0.0.1:3001 ou http://localhost:3001

 * Serving Flask app "produto.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:3001/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 201-171-970

---

## Instalação de Ferramentas e inicialização do servidor Front-End

Instalação do Node js
```sh
$ sudo apt install nodejs
$ sudo apt install npm
```

acesse a pasta frontEnd e Instale as dependencias
```sh
 $ npm i
```

Inicializar Servidor front-end
```sh
 $ npm start
```





