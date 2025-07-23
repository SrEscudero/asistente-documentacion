# 7. Gerenciamento e Atribuição de Rotas de Saída

Esta seção detalha o processo administrativo para gerenciar as rotas de envio de SMS, configurar suas propriedades e atribuí-las a clientes específicos. Esta é uma função de controle central para definir quais opções de envio cada cliente terá disponível.

## 7.1. Acessando a Lista de Rotas

Para começar, acesse a funcionalidade de gerenciamento de rotas no menu principal.

1.  No menu, clique em **Rotas** (ou "SMS - Rotas de Saída").
2.  Na tela que se abre, para visualizar todas as rotas de base disponíveis para atribuição, desmarque a opção **"Apenas rotas Raiz"** e mantenha a opção **"Apenas rotas ativas"** marcada.
3.  Uma lista com todas as rotas do sistema será exibida, com informações como **ID**, **NOME**, **SERVIÇO**, etc.

## 7.2. Editando as Propriedades de uma Rota Mestra

Cada rota na lista principal funciona como um "modelo" ou "rota mestra". Você pode editar suas propriedades padrão clicando em seu ID.

1.  Na lista de rotas, clique no **ID** da rota que deseja gerenciar.
2.  Você será direcionado para a tela **"SMS – Edição de Rota"**. Aqui, você pode configurar os seguintes parâmetros globais para esta rota:
    a. **Nome:** O nome principal da rota.
    b. **Serviço:** O tipo de serviço SMS associado à rota (ex: **SMS.LONG**, **SMS.SHORT-HQ**).
    c. **Custo:** O custo base por mensagem para esta rota.
    d. **Observações:** Um campo de texto livre para anotações internas.
    e. **Ativo / Visível:** Checkboxes para definir se a rota está globalmente ativa e visível.
    f. **Id Empresa / Id Empresa Revenda:** Campos informativos para associar a rota a uma empresa ou revenda específica.
    g. **Routing App / Country Code:** Parâmetros técnicos de roteamento.

## 7.3. Atribuindo uma Rota a um Cliente (Aba "Utilização")

Dentro da tela de edição de uma rota mestra, a aba "Utilização" é onde você efetivamente a atribui a um ou mais clientes.

1.  Clique no botão **"Nova Rota Para Cliente"**.
2.  Uma janela modal chamada **"Nova Rota"** aparecerá.
    a. **Cliente:** Comece a digitar o nome ou o ID do cliente desejado e selecione-o na lista que aparecer.
    b. **Serviço:** Este campo já virá preenchido com o serviço da rota mestra.
    c. **Ativo? / Visível?:** Marque estas caixas para definir se a rota estará ativa e visível para este cliente específico.
    d. Clique em **"Incluir"** para confirmar a atribuição.
3.  Após incluir, o cliente aparecerá na listagem da aba "Utilização".
4.  **Ajuste Fino:** Na lista de clientes que usam a rota, você pode editar o **NOME** da rota para que ele apareça de forma personalizada para aquele cliente (ex: "Short HQ").
5.  Para salvar todas as atribuições e edições, clique em **"Save changes"**. Para remover uma atribuição, selecione o cliente na lista e clique em **"Remover Selecionadas"**.

## 7.4. Testando a Rota (Aba "Testes")

Esta aba permite realizar um teste de ponta a ponta para validar o funcionamento e a performance de uma rota antes de liberá-la para o cliente.

1.  Dentro da tela de edição da rota, acesse a sub-aba **"Testes"**.
2.  Preencha os campos para o teste:
    a. **Destinos:** Insira um ou mais números de celular para receber a mensagem de teste.
    b. **Mensagem:** O campo já contém uma mensagem padrão com variáveis (como $id_rota$) que pode ser usada, ou você pode editar com seu próprio texto.
    c. **Tag:** Atribua uma etiqueta para identificar este teste.
3.  Clique em **"Testar Roteamento"**.
4.  O sistema exibirá o **"Resultado Roteamento"**, um log técnico que mostra o status do envio em tempo real.
    a. **Análise do Resultado:** Você poderá acompanhar o status mudar de Status 1 - Pronto para envio com **RemoteStatusPENDING_ACCEPTED** para Status 10 - Entrega confirmada com **RemoteStatusDELIVERED**, validando que a rota está operacional.
5.  Para informações ainda mais detalhadas sobre a entrega, clique no botão **"Consultar DLR"**.