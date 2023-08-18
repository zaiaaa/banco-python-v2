let lista = [{Nome: "Gustavo", CPF: "123", endereco: "Rua 12"},{Nome: "Eliete", CPF: "542", endereco: "Rua 12"}, {Nome: "Eliete", CPF: "542", endereco: "Rua 12"}] 

const lista_clientes = lista.map(e => console.log(`Cliente ${e.Nome}, CPF: ${e.CPF}`))

const valida_cpf = lista.filter(e => e.CPF == '542')

console.log(valida_cpf[0])

let numero_conta = 1

numero_conta++