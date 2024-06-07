import tkinter as tk
from tkinter import *
import customtkinter as Ctk
from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkFont, CTkEntry
from datetime import datetime

class BookingWindow(tk.Toplevel):
    def __init__(self, master=None, vehicle_type=""):
        super().__init__(master)
        self.title(f"{vehicle_type} Booking Window")
        self.geometry("500x500")
        self.resizable(False, False)
        self.configure(background="#C8E7F5")

        font2 = CTkFont(family= "Inter", size=20)

        self.booking_window_frame = CTkFrame(self, width=449, height=434, border_width=2, fg_color="#F6D2E0")
        self.booking_window_frame.place(relx=0.5, rely=0.5, anchor="center")

         # Pick-up Address
        self.pickup_label = CTkLabel(self.booking_window_frame, text="Pick-up Address:", text_color="#000000", font=font2)
        self.pickup_label.place(relx=0.1, rely=0.1, anchor="w")

        self.pickup_entry =CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_entry.place(relx=0.5, rely=0.1, anchor="w")

        # Drop-off Address
        self.pickup_label = CTkLabel(self.booking_window_frame, text="Drop-off Address:", text_color="#000000", font=font2)
        self.pickup_label.place(relx=0.1, rely=0.2, anchor="w")

        self.pickup_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_entry.place(relx=0.5, rely=0.2, anchor="w")

        # Pick-up Time
        self.pickup_label =CTkLabel(self.booking_window_frame, text="Pick-up Date:", text_color="#000000", font=font2)
        self.pickup_label.place(relx=0.1, rely=0.3, anchor="w")

        self.pickup_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_entry.place(relx=0.5, rely=0.3, anchor="w")


        # Pick-up Location
        self.pickup_label = CTkLabel(self.booking_window_frame, text="Pick-up Time:", text_color="#000000", font=font2)
        self.pickup_label.place(relx=0.1, rely=0.4, anchor="w")

        self.pickup_entry = CTkEntry(self.booking_window_frame, width=200, fg_color="#C8E7F5", text_color="#000000")
        self.pickup_entry.place(relx=0.5, rely=0.4, anchor="w")

        # Submit button
        self.submit_button = CTkButton(self.booking_window_frame, text=" Submit", fg_color="#000000", text_color="#C8E7F5")
        self.submit_button.place(relx=0.5, rely=0.9, anchor="center")









        # Update time every second
        self.update_time()

    def update_time(self):
        # Get current time and format it
        current_time = datetime.now().strftime("%H:%M:%S %p")
        # Update the label text
        self.time_label.config(text=current_time)
        # Call update_time function again after 1000 ms (1 second)
        self.after(1000, self.update_time)

        # Book Button
        self.book_button = tk.Button(self, text="Book", command=self.book_motor)
        self.book_button.place(relx=0.5, rely=0.5, anchor="center")

    def book_motor(self):
        # Implement booking functionality here
        pass











class RideApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Zoomers")




        # Fonts
        font1 = CTkFont(family= "Candara", size=70, weight= "bold", slant="italic")
        

        

        # Make the window resizable
        self.master.geometry("1200x1024")  # Initial size
        self.master.resizable(True, True)
        self.master.configure(bg="#F6D2E0")

        # Header frame (Logo, Name of the App) using customtkinter for a modern look
        self.header_frame = CTkFrame(master, corner_radius=10, fg_color="#C8E7F5", height=90, border_color="#C8E7F5", border_width=5)
        self.header_frame.pack(fill=tk.X)

        self.header_label = CTkLabel(self.header_frame, text="ZOOMERS", font= font1, text_color="#FFFFFF")
        self.header_label.place(relx=0.43, rely=0.5, anchor="w")

        self.header_img = tk.PhotoImage(file='zoomers_logo.png')
        self.header_image_label = CTkLabel(self.header_frame, image=self.header_img,fg_color="#C8E7F5")
        self.header_image_label.place(relx=0.35, rely=0.5, anchor= "w")

    

        # Motor frame 
        self.motor_frame = tk.Frame(master,  borderwidth=3, relief="groove")
        self.motor_frame.place(relx= 0.50, rely= 0.3,  relwidth=0.3, relheight=0.3, anchor="center")

        # Motor icon
        self.motor_img = tk.PhotoImage(file='motor.png')
        self.motor_image_label = tk.Label(self.motor_frame, image=self.motor_img, bg="#C8E7F5")
        self.motor_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Motor button
        self.motor_button = tk.Button(master, text="Book Motor",font= ("Lucida Console", 12),  bg="#FFFFFF", height=2, width=35, command=self.open_motor_booking_window)
        self.motor_button.place(relx=0.50, rely=0.49,anchor="center")


        # Car frame
        self.car_frame = tk.Frame(master,  borderwidth=3, relief="groove")
        self.car_frame.place(relx= 0.83, rely= 0.3,  relwidth=0.3, relheight=0.3, anchor="center")
       
        #  Car icon
        self.car_img = tk.PhotoImage(file='car.png')
        self.car_image_label = tk.Label(self.car_frame, image=self.car_img, bg="#C8E7F5")
        self.car_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Car button
        self.car_button = tk.Button(master, text="Book Car",font= ("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command=self.open_car_booking_window)
        self.car_button.place(relx=0.83, rely=0.49,anchor="center")


        # Taxi cab frame
        self.taxi_cab_frame = tk.Frame(master,  borderwidth=3, relief="groove")
        self.taxi_cab_frame.place(relx= 0.50, rely= 0.7,  relwidth=0.3, relheight=0.3, anchor="center")

        # Taxi cab icon
        self.taxi_cab_img = tk.PhotoImage(file='taxicab.png')
        self.taxi_cab_image_label = tk.Label(self.taxi_cab_frame, image=self.taxi_cab_img, bg="#C8E7F5")
        self.taxi_cab_image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Taxi cab button
        self.taxi_cab_button = tk.Button(master, text="Book Taxi Cab",font= ("Lucida Console", 12),  bg="#FFFFFF", height=2, width=35, command=self.open_taxi_booking_window)
        self.taxi_cab_button.place(relx=0.50, rely=0.89,anchor="center")


        # Premium cab frame
        self.prem_cab_frame = tk.Frame(master,  borderwidth=3, relief="groove")
        self.prem_cab_frame.place(relx= 0.83, rely= 0.7,  relwidth=0.3, relheight=0.3, anchor="center")
        
        # Premium cab icon
        self.prem_cab_img = tk.PhotoImage(file='premcab.png')
        self.prem_cab_image_label = tk.Label(self.prem_cab_frame, image=self.prem_cab_img, bg= "#C8E7F5")
        self.prem_cab_image_label.place(relx=0.5, rely=0.5,  anchor="center")

        # Premium cab button
        self.prem_cab_button = tk.Button(master, text="Book Premium Cab",font= ("Lucida Console", 12), bg="#FFFFFF", height=2, width=35, command= self.open_premium_booking_window)
        self.prem_cab_button.place(relx=0.83, rely=0.89,anchor="center")


        # Profile button
        self.profile_button = tk.Button(master,  text="PROFILE",font= ("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.profile_button.place(relx=0.30, rely=0.15,anchor="ne")

        # Bookings button
        self.bookings_button = tk.Button(master, text="BOOKINGS",font= ("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.bookings_button.place(relx=0.30, rely=0.30,anchor="ne")

        # History button
        self.history_button = tk.Button(master,  text="HISTORY",font= ("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.history_button.place(relx=0.30, rely=0.45,anchor="ne")

        # Feedback button
        self.feedback_button = tk.Button(master,  text="FEEDBACK",font= ("Candara", 20, "bold"), height=2, width=20, bg="#FFFFFF")
        self.feedback_button.place(relx=0.30, rely=0.60,anchor="ne")

        # Log-out Button
        self.out_button = tk.Button(master,text= "LOG OUT", font= ("Candara", 20, "bold"), height=2, width=20, fg="#FFFFFF", bg= "#000000")
        self.out_button.place(relx=0.30, rely=0.75,anchor="ne")



    # Bind the label and frame together
        self.prem_cab_frame.bind("<Configure>", self.on_frame_configure)
        self.prem_cab_image_label.bind("<Configure>", self.on_label_configure)


    def on_frame_configure(self, event):
        # Get the new size of the frame
        width = event.width
        height = event.height

        # Adjust the size of the label to match the frame
        self.prem_cab_image_label.config(width=width, height=height)
        self.motor_image_label.config(width=width, height=height)
        self.car_image_label.config(width=width, height=height)
        self.taxi_cab_image_label.config(width=width, height=height)

    def on_label_configure(self, event):
        # Get the new size of the label
        width = event.width
        height = event.height

        # Adjust the size of the frame to match the label
        self.prem_cab_frame.config(width=width, height=height)
        self.motor_image_label.config(width=width, height=height)
        self.car_image_label.config(width=width, height=height)
        self.taxi_cab_image_label.config(width=width, height=height)


    def open_motor_booking_window(self):
        # Open the booking window for motor
        booking_window = BookingWindow(self.master, "Motor")

    def open_car_booking_window(self):
        # Open the booking window for car
        booking_window = BookingWindow(self.master, "Car")

    def open_taxi_booking_window(self):
        # Open the booking window for taxi cab
        booking_window = BookingWindow(self.master, "Taxi Cab")

    def open_premium_booking_window(self):
        # Open the booking window for premium cab
        booking_window = BookingWindow(self.master, "Premium Cab")






       
      

root = tk.Tk()
app = RideApp(root)
root.mainloop()

