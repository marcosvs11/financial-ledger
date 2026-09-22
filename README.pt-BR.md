# Financial Ledger

[English](README.md) | Português (Brasil)

Aplicação de terminal para acompanhar receitas e despesas pessoais. Permite cadastrar lançamentos, consultar cada registro e calcular o total de receitas, o total de despesas e o saldo. Os dados são armazenados localmente em um arquivo CSV e permanecem disponíveis após encerrar a aplicação.

## Status

A primeira versão funcional está implementada. Ela utiliza a biblioteca padrão do Python e inclui validação de entradas, persistência em CSV e verificações manuais documentadas em [TESTING.md](TESTING.md).

Este é um projeto de aprendizado. As limitações atuais e as possíveis melhorias estão descritas abaixo.

## Primeira versão

- [x] Registrar receitas com descrição e valor.
- [x] Registrar despesas com descrição e valor.
- [x] Listar os lançamentos cadastrados.
- [x] Calcular o total de receitas, o total de despesas e o saldo.
- [x] Salvar os lançamentos em um arquivo CSV e consultá-los ao listar os registros ou visualizar o resumo.
- [x] Validar opções do menu, descrições e valores.
- [x] Exibir os valores dos lançamentos com duas casas decimais.
- [x] Abreviar descrições longas na listagem, preservando o texto completo no CSV.

## Requisitos

Python 3.12 ou superior.

Git, caso o repositório seja clonado com os comandos abaixo.

Não são necessários pacotes externos do Python. A aplicação utiliza csv para armazenar os dados e Decimal para representar os valores monetários e realizar os cálculos.

## Como executar

Confira a versão do Python:

python3 --version

Clone o repositório e execute a aplicação dentro da pasta do projeto:

```bash
git clone https://github.com/marcosvs11/financial-ledger.git
cd financial-ledger
python3 main.py
```
Na primeira execução, a aplicação cria financial_ledger.csv com o cabeçalho caso o arquivo não exista. As execuções seguintes preservam os lançamentos existentes.

## Como usar

1 — Add income
Informar a descrição e o valor recebido.

2 — Add expense
Informar a descrição e o valor pago.

3 — List transactions
Exibir o tipo, a descrição e o valor de cada lançamento.

4 — View summary
Exibir o total de receitas, o total de despesas e o saldo.

5 — Exit
Encerrar a aplicação.

Os valores de receitas e despesas são informados como números positivos. O saldo é calculado subtraindo as despesas das receitas e pode ser negativo.

Descrições com mais de 21 caracteres são exibidas com os primeiros 18 caracteres seguidos de .... A descrição completa permanece no CSV.

## Regras de entrada

- As opções do menu devem ser números inteiros de 1 a 5.

- As descrições devem conter texto; entradas vazias ou formadas apenas por espaços são recusadas. Espaços no início e no fim são removidos.

- Os valores devem ser números positivos e finitos, com no máximo duas casas decimais.

- É possível usar ponto ou vírgula como separador decimal: 5, 12.3, 12.30 e 12,30 são exemplos válidos.

- Digite valores sem R$ e sem separadores de milhar. Por exemplo, utilize 1500,50 ou 1500.50.

-Quando a entrada é inválida, o programa solicita uma nova tentativa.

Na listagem, os valores aparecem com R$, ponto como separador decimal e duas casas decimais, como R$5.00 e R$12.30.

## Armazenamento em CSV

O arquivo utiliza codificação UTF-8 e estas colunas:

type -> income para receita ou expense para despesa.

description -> Descrição completa do lançamento.

amount -> Texto numérico sem símbolo de moeda, utilizando ponto quando há separador decimal.

Exemplo:

type,description,amount
income,Freelance,250
expense,"Café, pão e leite",12.30

Cada lançamento é salvo ao ser cadastrado. Os valores armazenados não precisam conter zeros à direita; a listagem aplica a formatação com duas casas decimais na exibição.

O caminho do CSV é relativo à pasta atual do terminal. Execute o programa dentro da pasta do projeto para continuar utilizando o mesmo arquivo. Executá-lo a partir de outra pasta pode criar ou utilizar um CSV diferente.

O arquivo local financial_ledger.csv é excluído do versionamento por meio do .gitignore.

## Arquivos do projeto

Arquivo    Responsabilidade

main.py -> Fluxo da aplicação e ações do menu.

interface.py -> Exibição de títulos e do menu.

validation.py -> Leitura e validação das entradas do usuário.

file.py -> Inicialização do CSV, armazenamento, listagem e cálculo do resumo.

TESTING.md -> Procedimentos dos testes manuais e resultados observados.

## Testes

O [TESTING.md](TESTING.md) documenta atualmente dois testes manuais: alinhamento de descrições longas e exibição de valores com duas casas decimais. Cada registro contém o procedimento, o resultado esperado, o resultado observado e a situação do teste.

Utilize dados fictícios ao repetir os testes. O repositório ainda não possui uma suíte de testes automatizados.

## Limitações conhecidas

- A aplicação espera que um CSV existente tenha o cabeçalho correto e dados válidos. Ela não repara arquivos existentes vazios ou malformados; dados inválidos podem interromper a execução.

- Erros de permissão e outras falhas de leitura ou gravação ainda não possuem tratamento com mensagens amigáveis.

- Não é possível editar ou excluir lançamentos pelo menu.

- Possíveis melhorias incluem tratar erros esperados de arquivo e adicionar testes automatizados. Essas melhorias não estão implementadas na versão atual.

## Objetivos de aprendizado

Consolidar os fundamentos de Python por meio de um projeto completo: funções, dicionários, módulos, validação de entradas, tratamento de exceções, persistência em CSV, cálculos com decimais, testes manuais e versionamento com branches e pull requests.
