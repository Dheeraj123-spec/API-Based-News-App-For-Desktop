import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from tkinter import messagebox
from PIL import ImageTk,Image

class NewsApp:

    def __init__(self):

        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=569593d686f149d9858daf6d872dbef3').json()
        #print(self.data)

        # initial GUI load
        self.load_gui()
        # load the 1st news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('600x700+300+50')
        self.root.resizable(0,0)
        self.root.title('Desktop News App')
        self.root.configure(background='yellow')
        self.root.iconbitmap('news.ico')


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()



    def Exit(self):

        m=messagebox.askyesno('Exit','Would you really want to exit')

        if m==True:
            self.root.destroy()
        else:
            pass

    def load_news_item(self,index):

        # clear the screen for the new news item
        self.clear()
        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((600,300))
            photo = ImageTk.PhotoImage(im)

        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((600, 300))
            photo = ImageTk.PhotoImage(im)


        label = Label(self.root,image=photo)
        label.pack()


        heading = Label(self.root,text=self.data['articles'][index]['title'],font=('Times New Roman',15,'bold'),bg='red',fg='white',wraplength=500,justify='center')
        heading.pack(pady=(10,20))

        details = Label(self.root, text=self.data['articles'][index]['description'],font=('Times New Roman', 15), bg='black', fg='white',wraplength='500',justify='center')
        details.pack(pady=(2, 20))


        frame = Frame(self.root,bg='yellow')
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev = Button(frame,text='Prev',font=('times new roman',10,'bold'),width=18,height=3,command=lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)

        read = Button(frame, text='Read More', font=('times new roman',10,'bold'),width=18, height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next = Button(frame, text='Next',font=('times new roman',10,'bold'), width=16, height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)

        btn=Button(frame,text='Exit',font=('times new roman',10,'bold'),width=16,height=3,command=self.Exit)
        btn.pack(side=LEFT)

        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)


obj = NewsApp()