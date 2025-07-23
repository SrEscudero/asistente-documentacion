# 6. Entendendo as Rotas de Envio de SMS

Uma **rota de SMS** é uma interface de comunicação pré-configurada que estabelece a conexão entre a plataforma e as operadoras de telefonia móvel (MNOs), através de gateways SMSC (Short Message Service Center) ou agregadores. Cada rota é definida por um conjunto de parâmetros técnicos que determinam seu comportamento, performance e adequação para um caso de uso específico.

A escolha da rota correta impacta diretamente em:

* **SID (Sender ID):** O nome ou número que aparece como o remetente da mensagem.
* **Velocidade de Entrega:** O tempo que a mensagem leva para chegar ao destinatário.
* **Confiabilidade do DLR:** A precisão do relatório de entrega.
* **Custo por Mensagem:** O valor cobrado por cada SMS enviado.

A seguir, detalhamos as rotas disponíveis na plataforma e suas finalidades.

## 6.1. Rota HQ (High Quality) – Premium com Interatividade

* **Uso:** Mensagens críticas, marketing segmentado, cobranças e links.
* **Características:**
    * Tempo de entrega: até 30 segundos
    * Garantia de entrega: 100% para números válidos
    * Permite resposta: sim (resposta é cobrada)
    * Pode conter links
    * Rota short code multiuso (para marketing e OTPs menos exigentes)
    * Contém DLR confiável (relatório de entrega)
* **Ideal para:** notificações sensíveis, confirmações, cobranças, campanhas com interação.

## 6.2. Short Marketing – Promoções com Personalização

* **Uso:** Campanhas promocionais em massa com variação por nome.
* **Características:**
    * Tempo de entrega: até 1 minuto
    * Garantia de entrega: 100%
    * Permite resposta: sim
    * Pode conter links
    * Permite uso de variáveis em mensagens iguais (ex: nome do cliente)
    * Contém DLR confiável (relatório de entrega)
    * Rota short especializada em promoções
* **Ideal para:** datas comemorativas, ofertas, campanhas de grande escala.

## 6.3. Short OneWay – Notificações sem Interação

* **Uso:** Informativos, lembretes, mensagens que não exigem retorno.
* **Características:**
    * Tempo de entrega: até 1 minuto
    * Garantia de entrega: 100%
    * Permite resposta: não
    * Pode conter links (mas o ideal é usar apenas texto para mais velocidade)
    * Contém DLR confiável (relatório de entrega)
* **Ideal para:** avisos, lembretes automáticos, mensagens institucionais.

## 6.4. P2P (Person to Person) – Comunicação Bidirecional com Backup

* **Uso:** Atendimento humano, SAC, fallback de WhatsApp, tokens.
* **Características:**
    * Tempo de entrega: até 15 minutos
    * Garantia de entrega: 100%
    * Permite resposta: sim
    * Pode conter links
    * Risco de bloqueio por similaridade acima de 80%
    * Backup automático com rota OTP em caso de falha (sem custo)
    * Contém DLR confiável (relatório de entrega)
* **Ideal para:** atendimento direto, tokens com resposta, SAC.

## 6.5. OTP / Token – Segurança com Prioridade Máxima

* **Uso:** Autenticação em 2 fatores, códigos temporários, senhas.
* **Características:**
    * Tempo de entrega: até 15 segundos
    * Garantia de entrega: 100%
    * Permite resposta: não
    * Alta prioridade e velocidade
    * Rota acionada automaticamente como backup da P2P em caso de falha
    * Contém DLR confiável (relatório de entrega)
* **Ideal para:** validações, autenticação de sistemas, confirmações sensíveis.