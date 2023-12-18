import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import Caesar
import Afficode
import Vigcode
import RSA
import Base64
import Discode
import Vernam_Cipher
import steganography


class MY_GUI:
    def __init__(self, init_window_name):
        self.window = init_window_name
        self.path = 0

    def set_init_window(self):
        self.window.title = "Encryption"
        self.window.geometry("800x700")
        # Encryption Type
        type_file = ["Caesar Cipher", "Affine Cipher", "Vigener Cipher", "RSA Cipher", "Base64",
                     "Column shift Cipher", "Vernam Cipher", "steganography"]

        self.coFrame = Frame(self.window, bg='white')
        self.coFrame.grid(padx=15, pady=10, row=0, column=0, rowspan=3)

        self.codeVar = IntVar()

        for index in range(len(type_file)):
            self.code = Radiobutton(self.coFrame,
                                    text=type_file[index],
                                    bg='white',
                                    variable=self.codeVar,
                                    value=index)
            self.code.grid(ipadx=20, ipady=15, row=index, column=0)

        # Input and output framework

        self.entry = Frame(self.window, bg='white')
        self.entry.grid(padx=15, pady=10, row=0, column=3)

        self.enLabel = Label(self.entry, text='Input：', bg='white')
        self.enLabel.grid(ipadx=20, ipady=15, row=0, column=0)

        self.enText_input = Text(self.entry, width=30, height=7)
        self.enText_input.grid(ipadx=20, ipady=15, row=1, column=0)

        self.enLabel = Label(self.entry, text='Key：', bg='white')
        self.enLabel.grid(ipadx=20, ipady=15, row=2, column=0)

        self.enLabel_key = Text(self.entry, width=30, height=2)
        self.enLabel_key.grid(row=3, column=0)

        self.enLabel = Label(self.entry, text='Output：', bg='white')
        self.enLabel.grid(ipadx=20, ipady=15, row=6, column=0)

        self.enKey_output = Text(self.entry, width=30, height=7)
        self.enKey_output.grid(ipadx=20, ipady=15, row=7, column=0)

        # Encryption and decryption options

        self.en = Button(self.window, text='Read files', bg='white', command=self.read_from_file)
        self.en.grid(padx=10, pady=5, row=0, column=4)

        self.en = Button(self.window, text='Save file', bg='white', command=self.save_file)
        self.en.grid(padx=10, pady=5, row=0, column=10)

        self.en = Button(self.window, text='Encryption', bg='white', command=self.Encryption)
        self.en.grid(padx=10, pady=5, row=1, column=4)

        self.en = Button(self.window, text='Decryption', bg='white', command=self.Decryption)
        self.en.grid(padx=10, pady=5, row=1, column=10)

    def read_from_file(self):
        fpath = filedialog.askopenfilename(title='open a file')
        if fpath == '':
            tkinter.messagebox.showerror("error", "not select file")
            return
        if self.codeVar.get() == 7:
            self.path = fpath
        else:
            with open(fpath, "r", encoding="utf-8") as f:

                self.string = f.read()
                self.enText_input.insert(END, self.string)

    def read_from_picture(self):
        fpath = filedialog.askopenfilename(title='open a file')
        if fpath == '':
            tkinter.messagebox.showerror("error", "not select file")
            return
        return fpath

    def save_file(self):
        file = filedialog.asksaveasfile(defaultextension='.txt',
                                        filetypes=[
                                            ("Text file", ".txt"),
                                            ("HTML file", ".html"),
                                            ("All files", ".*"),
                                        ])
        if file is None:
            return
        filetext = str(self.enKey_output.get(1.0, END))
        file.write(filetext)
        file.close()

    # Encryption
    def Encryption(self):
        global encry
        if self.codeVar.get() == 0:
            encry = Caesar.Encrypt(self.enText_input.get(1.0, END),
                                   int(self.enLabel_key.get('1.0', END)))
            self.enKey_output.insert(END, encry)
        elif self.codeVar.get() == 1:
            str_key = list(self.enLabel_key.get(1.0, END).split())
            if len(str_key) != 2:
                tkinter.messagebox.showerror('error', 'The key you entered does not match, there should be a and b')
            a = int(str_key[0])
            b = int(str_key[1])
            encry = Afficode.encrypt(self.enText_input.get(1.0, END).strip(), a, b)
            self.enKey_output.insert(END, encry)
        elif self.codeVar.get() == 2:
            str_key = self.enLabel_key.get(1.0, END)
            encry = Vigcode.Encrypt(self.enText_input.get('1.0', END).strip(), str_key)
            self.enKey_output.insert(END, encry)
        elif self.codeVar.get() == 3:
            str_key = list(self.enLabel_key.get(1.0, END).split())
            if len(str_key) != 3:
                tkinter.messagebox.showerror('error', 'The keys you entered do not match, there should only be p, q, e')
            a = int(str_key[0])
            b = int(str_key[1])
            c = int(str_key[2])
            encry = RSA.RSA(1, self.enText_input.get(1.0, END).strip(), a, b, c)
            self.enKey_output.insert(END, encry)
        elif self.codeVar.get() == 4:
            str_key = list(self.enLabel_key.get(1.0, END).split())
            if len(str_key):
                tkinter.messagebox.showerror('error', 'No key input required')
            encry = Base64.Base(1, self.enText_input.get(1.0, END).strip())
            self.enKey_output.insert(END, encry)
        elif self.codeVar.get() == 5:
            str_key = list(self.enLabel_key.get(1.0, END).split())
            if len(str_key) != 1:
                tkinter.messagebox.showerror('error', 'Enter only one key')
            key = str_key[0]
            encry = Discode.Dis(1, self.enText_input.get(1.0, END).strip(), key)
            self.enKey_output.insert(END, encry)
        elif self.codeVar.get() == 6:
            str_key = list(self.enLabel_key.get(1.0, END))
            encry = Vernam_Cipher.Encrypt(self.enText_input.get(1.0, END), str_key)
            self.enKey_output.insert(END, encry)
        elif self.codeVar.get() == 7:
            path = self.path
            new_image = self.enLabel_key.get(1.0, END)
            steganography.encode(path, self.enText_input.get(1.0, END), new_image.strip())

    def Decryption(self):
        if self.codeVar.get() == 0:
            decry = Caesar.decrypt(self.enText_input.get(1.0, END),
                                     int(self.enLabel_key.get('1.0', END)))
            self.enKey_output.insert(END, decry)
        elif self.codeVar.get() == 1:
            str_key = list(self.enLabel_key.get(1.0, END).split())
            if len(str_key) != 2:
                tkinter.messagebox.showerror('error', 'The key you entered does not match, there should be a and b')
            a = int(str_key[0])
            b = int(str_key[1])
            decry = Afficode.decrypt(self.enText_input.get(1.0, END), a, b)
            self.enKey_output.insert(END, decry)
        elif self.codeVar.get() == 2:
            str_key = self.enLabel_key.get(1.0, END)
            decry = Vigcode.Decrypt(self.enText_input.get('1.0', END), str_key)
            self.enKey_output.insert(END, decry)
        elif self.codeVar.get() == 3:
            str_key = list(self.enLabel_key.get(1.0, END).split())
            if len(str_key) != 3:
                tkinter.messagebox.showerror('error', 'The keys you entered do not match, there should only be p, q, e')
            a = int(str_key[0])
            b = int(str_key[1])
            c = int(str_key[2])
            decry = RSA.RSA(2, self.enText_input.get(1.0, END).strip(), a, b, c)
            self.enKey_output.insert(END, decry)
        elif self.codeVar.get() == 4:
            str_key = list(self.enLabel_key.get(1.0, END).split())
            if len(str_key):
                tkinter.messagebox.showerror('error', 'No key input required')
            decry = Base64.Base(2, self.enText_input.get(1.0, END).strip())
            self.enKey_output.insert(END, decry)
        elif self.codeVar.get() == 5:
            str_key = list(self.enLabel_key.get(1.0, END))
            if len(str_key) != 1:
                tkinter.messagebox.showerror('error', 'Enter only one key')
            key = str_key[0]
            decry = Discode.Dis(2, self.enText_input.get(1.0, END), key)
            self.enKey_output.insert(END, decry)
        elif self.codeVar.get() == 6:
            str_key = self.enLabel_key.get(1.0, END)
            decry = Vernam_Cipher.Decrypt(self.enText_input.get(1.0, END), str_key)
            self.enKey_output.insert(END, decry)
        elif self.codeVar.get() == 7:
            path = self.path

            self.enKey_output.insert(END, steganography.decode(path))


def main():
    init_windows = Tk()
    A = MY_GUI(init_windows)
    A.set_init_window()
    init_windows.mainloop()


if __name__ == '__main__':
    main()
