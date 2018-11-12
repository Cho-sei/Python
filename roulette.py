import wx
import pandas as pd
import csv

class RouletteFrame(wx.Frame):
	def __init__(self,parent):

		#inputを元にランダマイズ----------------------------------------------
		categories = input.columns
		material_list = [0] * len(categories)
		for column_name,i in zip(categories,range(len(categories))):
			sample = input[column_name].sample()
			Nansample = sample.dropna()
			material_list[i] = Nansample.values.tolist()

		output = [flatten for inner in material_list for flatten in inner]
		outputList = set(output)
		last = list(outputList)
		print(last)
		kind = len(last)
		print(kind)

		#リザルトウィンドウの初期化--------------------------------------------
		wx.Frame.__init__(self,parent,-1,"Result",size=(kind*200,500))
		
		self.panel = wx.Panel(self)
		end_button = wx.Button(self.panel, wx.ID_ANY, '終了')

		end_button.Bind(wx.EVT_BUTTON, self.exit)

		self.layout = wx.BoxSizer(wx.VERTICAL)
		self.TextZone = wx.BoxSizer(wx.HORIZONTAL)
		ButtonZone = wx.BoxSizer(wx.HORIZONTAL)

		
		#気持ち悪いところ---------------------------------------------------------
		if kind == 1:
			text_0 = wx.StaticText(self.panel, wx.ID_ANY, last[0], style=wx.TE_CENTER)
			text_0.SetFont(font)
			self.TextZone.Add(text_0, proportion=1, flag=wx.ALIGN_CENTER)
		elif kind == 2:
			text_0 = wx.StaticText(self.panel, wx.ID_ANY, last[0], style=wx.TE_CENTER)
			text_0.SetFont(font)
			self.TextZone.Add(text_0, proportion=1, flag=wx.ALIGN_CENTER)
			text_1 = wx.StaticText(self.panel, wx.ID_ANY, last[1], style=wx.TE_CENTER)
			text_1.SetFont(font)
			self.TextZone.Add(text_1, proportion=1, flag=wx.ALIGN_CENTER)
		elif kind == 3:
			text_0 = wx.StaticText(self.panel, wx.ID_ANY, last[0], style=wx.TE_CENTER)
			text_0.SetFont(font)
			self.TextZone.Add(text_0, proportion=1, flag=wx.ALIGN_CENTER)
			text_1 = wx.StaticText(self.panel, wx.ID_ANY, last[1], style=wx.TE_CENTER)
			text_1.SetFont(font)
			self.TextZone.Add(text_1, proportion=1, flag=wx.ALIGN_CENTER)
			text_2 = wx.StaticText(self.panel, wx.ID_ANY, last[2], style=wx.TE_CENTER)
			text_2.SetFont(font)
			self.TextZone.Add(text_2, proportion=1, flag=wx.ALIGN_CENTER)
		elif kind == 4:
			text_0 = wx.StaticText(self.panel, wx.ID_ANY, last[0], style=wx.TE_CENTER)
			text_0.SetFont(font)
			self.TextZone.Add(text_0, proportion=1, flag=wx.ALIGN_CENTER)
			text_1 = wx.StaticText(self.panel, wx.ID_ANY, last[1], style=wx.TE_CENTER)
			text_1.SetFont(font)
			self.TextZone.Add(text_1, proportion=1, flag=wx.ALIGN_CENTER)
			text_2 = wx.StaticText(self.panel, wx.ID_ANY, last[2], style=wx.TE_CENTER)
			text_2.SetFont(font)
			self.TextZone.Add(text_2, proportion=1, flag=wx.ALIGN_CENTER)
			text_3 = wx.StaticText(self.panel, wx.ID_ANY, last[3], style=wx.TE_CENTER)
			text_3.SetFont(font)
			self.TextZone.Add(text_3, proportion=1, flag=wx.ALIGN_CENTER)
		elif kind == 5:
			text_0 = wx.StaticText(self.panel, wx.ID_ANY, last[0], style=wx.TE_CENTER)
			text_0.SetFont(font)
			self.TextZone.Add(text_0, proportion=1, flag=wx.ALIGN_CENTER)
			text_1 = wx.StaticText(self.panel, wx.ID_ANY, last[1], style=wx.TE_CENTER)
			text_1.SetFont(font)
			self.TextZone.Add(text_1, proportion=1, flag=wx.ALIGN_CENTER)
			text_2 = wx.StaticText(self.panel, wx.ID_ANY, last[2], style=wx.TE_CENTER)
			text_2.SetFont(font)
			self.TextZone.Add(text_2, proportion=1, flag=wx.ALIGN_CENTER)
			text_3 = wx.StaticText(self.panel, wx.ID_ANY, last[3], style=wx.TE_CENTER)
			text_3.SetFont(font)
			self.TextZone.Add(text_3, proportion=1, flag=wx.ALIGN_CENTER)
			text_4 = wx.StaticText(self.panel, wx.ID_ANY, last[4], style=wx.TE_CENTER)
			text_4.SetFont(font)
			self.TextZone.Add(text_4, proportion=1, flag=wx.ALIGN_CENTER)
		elif kind == 6:
			text_0 = wx.StaticText(self.panel, wx.ID_ANY, last[0], style=wx.TE_CENTER)
			text_0.SetFont(font)
			self.TextZone.Add(text_0, proportion=1, flag=wx.ALIGN_CENTER)
			text_1 = wx.StaticText(self.panel, wx.ID_ANY, last[1], style=wx.TE_CENTER)
			text_1.SetFont(font)
			self.TextZone.Add(text_1, proportion=1, flag=wx.ALIGN_CENTER)
			text_2 = wx.StaticText(self.panel, wx.ID_ANY, last[2], style=wx.TE_CENTER)
			text_2.SetFont(font)
			self.TextZone.Add(text_2, proportion=1, flag=wx.ALIGN_CENTER)
			text_3 = wx.StaticText(self.panel, wx.ID_ANY, last[3], style=wx.TE_CENTER)
			text_3.SetFont(font)
			self.TextZone.Add(text_3, proportion=1, flag=wx.ALIGN_CENTER)
			text_4 = wx.StaticText(self.panel, wx.ID_ANY, last[4], style=wx.TE_CENTER)
			text_4.SetFont(font)
			self.TextZone.Add(text_4, proportion=1, flag=wx.ALIGN_CENTER)
			text_5 = wx.StaticText(self.panel, wx.ID_ANY, last[5], style=wx.TE_CENTER)
			text_5.SetFont(font)
			self.TextZone.Add(text_5, proportion=1, flag=wx.ALIGN_CENTER)

		ButtonZone.Add(end_button, flag=wx.ALIGN_BOTTOM)
		self.layout.Add(self.TextZone, proportion=3, flag=wx.ALIGN_CENTER)
		self.layout.Add(ButtonZone, proportion=1, flag=wx.ALIGN_CENTER)
		self.panel.SetSizer(self.layout)

	#親ウィンドウに戻る--------------------------------------------------------
	def exit(self, event):
		self.Destroy()


class Mainframe(wx.Frame):
	def __init__(self):

		#親ウインドウの初期化------------------------------------------------
		super().__init__(None, wx.ID_ANY, 'たこ焼きダイス', size=(500,500))

		self.panel = wx.Panel(self)
		initText = wx.StaticText(self.panel, wx.ID_ANY, 'たこ焼きダイス')
		rou_button = wx.Button(self.panel, wx.ID_ANY, 'ルーレット')
		end_button = wx.Button(self.panel, wx.ID_ANY, '終了')
		initText.SetFont(font)

		self.layout = wx.BoxSizer(wx.VERTICAL)
		self.TextZone = wx.BoxSizer(wx.HORIZONTAL)
		ButtonZone = wx.BoxSizer(wx.HORIZONTAL)
		self.TextZone.Add(initText, flag=wx.ALIGN_CENTER)
		ButtonZone.Add(rou_button, flag=wx.ALIGN_BOTTOM)
		ButtonZone.Add(end_button, flag=wx.ALIGN_BOTTOM)
		self.layout.Add(self.TextZone, proportion=3, flag=wx.ALIGN_CENTER)
		self.layout.Add(ButtonZone, proportion=1, flag=wx.ALIGN_CENTER)
		self.panel.SetSizer(self.layout)

		rou_button.Bind(wx.EVT_BUTTON, self.roulette)
		end_button.Bind(wx.EVT_BUTTON, self.exit)

	#リザルトウィンドウに遷移---------------------------------------------------
	def roulette(self, event):
		frame = RouletteFrame(self)
		frame.Centre()
		frame.Show()		

	#プログラム終了--------------------------------------------------------
	def exit(self, event):
		self.Destroy()

#ファイル入出力------------------------------------------------------------
def InputAndOutputFile():
	#ただ具材を入力してリストアップして出力するだけ（なのに…）
	inputFile = pd.read_excel("materials.xlsx")
	#欠損値対策
	FillNan = inputFile.fillna(0)
	array = FillNan.values.tolist()
	output = [flatten for inner in array for flatten in inner]
	#書き込み準備
	outputList = set(output)
	outputList.remove(0)
	last = list(outputList)
	last.append('評価')
	with open('test.csv','w') as file:
	    writer = csv.writer(file, lineterminator='\n')
	    writer.writerow(last)
	return inputFile

#一応メイン（なのかな？）----------------------------------------------------
if __name__ == '__main__':
	app = wx.App()
	input = InputAndOutputFile()
	font = wx.Font(20,wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
	frame = Mainframe()
	frame.Centre()
	frame.Show()
	app.MainLoop()