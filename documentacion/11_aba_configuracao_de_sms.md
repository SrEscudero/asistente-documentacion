# 9. Aba: Configuração de SMS do Cliente

**Esta aba, localizada DENTRO DO PAINEL DE UM CLIENTE ESPECÍFICO, permite o ajuste fino do comportamento dos envios via API para esta conta em particular.**

## 9.1. Callbacks de Retorno (DLR e MO)

* **Função:** Permitem que o cliente receba, em seu próprio servidor, o status de entrega de cada SMS enviado (ex: "entregue", "enviado", "falha").
* **Como configurar:**
    * Marque a caixa de seleção Habilitar CallBack.
    * Insira a URL do cliente nos campos URL DLR e URL MO para que os retornos automáticos sejam enviados corretamente.

## 9.2. Chave API (API Key)

* **Função:** É o código de autenticação exclusivo da conta do cliente, indispensável para realizar qualquer envio via API.
* **Condição de Liberação:** Por segurança e política comercial, a Chave API só deve ser informada ao cliente após ele realizar a primeira recarga mínima de R$ 250,00 na plataforma.

## 9.3. Rota Preferencial

* **Função:** Define uma rota de envio padrão para as mensagens deste cliente, simplificando a integração.
* **Comportamento:**
    * **Rota Definida:** Se uma rota for selecionada neste campo, todos os envios do cliente usarão esta rota por padrão, sem que ele precise especificá-la no código.
    * **Campo em Branco:** Se nenhuma rota for selecionada, o cliente deve especificar o ID numérico da rota em sua requisição à API.
    * **Nota Importante:** O cliente deve usar apenas o ID da rota (ex: para "999 - short HQ", o valor a ser usado no parâmetro é 999).

## 9.4. Parâmetros de Controle e Segurança

* **API Habilitada:** Essencial. Esta caixa deve estar marcada para que a conta possa realizar envios via API.
* **Força Revisão:** Altamente recomendado para clientes novos. Ao marcar esta opção, todas as mensagens enviadas pelo cliente entram em uma fila de moderação para garantir que o conteúdo está de acordo com as políticas de uso da plataforma.
* **Tipo de Link:** Gerencia como os links dentro das mensagens de SMS são tratados.
    * **Sem Link:** Impede o envio de mensagens que contenham qualquer tipo de link.
    * **Requer Aprovação:** Padrão de segurança. Mensagens com links são direcionadas automaticamente para a fila de moderação.
    * **Link Livre:** Permite o envio de links sem moderação prévia. Use com cautela.
    * **Indefinido:** Utiliza a configuração padrão do sistema.

## 9.5. Painel de Horários

* **Função:** Define uma "janela de operação" para os envios do cliente.
* **Comportamento:**
    * **Dentro do Horário:** Mensagens enviadas nos dias e horários configurados são processadas diretamente (a menos que outra regra exija moderação).
    * **Fora do Horário:** Mensagens enviadas fora da janela configurada são automaticamente enviadas para a fila de moderação, aguardando aprovação manual.

Após ajustar todos os parâmetros, clique no botão **Salvar Configurações SMS** para aplicar as alterações.