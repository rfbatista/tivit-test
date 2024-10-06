# tivit-test

`git clone git@github.com:rfbatista/tivit-test.git && cd tivit-test`

# 1 Criar um ambiente virtual

```sh
python3.10 -m venv venv
source venv/bin/activate
```

# 2 Instalar dependencias

```sh
python3.10 -m venv venv
source venv/bin/activate
```

# 3 Executar aplicação

Copie o arquivo `.env.example` para `.env` e adicioner os valores esperados, exemplo:

```
SECRET_KEY=YOUR_SECRET_KEY
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Inicialize a aplicação

```
uvicorn app.main:app --reload
```

# 4 Buscar token de acesso

```sh
curl --location 'http://localhost:8000/token' \
--form 'username="admin"' \
--form 'password="JKSipm0YH"'
```

# Tentar acesso user

```sh
curl --location --request GET 'http://localhost:8000/user' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyODI1MTUyN30.jCWjyXQ9jIXsvMXVFuoy2AP21vJ1d7GcYA391QMU8K0'
```

# Tentar acesso admin

```sh
curl --location --request GET 'http://localhost:8000/admin' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyODI1MTUyN30.jCWjyXQ9jIXsvMXVFuoy2AP21vJ1d7GcYA391QMU8K0' 
```
