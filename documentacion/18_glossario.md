# GLOSSÁRIO

* **Ação:** Refere-se a uma operação que pode ser executada sobre um item selecionado. Exemplos incluem "Aprovar" ou "Rejeitar" uma mensagem na Moderação de Conteúdo, ou ações sobre contatos na Caixa de Entrada.
* **API (Application Programming Interface):** Conjunto de regras e ferramentas que permite que outros sistemas se comuniquem e utilizem as funcionalidades da plataforma witi.me, principalmente para o envio automatizado de SMS.
* **Envio Avulso:** Funcionalidade para o envio rápido de mensagens de SMS para um pequeno grupo de contatos (até 5 números), ideal para testes ou comunicações pontuais.
* **Callback (DLR/MO):** Funcionalidade técnica que "chama de volta" um sistema externo através de uma URL para notificá-lo sobre eventos de uma mensagem (status de entrega ou respostas).
* **Caixa de Entrada:** Seção da plataforma que centraliza todas as respostas de SMS (MO) enviadas pelos destinatários das campanhas.
* **Campanha:** Um conjunto de envios de SMS agrupados sob um mesmo nome para fins de organização e análise de resultados. Geralmente associado a um "Disparo" ou "Novo Envio".
* **Chave API (API Key):** Uma senha única e secreta usada para autenticar requisições de sistemas externos que desejam utilizar a API da plataforma.
* **Classificação:** Um motor de regras (JSON) que analisa e etiqueta respostas de SMS recebidas (MO) para processamento posterior por um script.
* **Consulta Operadora:** Ferramenta que permite validar uma lista de números de telefone para verificar sua autenticidade, identificar a operadora de telefonia móvel e, opcionalmente, checar se o número possui uma conta ativa no WhatsApp.
* **Disparo:** O ato de enviar uma campanha de SMS em massa. É sinônimo de "Envio".
* **DLR (Delivery Receipt):** Confirmação de Entrega. É o relatório de status que a operadora de telefonia retorna, informando se uma mensagem foi entregue com sucesso, falhou, etc.
* **Envios:** Seção da plataforma que funciona como um histórico de todas as campanhas de SMS (disparos) realizadas. Permite acompanhar o andamento e acessar relatórios detalhados de cada campanha.
* **Filtros de Conteúdo:** Conjunto de regras de segurança que analisa o conteúdo das mensagens antes do envio para bloquear ou reter textos que não estejam em conformidade com as políticas da plataforma.
* **Força Revisão:** Parâmetro na configuração de SMS de um cliente que, quando ativado, força todas as mensagens daquele cliente a passarem pela tela de Moderação de Conteúdo para aprovação manual.
* **ID (Identificador):** Um código único usado para identificar um registro no sistema (ex: Meu ID, MSG ID, Remote ID).
* **Importação (Direta / de Arquivo):** Métodos disponíveis na função "Novo Envio" para carregar listas de contatos e mensagens para um disparo em massa.
* **Moderação de Conteúdo:** Ferramenta administrativa onde mensagens retidas por filtros de segurança aguardam aprovação, rejeição ou redirecionamento manual.
* **MO (Mobile Originated):** Termo técnico para uma mensagem de SMS originada de um dispositivo móvel, ou seja, una respuesta enviada por un destinatario para a plataforma.
* **MT (Mobile Terminated):** Termo técnico para uma mensagem de SMS enviada pela plataforma para um destinatário.
* **Painel de Controle (Dashboard):** A tela inicial da plataforma após o login, que exibe um resumo geral das atividades.
* **Painel de Gerenciamento do Cliente:** A área central acessada ao clicar em um cliente na "Lista de Clientes". Contém todas as abas de configuração específicas para aquela conta.
* **Perfil de Acesso:** Um conjunto de permissões que pode ser criado e atribuído a usuários administradores para definir o que cada um pode acessar e fazer na plataforma.
* **Rota:** O caminho ou infraestrutura técnica utilizada para enviar uma mensagem de SMS. Diferentes rotas podem ter custos, velocidades e tipos de remetente distintos.
* **Script MO / API Submit:** Códigos C# customizados na Configuração SMS para automatizar ações em mensagens recebidas (Script MO) ou enviadas via API (Script API Submit).
* **SID (Sender ID):** É o nome ou número que aparece como o remetente da mensagem de SMS no celular do destinatário. Dependendo da rota utilizada, o SID pode ser un número curto (Short Code, ex: 29268), um número de celular largo (Long Code, ex: +55 11 9xxxx-xxxx) ou um nome alfanumérico (ex: "WITI.ME"). A capacidade de personalizar o SID é uma das principais características que diferenciam as rotas.
* **Templates de SMS:** Modelos de mensagens pré-salvas que podem ser reutilizadas em diferentes campanhas para agilizar o processo de criação de envios.
* **Tráfego SMS:** Ferramenta de auditoria técnica que exibe um relatório detalhado de cada mensagem individual trafegada, permitindo uma análise profunda e depuração de problemas.
* **Variáveis:** Marcadores especiais (ex: $nome$) usados no texto de uma mensagem que são substituídos por informações personalizadas de cada contato no momento do envio.