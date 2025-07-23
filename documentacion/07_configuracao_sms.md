# 5. Configurações Globais da Plataforma

**Esta seção agrupa as configurações que afetam TODA a plataforma e todos os clientes.** São ferramentas de administração de alto nível para automação e gerenciamento de acesso.

## 5.1. Gerenciamento de Usuários Administradores

Aqui você gerencia os acessos de outros administradores à plataforma.

* **Criar um Novo Usuário Administrador:** Permite conceder acesso para novos membros da equipe.
* **Gerenciar Perfis e Permissões de Acesso:** Permite criar perfis com permissões customizadas (ex: "Financeiro", "Suporte").

## 5.2. Configuração SMS (Global)

Esta seção, acessada pelo menu principal, permite definir configurações globais e automações avançadas que se aplicam a toda a plataforma.

### 5.2.1. Aba: Configuração Geral

Esta aba permite definir uma **Rota Preferencial** padrão para toda a plataforma. Se um envio for realizado sem especificar uma rota, o sistema utilizará automaticamente a que foi definida aqui.

### 5.2.2. Aba: Avançado

Esta aba contém ferramentas para automação de respostas e processamento de envios.

* **API e Callback:** Permite definir URLs de callback padrão para o sistema.
* **Processamento Automatizado de Retornos:** É um motor de automação composto por três partes que trabalham em conjunto:
    * **Classificação (JSON):** Utiliza uma estrutura em JSON para analisar e "etiquetar" (taggear) cada resposta de SMS recebida com base em seu conteúdo (ex: "LEAD", "blackList", "ignorar").
    * **Script MO (C#):** Um script em C# que é executado para cada resposta recebida. Ele usa a etiqueta da etapa de Classificação para tomar decisões e executar ações personalizadas, como enviar uma resposta automática ou adicionar um número a uma lista de bloqueio.
    * **Script API Submit (C#):** Um script em C# executado para cada mensagem enviada via API, permitindo validar ou modificar o conteúdo antes do disparo.
* **Testar Processamento:** Esta ferramenta é um simulador essencial para validar o comportamento do motor de **Classificação** e do **Script MO** sem um envio real.
    * **Como Usar:** Preencha os campos de simulação (**Origem**, **Data**, **Texto Recebido**, etc.) e clique em **Testar Processamento**.
    * **Analisando o Retorno:** Um painel verde exibirá o resultado completo do processamento, permitindo uma análise detalhada.