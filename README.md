# Entrega dos desafios da formação Python Developer da DIO
Repositórios com as entregas para os desafios da formação Python Developer da Digital Innovation One.

Objetivo Geral para a etapa 01:

- [x] Separar as funções existentes de saque, depósito e extrato em funções do Python;
- [x] Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária;
- [x] Criar uma função para listar todas as contas.
- [ ] Criar função para inativar conta.

### Requisitos

- [x] A conta corrente deve estar vinculada com o usuário;
- [x] A função saque deve receber os argumentos somente por nome (keyword only). Sugestões de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.
- [x] A função de depósito deve receber os argumentos somente por posição (positional only). Sugestões de argumentos: saldo, valor, extrato. Sugestõe de retorno: saldo e extrato;
- [x] A função extrato deve receber os argumentos por nome e posição (keyword and positional only). Argumentos posicionais: saldo; argumentos nomeados: extrato.
- [x] Requisitos para a nova função cadastrar usuário:
  - [x] Os usuários deverão estar armazenados em uma lista;
  - [x] Criar os seguintes campos para cadastro do usuário: nome, CPF, data de nascimento e endereço;
  - [x] O endereço é do tipo string com o formato: logradouro, nr - bairro - cidade/sigla estado;
  - [x] Deve ser armazenado somente os números do CPF (criar validação);
  - [x] Não podemos cadastrar 2 usuários com o mesmo CPF (runtime error? ou criar validação?).
- [x] Requisitos para a função criar conta:
  - [x] O programa deve armanezar contas em uma lista;
  - [x] A conta deve ser do tipo dict e ter as seguintes chaves: agência, número da conta e usuário;
  - [x] O número da conta é sequencial, iniciando em 1;
  - [x] O número da agência é fixo "0001";
  - [x] O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário;

### Dica

Para vincular uma conta a um usuário, filtre a lista de usuários buscando o número de CPF informado para cada usuário da lista.
