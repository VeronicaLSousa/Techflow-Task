# TechFlow Task Manager

##  Descrição do Projeto
O TechFlow Task Manager é um sistema simples de gerenciamento de tarefas desenvolvido para simular a aplicação de metodologias ágeis em um projeto de Engenharia de Software.  
O sistema foi pensado para atender uma startup fictícia do setor de logística, permitindo organizar tarefas, acompanhar o andamento do trabalho e melhorar a produtividade da equipe.

##  Objetivo
Desenvolver um sistema básico de gerenciamento de tarefas, aplicando boas práticas de Engenharia de Software, versionamento com GitHub, testes automatizados e integração contínua.

##  Escopo Inicial
- Cadastro de tarefas
- Listagem de tarefas
- Conclusão de tarefas
- Organização do código em camadas (model, service, repository)
- Testes automatizados
- Pipeline de integração contínua com GitHub Actions

##  Metodologia Utilizada
Foi adotada uma abordagem baseada em **Kanban**, utilizando a aba **Projects** do GitHub para organizar as tarefas nas colunas:
- To Do
- In Progress
- Done

Essa metodologia permitiu visualizar o fluxo de trabalho e acompanhar o progresso do desenvolvimento.

##  Tecnologias Utilizadas
- Python 3
- PyTest (testes automatizados)
- GitHub Actions (integração contínua)
- Git e GitHub (versionamento e gestão do projeto)

## Como Executar o Projeto

- Instalar dependências
pip install -r requirements.txt

- Executar os testes
python -m pytest

## Gestão de Mudanças

Durante o desenvolvimento do projeto, foi identificada a necessidade de melhorar a priorização das tarefas.
Como proposta de evolução do sistema, definiu-se a inclusão futura de um campo de prioridade (Alta, Média, Baixa), permitindo maior foco em tarefas críticas.

Essa mudança foi registrada no quadro Kanban e planejada para uma próxima iteração do projeto, demonstrando a flexibilidade das metodologias ágeis.
