from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os
# This line creates an instance of the Tk class. This instance (root) is the main window of an application.
root = Tk()
# This line sets the title of the window to ‘KEshare’.
root.title('KEshare')
# This line sets the size and position of the window. The window’s width is 450 pixels, height is 560 pixels, and it’s positioned 500 pixels from the left and 200 pixels from the top of the screen.
root.geometry("450x560+500+200")
# This line sets the background color of the window to #f4fdfe, which is a light blue color.
root.configure(bg="#610C9F")
# This line makes the window non-resizable. The two parameters (False, False) prevent resizing in both directions (horizontal and vertical).
root.resizable(False, False)

def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#B3A492")
    window.resizable(False, False)


    def select_file():
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Select image file",
                                            filetypes=(("file_type", "*.txt"),('all files', '*.*')))
    
    
    def sender():
        s = socket.socket()
        host = socket.gethostbyname()
        port = 8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print("waiting for any incoming connection...")
        conn, addr= s.accept()
        file = open(filename, 'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print('Files have been sent successfully')
    
    image_icon1 = PhotoImage(file="images/send.png")
    window.iconphoto(False, image_icon1)

    Sbackground=PhotoImage(file="images/sender.png")
    Label(window, image=Sbackground).place(x = -2, y = 0)
    Mbackground = PhotoImage(file="images/id.png")
    Label(window, image=Mbackground).place(x=100, y=260)

    host=socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white',fg='black').place(x=140, y=290)

    
    Button(window, text="+ choose file", width=10, height=1, font='aria 14 bold', bg='#fff', fg='#000', command=select_file).place(x = 160, y=150)
    Button(window, text="SEND", width=8, height=1, font='aria 14 bold', bg='#fff', fg='#000', command=sender).place(x = 300, y=150)


    



    window.mainloop()

def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg="#B3A492")
    main.resizable(False, False)

    def receiver():
        ID= SenderID.get()
        filename1 = incoming_file.get()
        s = socket.socket()
        port= 8080
        s.connect((ID, port))
        file = open(filename1, "wb")
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print('File has been received successfully')


    image_icon1 = PhotoImage(file="images/receive.png")
    main.iconphoto(False, image_icon1)

    Hbackground = PhotoImage(file="images/px.png")
    Label(main, image=Hbackground).place(x= -2, y = 0)
    logo = PhotoImage(file="images/px.png")

    Label(main, image=logo, bg="#B4A121").place(x = 10, y = 250)

    Label(main, text="Receive", font=("courier", 12, 'italic'), bg="#D5A121").place(x= 20, y=340)
    Label(main, text="Input sender ID", font=("arial", 11, "bold"), bg= "#f4fdfe").place(x= 100, y= 280)
    SenderID = Entry(main, width=25,fg="black", border=2, bg='yellow', font=('aria', 15))  
    SenderID.place(x=20, y=370)
    SenderID.focus()

    Label(main, text="filename for the incoming file:", font=("arial", 10, "bold", "italic"), bg="#f4fdfe").place(x=100, y=42)
    incoming_file = Entry(main, width=25, fg='black', border=2, bg='white', font=('arial', 15))
    incoming_file.place(x=20, y=450)

    image_icon = PhotoImage(file="images/arrow.png")
    rr = Button (main, text= "Receive", compound=LEFT, image=image_icon, width=130, bg="#39c790" , font="consolas 15 bold", command=receiver)
    rr.place(x=20, y=500)    


    main.mainloop()

#setting icon
image_icon = PhotoImage(file="images/icon.jpg")
root.iconphoto(False, image_icon)
Label(root, text='File transfer', font=("Times New Roman", 18, 'italic'), bg="#D0BFFF").place(x = 27, y = 28)
# Frame()
Frame(root, width=400, height=2, bg="#5B0888").place(x=25, y=80)

#creating send button
send_image= PhotoImage(file="images/send.png")
Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send).place(x=50, y=100)
#positioning send_button on screen
recieve_image = PhotoImage(file="images/receive.png")
Button(root, image=recieve_image, bg="#f4fdfe", bd=0, command=Receive).place(x=300, y=100)
Label(root, text="send", font=('consolas', 18, "italic"), bg="#f4fdfe").place(x = 65 , y = 200)
Label(root, text="receive", font=('consolas', 18, "italic"), bg="#f4fdfe").place(x = 300 , y = 200)

background = PhotoImage(file="images/background.png")
Label(root, image=background).place(x= -2, y=255)












# This line starts the GUI’s event loop. The event loop is an infinite loop waiting for events and updates the GUI. It must be the last line because it’s blocking: it stops the script from progressing until the window is closed.
root.mainloop()