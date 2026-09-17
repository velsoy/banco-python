import tkinter as tk

extrato1 = []
saldo = 1000


def extrato():
    texto = ""

    for x in extrato1:
        y = str(x)
        texto += "\n" + y

    label_extrato.config(text=f"{texto}")


def transferência():
    global saldo

    valor = int(entrada_valor_trasferencia.get())
    nome = str(entrada_nome.get())

    if valor > saldo or valor <= 0:
        mensagem_1.config(text="Transferência negada!")
        entrada_valor_trasferencia.delete(0, tk.END)

    else:
        entrada_valor_trasferencia.delete(0, tk.END)
        entrada_nome.delete(0, tk.END)

        mensagem_2.config(
            text=f"Transferência de R${valor} realizada para {nome}!"
        )

        saldo = saldo - valor
        saldo_label.config(text=f"Saldo: R${saldo}")

        extrato1.append(f"Transferência -R${valor}")


def depositar():
    global saldo

    valor = int(entrada.get())

    if valor <= 0:
        deposito.config(text="Depósito inválido!")
        entrada.delete(0, tk.END)

    else:
        deposito.config(text="Depósito realizado com sucesso")

        saldo = saldo + valor
        entrada.delete(0, tk.END)

        saldo_label.config(text=f"Saldo: R${saldo}")

        extrato1.append(f"Depósito: +R${valor}")


def sacar():
    global saldo

    valor = int(entrada2.get())

    if valor > saldo or valor <= 0:
        mensagem.config(text="Saldo insuficiente!")
        entrada2.delete(0, tk.END)

    else:
        mensagem.config(text="Saque realizado com sucesso!")

        saldo = saldo - valor
        entrada2.delete(0, tk.END)

        saldo_label.config(text=f"Saldo: R${saldo}")

        extrato1.append(f"Saque -R${valor}")


janela = tk.Tk()
janela.geometry("600x450")


# =========================
# TÍTULO
# =========================

texto = tk.Label(
    janela,
    text="==== Bem-vindo ao Banco Python! ====",
    font=("Arial", 22)
)

texto.place(x=60, y=20)


# =========================
# DEPÓSITO
# =========================

label_deposito = tk.Label(
    janela,
    text="Valor para depósito:",
    font=("Arial", 11, "bold")
)

label_deposito.place(x=40, y=75)

entrada = tk.Entry(janela, width=20)
entrada.place(x=40, y=100)

botao = tk.Button(
    janela,
    text="DEPOSITAR",
    command=depositar
)

botao.place(x=220, y=96)


# =========================
# SAQUE
# =========================

label_sacar = tk.Label(
    janela,
    text="Valor para sacar:",
    font=("Arial", 11, "bold")
)

label_sacar.place(x=40, y=135)

entrada2 = tk.Entry(janela, width=20)
entrada2.place(x=40, y=160)

botao2 = tk.Button(
    janela,
    text="SACAR",
    command=sacar
)

botao2.place(x=220, y=156)


# =========================
# SALDO
# =========================

saldo_label = tk.Label(
    janela,
    text="Saldo: R$ 1000",
    font=("Arial", 12, "bold"),
    fg="green"
)

saldo_label.place(x=40, y=205)


# =========================
# MENSAGENS
# =========================

mensagem = tk.Label(
    janela,
    text="",
    font=("Arial", 11, "bold")
)

mensagem.place(x=40, y=250)


deposito = tk.Label(
    janela,
    text="",
    font=("Arial", 11, "bold")
)

deposito.place(x=40, y=270)


# =========================
# TRANSFERÊNCIA
# =========================

label_transferencia = tk.Label(
    janela,
    text="TRANSFERIR",
    font=("Arial", 11, "bold")
)

label_transferencia.place(x=40, y=300)


nome = tk.Label(
    janela,
    text="nome",
    font=("Arial", 11, "bold")
)

nome.place(x=40, y=325)


entrada_nome = tk.Entry(
    janela,
    width=20
)

entrada_nome.place(x=40, y=350)


valor_trans = tk.Label(
    janela,
    text="valor",
    font=("Arial", 11, "bold")
)

valor_trans.place(x=220, y=325)


entrada_valor_trasferencia = tk.Entry(
    janela,
    width=20
)

entrada_valor_trasferencia.place(x=220, y=350)


botao_transferir = tk.Button(
    janela,
    text="TRANSFERIR",
    command=transferência
)

botao_transferir.place(x=400, y=347)


mensagem_1 = tk.Label(
    janela,
    text="",
    font=("Arial", 11, "bold")
)

mensagem_1.place(x=40, y=380)


mensagem_2 = tk.Label(
    janela,
    text="",
    font=("Arial", 11, "bold")
)

mensagem_2.place(x=40, y=405)


# =========================
# EXTRATO
# =========================

extrato_la = tk.Label(
    janela,
    font=("Arial", 11, "bold"),
    text="======== EXTRATO ========"
)

extrato_la.place(x=370, y=75)


extrato_but = tk.Button(
    janela,
    font=("Arial", 11, "bold"),
    text="EXTRATO",
    command=extrato
)

extrato_but.place(x=420, y=110)


label_extrato = tk.Label(
    janela,
    font=("Arial", 11, "bold"),
    justify="left",
    anchor="nw",
    width=22
)

label_extrato.place(x=350, y=150)


janela.mainloop()