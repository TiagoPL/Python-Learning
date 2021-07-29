import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title('Grid Demo')                               # Criando a janela
mainWindow.geometry('640x480+50+50')
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text='TKinter Grid Demo')        # Criando Texto e selecionando a posição
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=100)              # Criando as colunas e definindo a largura de cada
mainWindow.columnconfigure(1, weight=1)   # Deixar uma coluna muito menor que as outras pra ela nao sumir ao encolher
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)
mainWindow.rowconfigure(0, weight=1)                 # Criando as linhas e definindo a largura de cada
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)                      # Criando uma caixa dentro da janela
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('C:\\Windows\\System32'):        # Inserindo informações nessa janela
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)         # Criando a scroll bar
fileList['yscrollcommand'] = listScroll.set

optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')        # Criando uma caixa dentro da janela
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()                           # Criando os botões clicaveis dentro dessa janela
rbValue.set(2)
radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

resultLabel = tkinter.Label(mainWindow, text='Result')    # Criando o espaço pra mostrar o resultado
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

timeFrame = tkinter.LabelFrame(mainWindow, text='Time')    # Criando o espaço pra mostrar o time
timeFrame.grid(row=3, column=0, sticky='new')

hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)           # Criando os botoes do time
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)

hourSpinner.grid(row=0, column=0)                               # Colocando os botoes em posição
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36               # Centralizar os botoes

dateFrame = tkinter.Frame(mainWindow)                # Criando a janela pra data
dateFrame.grid(row=4, column=0, sticky='new')

dayLabel = tkinter.Label(dateFrame, text='Day')         # Criando os frames das datas
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')              # Posicionando os frames das datas
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)           # Criando os botoes das datas
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr',
                            'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)

daySpin.grid(row=1, column=0)      # Posicionando os botoes
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

okButton = tkinter.Button(mainWindow, text='OK')                # Criando e posicionado botoes OK e Cancel
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()
