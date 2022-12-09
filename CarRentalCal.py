#This made by Vera Trinh
from tkinter import *
from tkinter import ttk
root = Tk()
duration_entry = Entry(root)
update_label  = StringVar()
duration = int()
rent = StringVar()
gst = StringVar()
receipt = StringVar()
discount = StringVar()
rent_car = StringVar()
gst_car  = StringVar()
receipt_car = StringVar()
discount_car = StringVar()
rent_van = StringVar()
gst_van  = StringVar()
receipt_van = StringVar()
discount_van = StringVar()
rent_bike = StringVar()
gst_bike = StringVar()
receipt_bike = StringVar()
discount_bike = StringVar()
var = IntVar()
class HireVehicle():
    def __init__():
        pass
        
class car(HireVehicle):
    def __init__(self,duration):
        self.duration = duration
        
    def rent(self):
        return float(self.duration)*10
    def gst(self):
        
        return float(self.duration)*10*0.15
    def discount(self):
        if self.duration > 8:
            return float(self.duration)*10*0.2
        else:
            return 0
    def receipt(self):
       
        if self.duration > 8:
            return ((float(self.duration)*10) + (float(self.duration)*10*0.15)) - (float(self.duration)*10*0.2)
        else:
            return (float(self.duration)*10)+ ((float(self.duration)*10*0.15))

class van(HireVehicle):
    def __init__(self,duration):
        self.duration = duration
        
    def rent(self):
        return float(self.duration)*20
    def gst(self):
        return float(self.duration)*20*0.15
    def discount(self):
        if self.duration > 8:
            return float(self.duration)*20*0.2
        else:
            return 0
    def receipt(self):
        if self.duration > 8:
            return ((float(self.duration)*20) + (float(self.duration)*20*0.15)) - (float(self.duration)*20*0.2)
        else:
            return (float(self.duration)*20)+ ((float(self.duration)*20*0.15))
 
class bike(HireVehicle):
    def __init__(self,duration):
        self.duration=duration
    def rent(self):
        return float(self.duration)*10
    def gst(self):
        return float(self.duration)*10*0.15
    def discount(self):
        if self.duration > 3:
            return float(self.duration)*10*0.2
        else:
            return 0 
    def receipt(self):
        if self.duration > 3:
            return ((float(self.duration)*10) + (float(self.duration)*10*0.15)) - (float(self.duration)*10*0.2)
        else:
            return (float(self.duration)*10)+ ((float(self.duration)*10*0.15))
            
def CarCal(duration):
    duration = float(duration)
    car1 = car(duration)
    rent_car.set(car1.rent())
    gst_car.set(car1.gst())
    receipt_car.set(car1.receipt())  
    discount_car.set(car1.discount())
    l3 = Label(root, text="Price: ").grid(column=1, row=6)
    l4 = Label(root, text="GST: ").grid(column=1, row=8)
    l5 = Label(root, text="Rent: ").grid(column=1,row=9)
    l6 = Label(root, text="Included: ").grid(column=1, row=7)
    l7 = Label(root, text="Discount: ").grid(column=1, row=10)
    ttk.Label(root, background="white", width=15, textvariable=receipt_car).grid(column=2, row=6)
    ttk.Label(root, background="white", width=15, textvariable=gst_car).grid(column=2, row=8)
    ttk.Label(root,background="white", width=15, textvariable=rent_car).grid(column=2, row=9)  
    ttk.Label(root, background="white", width=15, textvariable=discount_car).grid(column=2, row=10)
    
def VanCal(duration):
    duration = float(duration)
    van1 = van(duration)
    rent_van.set(van1.rent())
    gst_van.set(van1.gst())
    receipt_van.set(van1.receipt())
    discount_van.set(van1.discount())
    l3 = Label(root, text="Price: ").grid(column=1, row=6)
    l4 = Label(root, text="GST: ").grid(column=1, row=8)
    l5 = Label(root, text="Rent: ").grid(column=1,row=9)
    l6 = Label(root, text="Included: ").grid(column=1, row=7)
    l7 = Label(root, text="Discount: ").grid(column=1, row=10)
    ttk.Label(root, background="white", width=15, textvariable=receipt_van).grid(column=2, row=6)
    ttk.Label(root, background="white", width=15, textvariable=gst_van).grid(column=2, row=8)
    ttk.Label(root,background="white", width=15, textvariable=rent_van).grid(column=2, row=9)  
    ttk.Label(root, background="white", width=15, textvariable=discount_van).grid(column=2, row=10)
def BikeCal(duration):  
    duration = float(duration)
    bike1 = bike(duration)
    rent_bike.set(bike1.rent())
    gst_bike.set(bike1.gst())
    receipt_bike.set(bike1.receipt())
    discount_bike.set(bike1.discount())
    l3 = Label(root, text="Price: ").grid(column=1, row=6)
    l4 = Label(root, text="GST: ").grid(column=1, row=8)
    l5 = Label(root, text="Rent: ").grid(column=1,row=9)
    l6 = Label(root, text="Included: ").grid(column=1, row=7)
    l7 = Label(root, text="Discount: ").grid(column=1, row=10)
    ttk.Label(root, background="white", width=15, textvariable=receipt_bike).grid(column=2, row=6)
    ttk.Label(root, background="white", width=15, textvariable=gst_bike).grid(column=2, row=8)
    ttk.Label(root,background="white", width=15, textvariable=rent_bike).grid(column=2, row=9)  
    ttk.Label(root, background="white", width=15, textvariable=discount_bike).grid(column=2, row=10)
def selection():
    return(var.get())
def textchange(var):
    if var.get() == 3:
        update_label.config(text="Days")
    else:
        update_label.config(text="Hour")
def durationcal(var):
    if var.get() == 1:
        CarCal(duration_entry.get())
    elif var.get() == 2:
        VanCal(duration_entry.get()) 
    elif var.get() == 3:
        BikeCal(duration_entry.get())
car_Button = Radiobutton(root, text="Car", variable=var, value = 1, command=lambda:[selection, textchange(var), CarCal(duration)]).grid(column=1, row=1)
van_Button = Radiobutton(root, text="Van", variable=var, value = 2, command=lambda:[selection, textchange(var), VanCal(duration)]).grid(column=1, row=2)
bike_Button = Radiobutton(root, text="Bike", variable=var, value = 3, command=lambda:[selection, textchange(var), BikeCal(duration)]).grid(column=1, row=3)
durationlabel = Label(root, text="Duration: ").grid(column=1, row=4)
duration_entry.grid(column=2, row=4)
update_label = Label(root, text="Hours")
update_label.grid(column=3, row=4)
cal_button = Button(root, text="Calculate", command= lambda:durationcal(var)).grid(column=2, row=5)
root.mainloop()    
