# **Plano de Férias — Julho 2026**

## **Objetivo Principal**

Transformar as férias em uma aceleração técnica focada em backend profissional e construção de produtos reais.

Ao final do mês, o objetivo é ser capaz de:

* Construir APIs com FastAPI.  
* Modelar bancos PostgreSQL.  
* Utilizar SQLAlchemy.  
* Implementar autenticação JWT.  
* Containerizar aplicações com Docker.  
* Explicar decisões arquiteturais.  
* Evoluir o ORION com conhecimento sólido e não apenas com funcionalidades.

---

# **Projetos das Férias**

## **Projeto 1 — Rename**

### **Objetivo**

Transformar o Rename em um projeto apresentável e profissional.

### **Aprendizados**

* Organização de código  
* Manipulação de arquivos  
* CLI  
* Documentação  
* Git

---

## **Projeto 2 — ORION**

### **Objetivo**

Fortalecer entendimento arquitetural.

### **Importante**

Não adicionar funcionalidades apenas por adicionar.

O foco será compreender profundamente:

* Fluxo interno  
* Contratos  
* Responsabilidades  
* Governança  
* Roadmap futuro

---

## **Projeto 3 — ORION Services**

### **Objetivo**

Criar a primeira infraestrutura backend que poderá futuramente servir ao ORION.

### **Tecnologias**

* FastAPI  
* PostgreSQL  
* SQLAlchemy  
* Alembic  
* JWT  
* Docker  
* Pytest

---

# **Semana 1 — Rename Profissional**

## **Meta**

Finalizar o Rename como projeto sério.

### **Estrutura**

* Revisar arquitetura  
* Revisar separação de responsabilidades  
* Revisar tratamento de erros

### **Documentação**

Criar:

* README profissional  
* Instalação  
* Exemplos de uso  
* Roadmap  
* Estrutura de pastas

### **Git**

Treinar:

* Commits organizados  
* Histórico limpo  
* Versionamento

---

## **Estudos Paralelos**

### **HTTP**

Entender profundamente:

* GET  
* POST  
* PUT  
* PATCH  
* DELETE

### **Status Codes**

* 200  
* 201  
* 204  
* 400  
* 401  
* 403  
* 404  
* 500

---

# **Semana 2 — Fundamentos Backend**

## **FastAPI**

Aprender:

* Rotas  
* Request  
* Response  
* Path Parameters  
* Query Parameters

### **Projeto de Laboratório**

Exemplos:

GET /health  
GET /users  
POST /users

---

## **Pydantic**

Aprender:

* Validação  
* Schemas  
* Modelos de entrada  
* Modelos de saída

---

## **Conceitos REST**

Entender:

* Recursos  
* Endpoints  
* Idempotência  
* Versionamento

---

# **Semana 3 — Banco de Dados**

## **PostgreSQL**

Estudar:

* PK  
* FK  
* JOIN  
* Índices  
* Relacionamentos

Praticar SQL manual:

SELECT  
INSERT  
UPDATE  
DELETE  
JOIN

---

## **SQLAlchemy**

Aprender:

* Models  
* Session  
* CRUD  
* Relacionamentos

---

## **Alembic**

Aprender:

* Migrations  
* Controle de schema

---

## **ORION Services — Módulo Usuários**

Endpoints:

POST /users

POST /auth/login

GET /users/me

---

# **Semana 4 — Backend Profissional**

## **JWT**

Aprender:

* Access Token  
* Expiração  
* Fluxo de autenticação

Pergunta obrigatória:

Como o usuário permanece autenticado?

---

## **RBAC**

Role Based Access Control

Papéis:

ADMIN  
POWER\_USER  
USER  
GUEST

Inspirado diretamente no ORION.

---

## **Docker**

Aprender:

* Imagens  
* Containers  
* Volumes  
* Networks  
* Docker Compose

---

## **Pytest**

Criar testes para:

* Login  
* Usuários  
* Tarefas

---

# **Estrutura Inicial do ORION Services**

orion-services/

├── app/  
├── auth/  
├── users/  
├── tasks/  
├── logs/  
├── settings/  
├── tests/  
├── migrations/  
├── docker/  
└── docs/

---

# **Módulos do ORION Services**

## **Users**

Responsável por:

* Cadastro  
* Login  
* Permissões

---

## **Tasks**

Responsável por:

* CRUD de tarefas  
* Relacionamento com usuários

---

## **Logs**

Responsável por:

* Auditoria  
* Histórico

Estrutura:

id  
timestamp  
user  
action  
resource  
details

---

## **Settings**

Responsável por:

* Preferências  
* Configurações persistentes

---

# **Blocos de Estudo Obrigatórios**

Durante todo o mês.

## **Linux**

### **Tempo mínimo**

30 minutos por dia.

### **Praticar**

* grep  
* find  
* chmod  
* systemctl  
* journalctl

---

## **Git**

### **Tempo mínimo**

20 minutos por dia.

### **Praticar**

* branch  
* merge  
* rebase  
* tags

---

## **Leitura de Código**

### **Tempo mínimo**

30 minutos por dia.

### **Ler**

* FastAPI  
* SQLAlchemy  
* Projetos Open Source

---

# **Resultado Esperado em Agosto**

Ser capaz de responder com segurança:

* O que é uma API REST?  
* Como funciona autenticação JWT?  
* Por que usar Docker?  
* O que é SQLAlchemy?  
* O que é uma migration?  
* Como modelar relacionamentos em banco?  
* Como organizar um backend profissional?  
* Como o ORION é estruturado internamente?  
* Como os futuros Services podem se integrar ao ORION?

---

# **Regra Mais Importante**

Entender profundamente \> terminar rápido

Construir bem \> construir muito

Aprender arquitetura \> acumular tecnologias

O objetivo não é terminar o maior número de projetos possível.

O objetivo é sair de julho sabendo construir sistemas que possam virar produtos reais, exatamente a habilidade que será útil tanto para o ORION quanto para os projetos da empresa.

