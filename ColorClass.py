from tkinter import messagebox

class Color():
    def __init__(self, code):
        try:
            self.code = code
            self.red = code[1:3]
            self.green = code[3:5]
            self.blue = code[5:]
            self.R = int(self.red, 16)
            self.G = int(self.green, 16)
            self.B = int(self.blue, 16)
        except ValueError:
            messagebox.showerror("エラー", "カラーコードには「# + 6桁の16進数の数値」を入力してください。")
            

    def adjustColor(self, r, g, b):
        if r == 1:
            if self.R < 255:
                self.R += 1
            if self.R < 16:
                self.red = "0" + str(hex(self.R).replace('0x', ''))
            else:
                self.red = str(hex(self.R).replace('0x', ''))
        elif r == -1:
            if self.R > 0:
                self.R -= 1
            if self.R < 16:
                self.red = "0" + str(hex(self.R).replace('0x', ''))
            else:
                self.red = str(hex(self.R).replace('0x', ''))
        if g == 1:
            if self.G < 255:
                self.G += 1
            else:
                self.G == 255
            if self.G < 16:
                self.green = "0" + str(hex(self.G).replace('0x', ''))
            else:
                self.green = str(hex(self.G).replace('0x', ''))
        elif g == -1:
            if self.G > 0:
                self.G -= 1
            else:
                self.G == 0
            if self.G < 16:
                self.green = "0" + str(hex(self.G).replace('0x', ''))
            else:
                self.green = str(hex(self.G).replace('0x', ''))
        if b == 1:
            if self.B < 255:
                self.B += 1
            else:
                self.B == 255
            if self.B < 16:
                self.blue = "0" + str(hex(self.B).replace('0x', ''))
            else:
                self.blue = str(hex(self.B).replace('0x', ''))
        elif b == -1:
            if self.B > 0:
                self.B -= 1
            else:
                self.B == 0
            if self.B < 16:
                self.blue = "0" + str(hex(self.B).replace('0x', ''))
            else:
                self.blue = str(hex(self.B).replace('0x', ''))
        return '#' + self.red + self.green + self.blue
