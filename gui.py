from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
import requests
import scrape
import webbrowser


def main():
    products = scrape.GetDeals()

    root = Tk()

    root.title("eBay New Deals - GUI")
    root.resizable(False, False)
    root.configure(background='#262626')

    title = Label(root, text="Today's Top Deals!", bg="#262626", fg="white", font="none 32 bold")
    title.pack()

    c = Canvas(root,bg="#262626", height=700, width=1400, bd=0, highlightthickness=0, relief='ridge')
    c.pack()

    #col 1
    photo_list = []
    title_list = []
    price_list = []
    display_url_list = []
    url_list = []

    img_y = 120
    title_y = 85
    canvas_y = 80
    canvas2_y = 80
    price_y = 120
    url_y = 150
    
    #col 2
    col2_photo_list = []
    col2_title_list = []
    col2_price_list = []
    col2_display_url_list = []
    col2_url_list = []

    col2_img_y = 120
    col2_title_y = 85
    col2_canvas_y = 80
    col2_canvas2_y = 80
    col2_price_y = 120
    col2_url_y = 150

    
    for i in range(0, len(products)):
        if i < 3:
            pCanvas = Canvas(root, bg="grey", height=170, width=560, bd=0, highlightthickness=0, relief='ridge').place(x=70,y=canvas_y)
            if len(products[i]['deal_title']) > 45:
                title_list.append(products[i]['deal_title'][:45] + '...')
            else:
                title_list.append(products[i]['deal_title'])

            Label(root, text=title_list[i], bg='grey', fg='#FFFFFF', font='Montserrat 19 bold').place(x=100,y=title_y)
            photo_list.append(getProductImg(products[i]['deal_img']))
            Label(root, image=photo_list[i], width=200, height=120, bd=0).place(x=100, y=img_y)

            price_list.append(products[i]['deal_price'])
            Label(root, text= f"Price (GBP): {price_list[i]}", bg='grey', fg='#FFFFFF', font='Montserrat 20 bold').place(x=320,y=price_y)

            if len(products[i]['deal_url']) > 20:
                display_url_list.append(products[i]['deal_url'][:20] + '...')
                url_list.append(products[i]['deal_url'])
            else:
                display_url_list.append(products[i]['deal_url'])
                url_list.append(products[i]['deal_url'])

            Label(root, text= f"URL: {display_url_list[i]}", bg='grey', fg='#FFFFFF', font='Montserrat 20 bold').place(x=320,y=url_y)
            
            img_y += 220
            title_y += 220
            canvas_y += 220
            price_y += 220
            url_y += 220

        if i >= 3 and i < 6:

            pCanvas2 = Canvas(root, bg="grey", height=170, width=560, bd=0, highlightthickness=0, relief='ridge').place(x=800,y=canvas2_y)
            
            if len(products[i]['deal_title']) > 45:
                col2_title_list.append(products[i]['deal_title'][:45] + '...')
            else:
                col2_title_list.append(products[i]['deal_title'])

            col2_photo_list.append(getProductImg(products[i]['deal_img']))
            col2_price_list.append(products[i]['deal_price'])

            if len(products[i]['deal_url']) > 20:
                col2_display_url_list.append(products[i]['deal_url'][:20] + '...')
                col2_url_list.append(products[i]['deal_url'])
            else:
                col2_display_url_list.append(products[i]['deal_url'])
                col2_url_list.append(products[i]['deal_url'])

            canvas2_y += 220
            
    
    #populates col2          
    for i in range(0, 3):
        Label(root, text=col2_title_list[i], bg='grey', fg='#FFFFFF', font='Montserrat 19 bold').place(x=830,y=col2_title_y)
        Label(root, image=col2_photo_list[i], width=200, height=120, bd=0).place(x=830, y=col2_img_y)
        Label(root, text= f"Price (GBP): {col2_price_list[i]}", bg='grey', fg='#FFFFFF', font='Montserrat 20 bold').place(x=1050,y=col2_price_y)
        Label(root, text= f"URL: {col2_display_url_list[i]}", bg='grey', fg='#FFFFFF', font='Montserrat 20 bold').place(x=1050,y=col2_url_y)
            
        col2_title_y += 220
        col2_img_y += 220
        col2_price_y += 220
        col2_url_y += 220

    button1 = Button(root, padx=10, pady=10, highlightbackground="#262626", fg="white", text="View Deal!", command= lambda: openURL(url_list[0])).place(x=420, y = 190)
    button2 = Button(root, padx=10, pady=10, highlightbackground="#262626", fg="white", text="View Deal!", command= lambda: openURL(url_list[1])).place(x=420, y = 410)
    button3 = Button(root, padx=10, pady=10, highlightbackground="#262626", fg="white", text="View Deal!", command= lambda: openURL(url_list[2])).place(x=420, y = 640)
    button4 = Button(root, padx=10, pady=10, highlightbackground="#262626", fg="white", text="View Deal!", command= lambda: openURL(col2_url_list[0])).place(x=1150, y = 190)
    button5 = Button(root, padx=10, pady=10, highlightbackground="#262626", fg="white", text="View Deal!", command= lambda: openURL(col2_url_list[1])).place(x=1150, y = 410)
    button6 = Button(root, padx=10, pady=10, highlightbackground="#262626", fg="white", text="View Deal!", command= lambda: openURL(col2_url_list[2])).place(x=1150, y = 640)


    root.mainloop()
            

def openURL(URL):
    webbrowser.open(URL,new=2)



def getProductImg(imgurl):
    response = requests.get(imgurl)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)).resize((200, 120), Image.ANTIALIAS))
    return img




if __name__ == "__main__":
    main()

