import pyautogui as bot
import openpyxl
import keyboard       # Pra escrever os acentos e pontuações, pois o pyautogui não coloca !.


# Carregar pasta de trabalho do excel.
planilha = openpyxl.load_workbook('Pasta de trabalho Excel.xlsx')
# selecionar a pagína certa da planilha e colocar numa variável.
planilha1 = planilha['Planilha1']
# Mostrar o que tem nessas linhas da planilha, de onde começar e de onde terminar.
for linha in planilha1.iter_rows(min_row=2, max_row=8):     # 'min_row' é de onde a vai começar e o 'max-row' é de onde termina.
    # Nome
    bot.click(x=906, y=483, duration=0.6)
    keyboard.write(linha[0].value)    # pra escrever o valor do que tem nessa linha da planilha1 ou seja o que tem dentro.
    # Produto
    bot.click(x=917, y=513, duration=0.6)
    keyboard.write(linha[1].value)
    # Quantidade
    bot.click(x=890, y=546, duration=0.6)
    keyboard.write(str(linha[2].value))
    # Categoria
    bot.click(x=898, y=580, duration=0.6)
    keyboard.write(linha[3].value)
    # apertar no botão 'salvar'
    bot.click(x=803, y=620, duration=0.6)
    bot.click(x=801, y=581, duration=0.6)




