# Simulador de Banco - Sistema de Transações Bancárias

Este é um simulador de sistema bancário simples desenvolvido em Python. Ele permite a realização de operações como depósito, saque, transferências entre contas, e exibição de extrato bancário. O sistema também oferece uma funcionalidade de ajuda e controle de saldo e limite de saque.

## Funcionalidades

1. **Depositar**: Permite adicionar dinheiro à conta, exibindo o saldo atualizado.
2. **Sacar**: Realiza a retirada de um valor da conta, verificando o saldo e o limite de saque.
3. **Transferência entre contas**: Suporta diferentes tipos de transferência: DOC, PIX e TEF.
4. **Extrato**: Exibe um resumo das últimas 10 transações.
5. **Help**: Fornece informações de contato com o suporte.
6. **Sair**: Encerra o sistema.

## Instruções de Uso

Ao iniciar o programa, o usuário deve escolher se deseja definir o saldo e o limite de saque:

- **[1] sim**: O usuário define os valores iniciais para saldo e limite de saque.
- **[2] não**: O saldo começa em 0 e o limite de saque é de R$500,00.

### Menu de Operações

Após definir o saldo, o sistema apresenta as seguintes opções:

```text
[1] Depositar
[2] Sacar
[3] Transferência entre contas
[4] Extrato
[5] Help
[6] Sair
