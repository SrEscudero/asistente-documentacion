# 10. Aba Filtros de Conteúdo

## Visão Geral

A seção de Filtros é uma ferramenta de segurança que permite criar regras para analisar o conteúdo das mensagens de SMS antes do envio. Sua principal função é bloquear, permitir ou redirecionar mensagens que contenham palavras, expressões ou padrões específicos, garantindo que os envios estejam em conformidade com as políticas da plataforma. O gerenciamento pode ser feito de duas formas: através de uma Lista interativa ou pela edição direta de um JSON.

## Gerenciamento via Modo Lista

Este modo oferece uma interface visual para gerenciar cada filtro individualmente.

* **Criando um Novo Filtro:** Clique no botão **Novo Filtro** na parte inferior da tabela. Uma nova linha será adicionada à lista para que você preencha os campos necessários.
* **Descrição dos Campos do Filtro:**
    * **Código:** Um nome ou identificador único para a regra (ex: seguranca-03).
    * **Tipo:** Define o método de correspondência do texto (**palavra**, **expressaoRegular**, **exata**).
    * **Texto:** O conteúdo a ser filtrado (uma palavra, lista de palavras ou expressão regular).
    * **Revisão?:** Se marcado, envia a mensagem correspondente para a moderação manual.
    * **Positiva?:** Caixa de seleção para regras de filtro positivo.
    * **Ação:** Define o que acontecerá com a mensagem (**Reject**, **Allow**, **RedirectRoute**, **none**).
    * **Rota:** Campo opcional para aplicar a regra apenas a uma rota específica.
* **Salvando, Desativando e Removendo Filtros:**
    * **Salvar Alterações:** Clique em **Save changes**.
    * **Cancelar Alterações:** Clique em **Cancel changes**.
    * **Desativar um Filtro:** Desmarque a caixa na coluna ATIVO e clique em **Save changes**.
    * **Remover um Filtro:** Clique no ícone de X vermelho e clique em **Save changes**.

## Gerenciamento via Modo JSON

Este modo é ideal para gerenciamento em massa ou para importar uma configuração de filtros predefinida.

* **Acessar o Editor:** Clique na aba **JSON** para visualizar e editar a estrutura de filtros completa.
* **Importar/Editar:** Cole uma estrutura JSON válida diretamente na área de texto.
* **Adicionar um Novo Filtro:** Crie um novo objeto dentro do array **[...]**, mantendo a sintaxe correta do JSON.
* **Salvar:** Clique em **Save changes** para aplicar a nova estrutura.
* **Restaurar Padrão:** O botão **Padrão** reverte para a configuração de filtros original da plataforma.