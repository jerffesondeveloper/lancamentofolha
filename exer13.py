# CALCULANDO SALÁRIO COM BASE EM HORAS TRABALHADAS
#importação de bibliotecas
import time
import colorama
from colorama import Fore, Back, Style
from datetime import datetime as dt
colorama.init()

#PARA DATA E HORA
data = dt.now()
Hora=0
Minuto=0
Segundo=0
Hora=data.hour
Minuto=data.minute
Segundo=data.second
HoraAtual=data.strftime("%d/%m/%y - %H:%M:%S") 
   


#CABEÇALHO
print('*-*-'*10)
print('\33[1;42mSISTEMA DE GERENCIAMENTO - MÓDULO FOLHA \33[m')
print('*-*-'*10)
print('\n')
print(Fore.LIGHTGREEN_EX + Style.BRIGHT + 'SEJA BEM VINDO! \n' + Fore.RESET)
print(HoraAtual )
print('\n')

#LOGIN DO OPERADOR
while True:
    opr = input(Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'INFORME DO CÓDIGO DO OPERADOR:' + Back.RESET + " " + Fore.RESET)
    if opr == '052' or opr == '581':
        if opr == '052':
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT +'\nBem Vindo, Jerffeson'+ Fore.RESET + Style.RESET_ALL)
        if opr == '581':
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT +'\nBem vindo Iasmin'+ Fore.RESET + Style.RESET_ALL)
        break
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + '\nOPERADOR NÃO CADASTRADO \nDigite o código novamente!')

# Dados do colaborador
print('\n')
cola = input(Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'INFORME O NOME DO COLABORADOR:'  + Back.RESET + " " + Fore.RESET).upper()
print(Fore.GREEN + Style.BRIGHT +'''\nOK!
A seguir insira as informações para {}
      '''.format(cola))

#time.sleep(2)
while True:
        while True:
            fun = input(Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'INFORME A FUNÇÃO DO COLABORADOR:' + Fore.RESET + Back.RESET + Style.RESET_ALL +
            '\n[1]CAIXA'
            '\n[2]GERAIS \n>>> ')

            #PARA A FUNÇÃO CAIXA
            if fun == ('1'):
                print(Fore.GREEN + '\nA hora trabalhada para esta função é R$ 17.30\n' )
                salario = float(input(Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'INFORME AS HORAS TRABLAHADAS DE {}:'.format(cola)  + Back.RESET + " "+ Fore.RESET  + Style.RESET_ALL ))
                cal1 = salario * 10.15
                print(Fore.GREEN +'\nA remuneração bruta na função Caixa é R$ {:.2f}\n'.format(cal1))
                
                while True:
                    r = input(Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + 'DESEJA ACRESENTAR HORA EXTRA PARA {}'.format(cola) + Fore.RESET + Back.RESET + Style.RESET_ALL + 
                            '\n[1]Sim'
                            '\n[2]Não \n>>>')
                    
                    if r == ('1'):
                        hx = float(input('\n' + Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + 'INSIRA A QUANTIDADE DE HORAS EXTRAS:' + Fore.RESET + Back.RESET+ " "))
                        hxr = hx * 12.78
                        print('\n')
                        print(Fore.GREEN + 'O valor da hora extra é de R$ {:.2f}\nSomado com o valor da hora extra o salário fica de R$ {:.2f}\n'.format(
                                    hxr, hxr + cal1))
                        while True:
                            vr = input(Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'DESEJA ACRESENTAR  "VR"?' + Back.RESET + Fore.RESET+
                                    '\n[1]Sim'
                                    '\n[2]Não'
                                    '\n>>> ')
                            if vr == ('1'):
                                vvr = float(input('\n' +Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'INFORME O VALOR DA "VR" R$:'+ Back.RESET + Fore.RESET+ " "))
                                print('\n'+Back.BLUE + Fore.GREEN + 'O salário final acrescido da "VR" é de {:.2f}'.format(vvr + hxr + cal1)+ Back.RESET + Fore.RESET)
                                break
                            elif vr == ('2'):
                                print('\n'+ Fore.LIGHTWHITE_EX + Style.BRIGHT+Back.BLUE +'O valor do salário final é de : R$ {:.2f}'.format(hxr + cal1) + Fore.RESET+Back.RESET+Style.RESET_ALL)
                                break

                            else:
                                print('\n' + Fore.RED + Back.BLUE +'Opção inesistente, escolha entre as opções "1" ou "2"'+ Fore.RESET + Back.RESET+'\n')
                        
                        break
                            
                    elif r== ('2'): 
                        while True:               
                            hx2 = input('\n'+Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'DESEJA ACRESENTAR  "VR"' + Fore.RESET+Style.RESET_ALL+Back.RESET  +
                                        '\n[1]Sim' 
                                        '\n[2]Não' '\n>>>')
                            if hx2 == ('1'):
                                hx21 = float(input('\n'+Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'INSIRA O VALOR: R$'+ Fore.RESET+Style.RESET_ALL+Back.RESET  + " "))
                                print('\n'+ Fore.LIGHTWHITE_EX + Style.BRIGHT+Back.BLUE +'O valor final do salário com o "VR" é R$ {}'.format(cal1 + hx21)+ Fore.RESET+Back.RESET+Style.RESET_ALL)
                                break
                            elif hx2 == ('2'):
                                print('\n'+ Fore.LIGHTWHITE_EX + Style.BRIGHT+Back.BLUE +'O valor final do salário do colaborador', cola, 'é de {}'.format(cal1)+ Fore.RESET+Back.RESET+Style.RESET_ALL)
                                break
                            else:
                                print('\n' + Fore.RED + Back.BLUE +'Opção inesistente, escolha entre as opções "1" ou "2"'+ Fore.RESET + Back.RESET+'\n')
                                
                        break

                    else:
                        print('\n' + Fore.RED + Back.BLUE +'Opção inesistente, escolha entre as opções "1" ou "2"'+ Fore.RESET + Back.RESET+'\n')
                
                break

            #PARA A FUNÇÃO GERAIS
            if fun == ('2'):
                print(Fore.GREEN+ Style.BRIGHT+'\nA hora trabalhada para esta função é R$ 13.20'+ Fore.RESET )
                salario1 = float(input('\n'+ Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + 'INFORME AS HORAS TRABALHADAS DE {}:'.format(cola)+ Fore.RESET + Back.RESET + Style.RESET_ALL + " "))
                cal2 = salario1 * 13.20
                print(Fore.GREEN + Style.BRIGHT + '\nA remuneração bruta na função {} é R$ {}'.format(fun, cal2) + Fore.RESET + Style.RESET_ALL)

                while True:
                    r2 = str(input('\n'+ Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + 'DESEJA ACRECENTAR HORA EXTRA PARA {}'.format(cola) + Fore.RESET + Back.RESET + Style.RESET_ALL +
                                '\n[1]Sim'
                                '\n[2]Não \n>>>'))
                    if r2==('1'):
                        hx2 = float(input('\n'+Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'INSIRA A QUANTIDADE DE HORAS:'+ Fore.RESET + Back.RESET + Style.RESET_ALL + " "))
                        hxr2 = hx2 * 15.00
                        print(Fore.GREEN + Style.BRIGHT +'\nO valor da hoa extra é de R$ {:.2f} \nSomado com o valor da hora extra o salário fica de R$ {:.2f}'.format(hxr2, hxr2+cal2)+ Fore.RESET + Style.RESET_ALL)

                        while True:
                            vr2=str(input('\n'+Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + 'DESEJA ACRESCENTAR  "VR"' +Fore.RESET + Back.RESET + Style.RESET_ALL + " "     
                                    '\n[1]Sim' 
                                    '\n[2]Não \n>>>'))
                            if vr2== ('1'):
                                vvr2 = float(input('\n' +Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'INFORME O VALOR DA "VR" R$:'+ Back.RESET + Fore.RESET+ " "))
                                print('\n'+Back.BLUE + Fore.GREEN + 'O salário final acrescido da "VR" é de {:.2f}'.format(vvr2 + hxr2 + cal2)+ Back.RESET + Fore.RESET)
                                break
                            elif vr2==('2'):
                                print('\n'+Back.BLUE + Fore.GREEN + 'O salário final acrescido da "VR" é de {:.2f}'.format(hxr2 + cal2)+ Back.RESET + Fore.RESET)
                                break
                            
                            else:
                                print('\n' + Fore.RED + Back.BLUE + 'A função {} é  INESISTENTE!  Por favor escolha uma função cadastrada.'.format(fun) + Fore.RESET + Back.RESET+'\n')      
                        break
                                    
                    elif r2==('2'):
                        while True:
                            vr2=str(input('\n'+Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + 'DESEJA ACRESCENTAR  "VR"' +Fore.RESET + Back.RESET + Style.RESET_ALL + " "     
                                    '\n[1]Sim' 
                                    '\n[2]Não \n>>>'))
                            if vr2== ('1'):
                                vvr2 = float(input('\n' +Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT +'INFORME O VALOR DA "VR" R$:'+ Back.RESET + Fore.RESET+ " "))
                                print('\n'+Back.BLUE + Fore.GREEN + 'O salário final acrescido da "VR" é de {:.2f}'.format(vvr2 + hxr2 + cal2)+ Back.RESET + Fore.RESET)
                                break
                            elif vr2==('2'):
                                print('\n'+Back.BLUE + Fore.GREEN + 'O salário final acrescido da "VR" é de {:.2f}'.format(hxr2 + cal2)+ Back.RESET + Fore.RESET)
                                break
                            
                            else:
                                print('\n' + Fore.RED + Back.BLUE + 'A função {} é  INESISTENTE!  Por favor escolha uma função cadastrada.'.format(fun) + Fore.RESET + Back.RESET+'\n')      

                        break     
                        
                    else:
                        print('\n' + Fore.RED + Back.BLUE + 'A função {} é  INESISTENTE!  Por favor escolha uma função cadastrada.'.format(fun) + Fore.RESET + Back.RESET+'\n')
                break           

            else:
                print('\n' + Fore.RED + Back.BLUE + 'A função {} é  INESISTENTE!  Por favor escolha uma função cadastrada.'.format(fun) + Fore.RESET + Back.RESET+'\n')

        print('\n'+Back.GREEN+Fore.LIGHTGREEN_EX+Style.BRIGHT+'LANÇAMENTO CONCUÍDO COM SUCESSO!'+Back.RESET+Fore.RESET+Style.RESET_ALL)

        retorno=input('\n'+Fore.GREEN +Style.BRIGHT+'DESEJA FAZER OU LANÇAMENTO?'+Fore.RESET+Style.RESET_ALL +
                  '\n[1]Sim'
                  '\n[2]não \n>>>')
        if retorno== ('2'):
            print(Fore.GREEN +'FIM DO PROCESSO'+Fore.RESET)
            break
        else:
            retorno==('1')
            print('\n')
            
