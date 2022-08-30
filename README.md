# Teste Prático Full Stack Python (Backend)

### Tecnologias utilizadas no Backend:
- Django
- Django Rest Framework
- Django Simple JWT
- PostgreSQL 11
- Docker compose ([como instalar](https://docs.docker.com/compose/install/))

### Casos de uso:
- Listagem, criação, edição e remoção de módulos e aulas
- Login com token JWT
- Rotas de listagens públicas
- Rotas de criação, edição e remoção privadas (necessária autenticação com JWT)

### Para rodar o projeto é preciso:
- Docker
- Docker compose ([como instalar](https://docs.docker.com/compose/install/))

### Rodando o projeto
- Vá para a raiz do projeto no terminal
- Agora, dependendo de como você instalou o docker compose, use o comando `docker-compose` ou `docker compose`
- Rode `docker-compose build` (esse comando construirá a imagem da api)
- Rode `docker-compose up`
- O banco de dados e a api já estão rodando, mas é necessário rodar as migrations e criar um usuário admin
- Em outro terminal, rode `docker-compose run api python manage.py migrate`
- Rode `docker-compose run api python manage.py createsuperuser`, digite usuário e senha fictíceis para o admin.
- Pronto! Agora siga para rodar o [frontend](https://github.com/RRFreitas/TesteVerzel-frontend)

### Screencast: [https://drive.google.com/file/d/1wUKDqTRoIb_GN9CULWu0t9Qo6NM2NEGW/view?usp=sharing](https://drive.google.com/file/d/1wUKDqTRoIb_GN9CULWu0t9Qo6NM2NEGW/view?usp=sharing)

## Endpoints

### /token/ (POST)
Endpoint de autenticação, é enviado login e senha e retornado dois tokens, um de access e outro de refresh, o de refresh tem maior duração e serve para pedir outro token de acesso
#### Exemplo de body
```json
{
  "username": "admin",
  "password": "admin123"
}
```
#### Retorno
```json
{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}
```

### /token/refresh/ (POST)
Endpoint para pedir um novo token de acesso, é enviado um token de refresh válido e é retornado um novo token de acesso e refresh.
#### Exemplo de body
```json
{
  "refresh" : "REFRESH_TOKEN"
}
```
#### Retorno
```json
{
  "access": "ACCESS_TOKEN",
  "refresh": "REFRESH_TOKEN"
}
```

### /modules/ (GET)
Endpoint público de listagem de módulos, não é necessário o envio de token.
#### Retorno
```json
[{
  "id": 1,
  "name": "Module name",
  "description": "Module description",
  "classes": [
    {
      "id": 1,
      "name": "Class 1",
      "date": "2022-10-25T22:10",
    }
  ]
}]
```

### /modules/{id} (GET)
Endpoint público para visualizar módulo, não é necessário o envio de token.
#### Retorno
```json
{
  "id": 1,
  "name": "Module name",
  "description": "Module description",
  "classes": [
    {
      "id": 1,
      "name": "Class 1",
      "date": "2022-10-25T22:10",
    }
  ]
}
```

### /modules/{id}/ (POST)
Endpoint privado de inserção de módulos, é necessário o envio de token JWT no header Authorization.
#### Exemplo de body
```json
{
  "name": "Module name",
  "description": "Module description"
}
```

### /modules/{id}/ (PUT)
Endpoint privado de edição de módulos, é necessário o envio de token JWT no header Authorization.
#### Exemplo de body
```json
{
  "name": "Module name",
  "description": "Module description"
}
```

### /classes/ (GET)
Endpoint público de listagem de aulas, não é necessário o envio de token.
#### Retorno
```json
[{
  "id": 1,
  "name": "Class name",
  "date": "2022-10-25T22:10",
  "module": 1
}]
```

### /classes/{id} (GET)
Endpoint público para visualizar aula, não é necessário o envio de token.
#### Retorno
```json
{
  "id": 1,
  "name": "Class name",
  "date": "2022-10-25T22:10",
  "module": 1
}
```

### /classes/{id}/ (POST)
Endpoint privado de inserção de aulas, é necessário o envio de token JWT no header Authorization.
#### Exemplo de body
```json
{
  "name": "Class name",
  "date": "2022-10-25T22:10",
}
```

### /classes/{id}/ (PUT)
Endpoint privado de edição de aulas, é necessário o envio de token JWT no header Authorization.
#### Exemplo de body
```json
{
  "name": "Class name",
  "date": "2022-10-25T22:10",
}
```
