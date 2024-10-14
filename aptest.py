import pandas as pd
#pd é abreviação de pandas
planilha = pd.read_excel('./sec.xlsx', sheet_name = 'Weibull')
print (planilha)
linhas_especificas = planilha.iloc[[1, 3, 5]]
print(linhas_especificas)

# isso é pra criar e escrever no arquivo
with open('sec3.txt', 'w') as arquivo:
    # Escrever no arquivo
    arquivo.write(str(linhas_especificas))

# O arquivo será automaticamente fechado ao sair do bloco "with"






















# nome = input('Diga com quem tu andas e eu direi quem és: ')
# lista = [1,1,2,3,5,8,13,21]
# for i in range(5,8):
    
#     print(lista[i]) 
# # if nome == 'com quem tu andas':
# #     pass  # O bloco if não faz nada

# # print('Quem tu és' + '\n')
