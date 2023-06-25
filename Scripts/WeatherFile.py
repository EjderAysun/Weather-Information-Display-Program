import os
import datetime

class WeatherFile:

    def __init__(self):
        pass
    
    def save_temp_pref(self, isFahr):
        with open('Records\Settings.txt', 'r') as f:
            lines = f.readlines()
        with open('Records\Settings.txt', 'w') as f:
            if len(lines) > 0:
                f.write(lines[0])
            f.write(f'{isFahr}')

    def save_last_city(self, city):
        with open('Records\Settings.txt', 'w') as f:
            f.write(f'{city}\n')

    def load_temp_pref(self):
        if os.path.exists('Records\Settings.txt'):
            with open('Records\Settings.txt', 'r') as f:
                lines = f.readlines()
                if(len(lines) > 1):
                    isFahr = lines[1].strip()
                    if (isFahr == 'True'):
                        return True
                else:
                    return False
        else:
            return False

    def load_last_city(self):
        if os.path.exists('Records\Settings.txt'):
            with open('Records\Settings.txt', 'r') as f:
                lines = f.readlines()
                city = lines[0].strip()
                if (city != ''):
                    return city
                else:
                    return "İzmir"
        else:
            return 'İzmir'
        
    def save_querys_result_with_time(self, text):
        with open('Records\Archive.txt', 'a') as f:
            current_time = datetime.datetime.now()
            f.write(f'{text}, Recorded at: {current_time}\n\n')