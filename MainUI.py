from AmazonPriceApiDemo import search_amazon
from BestBuyPriceApiDemo import search_bestbuy
from CostcoPriceApiDemo import search_costco
from SamsClubPriceApiDemo import search_samsclub
from TargetPriceApiDemo import search_target
from WalmartPriceApiDemo import search_walmart
from tkinter import *
import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
from io import BytesIO
import requests

'''
add a checkbox so you can select what places you want to search
add excepion handling so if there are any results it says that
think of all exceptions and handle them
'''

root = customtkinter.CTk()
root.title("Item Pricer")
root.geometry("1500x800")
my_frame = customtkinter.CTkScrollableFrame(root)
my_frame.pack(fill=tk.BOTH, expand=True)

Search_Item = None

Amazon_On_Off = tk.IntVar(value=1)
Amazon_counter = 0
Amazon_Label = None
Amazon_Product_Image_Label = None
BestBuy_On_Off = tk.IntVar(value=1)
BestBuy_counter = 0
BestBuy_Label = None
BestBuy_Product_Image_Label = None
Costco_On_Off = tk.IntVar(value=1)
Costco_counter = 0
Costco_Label = None
Costco_Product_Image_Label = None
SamsClub_On_Off = tk.IntVar(value=1)
SamsClub_counter = 0
SamsClub_Label = None
SamsClub_Product_Image_Label = None
Target_On_Off = tk.IntVar(value=1)
Target_counter = 0
Target_Label = None
Target_Product_Image_Label = None
Walmart_On_Off = tk.IntVar(value=1)
Walmart_Counter = 0
Walmart_Label = None
Walmart_Product_Image_Label = None

def display_image_from_url(url, parent_widget):
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url,headers=headers)
        response.raise_for_status()
        image_data = response.content
        pil_image = Image.open(BytesIO(image_data))
        w_percent = (200 / float(pil_image.size[0]))            
        new_height = int((float(pil_image.size[1]) * w_percent))
        pil_image = pil_image.resize((200, new_height), Image.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(pil_image)
        return tk_image
        
    except requests.exceptions.RequestException:
        error_label = tk.Label(parent_widget, text="There was no image found")
        error_label.pack()

    except Exception as e:
        error_label = tk.Label(parent_widget, text=f"Image Error: {str(e)}")
        error_label.pack()
        
def Increment_item(Retailor):
    match Retailor:
        case "Amazon":
            global Amazon_counter
            Amazon_counter +=1
            Amazon_Name,Amazon_Price,Amazon_Url,Amazon_Thumbnail = search_amazon(Amazon_counter)
            global Amazon_Label
            Amazon_Label.config(text=f"Title: {Amazon_Name}\nPrice: ${Amazon_Price}\nURL: {Amazon_Url}\n")
            global Amazon_Product_Image_Label
            Amazon_Product_Image = display_image_from_url(Amazon_Thumbnail,my_frame)
            Amazon_Product_Image_Label.config(image=Amazon_Product_Image)
            Amazon_Product_Image_Label.image = Amazon_Product_Image
        case "BestBuy":
            global BestBuy_counter
            BestBuy_counter +=1
            BestBuy_Name,BestBuy_Price,BestBuy_Url,BestBuy_Thumbnail = search_bestbuy(BestBuy_counter)
            global BestBuy_Label
            BestBuy_Label.config(text=f"Title: {BestBuy_Name}\nPrice: ${BestBuy_Price}\nURL: {BestBuy_Url}\n")
            global BestBuy_Product_Image_Label
            BestBuy_Product_Image = display_image_from_url(BestBuy_Thumbnail,my_frame)
            BestBuy_Product_Image_Label.config(image=BestBuy_Product_Image)
            BestBuy_Product_Image_Label.image = BestBuy_Product_Image
        case "Costco":
            global Costco_counter
            Costco_counter +=1
            Costco_Name,Costco_Price,Costco_Url,Costco_Thumbnail = search_costco(Costco_counter)
            global Costco_Label
            Costco_Label.config(text=f"Title: {Costco_Name}\nPrice: ${Costco_Price}\nURL: {Costco_Url}\n")
            global Costco_Product_Image_Label
            Costco_Product_Image = display_image_from_url(Costco_Thumbnail,my_frame)
            Costco_Product_Image_Label.config(image=Costco_Product_Image)
            Costco_Product_Image_Label.image = Costco_Product_Image
        case "SamsClub":
            global SamsClub_counter
            SamsClub_counter +=1
            SamsClub_Name,SamsClub_Price,SamsClub_Url,SamsClub_Thumbnail = search_samsclub(SamsClub_counter)
            global SamsClub_Label
            SamsClub_Label.config(text=f"Title: {SamsClub_Name}\nPrice: ${SamsClub_Price}\nURL: {SamsClub_Url}\n")
            global SamsClub_Product_Image_Label
            SamsClub_Product_Image = display_image_from_url(SamsClub_Thumbnail,my_frame)
            SamsClub_Product_Image_Label.config(image=SamsClub_Product_Image)
            SamsClub_Product_Image_Label.image = SamsClub_Product_Image
        case "Target":
            global Target_counter
            Target_counter +=1
            Target_Name,Target_Price,Target_Url,Target_Thumbnail = search_target(Target_counter)
            global Target_Label
            Target_Label.config(text=f"Title: {Target_Name}\nPrice: ${Target_Price}\nURL: {Target_Url}\n")
            global Target_Product_Image_Label
            Target_Product_Image = display_image_from_url(Target_Thumbnail,my_frame)
            Target_Product_Image_Label.config(image=Target_Product_Image)
            Target_Product_Image_Label.image = Target_Product_Image
        case "Walmart":
            global Walmart_Counter
            Walmart_Counter +=1
            Walmart_Name,Walmart_Price,Walmart_Url,Walmart_Thumbnail = search_walmart(Walmart_Counter)
            global Walmart_Label
            Walmart_Label.config(text=f"Title: {Walmart_Name}\nPrice: ${Walmart_Price}\nURL: {Walmart_Url}\n")
            global Walmart_Product_Image_Label
            Walmart_Product_Image = display_image_from_url(Walmart_Thumbnail,my_frame)
            Walmart_Product_Image_Label.config(image=Walmart_Product_Image)
            Walmart_Product_Image_Label.image = Walmart_Product_Image

def decrement_item(Retailor):
    match Retailor:
        case "Amazon":
            global Amazon_counter
            Amazon_counter -=1
            Amazon_Name,Amazon_Price,Amazon_Url,Amazon_Thumbnail = search_amazon(Amazon_counter)
            global Amazon_Label
            Amazon_Label.config(text=f"Title: {Amazon_Name}\nPrice: ${Amazon_Price}\nURL: {Amazon_Url}\n")
            Amazon_Product_Image = display_image_from_url(Amazon_Thumbnail,my_frame)
            Amazon_Product_Image_Label.config(image=Amazon_Product_Image)
            Amazon_Product_Image_Label.image = Amazon_Product_Image
        case "BestBuy":
            global BestBuy_counter
            BestBuy_counter -=1
            BestBuy_Name,BestBuy_Price,BestBuy_Url,BestBuy_Thumbnail = search_bestbuy(BestBuy_counter)
            global BestBuy_Label
            BestBuy_Label.config(text=f"Title: {BestBuy_Name}\nPrice: ${BestBuy_Price}\nURL: {BestBuy_Url}\n")
            global BestBuy_Product_Image_Label
            BestBuy_Product_Image = display_image_from_url(BestBuy_Thumbnail,my_frame)
            BestBuy_Product_Image_Label.config(image=BestBuy_Product_Image)
            BestBuy_Product_Image_Label.image = BestBuy_Product_Image
        case "Costco":
            global Costco_counter
            Costco_counter -=1
            Costco_Name,Costco_Price,Costco_Url,Costco_Thumbnail = search_costco(Costco_counter)
            global Costco_Label
            Costco_Label.config(text=f"Title: {Costco_Name}\nPrice: ${Costco_Price}\nURL: {Costco_Url}\n")
            global Costco_Product_Image_Label
            Costco_Product_Image = display_image_from_url(Costco_Thumbnail,my_frame)
            Costco_Product_Image_Label.config(image=Costco_Product_Image)
            Costco_Product_Image_Label.image = Costco_Product_Image
        case "SamsClub":
            global SamsClub_counter
            SamsClub_counter -=1
            SamsClub_Name,SamsClub_Price,SamsClub_Url,SamsClub_Thumbnail = search_samsclub(SamsClub_counter)
            global SamsClub_Label
            SamsClub_Label.config(text=f"Title: {SamsClub_Name}\nPrice: ${SamsClub_Price}\nURL: {SamsClub_Url}\n")
            global SamsClub_Product_Image_Label
            SamsClub_Product_Image = display_image_from_url(SamsClub_Thumbnail,my_frame)
            SamsClub_Product_Image_Label.config(image=SamsClub_Product_Image)
            SamsClub_Product_Image_Label.image = SamsClub_Product_Image
        case "Target":
            global Target_counter
            Target_counter -=1
            Target_Name,Target_Price,Target_Url,Target_Thumbnail = search_target(Target_counter)
            global Target_Label
            Target_Label.config(text=f"Title: {Target_Name}\nPrice: ${Target_Price}\nURL: {Target_Url}\n")
            global Target_Product_Image_Label
            Target_Product_Image = display_image_from_url(Target_Thumbnail,my_frame)
            Target_Product_Image_Label.config(image=Target_Product_Image)
            Target_Product_Image_Label.image = Target_Product_Image
        case "Walmart":
            global Walmart_Counter
            Walmart_Counter -=1
            Walmart_Name,Walmart_Price,Walmart_Url,Walmart_Thumbnail = search_walmart(Walmart_Counter)
            global Walmart_Label
            Walmart_Label.config(text=f"Title: {Walmart_Name}\nPrice: ${Walmart_Price}\nURL: {Walmart_Url}\n")
            global Walmart_Product_Image_Label
            Walmart_Product_Image = display_image_from_url(Walmart_Thumbnail,my_frame)
            Walmart_Product_Image_Label.config(image=Walmart_Product_Image)
            Walmart_Product_Image_Label.image = Walmart_Product_Image

def Search_For_Item():
    User_Product = Search_Item.get()
    for widget in my_frame.winfo_children():
        widget.destroy() 

    root.images = []

    Label3 = Label(my_frame, text=f"You've Clicked the Button and entered {User_Product}")
    Label3.pack()
    
    if Amazon_On_Off.get() == 1:
        Amazon_Logo = Image.open("Logo/amazon_logo.png").resize((200,120,))
        Amazon_Logo = ImageTk.PhotoImage(Amazon_Logo)
        root.images.append(Amazon_Logo)
        Label(my_frame, image=Amazon_Logo).pack(pady=2)

        Amazon_Name,Amazon_Price,Amazon_Url,Amazon_Thumbnail = search_amazon(Amazon_counter)
        Amazon_Product_Image = display_image_from_url(Amazon_Thumbnail,my_frame)
        global Amazon_Product_Image_Label
        Amazon_Product_Image_Label = tk.Label(my_frame, image=Amazon_Product_Image)
        Amazon_Product_Image_Label.image = Amazon_Product_Image
        Amazon_Product_Image_Label.pack()
    
        global Amazon_Label
        Amazon_Label = Label(my_frame, text=f"Title: {Amazon_Name}\nPrice: ${Amazon_Price}\nURL: {Amazon_Url}\n")
        Amazon_Label.pack()
        button_frame = Frame(my_frame)
        button_frame.pack(pady=5)
        Increment = Button(button_frame, text="->", command=lambda: Increment_item("Amazon"))
        decrement = Button(button_frame, text="<-", command=lambda: decrement_item("Amazon"))
        decrement.pack(side="left", padx=5)
        Increment.pack(side="left", padx=5)

    if BestBuy_On_Off.get() == 1:
        BestBuy_Logo = Image.open("Logo/bestbuy_logo.png").resize((200,137))
        BestBuy_Logo = ImageTk.PhotoImage(BestBuy_Logo)
        root.images.append(BestBuy_Logo)
        Label(my_frame, image=BestBuy_Logo).pack(pady=2)

        BestBuy_Name,BestBuy_Price,BestBuy_Url,BestBuy_Thumbnail = search_bestbuy(BestBuy_counter)
        BestBuy_Product_Image = display_image_from_url(BestBuy_Thumbnail,my_frame)
        global BestBuy_Product_Image_Label
        BestBuy_Product_Image_Label = tk.Label(my_frame, image=BestBuy_Product_Image)
        BestBuy_Product_Image_Label.image = BestBuy_Product_Image
        BestBuy_Product_Image_Label.pack()
        global BestBuy_Label
        BestBuy_Label = Label(my_frame, text=f"Title: {BestBuy_Name}\nPrice: ${BestBuy_Price}\nURL: {BestBuy_Url}\n")
        BestBuy_Label.pack()
        button_frame = Frame(my_frame)
        button_frame.pack(pady=5)
        Increment = Button(button_frame, text="->", command=lambda: Increment_item("BestBuy"))
        decrement = Button(button_frame, text="<-", command=lambda: decrement_item("BestBuy"))
        decrement.pack(side="left", padx=5)
        Increment.pack(side="left", padx=5)

    if Costco_On_Off.get() == 1:
        Costco_Logo = Image.open("Logo/costco_logo.png").resize((200,200))
        Costco_Logo = ImageTk.PhotoImage(Costco_Logo)
        root.images.append(Costco_Logo)
        Label(my_frame, image=Costco_Logo).pack(pady=2)

        Costco_Name,Costco_Price,Costco_Url,Costco_Thumbnail = search_costco(Costco_counter)
        Costco_Product_Image = display_image_from_url(Costco_Thumbnail,my_frame)
        global Costco_Product_Image_Label
        Costco_Product_Image_Label = tk.Label(my_frame, image=Costco_Product_Image)
        Costco_Product_Image_Label.image = Costco_Product_Image
        Costco_Product_Image_Label.pack()
        global Costco_Label
        Costco_Label = Label(my_frame, text=f"Title: {Costco_Name}\nPrice: ${Costco_Price}\nURL: {Costco_Url}\n")
        Costco_Label.pack()
        button_frame = Frame(my_frame)
        button_frame.pack(pady=5)
        Increment = Button(button_frame, text="->", command=lambda: Increment_item("Costco"))
        decrement = Button(button_frame, text="<-", command=lambda: decrement_item("Costco"))
        decrement.pack(side="left", padx=5)
        Increment.pack(side="left", padx=5)

    if SamsClub_On_Off.get() == 1:
        SamsClub_Logo = Image.open("Logo/samsclub_logo.png").resize((200,126))
        SamsClub_Logo = ImageTk.PhotoImage(SamsClub_Logo)
        root.images.append(SamsClub_Logo)
        Label(my_frame, image=SamsClub_Logo).pack(pady=2)

        SamsClub_Name,SamsClub_Price,SamsClub_Url,SamsClub_Thumbnail = search_samsclub(SamsClub_counter)
        SamsClub_Product_Image = display_image_from_url(SamsClub_Thumbnail,my_frame)
        global SamsClub_Product_Image_Label
        SamsClub_Product_Image_Label = tk.Label(my_frame, image=SamsClub_Product_Image)
        SamsClub_Product_Image_Label.image = SamsClub_Product_Image
        SamsClub_Product_Image_Label.pack()
        global SamsClub_Label
        SamsClub_Label = Label(my_frame, text=f"Title: {SamsClub_Name}\nPrice: ${SamsClub_Price}\nURL: {SamsClub_Url}\n")
        SamsClub_Label.pack()
        button_frame = Frame(my_frame)
        button_frame.pack(pady=5)
        Increment = Button(button_frame, text="->", command=lambda: Increment_item("SamsClub"))
        decrement = Button(button_frame, text="<-", command=lambda: decrement_item("SamsClub"))
        decrement.pack(side="left", padx=5)
        Increment.pack(side="left", padx=5)

    if Target_On_Off.get() == 1:
        Target_Logo = Image.open("Logo/target_logo.png").resize((200,113))
        Target_Logo = ImageTk.PhotoImage(Target_Logo)
        root.images.append(Target_Logo)
        Label(my_frame, image=Target_Logo).pack(pady=2)

        Target_Name,Target_Price,Target_Url,Target_Thumbnail = search_target(Target_counter)
        Target_Product_Image = display_image_from_url(Target_Thumbnail,my_frame)
        global Target_Product_Image_Label
        Target_Product_Image_Label = tk.Label(my_frame, image=Target_Product_Image)
        Target_Product_Image_Label.image = Target_Product_Image
        Target_Product_Image_Label.pack()
        global Target_Label
        Target_Label = Label(my_frame, text=f"Title: {Target_Name}\nPrice: ${Target_Price}\nURL: {Target_Url}\n")
        Target_Label.pack()
        button_frame = Frame(my_frame)
        button_frame.pack(pady=5)
        Increment = Button(button_frame, text="->", command=lambda: Increment_item("Target"))
        decrement = Button(button_frame, text="<-", command=lambda: decrement_item("Target"))
        decrement.pack(side="left", padx=5)
        Increment.pack(side="left", padx=5)

    if Walmart_On_Off.get() == 1:
        Walmart_Logo = Image.open("Logo/walmart_logo.png").resize((200,47))
        Walmart_Logo = ImageTk.PhotoImage(Walmart_Logo)
        root.images.append(Walmart_Logo)
        Label(my_frame, image=Walmart_Logo).pack(pady=2)

        Walmart_Name,Walmart_Price,Walmart_Url,Walmart_Thumbnail = search_walmart(Walmart_Counter)
        Walmart_Product_Image = display_image_from_url(Walmart_Thumbnail,my_frame)
        global Walmart_Product_Image_Label
        Walmart_Product_Image_Label = tk.Label(my_frame, image=Walmart_Product_Image)
        Walmart_Product_Image_Label.image = Walmart_Product_Image
        Walmart_Product_Image_Label.pack()
        global Walmart_Label
        Walmart_Label = Label(my_frame, text=f"Title: {Walmart_Name}\nPrice: ${Walmart_Price}\nURL: {Walmart_Url}\n")
        Walmart_Label.pack()
        button_frame = Frame(my_frame)
        button_frame.pack(pady=5)
        Increment = Button(button_frame, text="->", command=lambda: Increment_item("Walmart"))
        decrement = Button(button_frame, text="<-", command=lambda: decrement_item("Walmart"))
        decrement.pack(side="left", padx=5)
        Increment.pack(side="left", padx=5)

    Search_Again = Button(my_frame, text="Search for another Item", command=lambda: Main_Menu())
    Search_Again.pack()

def Main_Menu():
    for widget in my_frame.winfo_children():
        widget.destroy() 

    Intro_Label1 = Label(my_frame, text="Hello Welcome to Item Pricer")
    Intro_Label2 = Label(my_frame, text="Enter the Item you want to Compare the price to Below")

    global Search_Item
    Search_Item= Entry(my_frame, width= 50)
    Search_Item.focus_set()

    Submit_Button = Button(my_frame, text="Submit", command=Search_For_Item)

    Intro_Label1.pack()
    Intro_Label2.pack()
    Search_Item.pack()
    Submit_Button.pack()

    global Amazon_On_Off
    global BestBuy_On_Off
    global Costco_On_Off
    global SamsClub_On_Off
    global Target_On_Off
    global Walmart_On_Off

    Amazon_CheckBox = tk.Checkbutton(my_frame, text='Search Amazon?',variable=Amazon_On_Off, onvalue=1, offvalue=0)
    BestBuy_CheckBox = tk.Checkbutton(my_frame, text='Search BestBuy?',variable=BestBuy_On_Off, onvalue=1, offvalue=0)
    Costco_CheckBox = tk.Checkbutton(my_frame, text='Search Costco?',variable=Costco_On_Off, onvalue=1, offvalue=0)
    SamsClub_CheckBox = tk.Checkbutton(my_frame, text='Search SamsClub?',variable=SamsClub_On_Off, onvalue=1, offvalue=0)
    Target_CheckBox = tk.Checkbutton(my_frame, text='Search Target?',variable=Target_On_Off, onvalue=1, offvalue=0)
    Walmart_CheckBox = tk.Checkbutton(my_frame, text='Search Walmart?',variable=Walmart_On_Off, onvalue=1, offvalue=0)

    Amazon_CheckBox.pack()
    BestBuy_CheckBox.pack()
    Costco_CheckBox.pack()
    SamsClub_CheckBox.pack()
    Target_CheckBox.pack()
    Walmart_CheckBox.pack()    

if __name__ == "__main__":
    Main_Menu()

root.mainloop()





