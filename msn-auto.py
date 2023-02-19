import pyautogui

from tkinter import*

def msn():

	pyautogui.moveTo(140, 528, 4)

	pyautogui.doubleClick(140, 528)

	pyautogui.PAUSE = 3.0

	pyautogui.moveTo(430, 492, 4)

	pyautogui.PAUSE = 2.5

	pyautogui.click()

	pyautogui.moveTo(1071, 990, 4)

	pyautogui.click()

	pyautogui.write('Oie', interval = 0.25)

	pyautogui.press('enter', interval = 0.20)

	pyautogui.write('Esta e uma mensagem automatica do pyautogui :]', interval = 0.30)

	pyautogui.press('enter')
	
	exit()

def sair():
	
	exit(janela)


janela = Tk()

janela.title('Msn-Auto')

janela.geometry('500x100')

texto1 = Label(janela, text = 'Deseja mandar uma mensagem pré configurada?')
texto1.grid(column = 20, row = 0, padx = 10, pady = 10 )

btt1 = Button(janela, text = 'sim', command = msn)
btt1.grid(column = 10, row = 20, padx = 0, pady = 0)

btt2 = Button(janela, text = 'cancelar', command = sair)
btt2.grid(column = 30, row = 20, padx = 0, pady = 0)

janela.mainloop()


#“Há um grupo de pessoas que manda no mundo secretamente. Estou falando daqueles que ninguém conhece. Daquelas que são invisíveis. Aqueles poucos que brincam de Deus sem permissão.”
