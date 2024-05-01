from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from tkinter import messagebox
from threading import Thread
import time

def fazer_login():
    # Atualiza a interface para mostrar que o processo está carregando
    resultado_var.set("Aguardando resultado...")
    lucro_var.set("Aguardando resultado...")
    janela.update()

    # Configuração e inicialização do navegador
    options = Options()
    options.headless = True
    navegador = webdriver.Firefox(options=options)
    navegador.get('https://portal.meusdividendos.com/login')
    wait = WebDriverWait(navegador, 20)
    navegador.minimize_window()  # Minimiza a janela do navegador

    email = email_entry.get()
    senha = senha_entry.get()
    contrato = contrato_entry.get()

    # Login no site
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]'))).send_keys(email)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]'))).send_keys(senha)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button"]'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//img[@class="img-fluid mb-4 antigo  "]'))).click()
    
    # Verificação da presença da frase
    frase_esperada = "suporte@meusdividendos.com"
    if frase_esperada in navegador.page_source:
        messagebox.showinfo("Verificação", "Frase encontrada")
    else:
        messagebox.showinfo("Verificação", "Frase não encontrada.")
        navegador.quit()
        return
    
    # Captura de dados após login
    resultado = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[1]/span'))).text
    resultado_var.set(resultado)
    lucro = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]/span'))).text
    lucro_var.set(lucro)

    # Encerramento do navegador
    navegador.quit()

# Interface gráfica
janela = Tk()
janela.title("Análise de Contratos Habitacionais - Beta")
janela.geometry("500x300")

texto_email = Label(janela, text="E-mail:")
texto_email.grid(column=0, row=1)
email_entry = Entry(janela, width=25)
email_entry.grid(column=1, row=1)

texto_senha = Label(janela, text="Senha:")
texto_senha.grid(column=0, row=2)
senha_entry = Entry(janela, width=25, show='*')
senha_entry.grid(column=1, row=2)

texto_contrato = Label(janela, text="Contrato:")
texto_contrato.grid(column=0, row=3)
contrato_entry = Entry(janela, width=25,)
contrato_entry.grid(column=1, row=3)

botao = Button(janela, text="Pesquisar", command=lambda: Thread(target=fazer_login).start())
botao.grid(column=1, row=4)

#Mostrar Resultado:

resultado_var = StringVar()
resultado_var.set("Aguardando resultado...")
linha_resultado = Label(janela, text="Resultado:")
linha_resultado.grid(column=0, row=5)
mostrar_resultado = Label(janela, textvariable=resultado_var)
mostrar_resultado.grid(column=1, row=5)

lucro_var = StringVar()
lucro_var.set("Aguardando resultado...")
linha_lucro = Label(janela, text="Lucro:")
linha_lucro.grid(column=0, row=6)
mostrar_lucro = Label(janela, textvariable=lucro_var)
mostrar_lucro.grid(column=1, row=6)

janela.mainloop()





