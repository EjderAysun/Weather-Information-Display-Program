import tkinter as tk
from tkinter import ttk
from WeatherInfo import WeatherInfo
from WeatherFile import WeatherFile

class WeatherGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Weather Information System")
        self.root.geometry("1300x600")
        # Configure the background color
        self.root.configure(bg="#E8F5FD")  # Light blue color
        self.is_fahrenheit = False  # Initial temperature unit is Celsius

        self.forecast_days = []
        self.now_forecast=[]
        self.forecast_day_temps = []
        self.forecast_night_temps = []
        self.forecast = []
        self.forecast_precipitation = []
        self.forecast_humidity = []
        self.forecast_wind_speed = []
        self.day_forecast_icons = []
        self.now_forecast_icons = []

        self.search_entry = None

        self.clear_with_periodic_clouds_icon = None
        self.cloudy_icon = None
        self.default_icon = None
        self.fog_icon = None
        self.partly_cloudy_icon = None
        self.rain_and_snow_icon = None
        self.rain_icon = None
        self.scattered_showers_icon = None
        self.showers_icon = None
        self.snow_showers_icon = None
        self.snow_icon = None
        self.sunny_icon = None
        self.thundershower_icon = None

        self.forecast_frame = tk.Frame(self.root)
        self.forecast_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.now_forecast_frame = tk.Frame(self.root)
        self.now_forecast_frame.grid(row=1, column=8, columnspan=4, padx=10, pady=10)

        self.celsius_button = None
        self.fahrenheit_button = None

        self.weather_data = list()
        self.now_weather_data = list()

        self.city_var = None

        self.WI = WeatherInfo()
        self.WF = WeatherFile()

        self.sq = None

    def build_GUI(self):
        # Create and place logo at the top left
        self.logo_image = tk.PhotoImage(file="Icons\logo.png")
        logo_label = tk.Label(self.root, image=self.logo_image)
        logo_label.image = self.logo_image  # this line is added to keep a reference to the image
        logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Create toggle buttons for temperature units
        self.fahrenheit_button = tk.Button(self.root, text="Fahrenheit", command=self.toggle_fahrenheit, bg="#E8F5FD")
        self.fahrenheit_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.celsius_button = tk.Button(self.root, text="Celsius", command=self.toggle_celsius, bg="#AED6F1")
        self.celsius_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Create search entry field
        self.search_entry = tk.Entry(self.root, width=30)
        self.search_entry.grid(row=0, column=4, padx=10, pady=10)

        # Create search button
        search_button = tk.Button(self.root, text="Search", command = self.get_weather)
        search_button.grid(row=0, column=4, padx=10, pady=10, sticky="e")

        self.city_var = tk.StringVar(self.root)
        self.city_var.set("Select City")

        self.city_var.trace("w", self.city_var_changed) # TRACE

        all_cities_in_turkiye = ['İzmir', 'İstanbul', 'Ankara', 'Antalya', 'Eskişehir', 'Bursa', 'Adana', 'Adıyaman', 'Afyon', 
                                'Ağrı', 'Aksaray', 'Amasya', 'Artvin', 'Aydın', 'Balıkesir', 'Bartın', 'Batman', 'Bayburt',
                                'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Çanakkale', 'Çankırı', 'Çorum', 'Denizli',
                                'Diyarbakır', 'Düzce', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Gaziantep', 'Giresun',
                                'Gümüşhane', 'Hakkari', 'Hatay', 'Iğdır', 'Isparta', 'Kahramanmaraş', 'Karabük', 'Karaman',
                                'Kars', 'Kastamonu', 'Kayseri', 'Kırıkkale', 'Kırklareli', 'Kırşehir', 'Kilis', 'Kocaeli',
                                'Konya', 'Kütahya', 'Malatya', 'Manisa', 'Mardin', 'Mersin', 'Muğla', 'Muş', 'Nevşehir',
                                'Niğde', 'Ordu', 'Osmaniye', 'Rize', 'Sakarya', 'Samsun', 'Siirt', 'Sinop', 'Sivas',
                                'Şanlıurfa', 'Şırnak', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Uşak', 'Van', 'Yalova',
                                'Yozgat', 'Zonguldak']

        # city_dropdown = tk.OptionMenu(self.root, self.city_var, *all_cities_in_turkiye)
        # city_dropdown.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        city_dropdown = ttk.Combobox(self.root, textvariable=self.city_var, values=all_cities_in_turkiye, height=8, state="readonly")
        city_dropdown.grid(row=0, column=3, padx=10, pady=10, sticky="w")
        # city_dropdown.pack()

        # Placeholder weather icons
        self.clear_with_periodic_clouds_icon = tk.PhotoImage(file="Icons\clear_with_periodic_clouds.png")
        self.cloudy_icon = tk.PhotoImage(file="Icons\cloudy.png")
        self.default_icon = tk.PhotoImage(file="Icons\default.png")
        self.fog_icon = tk.PhotoImage(file="Icons\\fog.png")
        self.partly_cloudy_icon = tk.PhotoImage(file="Icons\partly_cloudy.png")
        self.rain_and_snow_icon = tk.PhotoImage(file="Icons\\rain_and_snow.png")
        self.rain_icon = tk.PhotoImage(file="Icons\\rain.png")
        self.scattered_showers_icon = tk.PhotoImage(file="Icons\scattered_showers.png")
        self.showers_icon = tk.PhotoImage(file="Icons\showers.png")
        self.snow_icon = tk.PhotoImage(file="Icons\snow.png")
        self.snow_showers_icon = tk.PhotoImage(file="Icons\snow_showers.png")
        self.sunny_icon = tk.PhotoImage(file="Icons\sunny.png")
        self.thundershower_icon = tk.PhotoImage(file="Icons\\thundershower.png")

        self.get_forecast_icons_for_days()
        self.get_forecast_icons_for_now()

        self.is_fahrenheit = self.WF.load_temp_pref()

        selected_city = self.WF.load_last_city()
        self.search_entry.insert(0, selected_city)
        self.get_weather()

    def city_var_changed(self, *args):
        selected_city = self.city_var.get()
        if selected_city != "Select City":
            self.search_entry.delete(0, tk.END)
            self.search_entry.insert(0, selected_city)
            self.get_weather()
            self.city_var.set("Select City")

    def get_weather(self):
        self.get_weather_for_days()
        self.get_weather_for_now()

        if self.is_fahrenheit:
            self.toggle_fahrenheit()
        else:
            self.toggle_celsius()

    def get_weather_for_days(self):
        search_query = self.search_entry.get()
        self.sq = search_query

        self.WI.get_initial_infos(search_query)
        self.WI.high_level_simultaneous_information_generator(search_query)

        daysInfos = list()
        daysInfos = self.WI.get_days_infos()

        # Placeholder weather data for demonstration
        weather_data = [
            {"Day", "Day Temperature", "Night Temperature", "Day Precipitation", "Day Humidity", "Day Wind Speed", "Day Forecast"},
            {"Day": daysInfos[0][0], "Day Temp": daysInfos[1][0], "Night Temp": daysInfos[2][0], "Day Precipitation": daysInfos[4][0], "Day Humidity": daysInfos[5][0], "Day Wind Speed": daysInfos[6][0], "Day Forecast": daysInfos[3][0]},
            {"Day": daysInfos[0][1], "Day Temp": daysInfos[1][1], "Night Temp": daysInfos[2][1], "Day Precipitation": daysInfos[4][1], "Day Humidity": daysInfos[5][1], "Day Wind Speed": daysInfos[6][1], "Day Forecast": daysInfos[3][1]},
            {"Day": daysInfos[0][2], "Day Temp": daysInfos[1][2], "Night Temp": daysInfos[2][2], "Day Precipitation": daysInfos[4][2], "Day Humidity": daysInfos[5][2], "Day Wind Speed": daysInfos[6][2], "Day Forecast": daysInfos[3][2]}
        ]
        self.weather_data = weather_data

        # Clear the previous forecast icons
        for icon_label in self.day_forecast_icons:
            icon_label.configure(image="")

        day_label = tk.Label(self.forecast_frame, text="Day".format(1))
        day_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        day_temps_label = tk.Label(self.forecast_frame, text="Day Temperature".format(1))
        day_temps_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        night_temps_label = tk.Label(self.forecast_frame, text="Night Temperature".format(1))
        night_temps_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        day_prec_label = tk.Label(self.forecast_frame, text="Precipitation".format(1))
        day_prec_label.grid(row=0, column=3, padx=10, pady=5, sticky="w")

        day_hm_label = tk.Label(self.forecast_frame, text="Humidity".format(1))
        day_hm_label.grid(row=0, column=4, padx=10, pady=5, sticky="w")

        day_ws_label = tk.Label(self.forecast_frame, text="Wind Speed".format(1))
        day_ws_label.grid(row=0, column=5, padx=10, pady=5, sticky="w")

        day_f_label = tk.Label(self.forecast_frame, text="Forecast".format(1))
        day_f_label.grid(row=0, column=6, padx=10, pady=5, sticky="w")

        # Update the forecast labels with new weather data
        for i in range(1, len(weather_data)):
            
            day_label = self.forecast_days[i-1]
            day_prec_label = self.forecast_precipitation[i-1]
            day_hm_label = self.forecast_humidity[i-1]
            day_ws_label = self.forecast_wind_speed[i-1]
            day_f_label = self.forecast[i-1]

            day_label.configure(text=weather_data[i]["Day"])
            #f_day_temps_label.configure(text=weather_data[i]["Day Temp"])
            #f_night_temps_label.configure(text=weather_data[i]["Night Temp"])
            day_prec_label.configure(text=weather_data[i]["Day Precipitation"])
            day_hm_label.configure(text=weather_data[i]["Day Humidity"])
            day_ws_label.configure(text=weather_data[i]["Day Wind Speed"])
            day_f_label.configure(text=weather_data[i]["Day Forecast"])

            # Update the forecast icon based on the weather condition
            weather_icon = self.get_weather_icon(weather_data[i]["Day Forecast"])
            self.day_forecast_icons[i-1].configure(image=weather_icon)
            self.day_forecast_icons[i-1].image = weather_icon

    def get_weather_for_now(self):
        
        nowInfos = list()
        nowInfos = self.WI.get_now_infos()
        print(nowInfos)

        now_weather_data = [
            {"Location": nowInfos[0], "Now Temp": nowInfos[1], "Now Precipitation": nowInfos[3], "Now Humidity": nowInfos[4], "Now Wind Speed": nowInfos[5], "Now Forecast": nowInfos[2]},
        ]
        self.now_weather_data = now_weather_data

        for icon_label in self.now_forecast_icons:
            icon_label.configure(image="")

        self.now_forecast_frame.grid(row=1, column=4, columnspan=4, padx=10, pady=10)

        now_loc_label = tk.Label(self.now_forecast_frame, text="Location".format(1))
        now_loc_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        now_temp_label = tk.Label(self.now_forecast_frame, text="Now Temp".format(1))
        now_temp_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        now_prec_label = tk.Label(self.now_forecast_frame, text="Now Precipitation".format(1))
        now_prec_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        now_hm_label = tk.Label(self.now_forecast_frame, text="Now Humidity".format(1))
        now_hm_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        now_ws_label = tk.Label(self.now_forecast_frame, text="Now Wind Speed".format(1))
        now_ws_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        now_f_label = tk.Label(self.now_forecast_frame, text="Now Forecast".format(1))
        now_f_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")


        now_loc_label = self.now_forecast[0]
        now_temp_label = self.now_forecast[1]
        now_prec_label = self.now_forecast[2]
        now_hm_label = self.now_forecast[3]
        now_ws_label = self.now_forecast[4]
        now_f_label = self.now_forecast[5]

        now_loc_label.configure(text=now_weather_data[0]["Location"])
        now_temp_label.configure(text=now_weather_data[0]["Now Temp"])
        now_prec_label.configure(text=now_weather_data[0]["Now Precipitation"])
        now_hm_label.configure(text=now_weather_data[0]["Now Humidity"])
        now_ws_label.configure(text=now_weather_data[0]["Now Wind Speed"])
        now_f_label.configure(text=now_weather_data[0]["Now Forecast"])

        # Update the forecast icon based on the weather condition
        now_weather_icon = self.get_weather_icon(now_weather_data[0]["Now Forecast"])
        self.now_forecast_icons[0].configure(image=now_weather_icon)
        self.now_forecast_icons[0].image = now_weather_icon

        self.WF.save_last_city(self.sq)

        print(self.WI.create_text_for_terminal())
        archive_output = self.WI.create_text_for_file()
        self.WF.save_querys_result_with_time(archive_output)

    def toggle_fahrenheit(self):
        self.is_fahrenheit = True
        # Set button colors
        self.fahrenheit_button.configure(bg="#AED6F1")
        self.celsius_button.configure(bg="#E8F5FD")

        for i in range(1, len(self.weather_data)):

            day_temps_label = self.forecast_day_temps[i-1]
            night_temps_label = self.forecast_night_temps[i-1]

            day_temp_c = self.weather_data[i]["Day Temp"]
            night_temp_c = self.weather_data[i]["Night Temp"]
            day_temp_f = self.celc_to_fahr(day_temp_c)
            night_temp_f = self.celc_to_fahr(night_temp_c)
            day_temps_label.configure(text="{}°F".format(day_temp_f))
            night_temps_label.configure(text="{}°F".format(night_temp_f))

        now_temp_label = self.now_forecast[1]
        now_temp_c = self.now_weather_data[0]["Now Temp"]
        now_temp_f = self.celc_to_fahr(now_temp_c)
        now_temp_label.configure(text="{}°F".format(now_temp_f))

    def toggle_celsius(self):
        self.is_fahrenheit = False
        # Set button colors
        self.celsius_button.configure(bg="#AED6F1")
        self.fahrenheit_button.configure(bg="#E8F5FD")

        for i in range(1, len(self.weather_data)):

            day_temps_label = self.forecast_day_temps[i-1]
            night_temps_label = self.forecast_night_temps[i-1]

            day_temp_c = self.weather_data[i]["Day Temp"]
            night_temp_c = self.weather_data[i]["Night Temp"]

            day_temps_label.configure(text="{}°C".format(day_temp_c))
            night_temps_label.configure(text="{}°C".format(night_temp_c))

        now_temp_label = self.now_forecast[1]
        now_temp_c = self.now_weather_data[0]["Now Temp"]
        now_temp_label.configure(text="{}°C".format(now_temp_c))

    def celc_to_fahr(self, celc_temp):
        return int(float(celc_temp) * 1.8 + 32)

    def get_weather_icon(self, weather):

        # Placeholder function to return the weather icon based on the weather condition
        if weather == "Partly cloudy" or weather == "Mostly cloudy" or weather == "Mostly sunny":
            return self.partly_cloudy_icon
        elif weather == "Scattered showers" or weather == "Scattered thunderstorms":
            return self.scattered_showers_icon
        elif weather == "Showers" or weather == "Light rain showers":
            return self.showers_icon
        elif weather == "Sunny" or weather == "Clear":
            return self.sunny_icon
        elif weather == "Clear with periodic clouds":
            return self.clear_with_periodic_clouds_icon
        elif weather == "Cloudy":
            return self.cloudy_icon
        elif weather == "Rain and snow":
            return self.rain_and_snow_icon
        elif weather == "Rain":
            return self.rain_icon
        elif weather == "Snow showers":
            return self.snow_showers_icon
        elif weather == "Snow":
            return self.snow_icon
        elif weather == "Thundershower":
            return self.thundershower_icon
        elif weather == "Fog":
            return self.fog_icon
        else:
            return self.default_icon

    def get_forecast_icons_for_days(self):
        for i in range(0, 3):

            day_label = tk.Label(self.forecast_frame)
            day_label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
            self.forecast_days.append(day_label)

            day_temps_label = tk.Label(self.forecast_frame)
            day_temps_label.grid(row=i+1, column=1, padx=10, pady=5, sticky="w")
            self.forecast_day_temps.append(day_temps_label)

            night_temps_label = tk.Label(self.forecast_frame)
            night_temps_label.grid(row=i+1, column=2, padx=10, pady=5, sticky="w")
            self.forecast_night_temps.append(night_temps_label)

            day_prec_label = tk.Label(self.forecast_frame)
            day_prec_label.grid(row=i+1, column=3, padx=10, pady=5, sticky="w")
            self.forecast_precipitation.append(day_prec_label)

            day_hm_label = tk.Label(self.forecast_frame)
            day_hm_label.grid(row=i+1, column=4, padx=10, pady=5, sticky="w")
            self.forecast_humidity.append(day_hm_label)

            day_ws_label = tk.Label(self.forecast_frame)
            day_ws_label.grid(row=i+1, column=5, padx=10, pady=5, sticky="w")
            self.forecast_wind_speed.append(day_ws_label)

            day_f_label = tk.Label(self.forecast_frame)
            day_f_label.grid(row=i+1, column=6, padx=10, pady=5, sticky="w")
            self.forecast.append(day_f_label)

            weather_icon_label = tk.Label(self.forecast_frame)
            weather_icon_label.grid(row=i+1, column=7, padx=10, pady=5)
            
            self.day_forecast_icons.append(weather_icon_label)

    def get_forecast_icons_for_now(self):

        now_loc_label = tk.Label(self.now_forecast_frame)
        now_loc_label.grid(row=0, column=4, padx=10, pady=5, sticky="w")
        self.now_forecast.append(now_loc_label)

        now_temp_label = tk.Label(self.now_forecast_frame)
        now_temp_label.grid(row=1, column=4, padx=10, pady=5, sticky="w")
        self.now_forecast.append(now_temp_label)

        now_prec_label = tk.Label(self.now_forecast_frame)
        now_prec_label.grid(row=2, column=4, padx=10, pady=5, sticky="w")
        self.now_forecast.append(now_prec_label)

        now_hm_label = tk.Label(self.now_forecast_frame)
        now_hm_label.grid(row=3, column=4, padx=10, pady=5, sticky="w")
        self.now_forecast.append(now_hm_label)

        now_ws_label = tk.Label(self.now_forecast_frame)
        now_ws_label.grid(row=4, column=4, padx=10, pady=5, sticky="w")
        self.now_forecast.append(now_ws_label)

        now_f_label = tk.Label(self.now_forecast_frame)
        now_f_label.grid(row=5, column=4, padx=10, pady=5, sticky="w")
        self.now_forecast.append(now_f_label)

        now_weather_icon_label = tk.Label(self.now_forecast_frame)
        now_weather_icon_label.grid(row=6, column=4, padx=10, pady=5)

        self.now_forecast_icons.append(now_weather_icon_label)

    def run(self):
        self.root.mainloop()
        self.WF.save_temp_pref(self.is_fahrenheit)

if __name__ == "__main__":
    app = WeatherGUI()
    app.run()