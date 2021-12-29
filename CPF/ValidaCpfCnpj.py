from Cpf_Cpnj2 import Documento

#cpf_um = Cpf("31940678854")
#print(cpf_um)

#exemplo_cnpj = "52736949004811"
exemplo_cpf = "31940678854"
#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))
documento = Documento.cria_documento(exemplo_cpf)
print(documento)








#cpf = "31940678854"
#objeto_cpf = Cpf(cpf)
#print(objeto_cpf)
