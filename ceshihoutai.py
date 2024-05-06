#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk


class HoutaiceshiWidget(ttk.Notebook):
    def __init__(self, master=None, **kw):
        super(HoutaiceshiWidget, self).__init__(master, **kw)
        self.frame1 = ttk.Frame(self)
        self.frame1.configure(height=200, width=200)
        self.frame2 = ttk.Frame(self.frame1)
        self.frame2.configure(height=200, relief="raised", width=200)
        self.frame4 = ttk.Frame(self.frame2)
        self.frame4.configure(height=300, relief="raised", width=500)
        self.label1 = ttk.Label(self.frame4)
        self.label1.configure(
            compound="top",
            font="TkMenuFont",
            text='近期天提交的订单数量')
        self.label1.pack(side="top")
        self.canvas1 = tk.Canvas(self.frame4)
        self.canvas1.configure(height=300, relief="flat", width=550)
        self.canvas1.pack(fill="both", side="top")
        self.frame4.pack(fill="x", side="left")
        self.frame4.pack_propagate(0)
        self.frame6 = ttk.Frame(self.frame2)
        self.frame6.configure(height=300, relief="raised", width=500)
        self.label3 = ttk.Label(self.frame6)
        self.label3.configure(compound="top", font="TkMenuFont", text='近期入库')
        self.label3.pack(side="top")
        self.canvas3 = tk.Canvas(self.frame6)
        self.canvas3.configure(height=300, relief="flat", width=550)
        self.canvas3.pack(fill="both", side="top")
        self.frame6.pack(fill="x", side="left")
        self.frame6.pack_propagate(0)
        self.frame12 = ttk.Frame(self.frame2)
        self.frame12.configure(height=300, relief="raised", width=500)
        self.label8 = ttk.Label(self.frame12)
        self.label8.configure(compound="top", font="TkMenuFont", text='近期出库')
        self.label8.pack(side="top")
        self.canvas7 = tk.Canvas(self.frame12)
        self.canvas7.configure(height=300, relief="flat", width=550)
        self.canvas7.pack(fill="both", side="top")
        self.frame12.pack(fill="x", side="left")
        self.frame12.pack_propagate(0)
        self.frame2.pack(fill="both", side="top")
        self.frame10 = ttk.Frame(self.frame1)
        self.frame10.configure(height=200, width=200)
        self.button2 = ttk.Button(self.frame10)
        self.button2.configure(text='按日')
        self.button2.pack(side="left")
        self.button3 = ttk.Button(self.frame10)
        self.button3.configure(text='按月')
        self.button3.pack(side="left")
        self.frame10.pack(expand=False, fill="y", side="top")
        self.frame3 = ttk.Frame(self.frame1)
        self.frame3.configure(height=200, relief="raised", width=200)
        self.frame5 = ttk.Frame(self.frame3)
        self.frame5.configure(height=200, relief="raised", width=200)
        self.label2 = ttk.Label(self.frame5)
        self.label2.configure(text='近期提交的订单信息')
        self.label2.pack(side="top")
        self.treeview1 = ttk.Treeview(self.frame5)
        self.treeview1.configure(selectmode="extended", show="headings")
        self.treeview1_cols = ['column1', 'column2', 'column3']
        self.treeview1_dcols = ['column1', 'column2', 'column3']
        self.treeview1.configure(
            columns=self.treeview1_cols,
            displaycolumns=self.treeview1_dcols)
        self.treeview1.column(
            "column1",
            anchor="w",
            stretch=True,
            width=50,
            minwidth=20)
        self.treeview1.column(
            "column2",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview1.column(
            "column3",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview1.heading("column1", anchor="w", text='用户')
        self.treeview1.heading("column2", anchor="w", text='单号')
        self.treeview1.heading("column3", anchor="w", text='提交时间')
        self.treeview1.pack(expand=True, fill="both", side="left")
        self.scrollbar2 = ttk.Scrollbar(self.frame5)
        self.scrollbar2.configure(orient="vertical")
        self.scrollbar2.pack(fill="y", side="left")
        self.frame5.pack(expand=True, fill="both", side="left")
        self.frame9 = ttk.Frame(self.frame3)
        self.frame9.configure(height=200, relief="raised", width=200)
        self.label7 = ttk.Label(self.frame9)
        self.label7.configure(text='近期入库信息')
        self.label7.pack(side="top")
        self.treeview2 = ttk.Treeview(self.frame9)
        self.treeview2.configure(selectmode="extended", show="headings")
        self.treeview2_cols = ['column4', 'column5', 'column6']
        self.treeview2_dcols = ['column4', 'column5', 'column6']
        self.treeview2.configure(
            columns=self.treeview2_cols,
            displaycolumns=self.treeview2_dcols)
        self.treeview2.column(
            "column4",
            anchor="w",
            stretch=True,
            width=50,
            minwidth=20)
        self.treeview2.column(
            "column5",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview2.column(
            "column6",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview2.heading("column4", anchor="w", text='用户')
        self.treeview2.heading("column5", anchor="w", text='单号')
        self.treeview2.heading("column6", anchor="w", text='入库时间')
        self.treeview2.pack(expand=True, fill="both", side="left")
        self.scrollbar3 = ttk.Scrollbar(self.frame9)
        self.scrollbar3.configure(orient="vertical")
        self.scrollbar3.pack(fill="y", side="left")
        self.frame9.pack(expand=True, fill="both", side="left")
        self.frame17 = ttk.Frame(self.frame3)
        self.frame17.configure(height=200, relief="raised", width=200)
        self.label17 = ttk.Label(self.frame17)
        self.label17.configure(text='近期出库信息')
        self.label17.pack(side="top")
        self.treeview12 = ttk.Treeview(self.frame17)
        self.treeview12.configure(selectmode="extended", show="headings")
        self.treeview12_cols = ['column34', 'column35', 'column36']
        self.treeview12_dcols = ['column34', 'column35', 'column36']
        self.treeview12.configure(
            columns=self.treeview12_cols,
            displaycolumns=self.treeview12_dcols)
        self.treeview12.column(
            "column34",
            anchor="w",
            stretch=True,
            width=50,
            minwidth=20)
        self.treeview12.column(
            "column35",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview12.column(
            "column36",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview12.heading("column34", anchor="w", text='用户')
        self.treeview12.heading("column35", anchor="w", text='单号')
        self.treeview12.heading("column36", anchor="w", text='提交时间')
        self.treeview12.pack(expand=True, fill="both", side="left")
        self.scrollbar7 = ttk.Scrollbar(self.frame17)
        self.scrollbar7.configure(orient="vertical")
        self.scrollbar7.pack(fill="y", side="left")
        self.frame17.pack(expand=True, fill="both", side="left")
        self.frame3.pack(expand=True, fill="both", side="top")
        self.button1 = ttk.Button(self.frame1)
        self.button1.configure(text='刷新')
        self.button1.pack(expand=False, fill="both", side="top")
        self.label33 = ttk.Label(self.frame1)
        self.label33.configure(text='状态')
        self.label33.pack(side="left")
        self.frame1.pack(side="top")
        self.add(self.frame1, text='首页')
        self.frame18 = ttk.Frame(self)
        self.frame18.configure(height=200, width=200)
        self.frame38 = ttk.Frame(self.frame18)
        self.frame38.configure(height=200, relief="raised", width=900)
        self.treeview13 = ttk.Treeview(self.frame38)
        self.treeview13.configure(selectmode="extended", show="headings")
        self.treeview13_cols = [
            'column37',
            'column38',
            'column39',
            'column40',
            'column41',
            'column42',
            'column43',
            'column44',
            'column45',
            'column46',
            'column47',
            'column48',
            'column49']
        self.treeview13_dcols = [
            'column37',
            'column38',
            'column39',
            'column40',
            'column41',
            'column42',
            'column43',
            'column44',
            'column45',
            'column46',
            'column47',
            'column48',
            'column49']
        self.treeview13.configure(
            columns=self.treeview13_cols,
            displaycolumns=self.treeview13_dcols)
        self.treeview13.column(
            "column37",
            anchor="w",
            stretch=True,
            width=30,
            minwidth=20)
        self.treeview13.column(
            "column38",
            anchor="w",
            stretch=True,
            width=80,
            minwidth=20)
        self.treeview13.column(
            "column39",
            anchor="w",
            stretch=True,
            width=60,
            minwidth=20)
        self.treeview13.column(
            "column40",
            anchor="w",
            stretch=True,
            width=60,
            minwidth=20)
        self.treeview13.column(
            "column41",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview13.column(
            "column42",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview13.column(
            "column43",
            anchor="w",
            stretch=True,
            width=50,
            minwidth=20)
        self.treeview13.column(
            "column44",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview13.column(
            "column45",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview13.column(
            "column46",
            anchor="w",
            stretch=True,
            width=140,
            minwidth=20)
        self.treeview13.column(
            "column47",
            anchor="w",
            stretch=True,
            width=140,
            minwidth=20)
        self.treeview13.column(
            "column48",
            anchor="w",
            stretch=True,
            width=140,
            minwidth=20)
        self.treeview13.column(
            "column49",
            anchor="w",
            stretch=True,
            width=80,
            minwidth=20)
        self.treeview13.heading("column37", anchor="w", text='ID')
        self.treeview13.heading("column38", anchor="w", text='用户名')
        self.treeview13.heading("column39", anchor="w", text='货物类型')
        self.treeview13.heading("column40", anchor="w", text='快递公司')
        self.treeview13.heading("column41", anchor="w", text='单号')
        self.treeview13.heading("column42", anchor="w", text='物品信息')
        self.treeview13.heading("column43", anchor="w", text='状态')
        self.treeview13.heading("column44", anchor="w", text='联系号码')
        self.treeview13.heading("column45", anchor="w", text='备注')
        self.treeview13.heading("column46", anchor="w", text='添加时间')
        self.treeview13.heading("column47", anchor="w", text='入库时间')
        self.treeview13.heading("column48", anchor="w", text='出库时间')
        self.treeview13.heading("column49", anchor="w", text='箱号')
        self.treeview13.pack(fill="y", side="left")
        self.scrollbar8 = ttk.Scrollbar(self.frame38)
        self.scrollbar8.configure(orient="vertical")
        self.scrollbar8.pack(fill="y", side="left")
        self.frame38.pack(fill="both", side="left")
        self.frame39 = ttk.Frame(self.frame18)
        self.frame39.configure(height=200, relief="raised")
        self.frame40 = ttk.Frame(self.frame39)
        self.frame40.configure(height=200, width=200)
        self.label32 = ttk.Label(self.frame40)
        self.label32.configure(text='订单总数：')
        self.label32.pack(side="top")
        self.button8 = ttk.Button(self.frame40)
        self.button8.configure(text='刷新数据')
        self.button8.pack(fill="x", pady=5, side="top")
        self.button7 = ttk.Button(self.frame40)
        self.button7.configure(text='重置', width=7)
        self.button7.pack(expand=True, fill="both", pady=5, side="top")
        self.button15 = ttk.Button(self.frame40)
        self.button15.configure(text='添加订单')
        self.button15.pack(expand=True, fill="x", pady=20, side="top")
        self.frame40.pack(fill="x", side="top")
        self.frame41 = ttk.Frame(self.frame39)
        self.frame41.configure(height=200, width=200)
        self.frame7 = ttk.Frame(self.frame41)
        self.frame7.configure(height=200, width=200)
        self.label4 = ttk.Label(self.frame7)
        self.label4.configure(text='状态筛选：')
        self.label4.pack(side="top")
        self.frame7.pack(pady=10, side="top")
        self.frame8 = ttk.Frame(self.frame41)
        self.frame8.configure(height=200, width=200)
        self.button4 = ttk.Button(self.frame8)
        self.button4.configure(text='未收货', width=7)
        self.button4.pack(side="left")
        self.button5 = ttk.Button(self.frame8)
        self.button5.configure(text='已入库', width=7)
        self.button5.pack(padx=5, side="left")
        self.button6 = ttk.Button(self.frame8)
        self.button6.configure(text='已出库', width=7)
        self.button6.pack(padx=5, side="left")
        self.frame8.pack(side="top")
        self.frame41.pack(side="top")
        self.frame42 = ttk.Frame(self.frame39)
        self.frame42.configure(height=200, width=200)
        self.frame13 = ttk.Frame(self.frame42)
        self.frame13.configure(height=200, width=200)
        self.label5 = ttk.Label(self.frame13)
        self.label5.configure(text='多层级筛选：')
        self.label5.pack(side="top")
        self.frame13.pack(side="top")
        self.frame14 = ttk.Frame(self.frame42)
        self.frame14.configure(height=200, width=200)
        self.combobox1 = ttk.Combobox(self.frame14)
        self.combobox1.configure(width=8)
        self.combobox1.pack(side="left")
        self.entry14 = ttk.Entry(self.frame14)
        self.entry14.configure(width=15)
        self.entry14.pack(padx=5, side="left")
        self.button9 = ttk.Button(self.frame14)
        self.button9.configure(text='确认')
        self.button9.pack(side="top")
        self.frame14.pack(side="top")
        self.frame42.pack(pady=10, side="top")
        self.frame39.pack(expand=True, fill="both", side="left")
        self.frame18.pack(side="top")
        self.add(self.frame18, text='订单处理')
        self.frame78 = ttk.Frame(self)
        self.frame78.configure(height=200, relief="raised", width=200)
        self.frame79 = ttk.Frame(self.frame78)
        self.frame79.configure(height=200, relief="raised", width=750)
        self.frame81 = ttk.Frame(self.frame79)
        self.frame81.configure(height=200, width=200)
        self.label56 = ttk.Label(self.frame81)
        self.label56.configure(font="{yahei} 12 {}", text='箱号处理')
        self.label56.pack(side="top")
        self.frame90 = ttk.Frame(self.frame81)
        self.frame90.configure(height=200, width=200)
        self.combobox9 = ttk.Combobox(self.frame90)
        self.combobox9.pack(side="left")
        self.entry40 = ttk.Entry(self.frame90)
        self.entry40.pack(side="left")
        self.button25 = ttk.Button(self.frame90)
        self.button25.configure(text='筛选')
        self.button25.pack(side="left")
        self.button26 = ttk.Button(self.frame90)
        self.button26.configure(text='重置')
        self.button26.pack(side="left")
        self.frame90.pack(fill="x", pady=10, side="top")
        self.frame81.pack(expand=False, fill="x", side="top")
        self.frame82 = ttk.Frame(self.frame79)
        self.frame82.configure(height=200, width=200)
        self.label57 = ttk.Label(self.frame82)
        self.label57.configure(text='箱信息')
        self.label57.pack(side="top")
        self.frame83 = ttk.Frame(self.frame82)
        self.frame83.configure(height=200, width=200)
        self.treeview3 = ttk.Treeview(self.frame83)
        self.treeview3.configure(selectmode="extended", show="headings")
        self.treeview3_cols = [
            'column7',
            'column8',
            'column9',
            'column10',
            'column11',
            'column12']
        self.treeview3_dcols = [
            'column7',
            'column8',
            'column9',
            'column10',
            'column11',
            'column12']
        self.treeview3.configure(
            columns=self.treeview3_cols,
            displaycolumns=self.treeview3_dcols)
        self.treeview3.column(
            "column7",
            anchor="w",
            stretch=True,
            width=40,
            minwidth=20)
        self.treeview3.column(
            "column8",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview3.column(
            "column9",
            anchor="w",
            stretch=True,
            width=200,
            minwidth=20)
        self.treeview3.column(
            "column10",
            anchor="w",
            stretch=True,
            width=140,
            minwidth=20)
        self.treeview3.column(
            "column11",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview3.column(
            "column12",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview3.heading("column7", anchor="w", text='ID')
        self.treeview3.heading("column8", anchor="w", text='箱名称')
        self.treeview3.heading("column9", anchor="w", text='创建时间')
        self.treeview3.heading("column10", anchor="w", text='箱重')
        self.treeview3.heading("column11", anchor="w", text='状态')
        self.treeview3.heading("column12", anchor="w", text='出库时间')
        self.treeview3.pack(expand=True, fill="both", side="left")
        self.scrollbar1 = ttk.Scrollbar(self.frame83)
        self.scrollbar1.configure(orient="vertical")
        self.scrollbar1.pack(expand=True, fill="y", side="left")
        self.frame83.pack(side="top")
        self.label58 = ttk.Label(self.frame82)
        self.label58.configure(text='箱预览')
        self.label58.pack(pady=10, side="top")
        self.frame84 = ttk.Frame(self.frame82)
        self.frame84.configure(height=200, width=200)
        self.treeview4 = ttk.Treeview(self.frame84)
        self.treeview4.configure(selectmode="extended", show="headings")
        self.treeview4_cols = ['column13', 'column14', 'column15', 'column16']
        self.treeview4_dcols = ['column13', 'column14', 'column15', 'column16']
        self.treeview4.configure(
            columns=self.treeview4_cols,
            displaycolumns=self.treeview4_dcols)
        self.treeview4.column(
            "column13",
            anchor="w",
            stretch=True,
            width=120,
            minwidth=20)
        self.treeview4.column(
            "column14",
            anchor="w",
            stretch=True,
            width=200,
            minwidth=20)
        self.treeview4.column(
            "column15",
            anchor="w",
            stretch=True,
            width=200,
            minwidth=20)
        self.treeview4.column(
            "column16",
            anchor="w",
            stretch=True,
            width=200,
            minwidth=20)
        self.treeview4.heading("column13", anchor="w", text='ID')
        self.treeview4.heading("column14", anchor="w", text='箱名称')
        self.treeview4.heading("column15", anchor="w", text='单号')
        self.treeview4.heading("column16", anchor="w", text='添加时间')
        self.treeview4.pack(fill="both", side="left")
        self.scrollbar4 = ttk.Scrollbar(self.frame84)
        self.scrollbar4.configure(orient="vertical")
        self.scrollbar4.pack(expand=True, fill="y", side="top")
        self.frame84.pack(side="top")
        self.frame82.pack(side="top")
        self.frame85 = ttk.Frame(self.frame79)
        self.frame85.configure(height=200, width=200)
        self.button21 = ttk.Button(self.frame85)
        self.button21.configure(text='新增箱', width=50)
        self.button21.pack(pady=20, side="top")
        self.button22 = ttk.Button(self.frame85)
        self.button22.configure(text='刷新箱数据', width=50)
        self.button22.pack(side="top")
        self.frame85.pack(side="top")
        self.frame79.pack(expand=False, fill="both", side="left")
        self.frame79.pack_propagate(0)
        self.frame80 = ttk.Frame(self.frame78)
        self.frame80.configure(height=200, relief="raised", width=200)
        self.frame86 = ttk.Frame(self.frame80)
        self.frame86.configure(height=200, width=200)
        self.label59 = ttk.Label(self.frame86)
        self.label59.configure(font="{yahei} 12 {}", text='用户处理')
        self.label59.pack(expand=True, side="top")
        self.frame91 = ttk.Frame(self.frame86)
        self.frame91.configure(height=200, width=200)
        self.combobox10 = ttk.Combobox(self.frame91)
        self.combobox10.pack(side="left")
        self.entry41 = ttk.Entry(self.frame91)
        self.entry41.pack(side="left")
        self.button27 = ttk.Button(self.frame91)
        self.button27.configure(text='筛选')
        self.button27.pack(side="left")
        self.button28 = ttk.Button(self.frame91)
        self.button28.configure(text='重置')
        self.button28.pack(side="left")
        self.frame91.pack(fill="x", pady=10, side="top")
        self.frame86.pack(fill="x", side="top")
        self.frame87 = ttk.Frame(self.frame80)
        self.frame87.configure(height=200, width=200)
        self.label60 = ttk.Label(self.frame87)
        self.label60.configure(text='用户信息')
        self.label60.pack(side="top")
        self.frame88 = ttk.Frame(self.frame87)
        self.frame88.configure(height=200, width=200)
        self.treeview5 = ttk.Treeview(self.frame88)
        self.treeview5.configure(selectmode="extended", show="headings")
        self.treeview5_cols = [
            'column17',
            'column18',
            'column19',
            'column20',
            'column21',
            'column22',
            'column23',
            'column24']
        self.treeview5_dcols = [
            'column17',
            'column18',
            'column19',
            'column20',
            'column21',
            'column22',
            'column23',
            'column24']
        self.treeview5.configure(
            columns=self.treeview5_cols,
            displaycolumns=self.treeview5_dcols)
        self.treeview5.column(
            "column17",
            anchor="w",
            stretch=True,
            width=20,
            minwidth=20)
        self.treeview5.column(
            "column18",
            anchor="w",
            stretch=True,
            width=60,
            minwidth=20)
        self.treeview5.column(
            "column19",
            anchor="w",
            stretch=True,
            width=60,
            minwidth=20)
        self.treeview5.column(
            "column20",
            anchor="w",
            stretch=True,
            width=40,
            minwidth=20)
        self.treeview5.column(
            "column21",
            anchor="w",
            stretch=True,
            width=80,
            minwidth=20)
        self.treeview5.column(
            "column22",
            anchor="w",
            stretch=True,
            width=100,
            minwidth=20)
        self.treeview5.column(
            "column23",
            anchor="w",
            stretch=True,
            width=150,
            minwidth=20)
        self.treeview5.column(
            "column24",
            anchor="w",
            stretch=True,
            width=200,
            minwidth=20)
        self.treeview5.heading("column17", anchor="w", text='ID')
        self.treeview5.heading("column18", anchor="w", text='用户名')
        self.treeview5.heading("column19", anchor="w", text='密码')
        self.treeview5.heading("column20", anchor="w", text='积分')
        self.treeview5.heading("column21", anchor="w", text='用户类别')
        self.treeview5.heading("column22", anchor="w", text='找回信息')
        self.treeview5.heading("column23", anchor="w", text='创建时间')
        self.treeview5.heading("column24", anchor="w", text='微信OPENID')
        self.treeview5.pack(side="left")
        self.scrollbar5 = ttk.Scrollbar(self.frame88)
        self.scrollbar5.configure(orient="vertical")
        self.scrollbar5.pack(expand=True, fill="y", side="top")
        self.frame88.pack(side="top")
        self.frame87.pack(side="top")
        self.frame89 = ttk.Frame(self.frame80)
        self.frame89.configure(height=200, width=200)
        self.button23 = ttk.Button(self.frame89)
        self.button23.configure(text='新增用户', width=50)
        self.button23.pack(pady=20, side="top")
        self.button24 = ttk.Button(self.frame89)
        self.button24.configure(text='刷新用户信息', width=50)
        self.button24.pack(side="top")
        self.frame89.pack(side="top")
        self.frame80.pack(expand=True, fill="both", side="left")
        self.frame78.pack(expand=True, fill="both", side="top")
        self.add(self.frame78, text='箱和用户名')
        self.configure(height=700, width=1500)
        self.pack(side="top")
