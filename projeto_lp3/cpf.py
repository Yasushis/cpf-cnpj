from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("242.534.059-32"))
print(cpf.validate("24253405932"))