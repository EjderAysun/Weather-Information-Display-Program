from bs4 import BeautifulSoup
import requests
import concurrent.futures

class WeatherInfo:

    def __init__(self):
        self.session = requests.Session() # optimization 1

        self.soup = None
        self.location = None
        self.day_list = None
        self.days_text_list = None

        self.now_temp = None
        self.now_forecast = None
        self.now_precipitation = None
        self.now_humidity = None
        self.now_wind_speed = None

        self.day_temp_list = list()
        self.night_temp_list = list()
        self.day_forecast_list = list()
        self.precipitation_list = list()
        self.humidity_list = list()
        self.wind_speed_list = list()

        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5672.127 Safari/537.3'
    }

    def get_soup(self, search_query):
        try:
            sq = search_query
            sq += " weather"
            sq = sq.replace(" ", "+")
            res = self.session.get(
            f'https://www.google.com/search?q={sq}&oq={sq}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8&hl=en', headers = self.headers)
            return BeautifulSoup(res.text, 'html.parser')
        except Exception as e:
            print("An error occurred: ", str(e))

    def get_location(self):
        try:
            return self.soup.select('span.BBwThe')[0].getText().strip()
        except Exception as e:
            print("An error occurred: ", str(e))

    def get_day_list(self):
        try:
            return self.soup.select('div.wob_df[data-wob-di]')
        except Exception as e:
            print("An error occurred: ", str(e))

    def get_days_text_list(self):
        try:
            return [day.select_one('.Z1VzSb')['aria-label'] for day in self.day_list]
        except Exception as e:
            print("An error occurred: ", str(e))

    def get_data(self, day, day_text, search_query):

        def get_day_temp():
            try:
                return day.select_one('.gNCp2e span.wob_t').text
            except Exception as e:
                print("An error occurred: ", str(e))
                # return placeholder values if there's an error
                return 'No forecast'
            
        def get_night_temp():
            try:
                return day.select_one('.QrNVmd span.wob_t').text
            except Exception as e:
                print("An error occurred: ", str(e))
                # return placeholder values if there's an error
                return 'No forecast'
            
        def get_day_forecast():
            try:
                return day.select_one('.YQ4gaf').get('alt')
            except Exception as e:
                print("An error occurred: ", str(e))
                # return placeholder values if there's an error
                return 'No forecast'

        def get_pp_hm_ws():
            try:
                soup = self.get_soup("%s+%s" %(search_query, day_text))
                precipitation = soup.find('span', id='wob_pp').text
                humidity = soup.find('span', id='wob_hm').text
                wind_speed = soup.find('span', id='wob_ws').text
                return [precipitation, humidity, wind_speed]
            except Exception as e:
                print("An error occurred: ", str(e))
                # return placeholder values if there's an error
                return ['No forecast', 'No forecast', 'No forecast']

        return get_day_temp(), get_night_temp(), get_day_forecast(), get_pp_hm_ws()

    def get_now_temp(self):
        try:
            return self.soup.select_one('span.q8U8x').text
        except Exception as e:
            print("An error occurred: ", str(e))

    def get_now_forecast(self):
        try:
            return self.soup.select_one('div.wob_dcp').text
        except Exception as e:
            print("An error occurred: ", str(e))

    def get_now_pp(self):
        try:
            precipitation = self.soup.select_one('#wob_pp').text
            return precipitation
        except Exception as e:
            print("An error occurred: ", str(e))

    def get_now_hm(self):
        try:
            humidity = self.soup.select_one('#wob_hm').text
            return humidity
        except Exception as e:
            print("An error occurred: ", str(e))

    def get_now_ws(self):
        try:
            wind_speed = self.soup.select_one('#wob_ws').text
            #wind_speed = wind_speed.replace(' km/h', '')
            return wind_speed
        except Exception as e:
            print("An error occurred: ", str(e))

    def get_initial_infos(self, search_query):
        self.soup = self.get_soup(search_query)
        self.location = self.get_location()
        self.day_list = self.get_day_list()[1:4] # next 3 days
        self.days_text_list = self.get_days_text_list()

    def get_now_info(self):
        self.now_temp = self.get_now_temp()
        self.now_forecast = self.get_now_forecast()
        self.now_precipitation = self.get_now_pp()
        self.now_humidity = self.get_now_hm()
        self.now_wind_speed = self.get_now_ws()
        

    def high_level_simultaneous_information_generator(self, search_query): # :D
        results = list()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            #results = executor.map(lambda x: self.get_data(*x, search_query), zip(self.day_list, self.days_text_list))
            results = executor.map(self.get_data, self.day_list, self.days_text_list, [search_query]*3)

        self.day_temp_list=list()
        self.night_temp_list=list()
        self.day_forecast_list=list()
        self.precipitation_list=list()
        self.humidity_list=list()
        self.wind_speed_list=list()

        for day_temp, night_temp, day_forecast, pp_hm_ws_list in results:
            self.day_temp_list.append(day_temp)
            self.night_temp_list.append(night_temp)
            self.day_forecast_list.append(day_forecast)
            self.precipitation_list.append(pp_hm_ws_list[0])
            self.humidity_list.append(pp_hm_ws_list[1])
            self.wind_speed_list.append(pp_hm_ws_list[2])

    def get_now_infos(self):
        self.get_now_info()
        return self.location, self.now_temp, self.now_forecast, self.now_precipitation, self.now_humidity, self.now_wind_speed

    def get_days_infos(self):
        return self.days_text_list, self.day_temp_list, self.night_temp_list, self.day_forecast_list, self.precipitation_list, self.humidity_list, self.wind_speed_list

    def celc_to_fahr(self, celc_temp):
        return celc_temp * 1.8 + 32
    
    def kmh_to_mph(self, kmh):
        return kmh * 0.62137
    
    def create_text_for_terminal(self):

        try:
            mph_now = str(self.kmh_to_mph(float(self.now_wind_speed.split()[0]))) + " mph"
        except:
            mph_now = "No Forecast"

        output = """
            On Now,
            \033[4mIn the location of %s:\033[0m\n
            A temperature is \033[1m%s°C/%sF\033[0;0m now.
            \033[32mAt the moment it is \x1B[3m%s\x1B[0m\033[32m.\033[00m
            \033[36mThe precipitation rate is \033[1m%s\033[0;0m\033[36m now.\033[00m
            \033[36mThe humidity rate is \033[1m%s\033[0;0m\033[36m now.\033[00m
            \033[36mThe wind speed rate is \033[1m%s / %s\033[0;0m\033[36m now.\033[00m

        """     %(self.location, 
                self.now_temp, 
                self.celc_to_fahr(float(self.now_temp)), 
                self.now_forecast,
                self.now_precipitation,
                self.now_humidity,
                self.now_wind_speed,
                mph_now)

        count = len(self.days_text_list)

        try:
            mph = str(self.kmh_to_mph(float(self.wind_speed_list[i].split()[0]))) + " mph"
        except:
            mph = "No Forecast"

        for i in range(count):
            output += """On %s,
        \033[34mA temperature of \033[1m%s°C/%sF\033[0;0m \033[34mis expected at day.\033[00m 
        \033[30mA temperature of \033[1m%s°C/%sF\033[0;0m \033[30mis expected at night.\033[00m
        \033[32mThe day will be \x1B[3m%s\x1B[0m\033[32m.\033[00m
        \033[36mThe precipitation rate is \033[1m%s\033[0;0m\033[36m.\033[00m
        \033[36mHumidity is \033[1m%s\033[0;0m\033[36m.\033[00m
        \033[36mThe average wind speed is \033[1m%s / %s\033[0;0m\033[36m.\033[00m
        """ %(self.days_text_list[i], 
            self.day_temp_list[i], 
            self.celc_to_fahr(float(self.day_temp_list[i])),
            self.night_temp_list[i], 
            self.celc_to_fahr(float(self.night_temp_list[i])), 
            self.day_forecast_list[i], 
            self.precipitation_list[i], 
            self.humidity_list[i], 
            self.wind_speed_list[i],
            mph)

        return output
    
    def create_text_for_file(self):

        try:
            mph_now = str(self.kmh_to_mph(float(self.now_wind_speed.split()[0]))) + " mph"
        except:
            mph_now = "No Forecast"

        output = """ 
            On Now,
            In the location of %s:\n
            A temperature is %s°C/%sF now.
            At the moment it is %s.
            The precipitation rate is %s now.
            The humidity rate is %s now.
            The wind speed rate is %s / %s now.

        """     %(self.location, 
                self.now_temp, 
                self.celc_to_fahr(float(self.now_temp)), 
                self.now_forecast,
                self.now_precipitation,
                self.now_humidity,
                self.now_wind_speed,
                mph_now)

        count = len(self.days_text_list)

        for i in range(count):

            try:
                mph_day = str(self.kmh_to_mph(float(self.wind_speed_list[i].split()[0]))) + " mph"
            except:
                mph_day = "No Forecast"

            output += """On %s,
        A temperature of %s°C/%sF is expected at day.
        A temperature of %s°C/%sF is expected at night.
        The day will be %s.
        The precipitation rate is %s.
        Humidity is %s.
        The average wind speed is %s / %s.

        """ %(self.days_text_list[i], 
            self.day_temp_list[i], 
            self.celc_to_fahr(float(self.day_temp_list[i])),
            self.night_temp_list[i], 
            self.celc_to_fahr(float(self.night_temp_list[i])), 
            self.day_forecast_list[i], 
            self.precipitation_list[i], 
            self.humidity_list[i], 
            self.wind_speed_list[i],
            mph_day)

        output += "***************************************************"
        return output