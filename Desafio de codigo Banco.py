menu = """

[1] Depositar
[2] Sacar
[3] Transferencia entre contas
[4] Extrato
[?] Recarga de celular e vale-transporte (indisponível)
[5] Help
[6] Sair

"""
saldo = 0
limite = 500
numero_de_saque = 1
LIMITE_DE_SAQUE = 3
extrato = [] 
i = 0


          
     
while True:

     opção = int(input(menu))
     
     if opção < 1 or opção > 6:
          print('\n opção invalida')
          continue
     
     if opção == 1:
          while True:
               
               depositar = float(input('Qual valor do Depositor: '))
               if depositar < 1 :
                    print('')
                    print( 'valor do depositor invalido \n tenta novamente')
                    print('')
                    continue
               saldo += depositar
               resposta = f"DEPOSITOR: R${depositar:.2f}"
               extrato.append( str(resposta))
               i += 1
               print('')
               print(f'depositor realizado \nsaldo atual de R${saldo:.2f}')
               print('')
               msg = int(input('[1] depositar mais um valor \n[2] sair\n\n'))
               if msg == 2:
                    break
               elif msg == 1:
                    continue
         
               
               
          
     elif opção == 2:
          if numero_de_saque > LIMITE_DE_SAQUE:
               print('')
               print('\nVoce já ultrapasso o limite de saque do mes\n ')
               print('')
               continue
          while True:
               if saldo == 0:
                    print('')
                    print('\nvc não tem saldo na sua conta\n ')
                    print('')
                    break
               numero_de_saque += 1
               print('')
               valor = float(input('qual valor do saque: '))
               print('')
               if valor > limite:
                    print('\nvalor ultrapassou o limite permitido por saque\n ')
                    continue
               conta = saldo - valor
               if conta < 0:
                    print('\ntranseferencia negada \n vc não pode sacar um valor maior que seu saldo \n ')
                    continue
               print('')     
               print(f'valor sacado de {valor:.2f} \nsaldo atual de {conta:.2f}')
               print('')
               resposta = f"SAQUE: R${valor:.2f}"
               extrato.append( str(resposta))
               i += 1
               msg = int(input('fazer mais um saque \n[1] SIM \n[2] NÂO\n\n'))
               if msg == 2:
                    break
               elif numero_de_saque > LIMITE_DE_SAQUE:
                    print('Voce já ultrapasso o limite de saque do mes')
                    break
               else: 
                    continue
               
     if opção == 3:   
          Menu_transferencia = """
               QUAL FORMA DE Transferencia?
     -----------------------------------------     
              [1] Transferencia em DOC
              [2] Transferencia em PIX
              [3] Transferencia em TEF
               
          """  
          escolha_transferencia = int(float(input(Menu_transferencia)))
          
          while escolha_transferencia != int and 1 > escolha_transferencia or escolha_transferencia > 3:
               escolha_transferencia = int(input("Erro \n \n " + Menu_transferencia)) 
          while True:
               if escolha_transferencia == 1:
                    menu_DOC = """
                         
                         Informe os dados do destinatário:
                         
                    """
                    print(menu_DOC)
                    print('')
                    nome = input('Nome(Completo): ')
                    CPF = int(input("Escreva o CPF: "))
                    numero_conta = int(input("Numero da Conta: "))
                    agencia = int(input("Numero da Agencia: "))
                    print('''
                          
                    ------------------------------------
                          [1] Itaú        [4] Banco do Brasil         [7] Banco ABC
                          [2] Bradesco    [5] Caixa Econômica Federa  [8] Nubank
                          [3] Santander   [6] Banco Pan               [9] Inter
                    -------------------------------------
                          ''')
                    while True:
                         Banco = int(input())
                         if Banco == 1: Banco = 'Itaú '
                         elif Banco == 2: Banco = 'Bradesco '
                         elif Banco == 3: Banco = 'Santander '
                         elif Banco == 4: Banco = 'Banco do Brasil  '
                         elif Banco == 5: Banco = 'Caixa Econômica Federa'
                         elif Banco == 6: Banco = 'Banco Pan '
                         elif Banco == 7: Banco = 'Banco ABC '
                         elif Banco == 8: Banco = 'Nubank'
                         elif Banco == 9: Banco = 'Inter '
                         else: 
                              print('opção invalida')
                              continue
                         break
                    print('')                   
                    valor_DOC = int(input("Qual valor da transeferencia: "))
                    while valor_DOC < 1:
                         print("valor incorreto")
                         valor_DOC = int(input("Qual valor da transeferencia: "))
                    saldo -= valor_DOC
                    print(f"""
                                   Verificar Informação
                                   
                         Transferencia em DOC | Valor R${valor_DOC}
                         {Banco} | Agencia: {agencia} | Numero da conta: {numero_conta}
                         -----------------------------------------------------
                         nome: {nome}    CPF: {CPF}  
                            
                                   """)
                    desistencia = int(input("""
                                            
                                            [1] Cancelar Transferencia
                                            [2] Continuar Transferencia
                                            
                                            """))
                    if desistencia == 1:
                         print('transeferencia Cancelada')
                         break 
                    else:
                         print('Transferencia realizada com susesso')
                         resposta = f"Transferencia em DOC | {Banco} | Valor R${valor_DOC}  | Nome: {nome} | CPF:{CPF}"
                         extrato.append(resposta)
                         break
                    
               if escolha_transferencia == 2: # isso ta em loop e faltando muitas partes 
                   while True: 
                         menu_PIX = """
                         Qual e a chave pix:
                         [1] Email
                         [2] CPF
                         [3] numero de telefone
                         """
                         Escolhar_pagamento_pix = int(input(menu_PIX))
                         if Escolhar_pagamento_pix == 1:
                              pagamento_pix = "Email"
                              infor_pagamento = input("Escreva o email: ")
                         elif Escolhar_pagamento_pix == 2:
                              pagamento_pix = "CPF"
                              infor_pagamento = input("Escreva o CPF: ")
                         elif Escolhar_pagamento_pix == 3:
                              pagamento_pix = "numero de telefone"
                              infor_pagamento = input("numero de telefone")
                         else:
                              print("opção invalida")
                              continue 
                              
                         print("")
    
                         while True:
                              valor_Pix = int(input("Qual valor da transeferencia: "))
                              if valor_Pix <= 1:
                                   print("valor incorreto")
                                   continue
                              else:
                                   saldo -= valor_Pix
    
                                   relatorio = f"""
                                   
                                        Verificar Informação
                                        Transferencia em PIX | Valor R${valor_Pix} 
                                        -----------------------------------------------------
                                        Chave Pix ({pagamento_pix})| {infor_pagamento} 
                                        
                                        """
    
                                   print(relatorio)
                                   desistencia = int(input("""
                                                           
                                                       [1] Cancelar Transferencia
                                                       [2] Continuar Transferencia
                                                           
                                                          """))
                                   if desistencia == 1:
                                        print('transeferencia Cancelada')                                             
                                   else:
                                        print('Transferencia realizada com susesso') 
                                        resposta = f"Transferencia em PIX | Valor R${valor_Pix} |  Chave Pix {pagamento_pix} | Nome: {infor_pagamento}"
                                        extrato.append(resposta)
                                                                  
                                   break
                              
                         print("PARADA 2")
                         break
                 
                         
                         
                         
                         
                         
               elif escolha_transferencia == 3: # isso ta com erro em tudo 
                    while True:
                         menu_TEF = """
                         
                              Qual forma de pagamento
                                   
                              [1] Debito
                              [2] Credito
                         
                         """                         
                         opcao_TEF = int(input(menu_TEF))
                         if opcao_TEF < 1:
                              print('opção Invalida')
                              continue
                         cartao = int(input("escrevar os numeros seu cartao: "))
                         senha = int(input("escrevar a senha do seu cartao: "))
                         cvv = int(input("escrevar o CVV do seu cartao: "))
                         if opcao_TEF == 1:
                              metodo_pagamento ="Debito"
                         elif  opcao_TEF == 2:
                              metodo_pagamento ="Credito"
                              
                              
                         valor_TEF = int(input("qual valor da transferencia: "))
                         
                         def formatar_numero(numero):
                              numero_str = str(numero)
                              return '*' * (len(numero_str) - 3) + numero_str[-3:]
                              
                         relatorio = f"""
                                                   Verificar Informação
                                                   
                                        Transferencia em TEF | Valor R${valor_TEF} 
                                        -----------------------------------------------------
                                        numero cartao {formatar_numero(cartao)}
                                        
                                        """
                         print(relatorio)
                         print("")
                         desistencia = int(input("""
                                                           
                                                       [1] Cancelar Transferencia
                                                       [2] Continuar Transferencia
                                                           
                                                          """))

                         if desistencia == 1:
                              print('transeferencia Cancelada')
                              break                                             
                         else:
                              saldo -= valor_TEF  
                              print('Transferencia realizada com susesso') 
                              resposta = f"Transferencia em TEF | Valor R${valor_TEF} |  Metodo de pagamento: {metodo_pagamento} |  numero cartao {formatar_numero(cartao)}"
                              extrato.append(resposta)                                  
                              break
                         
                         
                         
                         break
                             
                          

               break   

               
               
               
                         
     if opção == 4:
          print('')
          if i != 0:
               limite_de_visualizacao = 0
               extrato.reverse()
               for d in range(len(extrato)):
                    print(extrato[d])
                    limite_de_visualizacao += 1
                    if limite_de_visualizacao > 9:
                         break
          
          print('------------------------')
          print(f"R${saldo:.2f}")
          
          
          
     elif opção == 5:
          print("""
                
               Consulte nosso suporte
                
                 (11) 94253-2451
                       ou
                www.BancoTWA.com.br 🌀
                
                """)  
          
          
          
     elif opção == 6:
          break



  