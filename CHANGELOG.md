# 📘 Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.  
O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/)  
e este projeto segue [Versionamento Semântico](https://semver.org/lang/pt-BR/).

---

## [v1.0.0] - 2025-10-06
### 🚀 Adicionado
- Primeira versão estável da API.
- CRUD completo de **serviços**, com endpoints para:
  - Criar (`POST /services`)
  - Listar (`GET /services`)
  - Atualizar (`PUT /services/{service_name}`)
  - Deletar (`DELETE /services/{service_name}`)
- Rota de **cálculo** de valor total do serviço (`POST /services/calculate`).
- Validação de dados via **Pydantic**.
- Integração com banco de dados usando **SQLAlchemy**.
- Estrutura inicial do projeto com **FastAPI**.
- Testes unitários para endpoints principais.

### 🧱 Estrutura do projeto
- Organização em camadas:
  - `api/` → rotas e controladores
  - `core/` → configuração e conexão com banco
  - `service/` → camada de regras de negócio
  - `schemas/` → validações e modelos Pydantic
  - `models/` → modelos do banco (SQLAlchemy)
  - `test/` → testes unitários e integrados

## 📅 Histórico
- **2025-10-06:** Primeira release oficial `v1.0.0`