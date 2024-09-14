import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Entry, Button, Label


class TemperatureConverter:
    def __init__(self):
        self.style = Style(theme="darkly")

        self.window = self.style.master
        self.window.title("Temperature Converter")

        self.temperature_label = Label(
            self.window, text="Enter temperature:", font=("Arial", 12)
        )
        self.temperature_label.pack(pady=10, padx=20)

        self.temperature_entry = Entry(self.window, width=20)
        self.temperature_entry.pack(pady=5)

        self.unit_label = Label(
            self.window, text="Enter unit (C/F):", font=("Arial", 12)
        )
        self.unit_label.pack(pady=10)

        self.unit_entry = Entry(self.window, width=20)
        self.unit_entry.pack(pady=5)

        self.convert_button = Button(
            self.window,
            text="Convert",
            command=self.convert_temperature,
        )
        self.convert_button.pack(pady=10)

        self.output_label = Label(self.window, text="", font=("Arial", 12))
        self.output_label.pack(pady=10)

    def convert_temperature(self):
        try:
            temperature = float(self.temperature_entry.get())
            unit = self.unit_entry.get().upper()
            if unit not in "CF":
                self.output_label.config(text="Please enter a valid unit")
                return
            if unit == "C":
                converted_temp = (temperature * 9 / 5) + 32
                self.output_label.config(
                    text=f"{temperature}°C is {converted_temp:.2f}°F"
                )
            elif unit == "F":
                converted_temp = (temperature - 32) * 5 / 9
                self.output_label.config(
                    text=f"{temperature}°F is {converted_temp:.2f}°C"
                )
        except ValueError:
            self.output_label.config(text="Please enter a valid number")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    converter = TemperatureConverter()
    converter.run()
