# Financial Ledger

[English](README.md) | Português (Brasil)

Aplicação de controle financeiro pessoal em desenvolvimento com Python. A primeira versão funcionará pelo terminal e permitirá registrar receitas e despesas, consultar os lançamentos e acompanhar o saldo.

## Status

Configuração inicial e planejamento. As funcionalidades listadas abaixo estão previstas e ainda não foram implementadas.

## Primeira versão

- [ ] Registrar receitas com descrição e valor.
- [ ] Registrar despesas com descrição e valor.
- [ ] Listar os lançamentos cadastrados.
- [ ] Calcular o total de receitas, o total de despesas e o saldo.
- [ ] Salvar os lançamentos em um arquivo CSV e carregá-los ao iniciar a aplicação.
- [ ] Validar as entradas do usuário e tratar erros esperados ao trabalhar com arquivos.

## Dados de cada lançamento

Cada lançamento terá:

- **Tipo:** receita ou despesa.
- **Descrição:** a que o lançamento se refere.
- **Valor:** o valor monetário do lançamento.

## Etapas de desenvolvimento

1. Construir o menu no terminal e cadastrar lançamentos em memória.
2. Implementar a listagem e os cálculos de saldo.
3. Adicionar persistência em CSV.
4. Conferir a validação e o tratamento de erros e documentar a execução.

A primeira versão estará concluída quando for possível cadastrar e listar lançamentos, calcular o saldo e recuperar os dados após fechar e reabrir a aplicação, com a validação básica funcionando.

## Tecnologias

- **Python 3:** linguagem prevista para a aplicação.
- **Biblioteca padrão do Python:** incluindo o módulo `csv` para persistência.
- **Git e GitHub:** versionamento e documentação do projeto.

O escopo inicial utiliza somente a biblioteca padrão do Python; as funcionalidades planejadas não exigem pacotes externos.

## Primeiros passos

Clone o repositório:

```bash
git clone https://github.com/marcosvs11/financial-ledger.git
cd financial-ledger
```

A aplicação ainda não possui uma versão executável. As instruções de execução serão adicionadas quando a primeira versão funcional estiver disponível.

## Objetivos de aprendizado

Consolidar os fundamentos de Python em um projeto completo: funções, estruturas de dados, módulos, validação de entradas, tratamento de exceções, arquivos CSV e versionamento.
