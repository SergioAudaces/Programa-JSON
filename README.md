🎯 Sobre o Projeto
O Sistema de Manutenção JSON foi desenvolvido para proporcionar aos Analistas de Dados uma interface visual intuitiva para gerenciar arquivos JSON complexos utilizados em ETL.

  Principais Objetivos
✅ Facilitar a consulta de configurações ETL
✅ Permitir edição visual de dados estruturados
✅ Agilizar a criação de novos itens e transformações
✅ Garantir a integridade da estrutura JSON
✅ Melhorar a produtividade da equipe de dados

  ⚡ Funcionalidades
Operações Principais
Funcionalidade  - Descrição
🔍 Consulta    - Visualização organizada e hierárquica dos dados JSON
✏️ Edição      - Editor integrado com validação em tempo real
➕ Criação     - Assistente para novos itens, ETLs e Dimensions
💾 Download    - Exportação automática do JSON editado

  Gerenciamento Avançado
Transforms: Criação e edição de transformações de dados
Sources: Configuração de fontes de dados
Destinies: Definição de destinos de carga
Dimensions: Gerenciamento completo de dimensões
SQL Viewer: Visualização de queries SQL relacionadas
Validação: Verificação automática da estrutura do arquivo



📖 Guia de Uso
1️⃣ Iniciando o Sistema
Via Python
bashstreamlit run app.py
Via Executável
Na área de trabalho, clique duas vezes no ícone do Sistema de JSON.
O sistema será aberto automaticamente no seu navegador padrão.

2️⃣ Carregando um Arquivo JSON
Na tela inicial, clique no botão "Selecionar Arquivo JSON"
Navegue até o arquivo desejado e selecione-o
O sistema validará automaticamente se o arquivo contém as chaves obrigatórias:
TRANSFORMS
SOURCES
DESTINIES

⚠️ Atenção: Se o arquivo não contiver essas chaves, uma mensagem de erro será exibida e o carregamento será cancelado.

Após carregamento bem-sucedido, o sistema exibirá:
✅ Confirmação de arquivo válido
📊 Contagem de itens em cada chave
🗂️ Lista navegável de todos os elementos


3️⃣ Navegação e Visualização
Expandir/Recolher Visualização

Clique na seta (▼) ao lado de qualquer seção para expandir
Clique novamente na seta (▲) para recolher
Use a expansão para melhor visualização de estruturas aninhadas

Seleção de Chaves

Use o menu dropdown para selecionar entre:
TRANSFORMS: Transformações de dados
SOURCES: Fontes de origem
DESTINIES: Destinos de carga


Após selecionar a chave, o sistema listará todos os itens disponíveis
Busca e Filtro
Digite o nome do item desejado na caixa de busca
Selecione um item da lista suspensa
A visualização será atualizada automaticamente


4️⃣ Operações de Manutenção
➕ Criar Novo Item

Clique no botão "+ Novo Item"
Preencha o formulário:
Nome do Item: Identificador único
Tipo: Selecione o tipo apropriado

Clique em "Criar" para confirmar
🏗️ Criar Nova ETL
Clique no botão "+ Nova ETL"
Digite o nome da ETL
Clique em "Gerar"
O sistema criará automaticamente a estrutura base com:
Configurações padrão
Campos obrigatórios
Estrutura validada


5️⃣ Trabalhando com SQL e Detalhes
Visualização de SQL
Selecione um item da lista
Clique na barra "Expandir SQL"
A janela exibirá:
Query SQL completa
Parâmetros utilizados
Tabelas relacionadas

Janela de Detalhes do Item
Ao expandir um item, você visualizará:
📋 Informações Gerais: Nome, tipo, descrição
🔑 Keys: Chaves primárias e estrangeiras
🔍 IdFinder: Configurações de busca por ID
🔗 LookupAtts: Atributos de lookup
📊 Columns_name: Nomes das colunas
📈 Measures: Medidas e métricas
🔗 Keyrefs: Referências de chaves


6️⃣ Gerenciamento de Dimensions
As Dimensions são elementos fundamentais para análise dimensional de dados.
Visualizar Dimensions

Navegue até a seção "Dimensions"
A lista de dimensions será exibida automaticamente
Criar Nova Dimension
Clique em "+ Nova Dimension"
Uma janela modal será aberta com os campos:
Nome da Dimension
Tipo
Atributos
Preencha os dados necessários
Clique em "Salvar"

Editar Dimension Existente
Clique no nome da dimension desejada
O modal de edição será aberto
Modifique os campos desejados:

Tabela de Dimensions: Estrutura principal
IdFinder: Configuração de identificadores
Lookup e Columns: Atributos de busca

Clique em "Atualizar" para salvar

7️⃣ Gerenciamento de Transforms
Visualizar Transforms
A seção Transforms exibe todas as transformações de dados configuradas.
Criar Novo Transform

Clique em "+ Novo Transform"
Preencha a janela modal:
Nome do Transform
Tipo de Transformação
Parâmetros
Configurações adicionais

Valide os dados
Clique em "Criar"
Editar Transform
Selecione o transform desejado da lista
Modifique os campos necessários
Use o Editor JSON para ajustes avançados
Salve as alterações


8️⃣ Editor JSON Avançado
O sistema inclui um editor JSON integrado para modificações diretas.
Acessando o Editor

O editor será exibido automaticamente na lateral direita
O código JSON será formatado e colorizado

Editando JSON


9️⃣ Salvando e Exportando
Salvar Alterações
Após realizar todas as modificações desejadas
Clique no botão "💾 Salvar JSON" no topo da página
O sistema validará todas as alterações
Uma mensagem de sucesso será exibida

Download do Arquivo Editado

Após o salvamento bem-sucedido
Clique no botão "⬇️ Baixar JSON editado"
O arquivo será automaticamente salvo na pasta Downloads
Nome do arquivo: edited_[nome-original][nº-sequencia].json


✅ Boas Práticas
Antes de Começar
💾 Faça backup: Sempre mantenha uma cópia do arquivo original
📝 Documente alterações: Anote o que foi modificado e por quê
🧪 Teste em ambiente de desenvolvimento antes de produção

Durante a Edição
🎯 Use nomes descritivos: Facilita identificação posterior
📊 Mantenha consistência: Siga padrões de nomenclatura da equipe
✔️ Valide frequentemente: Salve e teste incrementalmente
🔍 Revise dependências: Verifique impactos em outros itens

Após Editar
🧹 Limpe dados não utilizados: Remova comentários e campos vazios
📤 Versione no Git: Commit das alterações com mensagem clara
👥 Comunique a equipe: Informe sobre mudanças importantes
