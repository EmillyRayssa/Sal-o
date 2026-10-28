# Agendamento de Salão

Sistema de agendamento para salão e barbearia feito com Django, Python e MySQL.

## Funcionalidades

- Cadastro de serviços, profissionais e clientes
- Agendamento com validação de horário ocupado
- Agenda organizada por dia
- Painel administrativo com filtros, busca e ações em massa

## Como rodar

1. Crie o banco no MySQL:

```sql
CREATE DATABASE salao_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. Clone o projeto e crie o ambiente virtual:

```
git clone https://github.com/EmillyRayssa/salao.git
cd salao
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

3. Copie `.env.example` para `.env` e preencha a senha do MySQL.

4. Crie as tabelas e o superusuário:

```
python manage.py migrate
python manage.py createsuperuser
```

5. Rode o servidor:

```
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/` para a agenda e `http://127.0.0.1:8000/admin/` para o painel.

## Tecnologias

Python, Django, MySQL, HTML e CSS.
