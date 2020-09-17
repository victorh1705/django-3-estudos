from validate_docbr import CPF


def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(rg):
    return len(rg) == 9


def celular_valido(celular):
    return len(celular) == 1
