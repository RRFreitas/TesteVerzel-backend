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
