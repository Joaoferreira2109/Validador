import openpyxl
import webbrowser
from time import sleep
import pyautogui

# Abre o WhatsApp Web e aguarda o login manual
webbrowser.open('https://web.whatsapp.com/')
sleep(10)

# Ler planilha e guardar informações sobre nome e telefone
workbook = openpyxl.load_workbook('clientes.xlsx')
pagina_clientes = workbook['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}'
    webbrowser.open(link_mensagem_whatsapp)
    sleep(5)

    try:
        # Verifica se apareceu a mensagem de URL inválida (imagem precisa existir no mesmo diretório)
        invalido = pyautogui.locateOnScreen("url_invalida.png", confidence=0.6)
        if invalido:
            print(f"⚠ URL inválida detectada para {telefone}")
            # Aqui você pode salvar no TXT os números inválidos
            with open("numeros_invalidos.txt", "a", encoding="utf-8") as f:
                f.write(f"{telefone} - {nome}\n")
        else:
            print(f"✅ Nenhuma URL inválida para {telefone}")

    except pyautogui.ImageNotFoundException:
        print("❌ Imagem de referência não encontrada.")

    # Fecha a aba aberta do WhatsApp
    pyautogui.hotkey("ctrl", "w")
    sleep(5)

    
