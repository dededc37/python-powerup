from pyautogui import *
from pandas import *
from time import sleep

press("win")
write("chrome")
press("enter")
sleep(0.5)
write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
press("enter")
sleep(3)
press("tab")
write("emailteste1234@gmail.com")
press("tab")
write("senhateste123")
press("enter")
tabela = read_csv("produtos.csv")
sleep(0.5)

#cadastro

for linha in tabela.index:
    sleep(1)
    click(x=647, y=251)

    #código
    codigo = tabela.loc[linha, "codigo"]
    write(str(codigo))
    press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    write(str(marca))
    press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    write(str(tipo))
    press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    write(str(categoria))
    press("tab")

    #preço unitário
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    write(str(preco_unitario))
    press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    write(custo)
    press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        write(str(obs))
    press("tab")

    press("enter")
    scroll(10000)
