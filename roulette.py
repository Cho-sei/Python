import wx
import pandas as pd
import csv
import random

class RouletteFrame(wx.Frame):
	def __init__(self,parent):

		#input達を元にランダマイズ----------------------------------------------
		kind = random.randint(2,4)
		sample = input_material.sample(n=kind)

		#評価シート出力のための処理
		array = sample['Index'].tolist()

		self.counter_list = [0] * (len(materials_list))
		for i in array:
			self.counter_list[i] = 1

		#論理演算の邪魔なのでIndex削除
		del sample['Index']

		or_data = sample.iloc[0]
		for i in range(len(sample.index) - 1):
		    or_data = or_data | sample.iloc[i+1]

		#具材達出力
		materials = sample.index
		last = materials.tolist()

		#ソースのランダムサンプリング
		pentagon = input_sauce | or_data
		pentagon_sum = pentagon.sum(axis=1)
		IndexSeries = pd.Series(data=range(4))
		IndexSeries.index = input_sauce.index

		rank = pd.DataFrame()
		rank['value'] = pentagon_sum
		rank['index'] = IndexSeries

		rank_index = rank[rank['value'] == rank['value'].max()].index
		sauce_name = rank.loc[rank_index.tolist(),:]
		sauce_row = sauce_name.sample()
		sauce = sauce_row.index.tolist()
		sauce_index = sauce_row['index'].tolist()
		sauce.extend(sauce_index)
		Result_sauce, Result_index = sauce

		#足りない味を一応出力
		fill = pentagon.loc[Result_sauce]
		lack = fill[fill == 0].index

		print(lack.tolist())

		#評価ファイルに出力
		self.counter_list[len(input_material.index) + Result_index] = 1

		#リザルトウィンドウの初期化--------------------------------------------
		wx.Frame.__init__(self,parent,-1,"Result",size=(kind*200,500))
		
		self.panel = wx.Panel(self)
		self.EnterText = wx.TextCtrl(self.panel, wx.ID_ANY)

		self.EnterText.Bind(wx.EVT_TEXT, self.TextEnter)

		self.layout = wx.BoxSizer(wx.VERTICAL)
		self.TextZone = wx.BoxSizer(wx.HORIZONTAL)
		ButtonZone = wx.BoxSizer(wx.HORIZONTAL)
		text_sauce = wx.StaticText(self.panel, wx.ID_ANY, Result_sauce, style=wx.TE_CENTER)
		text_sauce.SetForegroundColour('#FF0000')
		text_sauce.SetFont(font)

		
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

		self.TextZone.Add(text_sauce, proportion=1, flag=wx.ALIGN_CENTER)
		ButtonZone.Add(self.EnterText, flag=wx.ALIGN_BOTTOM)
		self.layout.Add(self.TextZone, proportion=3, flag=wx.ALIGN_CENTER)
		self.layout.Add(ButtonZone, proportion=1, flag=wx.ALIGN_CENTER)
		self.panel.SetSizer(self.layout)

	#親ウィンドウに戻る--------------------------------------------------------
	def TextEnter(self, event):
		self.counter_list[len(self.counter_list)-1] = self.EnterText.GetValue()
		#評価ファイルに書き込み
		with open('evaluate.csv','a') as file:
			writer = csv.writer(file, lineterminator='\n')
			writer.writerow(self.counter_list)
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

#一応メイン（なのかな？）----------------------------------------------------
if __name__ == '__main__':
	app = wx.App()
	#ファイル入出力
	input_material = pd.read_excel("materials.xlsx", sheet_name="materials", index_col=0)
	input_sauce = pd.read_excel("materials.xlsx", sheet_name="sauces", index_col=0)
	materials_list = input_material.index.tolist()
	sauces_list = input_sauce.index.tolist()
	materials_list.extend(sauces_list)
	materials_list.append('評価')
	with open('evaluate.csv','w') as file:
	    writer = csv.writer(file, lineterminator='\n')
	    writer.writerow(materials_list)
	#評価入力のための添え字付与
	input_material['Index'] = range(len(input_material.index))

	#親ウィンドウスタート
	font = wx.Font(20,wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
	frame = Mainframe()
	frame.Centre()
	frame.Show()
	app.MainLoop()