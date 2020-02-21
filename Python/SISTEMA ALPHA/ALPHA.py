import sqlite3, matplotlib
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image


matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        genero VARCHAR(9) NOT NULL,
        user  VARCHAR(8) NOT NULL,
        pass  VARCHAR(8) NOT NULL,
        nota_1 DECIMAL(4,2),
        nota_2 DECIMAL(4,2),
        media DECIMAL(4,2),
        vezes_f_teste INTEGER,
        cidade TEXT

);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS professor (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        genero VARCHAR(9) NOT NULL,
        user  VARCHAR(8) NOT NULL,
        pass  VARCHAR(8) NOT NULL,
        cidade TEXT
);
""")

conn.commit()
conn.close()

#FECHA JANELAS
def sair():
    screen.destroy()

def sair_janela(janela):
    janela.destroy()

#CONFERE RESPOSTAS
def apresentar_respostas_certas(respostas, respostas_certas, aluno, nota):
    apresentar_respostas = Toplevel(screen)
    apresentar_respostas.title("RESULTADO")
    apresentar_respostas.configure(background="#2F4F4F")
    apresentar_respostas.geometry("1300x450")
    apresentar_respostas.iconbitmap(r'favicon.ico')
    apresentar_respostas.maxsize(1300, 450)
    apresentar_respostas.attributes('-alpha', 0.9)

    frame1 = Frame(apresentar_respostas, width=10, height=10, bd=4, bg="DarkSlateGray", relief="raise")
    frame1.grid(row=3, column=4, rowspan=2, sticky=W)

    frame2 = Frame(apresentar_respostas, width=10, height=10, bd=4, bg="DarkSlateGray", relief="raise")
    frame2.grid(row=6, column=4, rowspan=2, sticky=W)


    lb1 = Label(apresentar_respostas, text="----- RESULTADO FINAL -----", fg="Black", bg="DarkSlateGray", font=("Agency FB", 40, "bold"))
    lb1.grid(row=0, column=1, columnspan=10, sticky=W)

    lbl03 = Label(apresentar_respostas, text=300 * "_", bg="DarkSlateGray")
    lbl03.grid(row=1, column=0, columnspan=10)


    lb = Label(apresentar_respostas, text="Matricula", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb.grid(row=2, column=0, sticky=W)
    lb0 = Label(apresentar_respostas, text=str(aluno[0]), fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb0.grid(row=2, column=1, sticky=W)


    lb2 = Label(apresentar_respostas, text="Aluno" , fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb2.grid(row=3, column=0, sticky=W)
    lb02 = Label(apresentar_respostas, text=str(aluno[1]), fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb02.grid(row=3, column=1, sticky=W)


    lb3 = Label(apresentar_respostas, text="Cidade", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb3.grid(row=4, column=0, sticky=W)
    lb03 = Label(apresentar_respostas, text=str(aluno[9]), fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb03.grid(row=4, column=1, sticky=W)


    lb4 = Label(apresentar_respostas, text="Tentativa", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb4.grid(row=5, column=0, sticky=W)
    lb04 = Label(apresentar_respostas, text=str(aluno[8]), fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb04.grid(row=5, column=1, sticky=W)

    lb6 = Label(apresentar_respostas, text="Nota da Avalição:", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb6.grid(row=6, column=0, sticky=W)
    lb06 = Label(apresentar_respostas, text=str(nota), fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb06.grid(row=6, column=1, sticky=W)

    lb7 = Label(apresentar_respostas, text="Resposta do Aluno", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb7.grid(row=3, column=3, sticky=W)

    lb9 = Label(apresentar_respostas, text="Gabarito", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
    lb9.grid(row=6, column=3, sticky=W)

    for i in range(0, 10):
        lb8 = Label(frame1, text=respostas_certas[i]+" ", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
        lb8.grid(row=0, column=i + 3)

    for i in range(0, len(respostas)):
        lb8 = Label(frame1, text=respostas[i]+" ", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
        lb8.grid(row=1, column=i + 3)

    for i in range(0, 10):
        lb08 = Label(frame2, text=respostas_certas[i]+" ", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
        lb08.grid(row=0, column=i + 3, sticky=W)

    for i in range(10, len(respostas_certas)):
        lb008 = Label(frame2, text=respostas_certas[i]+" ", fg="Black", bg="DarkSlateGray", font=("Agency FB", 18, "bold"))
        lb008.grid(row=1, column=(i + 3) - 10, sticky=W)

    bt10 = Button(apresentar_respostas, text="VOLTAR", bg="Silver", fg="Blue", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: area_aluno(aluno, apresentar_respostas))
    bt10.grid(row=8, column=3)
    
#CHECAR AS RESPOSTAS
def verifica_respostas(q1, q2, q3, q4, q5, aluno, questionario):
    print("Respostas")
    msg = f'1º: {q1.get()}\n2º: {q2.get()}\n3º: {q3.get()}\n4º: {q4.get()}\n5º: {q5.get()}'
    print(msg)

    respostas_aluno = []
    respostas_certas = ['1º', '2º', '3º', '4º', '5º','d', 'd', 'b', 'a', 'b']
    nota = 0

    def letras(letra):
        if letra == 1:
            return 'a'
        elif letra == 2:
            return 'b'
        elif letra == 3:
            return 'c'
        elif letra == 4:
            return 'd'
        elif letra == 5:
            return 'e'
        else:
            return '-'

    if q1.get() == 4:
        respostas_aluno.append("d")
        nota += 1
    else:
        respostas_aluno.append(letras(q1.get()))
    if q2.get() == 4:
        respostas_aluno.append("d")
        nota += 1
    else:
        respostas_aluno.append(letras(q2.get()))
    if q3.get() == 2:
        respostas_aluno.append("b")
        nota += 1
    else:
        respostas_aluno.append(letras(q3.get()))
    if q4.get() == 1:
        respostas_aluno.append("a")
        nota += 1
    else:
        respostas_aluno.append(letras(q4.get()))
    if q5.get() == 2:
        respostas_aluno.append("b")
        nota += 1
    else:
        respostas_aluno.append(letras(q5.get()))
    

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    vezes = aluno[8] + 1

    print(nota)
    print(vezes)
    print(aluno[0])
    print(aluno[5])
    print(aluno[6])
    print(aluno[7])

    if vezes == 1:
        media = nota
        cursor.execute("""
                UPDATE aluno
                SET nota_1 = ?, media = ?,  vezes_f_teste = ?
                WHERE id = ?
                """, (nota, media, vezes, aluno[0]))
    elif vezes == 2:
        media = (aluno[7] + nota) / vezes
        cursor.execute("""
                UPDATE aluno
                SET nota_2 = ?, media = ?, vezes_f_teste = ?
                WHERE id = ?
                """, (nota, media, vezes, aluno[0]))

    cursor.execute("select * from aluno")

    for row in cursor.fetchall():
        print(row[0], row[3], row[4])
        if aluno[0] == row[0]:
            aluno = row
    conn.commit()
    conn.close()

    questionario.destroy()
    apresentar_respostas_certas(respostas_aluno, respostas_certas, aluno, nota)
    print(respostas_aluno) 
    
    
#QUESTIONARIO
def questionario_aluno(aluno, aluno_aria):
    questionario = Toplevel(screen)
    questionario.geometry("1050x615+200+80")
    questionario.configure(background="DarkKhaki")
    questionario.attributes('-alpha', 0.9)
    questionario.maxsize(1280, 800)
    questionario.iconbitmap(r'favicon.ico')
    questionario.title("QUESTIONARIO")
   

    sair_janela(aluno_aria)


    Tops = Frame(questionario, bg='Indigo', width=500, height=650, bd=4, relief="raise")
    Tops.grid(row=0, column=0, columnspan=3)


    frame1 = Frame(questionario, width=900, height=650, bd=4)
    frame1.grid(row=1, column=0, columnspan=4, sticky=W)
    frame2 = Frame(questionario, bg='DarkKhaki', width=900, height=650, bd=4)
    frame2.grid(row=2, column=0, sticky=E)
    frame3 = Frame(questionario, bg='DarkKhaki', width=900, height=650, bd=4)
    frame3.grid(row=2, column=1, sticky=W)
    frame4 = Frame(questionario, width=500, height=180, bd=4)
    frame4.grid(row=3, column=0, columnspan=2, sticky=E)
    frame5 = Frame(questionario, bg='SlateBlue', width=500, height=500, bd=4)
    frame5.grid(row=3, column=3)
   


    q1 = IntVar()
    q2 = IntVar()
    q3 = IntVar()
    q4 = IntVar()
    q5 = IntVar()


    lblInfo = Label(Tops, font=("arial", 18, "bold"), text="QUESTIONARIO", bd=8, width=30)
    lblInfo.grid(row=0, column=0)

    Label(frame1, text="1ª) Quanto é 200 x 200?", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=0, sticky=W)
    Radiobutton(frame1, text="A)  5874", padx=14, variable=q1, value=1).grid(row=1, column=0, sticky=W)
    Radiobutton(frame1, text="B)  3333", padx=14, variable=q1, value=2).grid(row=2, column=0, sticky=W)
    Radiobutton(frame1, text="C)  73652", padx=14, variable=q1, value=3).grid(row=3, column=0, sticky=W)
    Radiobutton(frame1, text="D)  40000", padx=14, variable=q1, value=4).grid(row=4, column=0, sticky=W)
    Radiobutton(frame1, text="E)  12144", padx=14, variable=q1, value=5).grid(row=5, column=0, sticky=W)

    Label(frame1, text="2ª) Quanto é 600 / 3?", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=1, sticky=W)
    Radiobutton(frame1, text="A)  523", padx=14, variable=q2, value=1).grid(row=1, column=1, sticky=W)
    Radiobutton(frame1, text="B)  311", padx=14, variable=q2, value=2).grid(row=2, column=1, sticky=W)
    Radiobutton(frame1, text="C)  784", padx=14, variable=q2, value=3).grid(row=3, column=1, sticky=W)
    Radiobutton(frame1, text="D)  200", padx=14, variable=q2, value=4).grid(row=4, column=1, sticky=W)
    Radiobutton(frame1, text="E)  100", padx=14, variable=q2, value=5).grid(row=5, column=1, sticky=W)

    Label(frame1, text="3ª) Quanto é 200 / 5?", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=2, sticky=W)
    Radiobutton(frame1, text="A)  15", padx=14, variable=q3, value=1).grid(row=1, column=2, sticky=W)
    Radiobutton(frame1, text="B)  40", padx=14, variable=q3, value=2).grid(row=2, column=2, sticky=W)
    Radiobutton(frame1, text="C)  97", padx=14, variable=q3, value=3).grid(row=3, column=2, sticky=W)
    Radiobutton(frame1, text="D)  324", padx=14, variable=q3, value=4).grid(row=4, column=2, sticky=W)
    Radiobutton(frame1, text="E)  121", padx=14, variable=q3, value=5).grid(row=5, column=2, sticky=W)

    Label(frame1, text="4ª) Quanto é 5 - 3 ?", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=3, sticky=W)
    Radiobutton(frame1, text="A) 2", padx=14, variable=q4, value=1).grid(row=1, column=3, sticky=W)
    Radiobutton(frame1, text="B) 6", padx=14, variable=q4, value=2).grid(row=2, column=3, sticky=W)
    Radiobutton(frame1, text="C) 9", padx=14, variable=q4, value=3).grid(row=3, column=3, sticky=W)
    Radiobutton(frame1, text="D) 1", padx=14, variable=q4, value=4).grid(row=4, column=3, sticky=W)
    Radiobutton(frame1, text="E) 9", padx=14, variable=q4, value=5).grid(row=5, column=3, sticky=W)

    Label(frame1, text="5ª) QUANTO É 123 x 542?  ", font="lucida 12 bold", justify=LEFT, padx=14).grid(row=0, column=4, sticky=W)
    Radiobutton(frame1, text="A)  51142", padx=14, variable=q5, value=1).grid(row=1, column=4, sticky=W)
    Radiobutton(frame1, text="B)  66666", padx=14, variable=q5, value=2).grid(row=2, column=4, sticky=W)
    Radiobutton(frame1, text="C)  12547", padx=14, variable=q5, value=3).grid(row=3, column=4, sticky=W)
    Radiobutton(frame1, text="D)  40103", padx=14, variable=q5, value=4).grid(row=4, column=4, sticky=W)
    Radiobutton(frame1, text="E)  100001", padx=14, variable=q5, value=5).grid(row=5, column=4, sticky=W)
    
    
    bt1 = Button(frame3, text="FINALIZAR", bg="Chartreuse", fg="#0000CD", height="1", width="12", font=("Agency FB", 12, "bold"), command=lambda: verifica_respostas(q1, q2, q3, q4, q5, aluno, questionario))
    bt1.pack()
    bt2 = Button(frame2, text="VOLTAR", bg="Red", fg="#0000CD", height="1", width="12",font=("Agency FB", 12, "bold"), command=lambda: area_aluno(aluno, questionario))
    bt2.pack()
    
    lbl1 = Label(frame4, text="Matricula: ", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl1.grid(row=0, column=0, sticky=W)
    lbl1_1 = Label(frame4, text=str(aluno[0]), bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl1_1.grid(row=0, column=1, columnspan=2, sticky=W)


    lbl2 = Label(frame4, text="Nome: ", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl2.grid(row=1, column=0, sticky=W)
    lbl2_1 = Label(frame4, text=str(aluno[1]), bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl2_1.grid(row=1, column=1, columnspan=2, sticky=W)


    lbl3 = Label(frame4, text="Cidade: ", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl3.grid(row=2, column=0, sticky=W)
    lbl3_1 = Label(frame4, text=str(aluno[9]), bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl3_1.grid(row=2, column=1, columnspan=2, sticky=W)


    lbl4 = Label(frame4, text=str(aluno[8]+1)+"º", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl4.grid(row=3, column=0, sticky=W)
    lbl4_1 = Label(frame4, text="Tentativa ", bg="Yellow", fg="#0000CD", height="1", width="20", font=("Agency FB", 20, "bold"), justify=LEFT, padx=14)
    lbl4_1.grid(row=3, column=1, columnspan=2, sticky=W)
    
    photo = PhotoImage(file="fatepilogo.png")
    label = Label(frame5, image=photo)
    label.grid()
    
    
    questionario.mainloop()
    
#PRINT NOTAS
def mostrar_notas_aluno(aluno, frame2):
    lbl1 = Label(frame2, text="1º Nota: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1.grid(row=3, column=0)
    lbl1_1 = Label(frame2, text=aluno[5], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1_1.grid(row=3, column=1)

    lbl2 = Label(frame2, text="2º Nota: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2.grid(row=4, column=0)
    lbl2_1 = Label(frame2, text=aluno[6], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2_1.grid(row=4, column=1)

    lbl3 = Label(frame2, text="Media: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3.grid(row=5, column=0)
    lbl3_1 = Label(frame2, text=aluno[7], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3_1.grid(row=5, column=1)

    lbl4 = Label(frame2, text="Qtd. vezes: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl4.grid(row=6, column=0)
    lbl4_1 = Label(frame2, text=aluno[8], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl4_1.grid(row=6, column=1)   
    
#PRINT E BLOCK DE VEZES FEITAS DO TESTE
def verifica_tentativas(aluno, aluno_aria):
    if aluno[8] < 2:
        questionario_aluno(aluno, aluno_aria)
    else:
        messagebox.showerror(title='ERROR', 
                             message='VOCÊ JÁ FEZ O TESTE 2 VEZES!\nNÃO PODE FAZER MAIS!')
    
#LOGIN ALUNO
def area_aluno(aluno, janela):
    aluno_aria = Toplevel(screen)
    aluno_aria.geometry("1024x400+200+90")
    aluno_aria.maxsize(750, 400)
    aluno_aria.configure(background="DarkGoldenrod")
    aluno_aria.title("ÁREA DO ALUNO")
    aluno_aria.iconbitmap(r'favicon.ico')
    aluno_aria.attributes('-alpha', 0.9)

    sair_janela(janela)

    #===================================================================================================================
    #LABELS
    lbl0 = Label(aluno_aria, text="Área do Aluno", bg="DarkGoldenrod", font="lucida 40 bold", justify=LEFT, padx=14)
    lbl0.grid(row=0, column=0, columnspan=3)

    lbl02 = Label(aluno_aria, text=200 * "_", bg="DarkGoldenrod")
    lbl02.grid(row=1, column=0, columnspan=7)

    lbl03 = Label(aluno_aria, text=200 * "_", bg="DarkGoldenrod")
    lbl03.grid(row=3, column=0, columnspan=7)

    #===================================================================================================================
    #FRAMES
    frame1 = Frame(aluno_aria, width=400, height=200, bd=4, bg="Snow", relief="raise")
    frame1.grid(row=2, column=1)

    frame2 = Frame(aluno_aria, width=300, height=650, bd=4, bg="GreenYellow", relief="raise")
    frame2.grid(row=4, column=1)

    #===================================================================================================================
    #BOTÕES
    bt1 = Button(frame1, text="QUESTIONARIO", bg="#00FF00", font="lucida 14 bold", command=lambda: verifica_tentativas(aluno, aluno_aria))
    bt1.grid(row=0, column=0)

    bt3 = Button(frame1, text="NOTAS", bg="DarkMagenta", font="lucida 14 bold", command=lambda: mostrar_notas_aluno(aluno, frame2))
    bt3.grid(row=0, column=1)

    #===================================================================================================================
    #LABELS
    lbl1 = Label(frame2, text="Matricula: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1.grid(row=0, column=0)
    lbl1_1 = Label(frame2, text=aluno[0], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1_1.grid(row=0, column=1)

    lbl2 = Label(frame2, text="Nome: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2.grid(row=1, column=0)
    lbl2_1 = Label(frame2, text=aluno[1], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2_1.grid(row=1, column=1)

    lbl3 = Label(frame2, text="Cidade: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3.grid(row=2, column=0)
    lbl3_1 = Label(frame2, text=aluno[9], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3_1.grid(row=2, column=1)   
    
#LOGIN PROFESSOR
def area_professor(professor, janela):
    professor_aria = Toplevel(screen)
    professor_aria.geometry("950x400+500+120")
    professor_aria.configure(background="#D2691E")
    professor_aria.maxsize(1024, 600)
    professor_aria.title("ÁREA DO PROFESSOR")
    professor_aria.iconbitmap(r'favicon.ico')
    professor_aria.attributes('-alpha', 0.9)

    sair_janela(janela)

    pesquisa = IntVar()

    lbl0 = Label(professor_aria, text="       Área do Professor        ", bg="#D2691E", font="lucida 40 bold", justify=LEFT, padx=14)
    lbl0.grid(row=0, column=0, columnspan=2)
    lbl01 = Label(professor_aria, text=200*"_", bg="#D2691E")
    lbl01.grid(row=1, column=0, columnspan=10)
    lbl02 = Label(professor_aria, text=200*"_", bg="#D2691E")
    lbl02.grid(row=6, column=0, columnspan=10)
    lbl03 = Label(professor_aria, text=200*"_", bg="#D2691E")
    lbl03.grid(row=4, column=0, columnspan=10)

    frame1 = Frame(professor_aria, width=400, height=200, bd=4, bg="GreenYellow", relief="raise")
    frame1.grid(row=5, column=0)

    frame2 = Frame(professor_aria, width=300, height=650, bd=4, bg="Lime", relief="raise")
    frame2.grid(row=7, column=0)


    lbl1 = Label(frame1, text="ID: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1.grid(row=0, column=0)
    lbl1_1 = Label(frame1, text=professor[0], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1_1.grid(row=0, column=1)

    lbl2 = Label(frame1, text="Nome: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2.grid(row=1, column=0)
    lbl2_1 = Label(frame1, text=professor[1], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2_1.grid(row=1, column=1)

    lbl3 = Label(frame1, text="Cidade: ", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3.grid(row=2, column=0)
    lbl3_1 = Label(frame1, text=professor[5], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3_1.grid(row=2, column=1)

    lbl5 = Label(professor_aria, text="Pesquisa Aluno Pela Matricula", bg="#D2691E", font="lucida 16 bold", justify=LEFT, padx=14)
    lbl5.grid(row=2, column=0, sticky=E)
    entry_pesquisa = Entry(professor_aria, textvariable=pesquisa)
    entry_pesquisa.grid(row=2, column=1, sticky=W)
    bt0 = Button(professor_aria, text="Pesquisar", bg="Crimson", fg="White", font=("Agency FB", 14, "bold"), command=lambda: pequisa_aluno(pesquisa, professor_aria))
    bt0.grid(row=2, column=2, sticky=W)

    lbl6 = Label(professor_aria, text="Análise Estatística da Turma", bg="#D2691E", font="lucida 16 bold", justify=LEFT, padx=14)
    lbl6.grid(row=3, column=0, sticky=E)
    bt02 = Button(professor_aria, text="  Analise  ", bg="Crimson", fg="White", font=("Agency FB", 14, "bold"), command=lambda: mostra_dados_estatisticos_turma(professor_aria))
    bt02.grid(row=3, column=2, sticky=W)

    bt1 = Button(frame2, text="Cadastar Professor", bg="GreenYellow", fg="Black", font=("Agency FB", 14, "bold"), command=cadastra_professro)
    bt1.grid(row=0, column=0)

    bt2 = Button(frame2, text="Cadastrar Aluno", bg="GreenYellow", fg="Black", font=("Agency FB", 14, "bold"),command=cadastra_aluno)
    bt2.grid(row=0, column=1)

    bt3 = Button(frame2, text="SAIR", bg="GreenYellow", fg="Black", font=("Agency FB", 14, "bold"), command=lambda: sair_janela(professor_aria))
    bt3.grid(row=0, column=2)

    
#AUTENTICAÇÃO ALUNO
def aluno_login_def(nome_login, senha_login, aluno_login):
    use = nome_login.get()
    pas = senha_login.get()

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("select * from aluno")

    for row in cursor.fetchall():
        print(row[0], row[3], row[4])
        if use == row[3] and pas == row[4]:
            aluno = row
            conn.commit()
            conn.close()
            area_aluno(aluno, aluno_login)
            return 0

    conn.commit()
    conn.close()

    Label(aluno_login, text="Usuario ou senha invalida !",
          fg="black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()
          
          
#AUTENTICAÇÃO PROFESSOR          
def professor_login_def(nome_login, senha_login, professor_login):
    use = nome_login.get()
    pas = senha_login.get()

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("select * from professor")

    for row in cursor.fetchall():
        print(row[0], row[3], row[4])
        if use == row[3] and pas == row[4]:
            professor = row
            conn.commit()
            conn.close()
            area_professor(professor, professor_login)
            return 0

    conn.commit()
    conn.close()

    Label(professor_login, text="Usuario ou senha invalida!",
          fg="black", bg="#00BFFF", font=("Agency FB", 13, "bold")).pack()          
          
# CADASTRO DO ALUNO           
def cadastra_aluno_def(nome, user, pas, cidade, sexo):
    nome_1 = nome.get().upper()
    user_1 = user.get()
    pas_1 = pas.get()
    sexo_1 = sexo.get().upper()
    nota_1 = 0.0
    nota_2 = 0.0
    media = 0.0
    vezes_f_teste = 0
    cidade_1 = cidade.get().upper()

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("select * from aluno")

    verifica_senha = True
    for row in cursor.fetchall():
        print(type(str(pas_1)), ' -> ', sexo_1)
        print(type(row[2]), ' -> ', row[2])
        print(type(row[4]), ' -> ', row[4])

        if str(pas_1) == row[4] or pas_1 == '' or pas_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='USE OUTRA SENHA')
            break

        if str(user_1) == row[3] or user_1 == '' or user_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='USUARIO INVALIDO')
            break

        if (sexo_1 == 'FEMININO' or sexo_1 == 'MASCULINO') == False:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='DEFINA SEU GENERO')
            break

        if nome_1 == '' or nome_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='NOME INVALIDO')
            break

        if cidade_1 == '' or cidade_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR',message='CIDADE INEXISTENTE OU INCORRETA')
            break

        else:
            verifica_senha = True

    if verifica_senha:
        cursor.execute("""
            INSERT INTO aluno (nome, genero, user, pass, nota_1, nota_2, media, vezes_f_teste, cidade)
            VALUES (?,?,?,?,?,?,?,?,?)
            """, (nome_1, sexo_1, user_1, pas_1, nota_1, nota_2, media, vezes_f_teste, cidade_1))

        messagebox.showerror(title='SUCESSO', message='ALUNO CADASTRADO COM SUCESSO !')

        conn.commit()
        conn.close()
        return 0

    conn.commit()
    conn.close()
    
#CADASTRO PROFESSOR
def cadastra_professro_def(nome, user, pas, cidade, sexo, professro_cadastra):
    nome_1 = nome.get().upper()
    user_1 = user.get()
    pas_1 = pas.get()
    sexo_1 = sexo.get().upper()
    cidade_1 = cidade.get().upper()
    
    sair_janela(professro_cadastra)
    
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("select * from professor")

    verifica_senha = True
    for row in cursor.fetchall():
        print(type(str(pas_1)), ' -> ', pas_1)
        print(type(row[3]), ' -> ', row[3])
        print(type(row[4]), ' -> ', row[4])
        print(row)

        if str(pas_1) == row[4] or pas_1 == '' or pas_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='UTILIZE SENHA DE ULTRAPASSE MAIS FORTE !')
            break

        if str(user_1) == row[3] or user_1 == '' or user_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='USUARIO INVALIDO OU INAPTO PARA PROFESSOR!')
            break

        if (sexo_1 == 'FEMININO' or sexo_1 == 'MASCULINO') == False:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='DEFINA  SEU GENERO')
            break

        if nome_1 == '' or nome_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='NOME INAPROPRIADO OU INVALIDO')
            break

        if cidade_1 == '' or cidade_1.isspace() == True:
            verifica_senha = False
            messagebox.showerror(title='ERROR', message='CIDADE INVALIDA')
            break

        else:
            verifica_senha = True

    if verifica_senha:
        cursor.execute("""
            INSERT INTO professor (nome, genero, user, pass, cidade)
            VALUES (?,?,?,?,?)
            """, (nome_1, sexo_1, user_1, pas_1, cidade_1))

        conn.commit()
        conn.close()
        return 0

    conn.commit()
    conn.close()   
    
#ANALISE ESTATISTICA DOS ALUNOS 
def mostra_dados_estatisticos_turma(professor_aria):
    area_estatistica = Toplevel(professor_aria)
    area_estatistica.geometry("700x500+200+90")
    area_estatistica.configure(background="DeepSkyBlue")
    area_estatistica.title("ANALISE ESTATISTICA DA TURMA")
    area_estatistica.iconbitmap(r'favicon.ico')
    area_estatistica.attributes('-alpha', 0.9)

    # ===================================================================================================================
    # FRAMES QUE ESTÃO SENDO USADOS
    frame1 = Frame(area_estatistica, width=400, height=200, bd=4, bg="GreenYellow", relief="raise")
    frame1.grid(row=0, column=0, rowspan=2)
    #===================================================================================================================

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("select * from aluno")

    cont = 0
    lista_media = []
    lista_nome = []
    for row in cursor.fetchall():
        aluno = row
        cont += 1
        lista_media.append(aluno[7])
        lista_nome.append(aluno[0])

    # GRAFICO
    figure = Figure(figsize=(cont, cont), dpi=50)
    plt = figure.add_subplot(1, 1, 1)

    y_axis = lista_media
    x_axis = lista_nome
    width_n = 0.4
    bar_color = 'Red'


    plt.bar(x_axis, y_axis, label='MEDIA', width=width_n, color=bar_color)
    plt.legend()

    '''
    x = lista_nome
    y = lista_media
    plot.plot(x, y, color="Blue", marker="x", linestyle="--")
    '''

    canvas = FigureCanvasTkAgg(figure, frame1)
    canvas.get_tk_widget().grid(row=0, column=0)

    conn.commit()
    conn.close()

    area_estatistica.mainloop()  
#APRESENTAÇÃO DOS DADOS COLETADOS
def mostra_dados_aluno_professor(aluno, professor_aria):
    aria_professor_aluno = Toplevel(professor_aria)
    aria_professor_aluno.geometry("1050x650+300+120")
    aria_professor_aluno.maxsize(1366,768)
    aria_professor_aluno.configure(background="#FFD700")
    aria_professor_aluno.title("ÁREA DO ALUNO")
    aria_professor_aluno.iconbitmap(r'favicon.ico')
    aria_professor_aluno.attributes('-alpha', 0.9)
    
    #===================================================================================================================
    #LABEL PRINCIPAL
    lbl0 = Label(aria_professor_aluno, text="Dados do Aluno", bg="#FFD700", font="lucida 40 bold", justify=LEFT, padx=14)
    lbl0.grid(row=0, column=0, columnspan=3)

    #===================================================================================================================
    #FRAMES QUE ESTÃO SENDO USADOS
    frame1 = Frame(aria_professor_aluno, width=400, height=200, bd=4, bg="GreenYellow", relief="raise")
    frame1.grid(row=2, column=0, rowspan=2)

    frame2 = Frame(aria_professor_aluno, width=300, height=300, bd=4, bg="GreenYellow", relief="raise")
    frame2.grid(row=2, column=1)

    #===================================================================================================================
    #LABELS QUE EXPLICAM OS DADOS
    lbl1 = Label(frame1, text="Matricula", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1.grid(row=0, column=0, sticky=W)
    lbl1_1 = Label(frame1, text=aluno[0], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl1_1.grid(row=0, column=1, sticky=W)

    lbl2 = Label(frame1, text="Nome", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2.grid(row=2, column=0, sticky=W)
    lbl2_1 = Label(frame1, text=aluno[1], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl2_1.grid(row=2, column=1, sticky=W)

    lbl3 = Label(frame1, text="1º Nota", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3.grid(row=4, column=0, sticky=W)
    lbl3_1 = Label(frame1, text=aluno[5], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl3_1.grid(row=4, column=1, sticky=W)

    lbl4 = Label(frame1, text="2º Nota", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl4.grid(row=6, column=0, sticky=W)
    lbl4_1 = Label(frame1, text=aluno[6], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl4_1.grid(row=6, column=1, sticky=W)

    lbl5 = Label(frame1, text="Media", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl5.grid(row=8, column=0, sticky=W)
    lbl5_1 = Label(frame1, text=aluno[7], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl5_1.grid(row=8, column=1, sticky=W)

    lbl6 = Label(frame1, text="Cidade", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl6.grid(row=10, column=0, sticky=W)
    lbl6_1 = Label(frame1, text=aluno[9], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl6_1.grid(row=10, column=1, sticky=W)

    lbl7 = Label(frame1, text="Gênero", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl7.grid(row=12, column=0, sticky=W)
    lbl7_1 = Label(frame1, text=aluno[2], bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl7_1.grid(row=12, column=1, sticky=W)

    lbl8 = Label(frame1, text="Qtd de Testes", bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl8.grid(row=14, column=0, sticky=W)
    lbl8_1 = Label(frame1, text=str(aluno[8])+' vezes', bg="GreenYellow", font="lucida 14 bold", justify=LEFT, padx=14)
    lbl8_1.grid(row=14, column=1, sticky=W)

    if float(aluno[7]) < 7 and float(aluno[8]) > 1:
        lbl9 = Label(frame1, text="REPROVADO", bg="Red", font="lucida 14 bold", justify=LEFT, padx=14)
        lbl9.grid(row=16, column=0, sticky=W)

    elif float(aluno[7]) >= 7 and int(aluno[8]) > 1:
        lbl9 = Label(frame1, text="APROVADO", fg='Yellow', bg="Red", font="lucida 14 bold", justify=LEFT, padx=14)
        lbl9.grid(row=16, column=0, sticky=W)

    # ===================================================================================================================
    # GRAFICO 1
    figure = Figure(figsize=(10, 3), dpi=50)
    plot = figure.add_subplot(1, 1, 1)

    plot.plot(10, 10, color="red", marker="o", linestyle="")

    x = ['1°', '2°', 'MEDIA']
    y = [aluno[5], aluno[6], aluno[7]]
    plot.plot(x, y, color="blue", marker="x", linestyle="--")

    canvas = FigureCanvasTkAgg(figure, frame2)
    canvas.get_tk_widget().grid(row=0, column=0)

    # GRAFICO 2
    figure = Figure(figsize=(6, 3), dpi=70)
    plt = figure.add_subplot(1, 1, 1)

    y_axis = [aluno[5]]
    y_axis2 = [aluno[6]]
    y_axis3 = [aluno[7]]

    x_axis = [aluno[5]]
    x_axis2 = [aluno[6]]
    x_axis3 = [aluno[7]]

    width_n = 0.4

    plt.bar(x_axis, y_axis, label='1° NOTA', width=width_n, color="Red")
    plt.legend()

    plt.bar(x_axis2, y_axis2, label='2° NOTA', width=width_n, color="Yellow")
    plt.legend()

    plt.bar(x_axis3, y_axis3, label='MEDIA', width=width_n, color="Blue")
    plt.legend()

    canvas = FigureCanvasTkAgg(figure, frame2)
    canvas.get_tk_widget().grid(row=1, column=0)

    #===================================================================================================================
    #LINHAS
    lbl02 = Label(aria_professor_aluno, text=500 * "_", fg='Black', bg="#FFD700", font="20")
    lbl02.grid(row=1, column=0, columnspan=25)

    lbl03 = Label(aria_professor_aluno, text=500 * "_", fg='Black', bg="#FFD700", font="20")
    lbl03.grid(row=4, column=0, columnspan=25)

    i = 1
    while(i < 19):
        lbl04 = Label(frame1, text=100 * "_", bg="GreenYellow")
        lbl04.grid(row=i, column=0, columnspan=10)
        i += 2    
#ALGORITIMO DE BUSCA POR ID
def pequisa_aluno(pesquisa, professor_aria):
    
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("select * from aluno")

    for row in cursor.fetchall():
        if row[0] == pesquisa.get():
            aluno = row
            mostra_dados_aluno_professor(aluno, professor_aria)
            return 0
        
    lb1 = Label(professor_aria, text="Aluno não cadastrado",
                        fg="black", bg="#FFD700", font=("Agency FB", 12, "bold"))
    lb1.grid(row=3, column=1, sticky=W)
            
    print(pesquisa.get())
    print(row[0])

    conn.commit()
    conn.close()        
    
#JANELA PROFESSOR TOPLEVEL
def login_professor():
    professor_login = Toplevel(screen)
    professor_login.title("LOGIN PROFESSOR")
    professor_login.configure(background="DeepSkyBlue")
    professor_login.geometry("500x310+500+370")
    professor_login.iconbitmap(r'favicon.ico')
    professor_login.maxsize(600, 310)
    professor_login.attributes('-alpha', 0.9)

    lb1 = Label(professor_login, text="Por favor insira seus dados abaixo",
                fg="Black", bg="DeepSkyBlue", font=("Agency FB", 16, "bold"))
    lb1.pack()
    Label(professor_login, text="", bg="DeepSkyBlue").pack()

    nome_login = StringVar()
    senha_login = StringVar()

    frame1 = Frame(professor_login, width=900, height=650, bg="DeepSkyBlue", bd=8, relief="raise")
    frame1.pack()

    lb2 = Label(frame1, text="USUARIO ", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 13, "bold"))
    lb2.pack()

    nome_entry = Entry(frame1, textvariable=nome_login)
    nome_entry.pack()

    lb4 = Label(frame1, text="SENHA ", fg="Black", bg="DeepSkyBlue", font=("Agency FB", 13, "bold"))
    lb4.pack()

    senha_entry = Entry(frame1, show="*", textvariable=senha_login)
    senha_entry.pack()

    lb5 = Label(frame1, text="", bg="DeepSkyBlue")
    lb5.pack()

    frame2 = Frame(frame1, width=5, height=5, bg="DeepSkyBlue", bd=4, relief="raise")
    frame2.pack()

    bt1 = Button(frame2, text="Login", bg="Yellow", 
                 fg="Black", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: professor_login_def(nome_login, senha_login, professor_login))
    bt1.pack()

    lb6 = Label(frame1, text="", bg="DeepSkyBlue")
    lb6.pack()  
    
#JANELA ALUNO TOPLEVEL
def login_aluno():
    aluno_login = Toplevel(screen)
    aluno_login.title("LOGIN ALUNO")
    aluno_login.configure(background="#FF4500")
    aluno_login.geometry("500x310+500+30")
    aluno_login.iconbitmap(r'favicon.ico')
    aluno_login.maxsize(600, 310)
    aluno_login.attributes('-alpha', 0.9)

    lb1 = Label(aluno_login, text="Por favor insira seus dados abaixo", fg="Black", bg="#FF4500", font=("Agency FB", 16, "bold"))
    lb1.pack()
    Label(aluno_login, text="", bg="#FF4500").pack()

    frame1 = Frame(aluno_login, width=900, height=650, bg="#FF4500", bd=8, relief="raise")
    frame1.pack()

    nome_login = StringVar()
    senha_login = StringVar()

    lb2 = Label(frame1, text="USUARIO", fg="Black", bg="#FF4500", font=("Agency FB", 13, "bold"))
    lb2.pack()

    nome_entry = Entry(frame1, textvariable=nome_login)
    nome_entry.pack()

    lb4 = Label(frame1, text="SENHA", fg="Black", bg="#FF4500", font=("Agency FB", 13, "bold"))
    lb4.pack()

    senha_entry = Entry(frame1, show="*", textvariable=senha_login)
    senha_entry.pack()

    lb5 = Label(frame1, text="", bg="#FF4500")
    lb5.pack()

    frame2 = Frame(frame1, width=5, height=5, bg="#FF4500", bd=4, relief="raise")
    frame2.pack()

    bt1 = Button(frame2, text="Login", bg="Yellow", fg="Black",
                 height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: aluno_login_def(nome_login, senha_login, aluno_login))
    bt1.pack()

    lb6 = Label(frame1, text="", bg="#FF4500")
    lb6.pack()
    
#JANELA CADASTRO TOPLEVEL
def cadastra_professro():
    professro_cadastra = Toplevel(screen)
    professro_cadastra.title("CADASTRAR PROFESSOR")
    professro_cadastra.configure(background="#FFFF00")
    professro_cadastra.geometry("700x550+660+80")
    professro_cadastra.iconbitmap(r'favicon.ico')
    professro_cadastra.maxsize(600, 550)
    professro_cadastra.attributes('-alpha', 0.9)


    Label(professro_cadastra, text="", bg="#FFFF00").pack()
    frame1 = Frame(professro_cadastra, width=900, height=650, bg="Thistle", bd=8, relief="raise")
    frame1.pack()

    nome = StringVar()
    user = StringVar()
    pas = StringVar()
    sexo = StringVar()
    cidade = StringVar()

    Label(frame1, text="Por favor insira seus dados abaixo", fg="Black", bg="Thistle", font=("Agency FB", 13, "bold")).pack()
    Label(frame1, text="", bg="Thistle").pack()

    Label(frame1, text="Nome completo ", fg="Black", bg="Thistle", font=("Agency FB", 13, "bold")).pack()
    nome_entry = Entry(frame1, textvariable=nome)
    nome_entry.pack()

    Label(frame1, text="Cidade ", fg="Black", bg="Thistle", font=("Agency FB", 13, "bold")).pack()
    cidade_entry = Entry(frame1, textvariable=cidade)
    cidade_entry.pack()

    sexo1 = Radiobutton(frame1, text='Feminino', bg="Thistle", variable=sexo, value='FEMININO', font=("Agency FB", 13, "bold"))
    sexo1.pack()
    sexo2 = Radiobutton(frame1, text='Masculino', bg="Thistle", variable=sexo, value='MASCULINO', font=("Agency FB", 13, "bold"))
    sexo2.pack()

    Label(frame1, text="", bg="Thistle").pack()

    Label(frame1, text="USUARIO", fg="Black", bg="Thistle", font=("Agency FB", 13, "bold")).pack()
    use_entry = Entry(frame1, textvariable=user)
    use_entry.pack()

    Label(frame1, text="SENHA ", fg="Black", bg="Thistle", font=("Agency FB", 13, "bold")).pack()
    senha_entry = Entry(frame1, show="*", textvariable=pas)
    senha_entry.pack()

    Label(frame1, text="", bg="Thistle").pack()
    bt1 = Button(frame1, text="OK", bg="#4B0082", fg="Black", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: cadastra_professro_def(nome, user, pas, cidade, sexo, professro_cadastra))
    bt1.pack()

    Label(frame1, text="", bg="Thistle").pack()

    professro_cadastra.mainloop()
    
#JANELA CADASTRA ALUNO TOPLEVEL
def cadastra_aluno():
    aluno_cadastra = Toplevel(screen)
    aluno_cadastra.title("CADASTRAR ALUNO")
    aluno_cadastra.configure(background="ForestGreen")
    aluno_cadastra.geometry("700x550+350+80")
    aluno_cadastra.iconbitmap(r'favicon.ico')
    aluno_cadastra.maxsize(800, 550)
    aluno_cadastra.attributes('-alpha', 0.9)

    Label(aluno_cadastra, text="", bg="ForestGreen").pack()
    frame1 = Frame(aluno_cadastra, width=900, height=650, bg="#00008B", bd=8, relief="raise")
    frame1.pack()

    nome = StringVar()
    user = StringVar()
    pas = StringVar()
    sexo = StringVar()
    cidade = StringVar()


    Label(frame1, text="Por favor insira seus dados abaixo", fg="Black", bg="#00008B", font=("Agency FB", 13, "bold")).pack()
    Label(frame1, text="", bg="#00008B").pack()

    Label(frame1, text="Nome completo ", fg="Black", bg="#00008B", font=("Agency FB", 13, "bold")).pack()
    nome_entry_completo = Entry(frame1, textvariable=nome)
    nome_entry_completo.pack()

    Label(frame1, text="Cidade ", fg="Black", bg="#00008B", font=("Agency FB", 13, "bold")).pack()
    nome_entry_cidade = Entry(frame1, textvariable=cidade)
    nome_entry_cidade.pack()

    sexo1 = Radiobutton(frame1, text='Feminino', bg="#00008B", variable=sexo, value='Feminino', font=("Agency FB", 13, "bold"))
    sexo1.pack()
    sexo2 = Radiobutton(frame1, text='Masculino', bg="#00008B", variable=sexo, value='Masculino', font=("Agency FB", 13, "bold"))
    sexo2.pack()

    Label(frame1, text="", bg="#00008B").pack()

    Label(frame1, text="USUARIO ", fg="Black", bg="#00008B", font=("Agency FB", 13, "bold")).pack()
    nome_entry_login = Entry(frame1, textvariable=user)
    nome_entry_login.pack()

    Label(frame1, text="SENHA", fg="Black", bg="#00008B", font=("Agency FB", 13, "bold")).pack()
    senha_entry_login = Entry(frame1, show="*", textvariable=pas)
    senha_entry_login.pack()

    Label(frame1, text=" ", bg="#00008B").pack()
    bt1 = Button(frame1, text="OK", bg="#FFA500", fg="Black", height="1", width="15", font=("Agency FB", 14, "bold"), command=lambda: cadastra_aluno_def(nome, user, pas, cidade, sexo))
    bt1.pack()
    Label(frame1, text="", bg="#00008B").pack()

    aluno_cadastra.mainloop()  
    
#MAIN
def tela_principal():
    global screen
    screen = Tk()
    screen.maxsize(500, 300)
    screen.attributes('-alpha', 0.9)
    screen.configure(background="DarkCyan")
    screen.geometry("400x300")
    screen.iconbitmap(r'favicon.ico')
    screen.title("---SISTEMAS DE PROVAS ALPHA---")
    
    
    
    frame11 = Frame(screen, bg='DarkCyan',width=1000, height=650, bd=4)
    frame11.grid(row=0, column=1, columnspan=3)
    frame12 = Frame(screen, bg='DarkCyan', width=1000, height=650, bd=4)
    frame12.grid(row=1, column=1,sticky=E)
    frame13 = Frame(screen, bg='DarkCyan', width=1000, height=650, bd=4)
    frame13.grid(row=2, column=1,sticky=E)
    frame14 = Frame(screen, bg='DarkCyan', width=1000, height=650, bd=4)
    frame14.grid(row=1, column=3,sticky=E)
    frame15 = Frame(screen, bg='DarkCyan', width=1000, height=650, bd=4)
    frame15.grid(row=2, column=3,sticky=E)
    frame16 = Frame(screen, bg='DarkCyan', width=1000, height=650, bd=4)
    frame16.grid(row=3, column=2,sticky=E)
    
    Label(frame11,text = "----------- SISTEMAS DE PROVAS ALPHA -----------" , bg = "DarkCyan", fg="Cyan",
          font = ("Agency FB", 13)).grid(row=0, column=1, columnspan=3)
    
    Button(frame12,text = "    Login  Aluno    ",command = login_aluno,width=15, height=1).grid(row=1, column=1,sticky=E)
    Button(frame13,text = "  Login Professor  ", command = login_professor,width=15, height=1).grid(row=2, column=1,sticky=E)
    Button(frame14,text = "    Registar Aluno   " , command = cadastra_aluno,width=15, height=1).grid(row=1, column=3,sticky=E)
    Button(frame15,text = "Registrar Professor",command = cadastra_professro,width=15, height=1).grid(row=2, column=3,sticky=E)
    Button(frame16,text = "    Fechar    ",command = sair ,width=15, height=1).grid(row=3, column=2,sticky=E)
    
   
    screen.mainloop()

tela_principal()
    