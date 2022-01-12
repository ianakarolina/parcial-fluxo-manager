class Onibus:
    def __init__(self,placa,frota,Moto=None, Fis=None, Rota=[]):
        self.placa=placa
        self.frota=frota
        self.Moto=Moto
        self.Fis=Fis
        self.Rota=Rota

    
    @classmethod
    def mostrar(self):
        global listaOnibus
        for i in range(len(listaOnibus)):
                print(f"Informações do ônibus {i}: \
                     \n placa={listaOnibus[i].placa} \
                     \n frota={listaOnibus[i].frota} \
                     \n motorista={listaOnibus[i].Moto} \
                     \n fiscal={listaOnibus[i].Fis}")
        
    
    @classmethod
    def alterar(self):
        global listaOnibus
        info=input("Qual informação deseja alterar? ")
        lista_auxiliar_placa=[]
        lista_auxiliar_frota=[]
        
        if info=='placa':
            placa_antiga=input("Por favor, insira o número da placa que deseja alterar: ")
            self.placa=input("Digite a nova placa: ")
            for i in range(len(listaOnibus)):
                lista_auxiliar_placa.append(listaOnibus[i].placa)

            indica=lista_auxiliar_placa.index(placa_antiga)
            listaOnibus[indica].placa=self.placa
            return listaOnibus
            
        if info=='frota':
            frota_antiga=input("Por favor, insira o número da frota que deseja alterar: ")
            self.frota=input("Digite a nova frota: ")
            for i in range(len(listaOnibus)):
                lista_auxiliar_frota.append(listaOnibus[i].frota)

            indica=lista_auxiliar_frota.index(placa_antiga)
            listaOnibus[indica].placa=self.placa
            return listaOnibus
        
      
    @classmethod
    def deletar(self):
        global listaOnibus
        indice=(int(input("Digite o índice  do ônibus que deseja deletar: ")))
        del listaOnibus[indice]
        return listaOnibus
    
    
    @classmethod
    def assignar_motorista(self):
        global listaOnibus
        global listaMotorista
        lista_auxiliar_moto=[] #A lista dos nomes de todos os motoristas
        global lista_auxiliar_2  #A lista dos motoristas já adicionados
        lista_auxiliar_placa=[] #A lista de todas as placas do onibus
        nomeMoto=input("Insira o nome do motorista: ")
        placa=input("Insira a placa do ônibus ao qual deseja associar o motorista: ")
        
        for i in range(len(listaMotorista)):
            lista_auxiliar_moto.append(listaMotorista[i].nome)

        for i in range(len(listaOnibus)):
            lista_auxiliar_placa.append(listaOnibus[i].placa)

        indice_motorista=lista_auxiliar_moto.index(nomeMoto) #Acho o indice do nome dado pelo usuario na lista de nomes de motorista cadastrada
        self.Moto=listaMotorista[indice_motorista].nome

        indice_placa=lista_auxiliar_placa.index(placa) #Acho o indice da placa do onibus dada pelo usuario na lista de placas de onibus cadastradas

        if listaOnibus[indice_placa].Moto== None: #Se o parametro Moto da classe Onibus for None
            if nomeMoto not in lista_auxiliar_2:
                listaOnibus[indice_placa].Moto = self.Moto #Eu adiciono, na minha classe Onibus.Moto(), no indice da placa, o nome dado pelo usuario
                lista_auxiliar_2.append(nomeMoto)
            else:
                print("Esse motorista já está escalado em outro ônibus. Por favor, escolha outra pessoa.")
        else:
            print("Esse ônibus já possui um motorista!")
        return listaOnibus,listaMotorista
    
    @classmethod
    def assignar_fiscal(self):
        global listaOnibus
        global listaFiscal
        lista_auxiliar_fis=[] #A lista dos nomes de todos os motoristas
        global lista_auxiliar_3  #A lista dos motoristas já adicionados
        lista_auxiliar_placa=[] #A lista de todas as placas do onibus
        nomeFis=input("Insira o nome do fiscal: ")
        placa=input("Insira a placa do ônibus ao qual deseja associar o motorista: ")
        
        for i in range(len(listaFiscal)):
            lista_auxiliar_fis.append(listaFiscal[i].nome)

        for i in range(len(listaOnibus)):
            lista_auxiliar_placa.append(listaOnibus[i].placa)

        indice_fiscal=lista_auxiliar_fis.index(nomeFis) #Acho o indice do nome dado pelo usuario na lista de nomes de fiscais cadastrada
        self.Fis=listaFiscal[indice_fiscal].nome

        indice_placa=lista_auxiliar_placa.index(placa) #Acho o indice da placa do onibus dada pelo usuario na lista de placas de onibus cadastradas

        if listaOnibus[indice_placa].Fis== None: #Se o parametro Moto da classe Onibus for None
            if nomeFis not in lista_auxiliar_3:
                listaOnibus[indice_placa].Fis = self.Fis #Eu adiciono, na minha classe Onibus.Moto(), no indice da placa, o nome dado pelo usuario
                lista_auxiliar_3.append(nomeFis)
            else:
                print("Esse fiscal já está escalado em outro ônibus. Por favor, escolha outra pessoa.")
        else:
            print("Esse ônibus já possui um fiscal!")
        return listaOnibus,listaMotorista
        


class Paradas:
    def __init__(self,cep):
        self.cep = cep
        
    @classmethod
    def mostrar(self):
        global listaParada
        for i in range(len(listaParada)):
                print(f"Informações do ponto de parada {i}: \
                     \n cep={listaParada[i].cep}")
    @classmethod
    def adicionar_parada(self):
        global listaOnibus
        global listaParada
        lista_auxiliar_parada=[] #A lista dos ceps de todass as paradas
        lista_auxiliar_placa=[] #A lista de todas as placas do onibus
        lista_auxiliar_rota=[]
        cep=input("Insira o cep do ponto de parada que deseja adicionar: ")
        placa=input("Insira a placa do ônibus ao qual deseja adicionar o ponto de parada: ")
        
        for i in range(len(listaParada)):
            lista_auxiliar_parada.append(listaParada[i].cep)

        for i in range(len(listaOnibus)):
            lista_auxiliar_placa.append(listaOnibus[i].placa)

        for i in range(len(listaOnibus)):
            lista_auxiliar_rota.append(listaOnibus[i].Rota)

        indice_parada=lista_auxiliar_parada.index(cep) #Acho o indice do cep dado pelo usuario na lista de ceps cadastrados
        self.Rota.append(listaParada[indice_parada].cep)

        indice_placa=lista_auxiliar_placa.index(placa) #Acho o indice da placa do onibus dada pelo usuario na lista de placas de onibus cadastradas

        for i in range(len(lista_auxiliar_rota)):
            if cep not in lista_auxiliar_rota[i]: #Se o cep nao estiver dentro da lista de rotas do onibus
                self.Rota.append(listaOnibus[indice_placa].cep) #Eu adiciono, na minha classe Onibus.Moto(), no indice da placa, o nome dado pelo usuario
            else:
                print("Esse ônibus já para nesse ponto!")
            return listaOnibus,listaParada

    @classmethod
    def alterar(self):
        global listaParada
        info=input("Qual informação deseja alterar? ")
        lista_auxiliar_cep=[]
        
        if info=='cep':
            cep_antigo=input("Por favor, insira o número do cep que deseja alterar: ")
            self.cep=input("Digite o novo cep: ")
            for i in range(len(listaParada)):
                lista_auxiliar_cep.append(listaParada[i].cep)

            indica=lista_auxiliar_cep.index(cep_antigo)
            listaParada[indica].cep=self.cep
            return listaParada

    @classmethod
    def deletar(self):
        global listaParada
        indice=(int(input("Digite o índice  da parada que deseja deletar: ")))
        del listaParada[indice]
        return listaParada

class Motorista:

    def __init__(self,nome,idade,carteiratrabalho):
        self.nome=nome
        self.idade=idade
        self.carteiratrabalho=carteiratrabalho

    @classmethod
    def mostrar(self):
        global listaMotorista
        for i in range(len(listaMotorista)):
                print(f"Informações do motorista {i}: \
                     \n nome={listaMotorista[i].nome} \
                     \n idade={listaMotorista[i].idade} \
                     \n carteira de trabalho={listaMotorista[i].carteiratrabalho}")

    @classmethod
    def alterar(self):
        #ADICIONAR QUAIS AS POSSÍVEIS INFORMAÇÕES A ALTERAR
        info=input("Qual informação deseja alterar? ")
        global listaMotorista
        lista_auxiliar_nome=[]
        lista_auxiliar_idade=[]
        lista_auxiliar_carteiratrabalho=[]
        
        if info=='nome':
            nome_antigo=input("Por favor, insira o nome anterior: ")
            self.nome=input("Digite o novo nome: ")
            for i in range(len(listaMotorista)):
                lista_auxiliar_nome.append(listaMotorista[i].nome)
            
            indice=lista_auxiliar_nome.index(nome_antigo)
            listaMotorista[indice].nome=self.nome
            return listaMotorista
        
        if info=='idade':
            idade_antiga=input("Por favor, insira a idade anterior: ")
            self.idade=input("Digite a nova idade: ")
            for i in range(len(listaMotorista)):
                lista_auxiliar_idade.append(listaMotorista[i].idade)
                
            indice=lista_auxiliar_idade.index(idade_antiga)
            listaMotorista[indice].idade=self.idade
            return listaMotorista

        if info=='carteira de trabalho':
            carteira_antiga=input("Por favor, insira o número da carteira de trabalho anterior: ")
            self.carteiratrabalho=input("Digite a nova idade: ")
            for i in range(len(listaMotorista)):
                lista_auxiliar_carteiratrabalho.append(listaMotorista[i].carteiratrabalho)

            indice=lista_auxiliar_carteiratrabalho.index(carteira_antiga)
            listaMotorista[indice].carteiratrabalho=self.carteiratrabalho
            return listaMotorista

    @classmethod
    def deletar(self):
        global listaMotorista
        indice=(int(input("Digite o índice  do mootorista que deseja deletar: ")))
        del listaMotorista[indice]
        return listaMotorista
        
        
class Fiscal:

    def __init__(self,nome,idade,carteiratrabalho):
        self.nome=nome
        self.idade=idade
        self.carteiratrabalho=carteiratrabalho
        

    @classmethod
    def mostrar(self):
        global listaFiscal
        for i in range(len(listaFiscal)):
                print(f"Informações do fiscal {i}: \
                     \n nome={listaFiscal[i].nome} \
                     \n idade={listaFiscal[i].idade} \
                     \n carteira de trabalho={listaFiscal[i].carteiratrabalho}")

    @classmethod
    def alterar(self):
        #ADICIONAR QUAIS AS POSSÍVEIS INFORMAÇÕES A ALTERAR
        info=input("Qual informação deseja alterar? ")
        global listaFiscal
        lista_auxiliar_nome=[]
        lista_auxiliar_idade=[]
        lista_auxiliar_carteiratrabalho=[]
        
        if info=='nome':
            nome_antigo=input("Por favor, insira o nome anterior: ")
            self.nome=input("Digite o novo nome: ")
            for i in range(len(listaFiscal)):
                lista_auxiliar_nome.append(listaFiscal[i].nome)
                

            indice=lista_auxiliar_nome.index(nome_antigo)
            listaFiscal[indice].nome=self.nome
            return listaFiscal
        
        if info=='idade':
            idade_antiga=input("Por favor, insira a idade anterior: ")
            self.idade=input("Digite a nova idade: ")
            for i in range(len(listaFiscal)):
                lista_auxiliar_idade.append(listaFiscal[i].idade)
                
            indice=lista_auxiliar_idade.index(idade_antiga)
            listaFiscal[indice].idade=self.idade
            return listaFiscal

        if info=='carteira de trabalho':
            carteira_antiga=input("Por favor, insira o número da carteira de trabalho anterior: ")
            self.carteiratrabalho=input("Digite a nova idade: ")
            for i in range(len(listaFiscal)):
                lista_auxiliar_carteiratrabalho.append(listaFiscal[i].carteiratrabalho)
                
            indice=lista_auxiliar_carteiratrabalho.index(carteira_antiga)
            listaFiscal[indice].carteiratrabalho=self.carteiratrabalho
            return listaFiscal

    @classmethod
    def deletar(self):
        global listaFiscal
        indice=(int(input("Digite o índice  do fiscal que deseja deletar: ")))
        del listaFiscal[indice]
        return listaFiscal
   

def menu():
    print(f"Olá, seja bem-vindx ao sistema de gerenciamento FluxoManager! Seguem as funcionalidades do nosso sistema:\
          \n 1- Criar ônibus \
          \n 2- Criar ponto de parada \
          \n 3- Criar motorista \
          \n 4- Criar fiscal \
          \n 5- Mostrar ônibus \
          \n 6- Mostrar rotas \
          \n 7- Mostrar motoristas \
          \n 8- Mostrar fiscais \
          \n 9- Assignar motorista ao ônibus \
          \n 10- Assignar fiscal ao ônibus \
          \n 11- Adicionar ponto de parada ao ônibus \
          \n 12- Alterar dados do ônibus \
          \n 13- Alterar dados da parada \
          \n 14- Alterar dados do motorista \
          \n 15- Alterar dados do fiscal \
          \n 16- Alterar rota do ônibus \
          \n 17- Deletar ônibus \
          \n 18- Deletar ponto de parada \
          \n 19- Deletar motorista \
          \n 20- Deletar fiscal \
          \n 21- Sair do programa")
    cont='s'
    global listaOnibus
    listaOnibus=[]

    global listaParada
    listaParada=[]

    global listaMotorista
    listaMotorista=[]

    global listaFiscal
    listaFiscal=[]

    global lista_auxiliar_2
    lista_auxiliar_2=[] #A lista dos motoristas já adicionados

    global lista_auxiliar_3
    lista_auxiliar_3=[] #A lista dos fiscais já adicionados   
    
    while cont=='s':
        ans=input("Por favor, insira o número correspondente à funcionalidade desejada: ")
        if ans=='1':
            placa=input("Digite o numero da placa: ")
            frota=input("Digite o numero da frota: ")
            oni=Onibus(placa,frota)
            listaOnibus.append(oni)
            
        if ans=='2':
            cep=input("Insira o cep do ponto de parada: ")
            Parada=Paradas(cep)
            listaParada.append(Parada)
            
        if ans=='3':
            nome=input("Insira o nome do motorista: ")
            idade=input("Insira a idade do motorista: ")
            carteiradetrabalho=input("Insira o número da carteira de trabalho do motorista: ")
            Moto=Motorista(nome,idade,carteiradetrabalho)
            listaMotorista.append(Moto)
            
        if ans=='4':
            nome=input("Insira o nome do fiscal: ")
            idade=input("Insira a idade do fiscal: ")
            carteiradetrabalho=input("Insira o número da carteira de trabalho do fiscal: ")
            Fis=Fiscal(nome,idade,carteiradetrabalho)
            listaFiscal.append(Fis)
            
        if ans=='5': #MOSTRAR ONIBUS
            Onibus.mostrar()
            
        if ans=='6': #MOSTRAR ROTAS
            Parada.mostrar()
            
        if ans=='7': #MOSTRAR MOTORISTAS
            Motorista.mostrar()
            
        if ans=='8': #MOSTRAR FISCAIS
            Fiscal.mostrar()
        
        if ans=='9': #ASSIGNAR MOTORISTA AO ONIBUS
            Onibus.assignar_motorista()
            
        if ans=='10': #ASSIGNAR FISCAL AO ONIBUS
            Onibus.assignar_fiscal()
        
        if ans=='11': #ADICIONAR PONTO DE PARADA AO ONIBUS - EM DESENVOLVIMENTO
            pass
    
        if ans=='12': #ALTERAR DADOS DO ONIBUS
            Onibus.alterar()
            
        if ans=='13': #ALTERAR DADOS DA PARADA
            Parada.alterar()

        if ans=='14': #ALTERAR DADOS DO MOTORISTA
            Motorista.alterar()

        if ans=='15': #ALTERAR DADOS DO FISCAL 
            Fiscal.alterar()

        if ans=='16': #ALTERAR ROTA DO ONIBUS - EM DESENVOLVIMENTO
            pass    

        if ans=='17': #DELETAR ONIBUS
            if listaOnibus==[]:
                print("Não há mais ônibus registrados no sistema.")
            else:
                Onibus.deletar()    

        if ans=='18': #DELETAR PONTO DE PARADA
            if listaParada==[]:
                print("Não há mais pontos de paradas registrados no sistema.")
            else:
                Parada.deletar()  

        if ans=='19': #DELETAR MOTORISTA
            if listaMotorista==[]:
                print("Não há mais motoristas registrados no sistema.")
            else:
                Motorista.deletar() 

        if ans=='20': #DELETAR FISCAL
            if listaFiscal==[]:
                print("Não há mais fiscais registrados no sistema.")
            else:
                Fiscal.deletar() 

        if ans=='21': #SAIR DO PROGRAMA
            break

        cont=input("Deseja escolher outra funcionalidade?s/n ")

menu() 


