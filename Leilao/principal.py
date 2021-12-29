from dominio import Usuario, Lance, Leilao

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('Celular')

Leilao.lances.append(lance_do_gui)
Leilao.lances.append(lance_do_yuri)

for lance in Leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')
