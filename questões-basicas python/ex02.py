# Questão 2 - O IPVA é calculado de acordo com o tipo de veículo, cuja alíquota é definida por
#cada Estado sobre o valor venal do carro de acordo com a Tabela Fipe (Fundação
#Instituto de Pesquisas Econômicas), variando entre 1% e 4%. Escreva um programa em
#Python para calcular o valor do IPVA de um veículo com base nas informações a seguir:
#Alíquota Tipo do Veículo
#4,0% Automóveis
#3,0% Caminhonetes de carga e furgão.
#2,0% Automóveis para transporte público (ex: táxi,

#escolar)
#2,0% Motocicletas.
#1,0% Veículos de locadoras.
#1,0% Ônibus, micro-ônibus, caminhão, caminhão trator.
#OBS: o valor venal do carro deverá ser fornecido pelo usuário.

valor_venal = float(input('Digite o valor venal: '))
while valor_venal <= 0:
    print('Valor invalido')
    valor_venal = float(input('Digite o valor venal: '))

Tipo_veiculo = input('Informe o tipo de veiculo:\n Automovel \n Caminhonete de carga ou Furgão \n Transporte público \n Motocicleta \n Veiculo de locadora \n Ônibus, Trator, Micro-Ônibus ou Caminhão: ')

    
if Tipo_veiculo == 'Automovel':
    ipva_automovel = (valor_venal * 0.04)
    print(f" O IPVA do veiculo é: R${ipva_automovel:.2f}")
elif Tipo_veiculo == 'Caminhonete de carga' or 'Furgão':
    ipva_caminhao_furgao = (valor_venal * 0.03)
    print(f" O IPVA do veiculo é: R${ipva_caminhao_furgao:.2f}")
elif Tipo_veiculo == 'Transporte público':
    ipva_transporte_publico = (valor_venal * 0.02)
    print(f"O IPVA do veiculo é: R${ipva_transporte_publico:.2f} ")
elif Tipo_veiculo == 'Motocicletas':
    ipva_motocicletas = (valor_venal * 0.02)
    print(f"O IPVA do veiculo é: R${ipva_motocicletas:.2f}")
elif Tipo_veiculo == 'Veiculo de locadora':
    ipva_veiculos_locadoras = (valor_venal * 0.01)
    print(f"O valor do IPVA é: R${ipva_veiculos_locadoras:.2f}")
elif Tipo_veiculo == 'Ônibus' or 'Micro-Ônibus' or 'Caminhão' or 'Trator':
    ipva_onibus_micro = (valor_venal * 0.01)
    print(f"O IPVA do veiculo é: R${ipva_onibus_micro:.2f}")
