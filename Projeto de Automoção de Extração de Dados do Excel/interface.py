import PySimpleGUI as sg

def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print(f'Houve um erro na criação do arquivo "{nome}"')
    else:
        print(f'O arquivo "{nome}" criado com sucesso')

def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')        # 'rt' para abrir em modo leitura de arquivo texto
        a.close()                   # close pra fechar o arquivo
    except:
        return False
    else:
        return True

def adicionar(arquivo, cliente, produto, quantidade, categoria):
    try:
        a = open(arquivo, 'at')
    except:
        print('\33[31mErro ao adicionar no arquivo\33[m')
    else:
        a.write(f'Cliente: {cliente}\nProduto: {produto}\nQuantidade: {quantidade}\nCategoria: {categoria}\n\n')

# Criar arquivo Para colocar os dados
arquivo = 'Planilha excel.txt'     # 'txt' é o formato que o arquivo será criado
if not ArquivoExiste(arquivo):      # Se não existir tal arquivo, é pra ele criar !
    CriarArquivo(arquivo)

# Criando interface
while True:

    layout = [
        [sg.Txt('Cliente',size=(10,0)), sg.Input(size=(15,0),key='cliente')],
        [sg.Txt('Produto',size=(10,0)), sg.Input(size=(15,0),key='produto')],
        [sg.Txt('Quantidade',size=(10,0)), sg.Input(size=(5,0),key='quantidade')],
        [sg.Txt('categoria',size=(10,0)), sg.Input(size=(15,0),key='categoria')],
        [sg.Button('Salvar',size=(10,2))],
    ]
    janela = sg.Window('Plataforma de Cadastro', layout,)
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Salvar':
        cliente = valores['cliente']
        produto = valores['produto']
        quantidade = valores['quantidade']
        categoria = valores['categoria']
        adicionar(arquivo, cliente, produto, quantidade, categoria)
        interface = [
            [sg.Txt('Produto cadastrado com sucesso !',size=(15,0))],
            [sg.Button('Ok',size=(8,2))],
            ]
        janela2 = sg.Window('Concluindo',interface)
        while True:
            evento2, valores2 = janela2.read()
            if evento2 =='Ok' or evento2 == sg.WINDOW_CLOSED:
                break

            janela2.close()
    janela.close()
