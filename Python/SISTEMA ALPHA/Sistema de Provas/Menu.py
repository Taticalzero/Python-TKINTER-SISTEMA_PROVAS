from tkinter import *
import os


#FECHAMENTO  DE JANELAS#
def fechar5():
    screen.destroy()
def fechar2():
    questionario.destroy()
def fechar3():
    screen4.destroy()
def fechar4():
    screen5.destroy()
    
#CONFERE RESPOSTAS#
def apresentar_respostas_certas(respostas):
    global apresentar_respostas
    apresentar_respostas = Toplevel(screen)
    apresentar_respostas.title("RESULTADO")
    apresentar_respostas.configure(background="#00BFFF")
    apresentar_respostas.geometry("700x500")

    Tops = Frame(apresentar_respostas, width=900, height=650, bd=8, bg="#000000", relief="raise")
    Tops.grid(row=0, column=0, ipadx=2, ipady=2, padx=2, pady=2, columnspan=2)

    Tops1 = Frame(Tops, width=900, height=650, bd=8, bg="#00BFFF", relief="raise")
    Tops1.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5, columnspan=2)

    frame1 = Frame(apresentar_respostas, width=900, height=650, bg="#000000", bd=8, relief="raise")
    frame1.grid(row=1, column=0, padx=10, pady=10, sticky=NW)

    frame2 = Frame(frame1, width=900, height=650, bd=8, relief="raise")
    frame2.grid(row=0, column=0, padx=10, pady=10, sticky=NW)

    frame3 = Frame(apresentar_respostas, width=900, height=650, bd=8, relief="raise")
    frame3.grid(row=1, column=1, padx=10, pady=10,)

    lb1 = Label(Tops1, text="Pagina de verificação do resultado do questionario!", fg="#9400D3", bg="#00BFFF", font=("Agency FB", 45, "bold"))
    lb1.grid(row=1, column=1, rowspan=2, columnspan=2)

    lb2 = Label(frame1)
    lb2.grid(row=11, column=11, padx=105, pady=105)

    lb4 = Label(frame2)
    lb4.grid(row=10, column=10, padx=100, pady=100)

    lb5 = Label(frame2, text="QUESTÕES CERTAS", fg="#94FFD3", bg="#000000", font=("Agency FB", 26, "bold"))
    lb5.grid(row=0, column=0, sticky=NW)

    for i in range(0, len(respostas)):
        lb6 = Label(frame2, text=respostas[i], fg="#94FFD3", bg="#000000", font=("Agency FB", 26, "bold"))
        lb6.grid(row=1, column=i, sticky=NW)

    bt1 = Button(frame3, text="BOTÃO", bg="#FFFF00", fg="#0000CD", height="1", width="15", font=("Agency FB", 14, "bold"))
    bt1.grid(row=0, column=0)
    #CHECAR AS RESPOSTAS#
def verifica_respostas(q1, q2, q3, q4, q5):
    print("Respostas")
    msg = f'1º: {q1.get()}\n2º: {q2.get()}\n3º: {q3.get()}\n4º: {q4.get()}\n5º: {q5.get()}'
    print(msg)

    respostas = []

    if q1.get() == 4:
        respostas.append("1º")
    if q2.get() == 4:
        respostas.append("2º")
    if q3.get() == 2:
        respostas.append("3º")
    if q4.get() == 2:
        respostas.append("4º")
    if q5.get() == 2:
        respostas.append("5º")
  
    
    questionario.destroy()
    apresentar_respostas_certas(respostas)
    print(respostas)    
#QUESTIONARIO#
def questionario_aluno():
    global questionario
    questionario = Toplevel(screen)
    questionario.geometry("1024x700+200+90")
    questionario.title("QUESTIONARIO")

    Tops = Frame(questionario, width=400, height=550, bd=8, relief="raise")
    Tops.grid(row=0, column=0,columnspan=2)
    frame1 = Frame(questionario, width=400, height=550, bd=8, relief="raise")
    frame1.grid(row=1, column=0, columnspan=2, sticky=W)
   # frame2 = Frame(questionario, width=900, height=650, bd=8, relief="raise")
   # frame2.grid(row=2, column=0, sticky=W)
    frame3 = Frame(questionario, width=400, height=550, bd=8, relief="raise")
    frame3.grid(row=3, column=0, sticky=E)
    frame4 = Frame(questionario, width=400, height=550, bd=8, relief="raise")
    frame4.grid(row=3, column=1 ,sticky=W)


    q1 = IntVar()
    q2 = IntVar()
    q3 = IntVar()
    q4 = IntVar()
    q5 = IntVar()


    lblInfo = Label(Tops, font=("arial", 18, "bold"), text="QUESTIONARIO", bd=8, width=30)
    lblInfo.grid(row=0, column=0)

    Label(frame1, text="1ª) Quanto é 200*200?", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=0, sticky=W)
    radio = Radiobutton(frame1, text="A)  5874", padx=14, variable=q1, value=1).grid(row=1, column=0, sticky=W)
    radio = Radiobutton(frame1, text="B)  3333", padx=14, variable=q1, value=2).grid(row=2, column=0, sticky=W)
    radio = Radiobutton(frame1, text="C)  73652", padx=14, variable=q1, value=3).grid(row=3, column=0, sticky=W)
    radio = Radiobutton(frame1, text="D)  40000", padx=14, variable=q1, value=4).grid(row=4, column=0, sticky=W)
    radio = Radiobutton(frame1, text="E)  12144", padx=14, variable=q1, value=5).grid(row=5, column=0, sticky=W)

    Label(frame1, text="2ª) Quanto é 600/3?", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=1, sticky=W)
    radio = Radiobutton(frame1, text="A)  523", padx=14, variable=q2, value=1).grid(row=1, column=1, sticky=W)
    radio = Radiobutton(frame1, text="B)  311", padx=14, variable=q2, value=2).grid(row=2, column=1, sticky=W)
    radio = Radiobutton(frame1, text="C)  784", padx=14, variable=q2, value=3).grid(row=3, column=1, sticky=W)
    radio = Radiobutton(frame1, text="D)  200", padx=14, variable=q2, value=4).grid(row=4, column=1, sticky=W)
    radio = Radiobutton(frame1, text="E)  100", padx=14, variable=q2, value=5).grid(row=5, column=1, sticky=W)

    Label(frame1, text="3ª) Quanto é 200/5?", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=2, sticky=W)
    radio = Radiobutton(frame1, text="A)  15", padx=14, variable=q3, value=1).grid(row=1, column=2, sticky=W)
    radio = Radiobutton(frame1, text="B)  40", padx=14, variable=q3, value=2).grid(row=2, column=2, sticky=W)
    radio = Radiobutton(frame1, text="C)  97", padx=14, variable=q3, value=3).grid(row=3, column=2, sticky=W)
    radio = Radiobutton(frame1, text="D)  324", padx=14, variable=q3, value=4).grid(row=4, column=2, sticky=W)
    radio = Radiobutton(frame1, text="E)  121", padx=14, variable=q3, value=5).grid(row=5, column=2, sticky=W)

    Label(frame1, text="4ª) Quanto é 5 - 3 ?", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=3, sticky=W)
    radio = Radiobutton(frame1, text="A) 2", padx=14, variable=q4, value=1).grid(row=1, column=3, sticky=W)
    radio = Radiobutton(frame1, text="B) 6", padx=14, variable=q4, value=2).grid(row=2, column=3, sticky=W)
    radio = Radiobutton(frame1, text="C) 9", padx=14, variable=q4, value=3).grid(row=3, column=3, sticky=W)
    radio = Radiobutton(frame1, text="D) 1", padx=14, variable=q4, value=4).grid(row=4, column=3, sticky=W)
    radio = Radiobutton(frame1, text="E) 9", padx=14, variable=q4, value=5).grid(row=5, column=3, sticky=W)

    Label(frame1, text="5ª) QUANTO É 123*542?  ", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=4, sticky=W)
    radio = Radiobutton(frame1, text="A)  51142", padx=14, variable=q5, value=1).grid(row=1, column=4, sticky=W)
    radio = Radiobutton(frame1, text="B)  66666", padx=14, variable=q5, value=2).grid(row=2, column=4, sticky=W)
    radio = Radiobutton(frame1, text="C)  12547", padx=14, variable=q5, value=3).grid(row=3, column=4, sticky=W)
    radio = Radiobutton(frame1, text="D)  40103", padx=14, variable=q5, value=4).grid(row=4, column=4, sticky=W)
    radio = Radiobutton(frame1, text="E)  100001", padx=14, variable=q5, value=5).grid(row=5, column=4, sticky=W)
    

    
    bt1 = Button(frame3, text="FINALIZAR", bg="#FFFF00", fg="#0000CD", height="1", width="12", font=("Agency FB", 12, "bold"), command=lambda: verifica_respostas(q1, q2, q3, q4, q5))
    bt1.pack()
    bt2 = Button(frame4, text="VOLTAR", bg = "#FFFF00", fg="#0000CD", height="1", width="12",font=("Agency FB", 12, "bold"), command=fechar2)
    bt2.pack()
    

    questionario.mainloop()
    
#LOGIN SUCESS
def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Logado com Sucesso !")
    screen3.geometry("300x300")
    Label(screen3, text = "LOGADO").pack()
    Button(screen3, text = "OK", command = questionario_aluno).pack()
    #SENHA VERIFICAR
def senha_invalida():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("AUTENTICANDO ... ")
    screen4.geometry("300x300")
    Label(screen4 ,text = "SENHA INVALIDA").pack()
    Button(screen4 ,text = "OK", command = fechar3).pack()

    
def usuario_invalido():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("AUTENTICANDO ... ")
    screen5.geometry("300x300")
    Label(screen5, text = "USUARIO INVALIDO").pack()
    Button(screen5 ,text = "OK", command = fechar4).pack()

def register_usuario():
    nome_info = nome.get()
    senha_info = senha.get()
    
    file=open(nome_info, "w")
    file.write(nome_info+"\n")
    file.write(senha_info)
    file.close()
    
    nome_entry.delete(0,END)
    senha_entry.delete(0,END)
    
    Label(screen1 , text = "Registro efetuado com sucesso" , fg = "green",
          font = ("Calibri" , 11)).pack()
    

    
def login_verificar():
    nome1 = nome_verificar.get()
    senha1 = senha_verificar.get()
    nome_entry1.delete(0,END)
    senha_entry1.delete(0,END)
    
    print("Andamento...")
    
    list_of_files =  os.listdir()
    if nome1 in list_of_files:
        file1 = open(nome1,"r")
        verify = file1.read().splitlines()
        if senha1 in verify:
            login_sucess()
        else:
            senha_invalida()
    else:
            usuario_invalido()
                
    #REGISTRO        

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("---Register---")
    screen1.geometry("300x250")
    
    global nome
    global senha
    global nome_entry
    global senha_entry
    
    nome = StringVar()
    senha = StringVar()    
    
    Label(screen1 , text = "Por favor insira seus dados abaixo").pack()
    Label(screen1 , text = "").pack()
    Label(screen1 , text = "NOME:").pack()
    nome_entry = Entry(screen1 ,textvariable = nome)
    nome_entry.pack()
    Label(screen1 , text = "SENHA:").pack()
    senha_entry = Entry(screen1 ,textvariable = senha)
    senha_entry.pack()
    Label(screen1 , text = "").pack()
    Button(screen1 , text = "Register", width = 10 , height = 1 ,
           command = register_usuario).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("--LOGIN--")
    screen2.geometry("300x250")
    Label(screen2 , text = "Por favor insira seus dados abaixo !! ").pack()
    Label(screen2 , text = "").pack()
    
    global nome_verificar
    global senha_verificar
    
    nome_verificar = StringVar()
    senha_verificar = StringVar()
    
    global nome_entry1
    global senha_entry1
    
    Label(screen2 , text = "NOME:").pack()
    nome_entry1 = Entry(screen2, textvariable = nome_verificar)
    nome_entry1.pack()
    Label(screen2 , text = "").pack()
    Label(screen2 , text = "SENHA:").pack()
    senha_entry1 = Entry(screen2, textvariable = senha_verificar)
    senha_entry1.pack()
    Label(screen2 , text = "").pack()
    Button(screen2,text ="Login" ,width = 10 , height = 1 ,
           command = login_verificar).pack()
    
    print("Sessão Logada")
    #MAIN
def tela_principal():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("--SISTEMA DE PROVAS 1.0--")
    Label(text = "--SISTEMA DE PROVAS 1.0--" , bg = "blue" ,width ="300",
          height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2" , width = "30", 
           command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2" , width = "30", 
           command = register).pack()
    Label(text = "").pack()
    Button(text = "Fechar", height = "2" , width = "30", 
           command = fechar5).pack()
    
    screen.mainloop()

tela_principal()
    