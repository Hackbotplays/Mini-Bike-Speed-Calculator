import tkinter as tk

window = tk.Tk()
window.title("Z's Mini Bike Speed Calculator")
window.geometry("500x500")
window.configure(bg="#1e1e1e")

title = tk.Label(
    window,
    text="MINI BIKE SPEED CALCULATOR",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="#ff3333"
)
title.pack(pady=20)

# RPM TITLE COLOR
rpm_label = tk.Label(
    window,
    text="Engine RPM:",
    bg="#1e1e1e",
    fg="#ffffff",
    font=("Arial", 10)
)
rpm_label.pack()

rpm_entry = tk.Entry(
    window,
    bg="#2b2b2b",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief="flat"
)
rpm_entry.pack()

# CLUTCH TITLE COLOR
clutch_label = tk.Label(
    window,
    text="Clutch sprocket:",
    bg="#1e1e1e",
    fg="#ffffff",
    font=("Arial", 10)
)
clutch_label.pack()

clutch_entry = tk.Entry(
    window,
    bg="#2b2b2b",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief="flat"
)
clutch_entry.pack()

# REAR TITLE COLOR   
rear_label = tk.Label(
    window,
    text="Rear sprocket:",
    bg="#1e1e1e",
    fg="#ffffff",
    font=("Arial", 10)
)
rear_label.pack()

rear_entry = tk.Entry(
    window,
    bg="#2b2b2b",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief="flat"
)
rear_entry.pack()

# TIRE TITLE COLOR    
tire_label = tk.Label(
    window,
    text="Tire diameter (in.):",
    bg="#1e1e1e",
    fg="#ffffff",
    font=("Arial", 10)
)
tire_label.pack()

tire_entry = tk.Entry(
    window,
    bg="#2b2b2b",
    fg="#ffffff",
    insertbackground="#ffffff",
    relief="flat"
)
tire_entry.pack()


def calculate_speed():
    try:
        rpm = int(rpm_entry.get())
        clutch = int(clutch_entry.get())
        rear = int(rear_entry.get())
        tire = float(tire_entry.get())
    except ValueError:
        result_label.config(text="Invalid input! Please enter positive numbers. ")
        return
    if rpm <= 0 or clutch <= 0 or rear <= 0 or tire <= 0:
        result_label.config(text="Invalid input! Please enter positive numbers. ")
        return
    
    
    # GEAR RATIO SECTION
    ratio = rear / clutch

    # WHEEL RPM SECTION
    wheel_rpm = rpm / ratio

    # TIRE DIAMETER MATH
    circumference = tire * 3.14159
    inches_per_minute = wheel_rpm * circumference
    mph = inches_per_minute * 60 / 63360

    # DISPLAY RESULTS
    result_label.config(
        text=f"Gear Ratio: {ratio:.2f}:1\n"
             f"Wheel RPM: {wheel_rpm:.1f}\n"
             f"Estimated Speed: {mph:.1f} MPH"
    )


# RESULT LABEL
result_label = tk.Label(
    window,
    text="Results will appear here",
    bg="#2b2b2b",
    fg="#ffffff",
    font=("Arial", 11, "bold"),
    justify="left"
)

result_label.pack(pady=10, ipadx=10, ipady=5)

# CALCULATE BUTTON
button = tk.Button(
    window,
    text="Calculate",
    command=calculate_speed,
    bg="#ff3333",
    fg="#ffffff",
    font=("Arial", 11, "bold"),
    relief="flat",
)


button.pack()


window.mainloop()