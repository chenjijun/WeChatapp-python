import json
import threading

from PIL import Image
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import Menu,ttk,messagebox,filedialog
import datetime
import requests
import ceshihoutai,topview


httpurl = 'x.x.x.x'
jieMian = ceshihoutai.HoutaiceshiWidget()
xiangxinxi = topview.xiangxinxi

comboxlist = ['ID', '用户名', '货物类型', '快递公司', '单号', '物品信息', '状态', '联系号码', '备注', '添加时间', '入库时间',
              '出库时间', '箱号']
alldingdan={}
allbox=[]
allboxinfo=[]
url = f"http://{httpurl}/api/getviewvalue"
statuschangeurl = f"http://{httpurl}/api/statuschange"
getallboxurl = f"http://{httpurl}/api/getallbox"
danhaotoboxurl = f"http://{httpurl}/api/danhaotobox"
changelisturl = f"http://{httpurl}/api/houtaichangelist"
adddingdanurl = f"http://{httpurl}/api/adddingdan"
deldingdanurl = f"http://{httpurl}/api/deldingdan"
headers = {
      "Accept": "application/json, text/javascript, */*; q=0.01",
      "Accept-Encoding": "gzip, deflate",
      "Accept-Language": "zh-CN,zh;q=0.9",
      "Connection": "keep-alive",
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "Authorization": "chenjijun123",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"
}

addheaders = {
      "Accept": "application/json, text/javascript, */*; q=0.01",
      "Accept-Encoding": "gzip, deflate",
      "Accept-Language": "zh-CN,zh;q=0.9",
      "Connection": "keep-alive",
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "Authorization": "chenjijun",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"
}


class SetBox(tk.Toplevel):
    def __init__(self, master=None, danhao='', boxlist=[], **kw):
        super(SetBox, self).__init__(master, **kw)
        self.danhao = danhao
        self.frame15 = ttk.Frame(self)
        self.frame15.configure(height=200, width=200)
        self.label6 = ttk.Label(self.frame15)
        self.label6.configure(state="normal", text='选择箱号')
        self.label6.pack(pady=10, side="top")
        self.label10 = ttk.Label(self.frame15)
        self.label10.configure(text='ID:')
        self.label10.pack(side="top")
        self.combobox2 = ttk.Combobox(self.frame15)
        self.combobox2.pack(pady=20, side="top")
        self.button10 = ttk.Button(self.frame15)
        self.button10.configure(text='确认')
        self.button10.pack(side="top")
        self.frame15.pack(side="top")
        self.frame15.pack_propagate(0)
        self.configure(height=200, width=200)

        self.label10.configure(text="单号:"+self.danhao)
        self.combobox2['values'] = boxlist

        self.button10.configure(command=self.danhaotobox)

    def danhaotobox(self):
        if self.combobox2.get():
            data = {'danhaotobox':{'danhao': self.danhao,'box':[self.combobox2.get()]}}
            print(data)
            response = requests.post(danhaotoboxurl, headers=headers, json=data, verify=False, timeout=5)
            res = response.json()
            if res['return'] == '添加成功':
                selected_item = jieMian.treeview13.focus()
                jieMian.treeview13.set(selected_item, 'column49', self.combobox2.get())
                self.destroy()
                messagebox.showinfo('成功','添加成功')

            else:
                messagebox.showerror('错误','添加失败')


class SetOrder(tk.Toplevel):
    def __init__(self, master=None,data=[],boxlist=[],selected_item='', tree='', **kw, ):
        super(SetOrder, self).__init__(master, **kw)

        self.frame16 = ttk.Frame(self)
        self.frame16.configure(height=600, width=300)
        self.frame43 = ttk.Frame(self.frame16)
        self.frame43.configure(height=200, width=200)
        self.label11 = ttk.Label(self.frame43)
        self.label11.configure(text='详细信息：')
        self.label11.pack(side="top")
        self.frame43.pack(side="top")
        self.frame44 = ttk.Frame(self.frame16)
        self.frame44.configure(height=200, width=200)
        self.frame45 = ttk.Frame(self.frame44)
        self.frame45.configure(height=200, width=200)
        self.frame46 = ttk.Frame(self.frame45)
        self.frame46.configure(height=200, width=200)
        self.label12 = ttk.Label(self.frame46)
        self.label12.configure(text='ID')
        self.label12.pack(side="left")
        self.entry17 = ttk.Entry(self.frame46)
        self.entry17.pack(side="right")
        self.frame46.pack(ipady=5, side="top")
        self.frame47 = ttk.Frame(self.frame45)
        self.frame47.configure(height=200, width=200)
        self.label13 = ttk.Label(self.frame47)
        self.label13.configure(text='用户名')
        self.label13.pack(side="left")
        self.entry18 = ttk.Entry(self.frame47)
        self.entry18.pack(side="top")
        self.frame47.pack(ipady=5, side="top")
        self.frame48 = ttk.Frame(self.frame45)
        self.frame48.configure(height=200, width=200)
        self.label14 = ttk.Label(self.frame48)
        self.label14.configure(text='类型')
        self.label14.pack(side="left")
        self.combobox3 = ttk.Combobox(self.frame48)
        self.combobox3.configure(values=['普通货','敏感货','书籍'])
        self.combobox3.pack(side="left")
        self.frame48.pack(ipady=5, side="top")
        self.frame49 = ttk.Frame(self.frame45)
        self.frame49.configure(height=200, width=200)
        self.label15 = ttk.Label(self.frame49)
        self.label15.configure(text='快递公司')
        self.label15.pack(side="left")
        self.entry20 = ttk.Entry(self.frame49)
        self.entry20.pack(side="top")
        self.frame49.pack(ipady=5, side="top")
        self.frame50 = ttk.Frame(self.frame45)
        self.frame50.configure(height=200, width=200)
        self.label16 = ttk.Label(self.frame50)
        self.label16.configure(text='快递单号')
        self.label16.pack(side="left")
        self.entry21 = ttk.Entry(self.frame50)
        self.entry21.pack(side="top")
        self.frame50.pack(ipady=5, side="top")
        self.frame51 = ttk.Frame(self.frame45)
        self.frame51.configure(height=200, width=200)
        self.label34 = ttk.Label(self.frame51)
        self.label34.configure(text='物品信息')
        self.label34.pack(side="left")
        self.entry22 = ttk.Entry(self.frame51)
        self.entry22.pack(side="top")
        self.frame51.pack(ipady=5, side="top")
        self.frame52 = ttk.Frame(self.frame45)
        self.frame52.configure(height=200, width=200)
        self.label35 = ttk.Label(self.frame52)
        self.label35.configure(text='状态')
        self.label35.pack(side="left")
        self.combobox4 = ttk.Combobox(self.frame52)
        self.combobox4.configure(values=['未收货','已入库','已出库'])
        self.combobox4.pack(side="left")
        self.frame52.pack(ipady=5, side="top")
        self.frame53 = ttk.Frame(self.frame45)
        self.frame53.configure(height=200, width=200)
        self.label36 = ttk.Label(self.frame53)
        self.label36.configure(text='联系号码')
        self.label36.pack(side="left")
        self.entry24 = ttk.Entry(self.frame53)
        self.entry24.pack(side="top")
        self.frame53.pack(ipady=5, side="top")
        self.frame54 = ttk.Frame(self.frame45)
        self.frame54.configure(height=200, width=200)
        self.label37 = ttk.Label(self.frame54)
        self.label37.configure(text='备注')
        self.label37.pack(side="left")
        self.entry25 = ttk.Entry(self.frame54)
        self.entry25.pack(side="top")
        self.frame54.pack(ipady=5, side="top")
        self.frame55 = ttk.Frame(self.frame45)
        self.frame55.configure(height=200, width=200)
        self.label38 = ttk.Label(self.frame55)
        self.label38.configure(text='添加时间')
        self.label38.pack(side="left")
        self.entry26 = ttk.Entry(self.frame55)
        self.entry26.pack(side="left")
        self.button12 = ttk.Button(self.frame55)
        self.button12.configure(text='当前时间')
        self.button12.pack(side="left")
        self.frame55.pack(ipady=5, side="top")
        self.frame56 = ttk.Frame(self.frame45)
        self.frame56.configure(height=200, width=200)
        self.label39 = ttk.Label(self.frame56)
        self.label39.configure(text='入库时间')
        self.label39.pack(side="left")
        self.entry27 = ttk.Entry(self.frame56)
        self.entry27.pack(side="left")
        self.button13 = ttk.Button(self.frame56)
        self.button13.configure(text='当前时间')
        self.button13.pack(side="left")
        self.frame56.pack(ipady=5, side="top")
        self.frame57 = ttk.Frame(self.frame45)
        self.frame57.configure(height=200, width=200)
        self.label40 = ttk.Label(self.frame57)
        self.label40.configure(text='出库时间')
        self.label40.pack(side="left")
        self.entry28 = ttk.Entry(self.frame57)
        self.entry28.pack(side="left")
        self.button14 = ttk.Button(self.frame57)
        self.button14.configure(text='当前时间')
        self.button14.pack(side="left")
        self.frame57.pack(ipady=5, side="top")
        self.frame58 = ttk.Frame(self.frame45)
        self.frame58.configure(height=200, width=200)
        self.label41 = ttk.Label(self.frame58)
        self.label41.configure(text='箱号')
        self.label41.pack(side="left")
        self.combobox5 = ttk.Combobox(self.frame58)
        self.combobox5.pack(side="left")
        self.frame58.pack(ipady=5, side="top")
        self.frame45.pack(side="top")
        self.frame44.pack(side="top")
        self.button11 = ttk.Button(self.frame16)
        self.button11.configure(text='确认')
        self.button11.pack(pady=20, side="top")
        self.frame16.pack(side="top")
        self.frame16.pack_propagate(0)
        self.configure(height=200, relief="raised", width=200)

        self.select_item = selected_item
        self.tree = tree
        self.alldata = data
        self.allbox = ['None']
        for i in boxlist:
            self.allbox.append(i[0])
        print(self.allbox)
        self.entry17.insert('0', data[0])
        self.entry18.insert('0', data[1])
        self.combobox3.set(data[2])
        self.entry20.insert('0', data[3])
        self.entry21.insert('0', data[4])
        self.entry22.insert('0', data[5])
        self.combobox4.set(data[6])
        self.entry24.insert('0', data[7])
        self.entry25.insert('0', data[8])
        self.entry26.insert('0', data[9])
        self.entry27.insert('0', data[10])
        self.entry28.insert('0', data[11])
        self.combobox5.config(values=self.allbox)
        self.combobox5.set(data[12])


        self.entry17.config(state='disabled')
        self.entry18.config(state='disabled')

        self.button11.configure(command=self.submit)
        self.button12.configure(command=lambda i='1': self.changetime(i))
        self.button13.configure(command=lambda i='2': self.changetime(i))
        self.button14.configure(command=lambda i='3': self.changetime(i))
    def changetime(self,i):
        nowtime = str(datetime.datetime.now().replace(microsecond=0))
        if i == '1':
            self.entry26.delete(0,'end')
            self.entry26.insert(0,nowtime)
        if i == '2':
            self.entry27.delete(0,'end')
            self.entry27.insert(0,nowtime)
        if i == '3':
            self.entry28.delete(0,'end')
            self.entry28.insert(0,nowtime)
    def submit(self):
        afterchange = [self.entry17.get(),self.entry18.get(),self.combobox3.get(),self.entry20.get(),
                       self.entry21.get(),self.entry22.get(),self.combobox4.get(),self.entry24.get(),
                       self.entry25.get(),self.entry26.get(),self.entry27.get(),self.entry28.get(),
                       self.combobox5.get()]
        if afterchange == list(self.alldata):
            messagebox.showerror('错误','数据相同，未修改',parent=self)
        else:
            data={'houtairequest':{'list':afterchange}}
            response = requests.post(changelisturl, headers=headers, json=data, verify=False, timeout=5)
            res = response.json()


            if res['return'] == '修改成功':
                self.tree.item(self.select_item,values=afterchange)
                messagebox.showinfo('成功','修改成功')
            else:
                messagebox.showerror('错误','修改失败')


class adddingdan(tk.Toplevel):
    def __init__(self, master=None, **kw):
        super(adddingdan, self).__init__(master, **kw)
        self.frame61 = ttk.Frame(self)
        self.frame61.configure(height=400, width=300)
        self.frame62 = ttk.Frame(self.frame61)
        self.frame62.configure(height=200, width=200)
        self.label42 = ttk.Label(self.frame62)
        self.label42.configure(text='提交订单：')
        self.label42.pack(ipady=20, side="top")
        self.frame62.pack(side="top")
        self.frame63 = ttk.Frame(self.frame61)
        self.frame63.configure(height=200, width=200)
        self.frame64 = ttk.Frame(self.frame63)
        self.frame64.configure(height=200, width=200)
        self.frame66 = ttk.Frame(self.frame64)
        self.frame66.configure(height=200, width=200)
        self.label44 = ttk.Label(self.frame66)
        self.label44.configure(text='用户名')
        self.label44.pack(side="left")
        self.entry31 = ttk.Entry(self.frame66)
        self.entry31.pack(side="top")
        self.frame66.pack(side="top")
        self.frame67 = ttk.Frame(self.frame64)
        self.frame67.configure(height=200, width=200)
        self.label45 = ttk.Label(self.frame67)
        self.label45.configure(text='类型')
        self.label45.pack(side="left")
        self.combobox6 = ttk.Combobox(self.frame67)
        self.combobox6.configure(values=['普通货','敏感货','书籍'])
        self.combobox6.pack(side="left")
        self.frame67.pack(ipady=5, side="top")
        self.frame68 = ttk.Frame(self.frame64)
        self.frame68.configure(height=200, width=200)
        self.label46 = ttk.Label(self.frame68)
        self.label46.configure(text='快递公司')
        self.label46.pack(side="left")
        self.entry32 = ttk.Entry(self.frame68)
        self.entry32.pack(side="top")
        self.frame68.pack(ipady=5, side="top")
        self.frame69 = ttk.Frame(self.frame64)
        self.frame69.configure(height=200, width=200)
        self.label47 = ttk.Label(self.frame69)
        self.label47.configure(text='快递单号')
        self.label47.pack(side="left")
        self.entry33 = ttk.Entry(self.frame69)
        self.entry33.pack(side="left")
        self.button20 = ttk.Button(self.frame69)
        self.button20.configure(text='扫描图片')
        self.button20.pack(side="left")
        self.frame69.pack(ipady=5, side="top")
        self.frame70 = ttk.Frame(self.frame64)
        self.frame70.configure(height=200, width=200)
        self.label48 = ttk.Label(self.frame70)
        self.label48.configure(text='物品信息')
        self.label48.pack(side="left")
        self.entry34 = ttk.Entry(self.frame70)
        self.entry34.pack(side="top")
        self.frame70.pack(ipady=5, side="top")
        self.frame72 = ttk.Frame(self.frame64)
        self.frame72.configure(height=200, width=200)
        self.label50 = ttk.Label(self.frame72)
        self.label50.configure(text='联系号码')
        self.label50.pack(side="left")
        self.entry35 = ttk.Entry(self.frame72)
        self.entry35.pack(side="top")
        self.frame72.pack(ipady=5, side="top")
        self.frame73 = ttk.Frame(self.frame64)
        self.frame73.configure(height=200, width=200)
        self.label51 = ttk.Label(self.frame73)
        self.label51.configure(text='备注')
        self.label51.pack(side="left")
        self.entry36 = ttk.Entry(self.frame73)
        self.entry36.pack(side="top")
        self.frame73.pack(ipady=5, side="top")
        self.frame64.pack(side="top")
        self.frame63.pack(side="top")
        self.button19 = ttk.Button(self.frame61)
        self.button19.configure(text='确认')
        self.button19.pack(pady=20, side="top")
        self.frame61.pack(side="top")
        self.frame61.pack_propagate(0)
        self.configure(height=200, relief="raised", width=200)


        def checktxm(self):
            file_path = filedialog.askopenfilename(title="选择图片文件",
                                                   filetypes=(("Image files", "*.jpg;*.png"), ("all files", "*.*")),
                                                   parent=self)

            if file_path:
                # 读取并解码图片中的条形码或二维码
                image = Image.open(file_path)
                decoded_objects = decode(image)

                if decoded_objects:
                    danhao = decoded_objects[0].data.decode('utf-8')
                    print(danhao)
                    self.entry33.delete(0,'end')
                    self.entry33.insert(0,danhao)



        def submit(self):
            self.requestdata = {'user': self.entry31.get(), 'leixing': self.combobox6.get(), 'kdgs': self.entry32.get(),
                                'danhao': self.entry33.get(), 'lxhm': self.entry34.get(), 'wpxx': self.entry35.get(),
                                'beizhu': self.entry36.get()}
            yesorno = messagebox.askyesno('确认', '确认提交订单？',parent=self)
            if yesorno:
                try:
                    respone = requests.post(adddingdanurl, headers=addheaders, json=self.requestdata, verify=False, timeout=5)
                    res = respone.json()
                    if res['return'] == '添加成功':
                        jieMian.treeview13.insert('',0,values=list(res['values'][0]))
                        messagebox.showinfo('成功', '添加成功')
                    elif res['return'] == '用户名不存在':
                        messagebox.showerror('错误', '用户名不存在')
                    else:
                        messagebox.showerror('错误', '添加失败')
                except Exception as e:
                    messagebox.showerror('错误', f'服务器连接错误{e}')


        self.button19.configure(command=lambda: submit(self))
        self.button20.configure(command=lambda: checktxm(self))




def viewboxvalue():
    for i in allbox:
        print(i)
        jieMian.treeview4.insert('',0,values=i)
    for i in allboxinfo:
        print(i)
        jieMian.treeview3.insert('',0,values=i)



def plot_bar_chart():
    global alldingdan
    global allbox
    global allboxinfo

    data = {'houtairequest': {'request': 'historydingdan'}}
    try:
        response = requests.post(url, headers=headers, json=data, verify=False,timeout=5)
        alldingdan = response.json()
        print(222,alldingdan)
        print(1)
        allbox = alldingdan['allbox']
        allboxinfo = alldingdan['boxinfo']
        order_by_day()


    except Exception as e:
        messagebox.showerror('错误', f'服务器连接错误{e}')

def zhuyethread():
    if jieMian.label33['text'] == '运行中':
        messagebox.showerror('错误','获取中，请稍等！！！')
    else:
        t = threading.Thread(target=plot_bar_chart)
        t.start()

def clear_widgets(*args):
    for widget in args:
        if isinstance(widget, tk.Canvas):
            for child in widget.winfo_children():
                child.destroy()
        if isinstance(widget, tk.ttk.Treeview):
            widget.delete(*widget.get_children())


def order_by_day():
    jieMian.label33.configure(text='运行中')
    canvas = jieMian.canvas1
    secanvas = jieMian.canvas3
    threecanvas = jieMian.canvas7

    clear_widgets(canvas, secanvas, threecanvas, jieMian.treeview1, jieMian.treeview2, jieMian.treeview12,
                  jieMian.treeview13,jieMian.treeview3,jieMian.treeview4)

    viewboxvalue()
    today = datetime.date.today()
    date_labels = [str(today - datetime.timedelta(days=i)) for i in range(5)]
    date_dd = {label: [] for label in date_labels}
    date_rk = {label: [] for label in date_labels}
    date_ck = {label: [] for label in date_labels}

    for i in alldingdan['values']:
        jieMian.treeview13.insert('', 0, values=i)
        for label in date_labels:
            if label in i[9]:
                date_dd[label].append(i)
                if '已入库' in i[6]:
                    date_rk[label].append(i)
                if '已出库' in i[6]:
                    date_ck[label].append(i)

    jieMian.label32.configure(text='订单总量：{}个'.format(len(alldingdan['values'])))

    data_dd = [len(date_dd[label]) for label in date_labels]
    fig = plt.Figure(figsize=(5, 5), dpi=80)
    ax = fig.add_subplot(111)
    bars = ax.bar(date_labels, data_dd)
    for bar, value in zip(bars, data_dd):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), value, ha='center', va='bottom')

    canvasone = FigureCanvasTkAgg(fig, master=canvas)
    canvasone.draw()
    canvasone.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvasone.get_tk_widget().configure(height=300, relief="raised", width=350)


    fig = plt.Figure(figsize=(5, 5), dpi=80)
    ax = fig.add_subplot(111)

    data_rk = [len(date_rk[label]) for label in date_labels]
    bars = ax.bar(date_labels, data_rk)
    for bar, value in zip(bars, data_rk):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), value, ha='center', va='bottom')

    canvastwo = FigureCanvasTkAgg(fig, master=secanvas)
    canvastwo.draw()
    canvastwo.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvastwo.get_tk_widget().configure(height=300, relief="raised", width=350)


    fig = plt.Figure(figsize=(5, 5), dpi=80)
    ax = fig.add_subplot(111)

    data_ck = [len(date_ck[label]) for label in date_labels]

    bars = ax.bar(date_labels, data_ck)
    for bar, value in zip(bars, data_ck):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), value, ha='center', va='bottom')

    threecanvas = FigureCanvasTkAgg(fig, master=threecanvas)
    threecanvas.draw()
    threecanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    threecanvas.get_tk_widget().configure(height=300, relief="raised", width=350)

    jieMian.label1.configure(text='近5天提交的订单总量：{}个'.format(sum(data_dd)))
    jieMian.label3.configure(text='近5天入库的订单总量：{}个'.format(sum(data_rk)))
    jieMian.label8.configure(text='近5天出库的订单总量：{}个'.format(sum(data_ck)))



    for label in date_labels:
        for i in date_rk[label]:
            jieMian.treeview2.insert('', 0, values=[i[1], i[4], i[10]])

        for i in date_dd[label]:
            jieMian.treeview1.insert('', 0, values=[i[1], i[4], i[9]])

        for i in date_ck[label]:
            jieMian.treeview12.insert('', 0, values=[i[1], i[4], i[11]])

    treeviewsort()

    jieMian.label33.configure(text='获取成功')
    messagebox.showinfo('成功','获取数据成功')


def order_by_month():
    def monthjisuan(year, month):
        if month == 1:
            return year - 1, 12
        else:
            return year, month - 1

    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month

    labels = []
    for i in range(5):
        labels.append(f"{current_year}-{'{:02d}'.format(current_month)}")
        current_year, current_month = monthjisuan(current_year, current_month)
    print(labels)

    canvas = jieMian.canvas1

    date_labels = labels
    date_dd = {label: [] for label in date_labels}
    date_rk = {label: [] for label in date_labels}
    date_ck = {label: [] for label in date_labels}

    for i in alldingdan['values']:

        for label in date_labels:
            if label in i[9]:
                date_dd[label].append(i)
                if '已入库' in i[6]:
                    date_rk[label].append(i)
                if '已出库' in i[6]:
                    date_ck[label].append(i)

    data_dd = [len(date_dd[label]) for label in date_labels]

    fig = plt.Figure(figsize=(5, 5), dpi=80)
    ax = fig.add_subplot(111)
    bars = ax.bar(date_labels, data_dd)
    for bar, value in zip(bars, data_dd):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), value, ha='center', va='bottom')

    for widget in canvas.winfo_children():
        widget.destroy()

    canvasone = FigureCanvasTkAgg(fig, master=canvas)
    canvasone.draw()
    canvasone.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvasone.get_tk_widget().configure(height=300, relief="raised", width=350)

    secanvas = jieMian.canvas3
    for widget in secanvas.winfo_children():
        widget.destroy()
    fig = plt.Figure(figsize=(5, 5), dpi=80)
    ax = fig.add_subplot(111)

    data_rk = [len(date_rk[label]) for label in date_labels]

    bars = ax.bar(date_labels, data_rk)
    for bar, value in zip(bars, data_rk):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), value, ha='center', va='bottom')

    canvastwo = FigureCanvasTkAgg(fig, master=secanvas)
    canvastwo.draw()
    canvastwo.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvastwo.get_tk_widget().configure(height=300, relief="raised", width=350)

    threecanvas = jieMian.canvas7
    for widget in threecanvas.winfo_children():
        widget.destroy()
    fig = plt.Figure(figsize=(5, 5), dpi=80)
    ax = fig.add_subplot(111)

    data_ck = [len(date_ck[label]) for label in date_labels]

    bars = ax.bar(date_labels, data_ck)
    for bar, value in zip(bars, data_ck):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), value, ha='center', va='bottom')

    threecanvas = FigureCanvasTkAgg(fig, master=threecanvas)
    threecanvas.draw()
    threecanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    threecanvas.get_tk_widget().configure(height=300, relief="raised", width=350)

    jieMian.label1.configure(text='近5天提交的订单总量：{}个'.format(sum(data_dd)))
    jieMian.label3.configure(text='近5天入库的订单总量：{}个'.format(sum(data_rk)))
    jieMian.label8.configure(text='近5天出库的订单总量：{}个'.format(sum(data_ck)))

    jieMian.treeview1.delete(*jieMian.treeview1.get_children())
    jieMian.treeview2.delete(*jieMian.treeview2.get_children())
    jieMian.treeview12.delete(*jieMian.treeview12.get_children())

    for label in date_labels:
        for i in date_rk[label]:
            jieMian.treeview2.insert('', 0, values=[i[1], i[4], i[10]])

        for i in date_dd[label]:
            jieMian.treeview1.insert('', 0, values=[i[1], i[4], i[9]])

        for i in date_ck[label]:
            jieMian.treeview12.insert('', 0, values=[i[1], i[4], i[11]])


def popup(event):
    # 获取事件来源的Treeview控件
    tree = event.widget
    # 获取鼠标在Treeview中的位置
    x, y, col = event.x, event.y, tree.identify_column(event.x)
    # 获取当前位置对应的项ID
    item_id = tree.identify_row(y)
    # 检查是否点击在有效的项上
    if item_id:
        # 高亮显示被点击的项
        tree.selection_set(item_id)
        tree.focus(item_id)
        # 创建右键菜单
        popup_menu = Menu(tree, tearoff=0)
        popup_menu.add_command(label="详细信息", command=lambda: show_selected_content(tree))
        # 显示菜单
        popup_menu.tk_popup(event.x_root, event.y_root)
        # 如果没有点击在项上，则清除任何已存在的高亮，并不显示菜单
    else:
        tree.selection_clear()


def show_selected_content(tree):
    # 获取当前选中的项，并显示其文本内容
    selected_item = tree.focus()
    if selected_item:
        value = tree.item(selected_item, "values")
        i = next(j for j in alldingdan['values'] if value[1] == j[4])
        print(i)
        xiangxinxi(data=i)


def dingdanpopup(event):
    # 获取事件来源的Treeview控件
    tree = event.widget
    # 获取鼠标在Treeview中的位置
    x, y, col = event.x, event.y, tree.identify_column(event.x)
    # 获取当前位置对应的项ID
    item_id = tree.identify_row(y)
    # 检查是否点击在有效的项上
    if item_id:
        # 高亮显示被点击的项
        tree.selection_set(item_id)
        tree.focus(item_id)
        # 创建右键菜单
        popup_menu = Menu(tree, tearoff=0)
        popup_menu.add_command(label="修改", command=lambda: change_allvalue(tree))
        popup_menu.add_command(label="修改状态->未收货", command=lambda i = '未收货': change_content(tree,i))
        popup_menu.add_command(label="修改状态->已入库", command=lambda i = '已入库': change_content(tree,i))
        popup_menu.add_command(label="修改状态->已出库", command=lambda i = '已出库': change_content(tree,i))
        popup_menu.add_command(label="修改箱号", command=lambda: change_box(tree))
        popup_menu.add_command(label="删除订单", command=lambda: del_order(tree))
        # 显示菜单
        popup_menu.tk_popup(event.x_root, event.y_root)
        # 如果没有点击在项上，则清除任何已存在的高亮，并不显示菜单
    else:
        tree.selection_clear()


def del_order(tree):
    queren =  messagebox.askyesno(title='请确认',message='是否确认删除')
    # 获取当前选中的项，并显示其文本内容
    if queren:
        selected_item = tree.focus()

        if selected_item:
            value = tree.item(selected_item, "values")
            if value[12] == 'NONE' or value[12] == 'None' or not value[12]:
                yesorno = 'no'
            else:
                yesorno = value[4]
            data = {'houtairequest': {'id': value[0],'delbox':yesorno}}
            try:
                response = requests.post(url=deldingdanurl,headers=headers,json=data,verify=False,timeout=5)
                res = response.json()
                if res['return'] == '删除成功':
                    tree.delete(selected_item)
                    messagebox.showinfo('成功','删除成功')
                else:
                    messagebox.showerror('错误',f'删除失败{res["return"]}')

            except Exception as e:
                messagebox.showerror('错误', '删除失败')

def change_content(tree,i):
    queren =  messagebox.askyesno(title='请确认',message=f'是否确认修改为{i}')
    # 获取当前选中的项，并显示其文本内容
    if queren:
        selected_item = tree.focus()
        if selected_item:
            value = tree.item(selected_item, "values")
            data = {'houtairequest': {'id': value[0], 'status': i}}
            try:
                response = requests.post(statuschangeurl, headers=headers, json=data, verify=False,timeout=5)
                res = response.json()
                print(res)
                if res['return'] == '修改成功':
                    tree.set(selected_item, 'column43', i)
                messagebox.showinfo('成功','修改成功')
            except Exception as e:
                messagebox.showerror('错误',f'修改失败{e}')
def getboxfun():
    try:
        data = {'requestvalue': 'all'}
        response = requests.post(getallboxurl, headers=headers, json=data, verify=False, timeout=5)
        res = response.json()
        print(res)
        return res
    except Exception as e:
        return e

def change_box(tree):
    selected_item = tree.focus()
    if selected_item:
        res = getboxfun()
        if res['return'] == '查询成功':
            value = tree.item(selected_item, "values")
            danhao= value[4]
            SetBox(danhao=danhao, boxlist= res['boxs'])
        else:
            messagebox.showerror('错误','获取箱号列表失败')

def change_allvalue(tree):
    selected_item = tree.focus()
    print(tree,selected_item)
    if selected_item:
        value = tree.item(selected_item, "values")
        res = getboxfun()
        if res['return'] == '查询成功':
            SetOrder(data=value, boxlist=list(res['boxs']), selected_item= selected_item,
                      tree=tree)
        else:
            messagebox.showerror('错误','获取信息失败')

def sort_treeview(col, descending, j):
    if j == 'tone':
        view = jieMian.treeview1
    elif j == 'ttwo':
        view = jieMian.treeview2
    elif j == 'tthree':
        view = jieMian.treeview12
    elif j == 'tfour':
        view = jieMian.treeview13
    elif j == 'tfive':
        view = jieMian.treeview3
    elif j == 'tsix':
        view = jieMian.treeview4
    elif j == 'tseven':
        view = jieMian.treeview5
    data = [(view.set(child, col), child) for child in view.get_children('')]
    data.sort(reverse=descending)
    for i, item in enumerate(data):
        view.move(item[1], '', i)


def on_header_click(col, j):
    descending = not jieMian.sort_order.get()
    sort_treeview(col, descending, j)
    jieMian.sort_order.set(not jieMian.sort_order.get())


def treeviewsort():
    jieMian.sort_order = tk.BooleanVar()
    jieMian.sort_order.set(False)

    for i in ['column1', 'column2', 'column3']:
        j = 'tone'
        jieMian.treeview1.heading(i, command=lambda c=i, j=j: on_header_click(c, j))

    for i in ['column4', 'column5', 'column6']:
        j = 'ttwo'
        jieMian.treeview2.heading(i, command=lambda c=i, j=j: on_header_click(c, j))

    for i in ['column34', 'column35', 'column36']:
        j = 'tthree'
        jieMian.treeview12.heading(i, command=lambda c=i, j=j: on_header_click(c, j))

    for i in ['column37', 'column38', 'column39', 'column40', 'column41', 'column42', 'column43'
              , 'column44', 'column45', 'column46', 'column47', 'column48', 'column49']:
        j = 'tfour'
        jieMian.treeview13.heading(i, command=lambda c=i, j=j: on_header_click(c, j))

    for i in ['column7', 'column8', 'column9', 'column10', 'column11', 'column12']:
        j = 'tfive'
        jieMian.treeview3.heading(i, command=lambda c=i, j=j: on_header_click(c, j))
    for i in ['column13', 'column14', 'column15', 'column16']:
        j = 'tsix'
        jieMian.treeview4.heading(i, command=lambda c=i, j=j: on_header_click(c, j))
    for i in ['column17', 'column18', 'column19', 'column20', 'column21', 'column22', 'column23', 'column24']:
        j = 'tseven'
        jieMian.treeview5.heading(i, command=lambda c=i, j=j: on_header_click(c, j))

def huowuzt(o):
    n = 0
    jieMian.treeview13.delete(*jieMian.treeview13.get_children())
    for i in alldingdan['values']:
        if i[6] == o:
            n+=1
            jieMian.treeview13.insert('',0,values=i)
    jieMian.label32.configure(text=f'订单总数:{n}')


def reset_dd_treeview():
    n = 0
    jieMian.treeview13.delete(*jieMian.treeview13.get_children())
    for i in alldingdan['values']:
        n += 1
        jieMian.treeview13.insert('', 0, values=i)
    jieMian.label32.configure(text=f'订单总数:{n}')


def filter_more():
    mohuvalue = str(jieMian.entry14.get())
    mohuindex = jieMian.combobox1.current()
    dingdan_shuju = jieMian.treeview13.get_children()
    content = []
    for item in dingdan_shuju:
        content.append(jieMian.treeview13.item(item, "values"))
    if mohuindex != -1 and mohuvalue:
        jieMian.treeview13.delete(*jieMian.treeview13.get_children())
        for i in content:
            if mohuvalue in i[mohuindex]:
                jieMian.treeview13.insert('',0,values=i)

    else:
        messagebox.showerror('错误','请输入')





zhuyethread()


jieMian.combobox1['values'] = comboxlist
jieMian.treeview1.bind("<Button-3>",popup)
jieMian.treeview2.bind("<Button-3>",popup)
jieMian.treeview12.bind("<Button-3>",popup)
jieMian.treeview13.bind("<Button-3>",dingdanpopup)

jieMian.button1.configure(command=zhuyethread)
jieMian.button8.configure(command=zhuyethread)
jieMian.button22.configure(command=zhuyethread)
jieMian.button2.configure(command=order_by_day)
jieMian.button3.configure(command=order_by_month)

jieMian.button4.configure(command=lambda c = '未收货':huowuzt(c))
jieMian.button5.configure(command=lambda c = '已入库':huowuzt(c))
jieMian.button6.configure(command=lambda c = '已出库':huowuzt(c))
jieMian.button7.configure(command=reset_dd_treeview)
jieMian.button9.configure(command=filter_more)
jieMian.button15.configure(command=adddingdan)


jieMian.scrollbar2.config(command=jieMian.treeview1.yview)
jieMian.treeview1.configure(yscrollcommand=jieMian.scrollbar2.set)
jieMian.scrollbar3.config(command=jieMian.treeview2.yview)
jieMian.treeview2.configure(yscrollcommand=jieMian.scrollbar3.set)
jieMian.scrollbar7.config(command=jieMian.treeview12.yview)
jieMian.treeview12.configure(yscrollcommand=jieMian.scrollbar7.set)
jieMian.scrollbar8.config(command=jieMian.treeview13.yview)
jieMian.treeview13.configure(yscrollcommand=jieMian.scrollbar8.set)
jieMian.scrollbar4.config(command=jieMian.treeview4.yview)
jieMian.treeview4.configure(yscrollcommand=jieMian.scrollbar4.set)
jieMian.scrollbar5.config(command=jieMian.treeview5.yview)
jieMian.treeview5.configure(yscrollcommand=jieMian.scrollbar5.set)
jieMian.scrollbar1.config(command=jieMian.treeview3.yview)
jieMian.treeview3.configure(yscrollcommand=jieMian.scrollbar1.set)
jieMian.mainloop()

