Análise de Uso do Sistema de Bicicletas Cyclistic

📌 Visão Geral do Projeto

Este projeto tem como objetivo analisar os padrões de uso do sistema de bicicletas compartilhadas Cyclistic, identificando diferenças de comportamento entre usuários membros (assinantes anuais) e usuários ocasionais (casual riders).

A análise busca gerar insights baseados em dados para apoiar a equipe de marketing da empresa na criação de estratégias que incentivem usuários ocasionais a se tornarem membros anuais.

O projeto segue as etapas clássicas do processo de análise de dados:

  1. Perguntar (Ask)

  2. Preparar (Prepare)

  3. Processar (Process)

  4. Analisar (Analyze)

  5. Compartilhar (Share)

  6. Agir (Act)

A análise foi realizada utilizando o Python para a realização da limpeza do arquivo e Análise Descritiva e o Power BI com a criação de dashboards interativos para visualização dos dados e geração de insights estratégicos.

🎯 Problema de Negócio

A equipe de marketing da Cyclistic deseja aumentar o número de assinaturas anuais.

Para isso, três perguntas orientam esta análise:

  1. De que maneiras os membros anuais e os usuários ocasionais utilizam as bicicletas da Cyclistic de forma diferente?

  2. Por que usuários ocasionais comprariam assinaturas anuais da Cyclistic?

  3. Como a Cyclistic pode utilizar mídias digitais para influenciar usuários ocasionais a se tornarem membros?


📊 Conjunto de Dados

O conjunto de dados contém informações sobre viagens realizadas no sistema de bicicletas, incluindo:

  - Data e hora de início da viagem
  - Data e hora de término da viagem
  - Duração da viagem
  - Tipo de usuário (member ou casual)
  - Tipo de bicicleta
  - Dia da semana
  - Mês da viagem

  Link: [Dataset](https://divvy-tripdata.s3.amazonaws.com/index.html)
  
  Termos de Uso: [Licença](https://divvybikes.com/data-license-agreement)


🧹 Limpeza e Preparação dos Dados

Antes da análise, foram realizadas etapas de limpeza e preparação para garantir maior qualidade dos dados.

  - Conversão da Duração das Viagens
  - A duração das viagens estava originalmente em segundos.

Foi criada uma nova coluna para converter a duração para minutos:

Ride Minutes = ride_length / 60
Remoção de Valores Irreais

Alguns registros apresentavam durações extremamente curtas ou extremamente longas, o que poderia distorcer a análise.

Foram aplicados os seguintes filtros:

  - Remoção de viagens menores que 1 minuto
  - Remoção de viagens maiores que 24 horas

Esses casos podem representar:

  - Erros de desbloqueio da bicicleta
  - Bicicletas não devolvidas corretamente
  - Falhas no sistema de registro

Essa etapa garante que a análise represente comportamentos reais de uso do serviço.

🛠 Ferramentas Utilizadas

  - Python / Pandas - Limpeza dos dados e exclusão de colunas
  - Seaborn / Matplotlib - Geração de gráficos
  - Power BI – Visualização e criação de dashboards
  - DAX – Criação de métricas e cálculos analíticos
  - GitHub – Documentação e portfólio do projeto

📈 Estrutura do Dashboard

O dashboard foi estruturado seguindo uma abordagem de data storytelling, conduzindo o usuário da visão geral até os insights estratégicos.

📍 1. Executive Overview (Visão Geral)

<img width="700" height="450" alt="Captura de tela 2026-03-12 163903" src="https://github.com/user-attachments/assets/3e949901-e21b-4850-b258-46ad1a94638c" />

Esta página apresenta uma visão geral do uso do sistema.

  Principais indicadores apresentados:

  - Total de viagens realizadas
  - Tempo médio de viagem
  - Percentual de usuários membros

  Visualizações incluídas:

  - Distribuição de viagens por tipo de usuário
  - Tendência mensal de viagens
  - Indicadores principais (KPIs)

Objetivo:
Fornecer uma visão rápida sobre o comportamento geral dos usuários.

📍 2. Análise Comportamental dos Usuários

<img width="700" height="450" alt="Captura de tela 2026-03-12 164217" src="https://github.com/user-attachments/assets/6fb1527b-9bac-4dd8-9f32-c806f027ed7a" />

Esta página explora as diferenças de comportamento entre membros e usuários ocasionais.

  Visualizações utilizadas:

  - Duração média das viagens por tipo de usuário
  - Volume de viagens por dia da semana
  - Preferência de tipo de bicicleta

  Principais observações:

  - Usuários ocasionais realizam viagens mais longas
  - Membros utilizam o sistema com maior frequência
  - Membros apresentam maior preferência por bicicletas elétricas

Objetivo:

Identificar padrões de comportamento que possam orientar estratégias de marketing.

📍 3. Insights Estratégicos

<img width="700" height="450" alt="Captura de tela 2026-03-12 164413" src="https://github.com/user-attachments/assets/daa359a3-4ed9-4606-b975-59ed031436bb" />

Esta página transforma a análise de dados em insights de negócio.

  Principais descobertas:

  - Membros representam a maior parte das viagens, indicando uso frequente do serviço.
  - Usuários ocasionais fazem viagens mais longas, sugerindo uso recreativo.
  - A demanda por viagens aumenta durante os meses de verão, indicando sazonalidade.
  - Usuários ocasionais apresentam maior atividade nos fins de semana.

Objetivo:

Identificar oportunidades de conversão de usuários ocasionais em membros.

💡 Principais Insights de Negócio
  Insight 1 — Diferença de comportamento

  - Usuários membros utilizam o serviço com maior frequência, indicando uso voltado para deslocamento diário.
  - Usuários ocasionais realizam viagens mais longas, indicando uso voltado para lazer ou turismo.

  Insight 2 — Sazonalidade

  - O número de viagens aumenta significativamente durante os meses de verão, demonstrando forte influência sazonal no uso do serviço.
  - Isso abre oportunidades para campanhas sazonais de marketing.

  Insight 3 — Uso nos finais de semana

  - Usuários ocasionais apresentam maior volume de viagens durante finais de semana, reforçando o comportamento recreativo.
  - Esse padrão pode ser explorado em estratégias de conversão para assinaturas.

📢 Recomendações de Marketing

Com base na análise, algumas estratégias podem ser consideradas:

  - Criar promoções de assinatura focadas em finais de semana.
  - Lançar campanhas de marketing durante o verão, quando a demanda é maior.
  - Oferecer períodos de teste gratuitos para incentivar usuários ocasionais a experimentar os benefícios da assinatura.
  - Destacar as vantagens econômicas da assinatura anual em comparação com múltiplas viagens ocasionais.

📊 Dashboard do Projeto

O dashboard interativo inclui três páginas principais:

  Executive Overview
  Análise Comportamental dos Usuários
  Insights Estratégicos
  Essas páginas conduzem o usuário da exploração dos dados até a geração de estratégias de negócio.

📌 Conclusão

  Este projeto demonstra como a análise de dados pode ajudar empresas a compreender melhor o comportamento de seus usuários e apoiar decisões estratégicas.

  Ao identificar as diferenças entre usuários ocasionais e membros, a Cyclistic pode desenvolver estratégias de marketing mais eficientes para aumentar o número de assinaturas anuais.

👨‍💻 Autor

  - Luiz Felipe Caetano Rodrigues
  - Projeto de Portfólio – Análise de Dados

