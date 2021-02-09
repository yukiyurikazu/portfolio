import tkinter as tk
import pyautogui as ag
import pyperclip
import functools
from ColorClass import Color   #自作クラスのインポート


#カラーコード読み取り・反映関数
def colorGet():
    try:
        window.config(bg=txt1.get())
    except tk.TclError:
        error = 0
    finally:
        after = root.after(1000, colorGet)  #1秒後にcolorGet()を再読み込み
        

#カラー表示ラベル変更関数(カラーコードも変更)
def changeColor():
    global cc
    txt1.delete(0, tk.END)
    txt1.insert(tk.END, cc)
    try:
        window.config(bg=cc)
    except tk.TclError:
        error = 0


#ベースカラー読込み関数
def setColor(event, param):
    global cc
    cc = param
    changeColor()


#微調整トリガー関数
def setTrigger(event, params, paramr, paramg, paramb):
    global switch, r, g, b
    switch = params
    r = paramr
    g = paramg
    b = paramb
    adjustColor()


#微調整実行関数
def adjustColor():
    global switch, cc, r, g, b
    code = Color(txt1.get())        #自作のクラスColorのインスタンスを生成
    cc = code.adjustColor(r, g, b)  #Colorクラスのメソッドを使用
    changeColor()
    #トリガー変数switch==1の間0.05秒ごとにadjustColor()を再読み込み
    if switch == 1:
        root.after(50, adjustColor)


#コピー＆ペースト関数
def release_action(event):
    pyperclip.copy(event.widget["bg"])
    click_paste()


def click_paste():
    #マウスをドロップした場所のポジションを取得
    x, y = ag.position()
    #マウスをドロップした場所をクリックさせる
    ag.click(x, y, clicks=1)
    #テキストボックス内の全消去(コード入力時に使用する場合は要コメントアウト)
    ag.hotkey("ctrl", "a", "del")
    #カラーコードのペースト
    ag.hotkey("ctrl", "v")


#カラーコード格納用変数
cc = '#ffffff'            #初期値は白

#微調整関数ON/OFFトリガー変数
switch = 0                #関数持続トリガー
r = 0                     #赤変更トリガー
g = 0                     #緑変更トリガー
b = 0                     #青変更トリガー

#サイズ及び位置用変数
fw0 = 200                 #column=0のwidth変数
fw1 = 500                 #column=1のwidth変数
fw2 = 800 - (fw0 + fw1)   #column=2のwidth変数(rootサイズ変更時数値部分変更する)
fh0 = 70                  #row=0,1,2,4のheight変数
fh1 = 270                 #row=3のheight変数
#ラベルのheight値はフレームのheight値の14倍?
#ラベルのwidth値はフレームのwidth値の7倍?

bh = 2  #ベースカラーのheight変数

ww = 50                   #カラー表示用ラベルのwidth変数
wh = 17                   #カラー表示用ラベルのheight変数
wx = (fw1 - ww * 7) / 2   #カラー表示用、赤、白ラベルの位置座標変数(x軸)
wy = 10                   #カラー表示用、赤、緑、青ラベルの位置座標変数(y軸)

tx = (fw1 / 2) - (bh * 15)   #カラーコード表示ボックスの位置座標変数(x軸)
ty = 20                      #カラーコード表示ボックスの位置座標変数(y軸)
btx = (fw1 / 2) + (bh * 30)  #カラーコード送信ボタンの位置座標変数(x軸)
bty = 15                     #カラーコード送信ボタンの位置座標変数(y軸)

cx = (fw1 / 2) - (bh * 7)     #緑ラベルの位置座標変数(x軸)
ex = (wx + ww * 7) - (bh * 14)  #青、黒ラベルの位置座標変数(x軸)
sh = (wy + wh * 14) - (bh * 7)  #白、黒ラベルの位置座標変数(y軸)



#メインウィンドウ作成
root = tk.Tk()
root.geometry('820x600')
root.title('Color_selection')

#フレーム作成
base0_0 = tk.Frame(root, width=fw0, height=fh0)
base0_1 = tk.Frame(root, width=fw0, height=fh0)
base0_2 = tk.Frame(root, width=fw0, height=fh0)
base0_3 = tk.Frame(root, width=fw0, height=fh1)
base1_1 = tk.Frame(root, width=fw1, height=fh0, bd=1, relief="ridge", bg="#cccccc")
base1_3 = tk.Frame(root, width=fw1, height=fh1)
base1_4 = tk.Frame(root, width=fw1, height=fh0)
base1_5 = tk.Frame(root, width=fw1, height=fh0)
base2_4 = tk.Frame(root, width=fw2, height=fh0)


#フレーム配置
base0_0.grid(column=0, row=0)
base0_1.grid(column=0, row=1)
base0_2.grid(column=0, row=2)
base0_3.grid(column=0, row=3)
base1_1.grid(column=1, row=1)
base1_3.grid(column=1, row=3)
base1_4.grid(column=1, row=4)
base1_5.grid(column=1, row=5)
base2_4.grid(column=2, row=4)


#カラー表示用ラベル
window = tk.Label(base1_3, width=ww, height=wh, bd=1, relief="ridge", bg=cc)
window.place(x=wx, y=wy)
window.bind("<ButtonRelease>", release_action)


#カラーコード表示ボックス
txt1 = tk.Entry(base1_4, width=bh*5, bd=1, relief="ridge")
txt1.insert(0, cc)
txt1.place(x=tx, y=ty)


#カラーコード送信ボタン(カラーホルダーへ)
btn = tk.Button(base1_4, text="送信")
btn.place(x=btx, y=bty)


#ここからベースカラー
colors = ['#ffffff', '#000000', '#795548', '#ff0000',  #白、黒、茶、赤
          '#ff6f00', '#ffff00', '#76ff03', '#00ff00',  #橙、黄、黄緑、緑
          '#18ffff', '#0000ff', '#1a237e', '#6200ea']  #水色、青、紺、紫

bclist = []  #各ラベルを格納するリスト
bclp = 0     #for文用リスト位置変数

for i in colors:
    bclist.append(tk.Label(base1_1, width=bh*2, height=bh, bd=1, relief="ridge", bg=i))
    bclist[bclp].pack(side=tk.LEFT, padx=5, pady=10)
    bclist[bclp].bind("<Double-ButtonPress-1>", functools.partial(setColor, param=i))
    bclp += 1
#ここまでベースカラー


#微調整用ラベル作成(赤、緑、青、白、黒)
aka = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#ff0000")
midori = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#00ff00")
ao = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#0000ff")
siro = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#ffffff")
kuro = tk.Label(base1_3, width=bh*2, height=bh, bd=1, relief="ridge", bg="#000000")


#微調整用ラベル配置
aka.place(x=wx, y=wy)
midori.place(x=cx, y=wy)
ao.place(x=ex, y=wy)
siro.place(x=wx, y=sh)
kuro.place(x=ex, y=sh)


#微調整機能実装
aka.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=1, paramg=0, paramb=0))
aka.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=-1, paramg=0, paramb=0))
aka.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))
midori.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=0, paramg=1, paramb=0))
midori.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=0, paramg=-1, paramb=0))
midori.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))
ao.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=0, paramg=0, paramb=1))
ao.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=0, paramg=0, paramb=-1))
ao.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))
siro.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=1, paramg=1, paramb=1))
siro.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=-1, paramg=-1, paramb=-1))
siro.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))
kuro.bind("<ButtonPress-1>", functools.partial(setTrigger, params=1, paramr=-1, paramg=-1, paramb=-1))
kuro.bind("<ButtonPress-3>", functools.partial(setTrigger, params=1, paramr=1, paramg=1, paramb=1))
kuro.bind("<ButtonRelease>", functools.partial(setTrigger, params=0, paramr=0, paramg=0, paramb=0))


#colorGet()関数起動
colorGet()


root.mainloop()
