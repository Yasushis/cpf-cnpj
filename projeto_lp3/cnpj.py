from validate_docbr import CNPJ

cnpj = CNPJ()

print(cnpj.generate(True))
print(cnpj.generate(False))

print(cnpj.validate("242.534.059-32"))
print(cnpj.validate("24253405932"))