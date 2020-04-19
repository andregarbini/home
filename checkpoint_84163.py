
# PARA TESTAR EMAIL USE: teste@gmail.com
# PARA TESTAR TELEFONE USE: 91234-5678
# PARA TESTAR CPF USE: 123456789/00

dadosVazados = ["teste@gmail.com","91234-5678","123456789/00","marcelosilva@gmail.com", "gabrielarodrigues@hotmail.com", "94813-9805", "95845-3518", "784596548/58", "782165492/45", "258439548/14", "365894843/61", "andrepinheiros@outlook.com", "vinicius.silva@fiap.com", "94585-3984", "98468-6512", "96528-3618", "94210-9780", "93284-4905", "99405-1565", "Dudamoraesdeoliveira@hotmail.com", "91033-1529", "92225-2478","91822-2392","91807-3613","274980880/45","861686330/30","558392880/80","866007420/38","127997290/45","275644180/52","patthy.costa@gmail.com","andressaccdasilva@gmail.com","amarcom2215@gmail.com"]

def busca():# FUNÇÃO PARA DEFINIR, TODOS OS DADOS VAZADOS OU BUSCAR SE O DADO FOI VAZADO OU NÃO
    print("╔═════════════════════════════════════════════════════════════════════════════════╗")
    print("║      Selecione o que você quer procurar? \033[1;32mTodos os dados: 1 \033[1;97m/ \033[1;34mDado Único: 2  \033[1;97m    ║")
    print("╚════════════════════════════════════════════════════════════════════════════════╝")
    buscaNum = int(input(""))
    return buscaNum

def todos():#FUNÇÃO DA PERGUNTA (TODOS OS DADOS)
    print("╔═════════════════════════════════════════════════════════════════════════════════╗")
    print("║  Selecione o que você quer procurar? \033[1;32mEmail: 1 \033[1;97m/ \033[1;34mNumero de telefone: 2 \033[1;97m/ \033[1;33mCPF: 3  \033[1;97m║")
    print("\033[1;97m╚═════════════════════════════════════════════════════════════════════════════════╝")
    todosNum = int(input(""))
    return todosNum

def unico():#FUNÇÃO DA PERGUNTA (TODOS OS DADOS)
    print("╔═════════════════════════════════════════════════════════════════════════════════╗")
    print("║                 Digite o dado que você deseja verificar:                        ║")
    print("╚═════════════════════════════════════════════════════════════════════════════════╝")
    unicoNum = input("")
    return unicoNum

define = busca() #PRIMEIRA PERGUNTA

while define != 1 and define != 2:#CASO NÃO SEJA 1 OU 2, PERGUNTA NOVAMENTE
    define = busca()
if define == 1:#SE FOR TODOS
    procuraTodos = todos()
    while procuraTodos != 1 and procuraTodos != 2 and procuraTodos != 3: # ENQUANTO NÃO DIGITAR 1, 2 OU 3 ELE REPETIRÁ A PERGUNTA
        procuraTodos = todos()
    if procuraTodos == 1: #EMAIL
        emails = [s for s in dadosVazados if "@" in s]
        print(emails)
    elif procuraTodos == 2: #TELEFONE
        telefone = [s for s in dadosVazados if "-" in s]
        print(telefone)
    elif procuraTodos == 3: #CPF
        cpf = [s for s in dadosVazados if "/" in s]
        print(cpf)
elif define == 2:#SE FOR UNICO
    procuraUnico = unico()
    while procuraUnico == "":
        procuraUnico = unico()
    if procuraUnico in dadosVazados:
        print("\033[1;31mSeu dado foi vazado!")
    else:
        print("\033[1;32mSeu dado não foi vazado!")
