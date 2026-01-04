## TechFlow Task Manager

# Descrição do Projeto
O TechFlow Task Manager é um sistema simples de gerenciamento de tarefas desenvolvido para simular a aplicação de metodologias ágeis em um projeto de Engenharia de Software.
O sistema foi pensado para atender uma startup fictícia do setor de logística, permitindo organizar tarefas, acompanhar o andamento do trabalho e melhorar a produtividade da equipe.

# Objetivo
Desenvolver um sistema básico de gerenciamento de tarefas, aplicando boas práticas de Engenharia de Software, versionamento com GitHub, testes automatizados e integração contínua.

# Escopo Inicial
- Cadastro de tarefas
- Listagem de tarefas
- Conclusão de tarefas
- Organização do código em camadas (model, service, repository)
- Testes automatizados
- Pipeline de integração contínua com GitHub Actions
- Metodologia Utilizada

# Foi adotada uma abordagem baseada em Kanban, utilizando a aba Projects do GitHub para organizar as tarefas nas colunas:

- To Do
- In Progress
- Done
Essa metodologia permitiu visualizar o fluxo de trabalho e acompanhar o progresso do desenvolvimento.

# Tecnologias Utilizadas
Python 3
PyTest (testes automatizados)
GitHub Actions (integração contínua)
Git e GitHub (versionamento e gestão do projeto)

# Como Executar o Projeto
- Instalar dependências pip install -r requirements.txt
- Executar os testes python -m pytest

## Gestão de Mudanças
Durante o desenvolvimento do projeto, foi identificada a necessidade de melhorar a priorização das tarefas. Como proposta de evolução do sistema, definiu-se a inclusão futura de um campo de prioridade (Alta, Média, Baixa), permitindo maior foco em tarefas críticas.

Essa mudança foi registrada no quadro Kanban e planejada para uma próxima iteração do projeto, demonstrando a flexibilidade das metodologias ágeis.

# Quadro GitHub Projects (Kanban)
O projeto utiliza Kanban com pelo menos 10 cards distribuídos nas colunas To Do, In Progress e Done. 

Exemplo de organização:
- To Do 
Criar endpoint GET /tasks Criar endpoint POST /tasks Adicionar validação de dados no POST /tasks Implementar endpoint DELETE /tasks/

- In Progress 
Implementar endpoint PATCH /tasks/ Implementar endpoint PUT /tasks/ Criar testes unitários para PATCH /tasks/ Criar testes unitários para DELETE /tasks/

- Done
Configurar ambiente
Flask

- Criar estrutura inicial de pastas (/src e /tests)

Cada card contém: 
Título 
Descrição

## Commits Semânticos e Frequentes
O projeto utiliza mensagens de commit claras e padronizadas (ex: feat:, fix:, test:, docs:). 
Exemplo de commits realizados:

feat: criar endpoint GET /tasks 
feat: criar endpoint POST /tasks 
test: criar testes para GET e POST 
feat: implementar PATCH /tasks/ 
test: adicionar testes de PATCH 
feat: implementar DELETE /tasks/ 
test: criar testes de DELETE 
fix: corrigir importações em services.py 
feat: adicionar filtro de tarefas por status 
test: criar teste para filtro de status

## Testes Automatizados
Utiliza PyTest para testes de unidade e integração dos endpoints Flask.

Testes cobrem:

Criação de tarefas (POST) Listagem de tarefas (GET) Atualização de tarefas (PATCH e PUT) Exclusão de tarefas (DELETE) Filtro de tarefas por status (nova feature) Todos os testes são executados automaticamente via GitHub Actions a cada push ou pull request, garantindo a integridade do código.

## Pipeline de Integração Contínua (CI)
O projeto possui pipeline configurado no GitHub Actions, com workflow que:

Instala dependências Python Executa todos os testes (pytest) Valida o comportamento da aplicação em cada push ou pull request

## Mudança de Escopo
Durante o desenvolvimento, foi implementada a feature de filtragem de tarefas por status:

Novo card criado no Kanban: “Adicionar filtro de tarefas por status”

Implementação: Ajuste no endpoint GET /tasks para aceitar parâmetro status Atualização da função get_all_tasks em services.py Teste unitário criado para verificar o filtro
Commit correspondente: feat: adicionar filtro de tarefas por status no endpoint GET /tasks

<img width="567" height="254" alt="workflows" src="https://github.com/user-attachments/assets/6aa0d374-e0d0-4c75-b797-df3c11133897" />
<img width="567" height="276" alt="tabela kanban" src="https://github.com/user-attachments/assets/29674b4a-b3b8-4964-b530-54379220923b" />
