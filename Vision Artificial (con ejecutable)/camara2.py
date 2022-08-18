from tkinter import * 
import time
from threading import Thread
import cv2 as cv
import numpy as np
from PIL import Image, ImageTk

cap = cv.VideoCapture('deteccion.mp4')

release = True
limit1 = 255
limit2 = 0
st = 0

def normal(e):
    global release
    release = True

def start_b():
    global a
    global st
    st=1
    def camara():
        global producto
        if st == 1:
            _, frame = cap.read()
            frame = cv.resize(frame, (630,480),interpolation=cv.INTER_CUBIC)
            #umbralizacion
            kernel = np.ones((2,2),np.uint8)
            grises = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
            grises = cv.GaussianBlur(grises,(7,7),0)
            _, th = cv.threshold(grises, a, 255, cv.THRESH_BINARY_INV)
            #deteccion de bordes en un area determinada
            area_analizar = np.array([[130, 150], [th.shape[1]-100, 150], [th.shape[1]-100, 330], [130, 330]])
            imAux = np.zeros(shape=(th.shape[:2]), dtype=np.uint8)
            imAux = cv.drawContours(imAux, [area_analizar], -1, (255), -1)
            img_Area = cv.bitwise_and(th,th, mask=imAux)
            #resalto de las zonas a analizar
            th = cv.dilate(th,kernel,iterations=1)
            th = cv.erode(th,kernel,iterations=3)
            cont = 0
            cv.drawContours(frame,[area_analizar],-1,(255,0,255),2)
            #contornos a encontrar en la zona asignada
            cnts,_ = cv.findContours(img_Area,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
            for c in cnts:
                area = cv.contourArea(c)
                if area > 600:
                    cont = len(c)
                    x,y,w,h = cv.boundingRect(c)
                    cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            #estableciendo condiciones
            cv.putText(frame,str(cont),(10,30),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),1) #
            #LabC.config(text=cont)

            imgcv2 = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            borde = np.zeros(shape=(frame.shape[:2]),dtype=np.uint8)
            borde[1:430,1:629]=255
            imgAnd = cv.bitwise_and(imgcv2,imgcv2, mask=borde)
            
            if cont == 27:
                cv.putText(imgAnd,'producto conforme',(50,450),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2) #
                circulo=cv.circle(imgAnd,(30,448),10,(0,255,0),-1) #
                producto = producto + 1 #

            elif cont < 27 or cont > 27:
                cv.putText(imgAnd,'producto rechazado',(240,450),cv.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2) #
                circulo=cv.circle(imgAnd,(200,448),10,(255,0,0),-1) #

            cv.putText(imgAnd,'productos: ' + str(producto),(480,450),cv.FONT_HERSHEY_COMPLEX,0.5,(255,0,255),2) #

            img = Image.fromarray(imgAnd)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(50, camara)
            lmain.pack(side='right', padx=10,pady=10)
    camara()

def stop_b():
    global lmain
    global st
    st = 0
    lmain.pack_forget()

def incremento():
    global release
    release = False
    global a
    while not release and  a< limit1:
        time.sleep(0.12)
        a=a+1
        Lab1.config(text=a)

def decremento():
    global release
    release = False
    global a
    while not release and a > limit2:
        time.sleep(0.12)
        a=a-1
        Lab1.config(text=a)

def destruir_principal():
    if st == 0:
        root.destroy()

root = Tk()
root.geometry('990x500')

valor = IntVar()
valor.set(134)
a = valor.get()

product = IntVar()
product.set(0)
producto = product.get()

b_start =PhotoImage(file='b_start.gif')
StartB = Button(root,image=b_start,command=start_b,borderwidth=0)
StartB.place(x=20,y=40)

b_stop =PhotoImage(file='b_stop.gif')
StopB = Button(root,image=b_stop,command=stop_b,borderwidth=0)
StopB.place(x=180,y=40)

Close_window = Button(root, text='Cerrar',font='Calibri 16',width=10,command=destruir_principal)
Close_window.place(x=90,y=400)

b1 = Button(root, text='+',font='Calibri 18',width=2,height=1)
b1.place(x=80,y=300)
b1.bind('<Button-1>', lambda e: Thread(target=incremento, daemon=True).start())
b1.bind('<ButtonRelease-1>', normal)

b2 = Button(root, text='-',font='Calibri 18',width=2,height=1)
b2.place(x=180,y=300)
b2.bind('<Button-1>', lambda e: Thread(target=decremento, daemon=True).start())
b2.bind('<ButtonRelease-1>', normal)

Titulo = Label(root, text='Ajuste de contorno',font='Calibri 16')
Titulo.place(x=60,y=270)
Lab1 = Label(root,text=a,font='Calibri 20')
Lab1.place(x=125,y=300)

lmain = Label(root)
root.mainloop()