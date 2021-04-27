import openpyxl
import pyautogui as pa
import pyperclip as pp
import time
import pandas as pd

#inicio
pa.alert('O rograma vai começar')

#Abrir programa ( navegador chrome )
pa.PAUSE = 1

pa.press('win')
pa.write('chrome')
pa.press('enter')
time.sleep(3)

#abrir o link do google drive
link = "https://drive.google.com/drive/folders/1wRTFw0sUVBjRr4hW5U9LF7DjLixRyxym"
pp.copy(link)
pa.hotkey('ctrl', 'v')
pa.press('enter')
time.sleep(3)

#download do arquivo excel
pa.click(1039,346) #clica no arquivo
time.sleep(1)
pa.click(1157, 190)#opções
time.sleep(2)
pa.click(1033,590)#donwload
time.sleep(20)#aguarda donwload 


tabela = pd.read_excel(r"C:\Users\PC\Downloads\Vendas - Dez.xlsx", engine='openpyxl')

faturamento = tabela['Valor Final'].sum()
qtdeProduos = tabela['Quantidade'].sum()

assunto = 'Relatório de vendas'

corpoEmail = f'''
    Presados, bom dia!

    Segue os resultados do relatório.

    O faturamento foi de R$ {faturamento:,.2f}.
    E a quantidade de itens vendidos foi de {qtdeProduos:,}.

    Atenciosamente
    André Nechio - Gestão de Informações
'''


#Abre e-mail
pa.hotkey('ctrl', 't')
link = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
pp.copy(link)
pa.hotkey('ctrl', 'v')
pa.press('enter')
time.sleep(5)

pa.click(70,210)
time.sleep(3)

#endereços de e-mails
pa.write('kgsnechio@gmail.com')
pa.press('tab')

#assunto
pp.copy(assunto)

pa.press('tab')
pa.hotkey('ctrl', 'v')

#corpo do e-mail
pp.copy(corpoEmail)

pa.press('tab')
pa.hotkey('ctrl', 'v')

#envia e-mail
pa.hotkey('ctrl', 'enter')

#fim
pa.alert('E-meil enviado, programa encerrado!')