# [DOCS] Implantação de Documentação Técnica Mintlify Integrada à API FastAPI

**Versão:** 1.0  
**Data de início:** 21/10/2025  
**Data limite:** 22/10/2025  
**Duração total:** 2 dias úteis  
**Responsável:** Ylgner Becton Ferreira  

---

## 🏷️ Título da Atividade  
[DOCS] Integração da Documentação Mintlify com FastAPI (Python) — OpenAPI, Autenticação Parcial, Deploy e Qualidade

---

## 📘 Descrição (Contexto e Objetivo)

Esta atividade tem como objetivo criar, documentar e publicar uma **prova de conceito (POC)** de documentação técnica integrada entre **Mintlify** e **FastAPI**.  
A iniciativa faz parte da padronização da camada de documentação dos serviços Python e tem como foco **conectar automaticamente a especificação OpenAPI** gerada pela FastAPI com a **plataforma Mintlify**, permitindo publicação automatizada, visual moderna e navegação estruturada.

Além disso, a POC demonstrará o uso de:
- **Autenticação parcial (páginas públicas/privadas)**,  
- **Deploy automatizado via GitHub App**,  
- **Domínio customizado (CNAME)**,  
- e **checagens automáticas de qualidade** (links quebrados, acessibilidade e validação do OpenAPI).

O resultado esperado é uma base replicável para documentar serviços futuros, reduzindo o esforço manual e aumentando a consistência entre os times técnicos.

---

## 🎯 Escopo e Requisitos

### Técnicos e Funcionais
- **Stack principal:**  
  - Python 3.11+  
  - FastAPI + Uvicorn  
  - Mintlify (CLI Node LTS)  
  - GitHub App (deploy automático)  
  - OpenAPI 3.0+  

- **Requisitos técnicos:**
  1. Gerar arquivo `docs/api/openapi.json` a partir da FastAPI usando `app.openapi()`.  
  2. Configurar o arquivo `docs/docs.json` com tema, navegação (tabs e grupos) e referência à OpenAPI.  
  3. Criar páginas MDX (index, quickstart, guides/faq) com autenticação parcial (`public: true`).  
  4. Implementar a seção **API Reference** com playground funcional.  
  5. Ativar deploy automatizado via GitHub App com rebuild manual disponível no dashboard Mintlify.  
  6. Configurar domínio customizado (`docs.suaempresa.com`) com CNAME → `cname.vercel-dns.com.`.  
  7. Rodar verificações de qualidade:
     - `mint broken-links`  
     - `mint a11y`  
     - `mint openapi-check ./docs/api/openapi.json`

- **Critérios visuais e de padronização:**
  - Layout Mintlify padrão (tema “mint”).  
  - Navegação em abas: `Guia`, `API reference`, `FAQ`.  
  - Logotipo e cores da marca.  
  - OpenAPI 3.0+ com servidores e segurança definidos.

---

## 🧩 Critérios de Aceitação (ACs)

1. **Dado** o repositório configurado com `docs.json`,  
   **quando** executo `mint dev`,  
   **então** o site deve abrir localmente com tema, logo e navegação definidos.

2. **Dado** a aplicação FastAPI,  
   **quando** gero `docs/api/openapi.json` e referencio no `docs.json`,  
   **então** a aba “API reference” deve exibir todos os endpoints com playground ativo.

3. **Dado** páginas com `public: true`,  
   **quando** um visitante acessa a documentação,  
   **então** deve conseguir visualizar apenas as páginas públicas sem autenticação.

4. **Dado** o GitHub App instalado,  
   **quando** realizo `git push` na branch principal,  
   **então** o deploy deve ser disparado automaticamente no Mintlify Dashboard.

5. **Dado** o domínio customizado configurado,  
   **quando** o CNAME propaga,  
   **então** o site deve estar acessível em `https://docs.suaempresa.com`.

6. **Dado** os comandos de qualidade,  
   **quando** executo `mint broken-links`, `mint a11y` e `mint openapi-check`,  
   **então** o pipeline deve finalizar sem falhas.

---

## ✅ Definition of Ready (DoR)
- Contexto técnico definido e validado pelo time.  
- Dependências e integrações confirmadas (FastAPI, Mintlify, GitHub App).  
- Critérios de aceitação revisados e aprovados.  
- Acesso ao Mintlify Dashboard e DNS disponível.  
- OpenAPI 3.0+ validado e funcional na aplicação base.

---

## 🧾 Definition of Done (DoD)
- Código e configuração testados e revisados (lint + review).  
- `openapi.json` exportado corretamente e consumido pela doc.  
- `docs.json` válido (sem erros de schema).  
- Documentação visual e navegável publicada no ambiente Mintlify.  
- Deploy automatizado e rebuild manual validados.  
- Checagens de qualidade executadas com sucesso.  
- README atualizado explicando comandos (`mint dev`, `mint build`, `mint deploy`).  
- Artefato final validado pelo Tech Lead e pronto para reuso em novos serviços.

---

## 🔄 Subtarefas Técnicas

1. **Exportar OpenAPI da FastAPI**  
   - Criar script `tools/export_openapi.py` que gera `docs/api/openapi.json`.

2. **Criar estrutura base do Mintlify**  
   - Adicionar `docs/docs.json` com tema, cores e navegação inicial.

3. **Gerar conteúdo MDX inicial**  
   - Criar `docs/pages/index.mdx`, `quickstart.mdx` e `guides/faq.mdx`.

4. **Configurar seção de API Reference**  
   - Integrar o OpenAPI gerado na aba “API reference” do Mintlify.

5. **Implementar autenticação parcial**  
   - Definir páginas públicas (`public: true`) e privadas.

6. **Rodar verificações de qualidade**  
   - Executar `mint broken-links`, `mint a11y`, `mint openapi-check`.

7. **Deploy e domínio customizado**  
   - Instalar GitHub App e configurar CNAME para `cname.vercel-dns.com.`.

8. **Documentar e validar resultado final**  
   - Atualizar README, capturar screenshots e validar acessos.

---

## 🪜 Dependências e Observações

- **Serviços externos:** Mintlify Dashboard, GitHub App e DNS provider.  
- **Time envolvido:** Arquitetura, Backend e Infra.  
- **Ambiente:** Dev e Staging (não há impacto em produção).  
- **Observações adicionais:**  
  - Exportação de PDF é opcional e pode ser feita diretamente pelo Mintlify Dashboard.  
  - Recomenda-se configurar `mint lint` no pipeline CI/CD.  
  - O arquivo `openapi.json` deve conter `servers` e `securitySchemes` para permitir testes no playground.  
  - Este modelo servirá como **template base** para futuras documentações técnicas dos microserviços FastAPI.

---

## 🗓️ Cronograma (2 dias)

| Data | Entregável | Descrição |
|------|-------------|-----------|
| **21/10/2025 (Terça)** | Setup e Integração | Criação do repositório, geração do `openapi.json`, configuração do `docs.json`, navegação inicial e validação local (`mint dev`). |
| **22/10/2025 (Quarta)** | Deploy e Validação Final | Instalação do GitHub App, testes de deploy e rebuild, aplicação do CNAME customizado e execução dos checks de qualidade. |

---

## 📂 Estrutura Sugerida do Projeto


repo/
├─ app/
│ └─ main.py # FastAPI base
├─ docs/
│ ├─ docs.json # Configuração Mintlify
│ ├─ api/openapi.json # Export da API
│ ├─ pages/
│ │ ├─ index.mdx
│ │ ├─ quickstart.mdx
│ │ └─ guides/faq.mdx
└─ tools/
└─ export_openapi.py

python
Copiar código

---

## 🧪 Exemplos Técnicos

### FastAPI mínima e exportação de OpenAPI
```python
# app/main.py
from fastapi import FastAPI

app = FastAPI(title="Acme API", version="1.0.0")

@app.get("/users")
def list_users():
    return [{"id": 1, "name": "Ada"}]
python
Copiar código
# tools/export_openapi.py
import json, pathlib
from app.main import app

out = pathlib.Path("docs/api/openapi.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(app.openapi(), indent=2), encoding="utf-8")
print(f"✅ OpenAPI exportado para {out}")
Configuração básica do Mintlify
json
Copiar código
{
  "$schema": "https://mintlify.com/docs.json",
  "name": "Acme Docs",
  "theme": "mint",
  "colors": { "primary": "#0057FF" },
  "navigation": {
    "tabs": [
      { "tab": "Guia", "pages": ["quickstart", "guides/faq"] },
      { "tab": "API reference", "openapi": "/api/openapi.json" }
    ]
  }
}
Comandos principais da CLI
bash
Copiar código
# Visualização local
mint dev

# Verificação de qualidade
mint broken-links
mint a11y
mint openapi-check ./docs/api/openapi.json

# Deploy (via GitHub App)
git push origin main
Exemplo de página pública (MDX)
md
Copiar código
---
title: "Introdução"
public: true
description: "Visão geral do serviço"
---

# Bem-vindo à documentação Acme
Esta página é pública. As seções de API e integrações exigem autenticação.
✅ Checklist de Go/No-Go (22/10/2025)
 Estrutura docs/ e openapi.json válidas

 Navegação e layout configurados corretamente

 Deploy automatizado funcionando via GitHub App

 Domínio customizado apontando corretamente

 Checks de qualidade executados e aprovados

 README técnico atualizado

 Documentação publicada no ambiente Mintlify

📄 Observação Final:
Esta entrega consolida o padrão de documentação técnica com Mintlify no ecossistema Python, garantindo reuso, consistência e integração direta com APIs FastAPI.
O modelo servirá como referência oficial para os próximos microserviços documentados.

yaml
Copiar código

---

Deseja que eu gere agora o **PDF pronto** a partir desse conteúdo (com layout limpo e cabeçalhos visuais)?  
Posso gerar e te devolver o arquivo `atividade-docs-mintlify-fastapi.pdf` diretamente aqui.