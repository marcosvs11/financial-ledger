# Testes manuais

## 1. Alinhamento da listagem

*Procedimento:*
1. Cadastrar um lançamento com uma descrição curta.
2. Cadastrar outro com uma descrição de mais de 21 caracteres.
3. Selecionar a opção 3 para consultar os lançamentos.
4. Abrir o CSV e conferir a descrição completa.

*Resultado esperado:*
A descrição longa aparece abreviada com "...".
A coluna dos valores permanece alinhada.
A descrição completa continua armazenada no CSV.

*Resultado observado:*
A descrição longa apareceu abreviada com "...", preservando
o alinhamento da listagem. A descrição completa permaneceu no CSV.

*Situação:* Passou.

## 2. Exibição dos valores com duas casas decimais

*Procedimento:*
1. Cadastrar um lançamento com o valor 5.
2. Cadastrar outro com o valor 12,3.
3. Selecionar a opção 3 para consultar os lançamentos.

*Resultado esperado:*
Os valores aparecem como R$5.00 e R$12.30, respectivamente.

*Resultado observado:*
A listagem apresentou R$5.00 e R$12.30, ambos com duas casas
decimais e ponto como separador decimal.

*Situação:* Passou.
