#''' padrão para encontra email em texto

padrao = "\w{5,50}@\w{3,10}.\w{2,3}"
texto = "aaabbbcc juniorppb@gmail.com asdfaddpvdsvpasdvafv"
resposta = re.search(padrao,texto)
print(resposta.group())'''

