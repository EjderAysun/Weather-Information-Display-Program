# WEATHER INFORMATION DISPLAY PROGRAM
* This project is a simple weather information display program for Software Engineering (SE 226) term project.

---
## Table of Contents
  * [Table of Contents](#table-of-contents)
  * [General Info](#general-info)
  * [Screenshots](#screenshots)
  * [Technologies](#technologies)
  * [Setup](#setup)
  * [Features](#features)
  * [Status](#status)
  * [Inspiration](#inspiration)
  * [Version](#version)
  * [Contributors](#contributors)
  * [Licence & Copyright](#licence--copyright)

---
## General Info
* This application has been made by **adhering to a document**.
* This project is a *simple* **weather information display program**.

---
## Screenshots
![izmir_celcius](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248579184-167a13a8-6093-46d0-a576-cadcaae6539f.png)
![chernobyl_fahrenheit](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248579178-96dd39b9-b8de-4bb1-bf1a-601047beaaaf.png)

---
## Technologies
* Python 3.11.2
* os library
* datetime library
* tkinter library
* bs4 library
* requests library
* concurrent.futures library

---
## Setup

#### To install "beautifulsoup4" and "requests" library (if you don't have):
The "beautifulsoup4" and "requests" library were used in the project. In order to run the project successfully, these two libraries must be installed.

If the "beautifulsoup4" library is not installed, open CMD (Command Prompt) and type the following command to download and install it:
```
>pip install beautifulsoup4
```

If the "requests" library is not installed, open CMD (Command Prompt) and type the following command to download and install it:
```
>pip install requests
```

---
## Features / Evaluation

### **GUI Development Mission**

#### **Requirement I.** *"Use `Tkinter` or any other suitable GUI library to create the graphical interface for the program."*

We used the `Tkinter` library to create a graphical interface for our program. `Tkinter` proved to be a suitable library that met our requirements. With `Tkinter`, we were able to create `Combobox` *(dropdown list)*, `Entry` *(search entry)*, `Button` *(search button, Fahrenheit button, Celsius button)*, `PhotoImage` *(logo image and icons)*, `StringVar` *(variable for the selected city in the dropdown list)*, and `Labels`.

![image (1)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967048-7c8d3248-8298-4c17-a48f-6eaaa69887e1.png)

#### **Requirement II.** *"Design and implement a dropdown list to allow users to select a city."*

We have created a *dropdown list* (`Combobox`) for users to select a city. This list includes all cities in Turkey, with the first 6 cities followed by the rest in alphabetical order. The list displays 8 cities at a time to avoid overflowing onto other elements, and it includes a scroll button to navigate and see the remaining cities. By default, the list is closed and displays the text "***Select City***." If you have previously selected a city using this list, the text "***Select City***" will appear in *blue*, and the city you selected will be shown in the ***search field***. You can delete the selected city in the search field and *manually* enter a city using the keyboard. After doing so, if you click the search button, you will see the results for the city you entered. We added this functionality because the list only includes cities in Turkey. *If you want to search for a city outside of Turkey, you can use the search field.*

Before selecting *Adana*, it would look like this:  
![image (2)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967050-26c42021-140f-4ba9-a746-a2e1f6757ed8.png)

After selecting *Adana*, it would look like this:  
![image (3)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967051-5a0c22ac-82c3-4caf-a6d1-20b144270059.png)

If you use the search field, it would look like this:  
![image (4)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967053-451aada5-5de1-4c91-8815-357f4f618d90.png)

#### **Requirement III.** *"Create an area in the GUI to display the weather information."*

We have created the field as follows. When you look at the two examples below, you can see that the fields expand and contract based on the length of the displayed result, meaning they are *dynamic*.

![image (5)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967056-8a9a376c-5fbb-499f-ac8c-c064d1065f07.png)  
![image (6)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967059-4ed994c3-6d13-4c8d-ab3d-360c8df53782.png)

### **Retrieve Weather Data Information Mission**

#### **Requirement I.** *"Utilize the `requests` library to send HTTP requests and fetch the weather information from the internet. Choose a website as your resource."*

We used the `requests` library to send **HTTP requests** and **retrieve weather information** from the internet.

![image (7)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967065-c08fedcf-f604-4356-bd44-72bc9a5fa467.png)  
![image (8)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967067-8830640e-921d-4153-ae84-03b6b9ade52e.png)  
![image (9)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967068-8f673144-aa32-4caa-b84e-1e701294027d.png)

#### **Requirement II.** *"Use the `beautifulsoup4` library to parse the HTML content and extract the necessary weather data for the chosen city."*
![image (10)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967071-5c323b73-2577-446c-ab6a-5ae5f6670147.png)

You can find more detailed information about this topic in the *upcoming sections*.

### **Store and Display Weather Information Mission**

#### **Requirement I.** *"Utilize Python data structures, such as lists and dictionaries, to store the weather data retrieved from the internet."*

**Dictionary** and **list structures** have been used extensively in various parts of the project. 

![image (11)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967072-99566027-a164-4699-a86c-3069e3a6b8a6.png)  
![image (12)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967076-8c0c8c21-9f40-42e9-a42c-4a610d22e65f.png)  
![image (13)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967078-d49eda00-c1fa-45b6-8754-fccf7406680e.png)

#### **Requirement II.** *"Create a display area in the GUI to present the weather information."*

View areas have been created using the following methods and have been filled/modified as needed.

![image (14)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967081-68192014-6f70-4683-ba61-ec6d14c94b4d.png)  
![image (15)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967096-a72075f8-ba39-48bd-96dd-0855e3c91355.png)

#### **Requirement III.** *"Show the weather information for the chosen city, including the temperature (day and night) and wind speed for the next three days."*

Weather information has been displayed as follows and detailed explanations have been provided in the [Additional Notes](#additional-notes) section.

![image (16)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967102-f69457aa-6329-4357-8600-609189a87914.png)

### **Temperature Conversion Mission**

#### **Requirement I.** *"Implement a button in the GUI that allows users to toggle between Celsius and Fahrenheit temperature units."*

As seen in the two screenshots below, you can perform real-time conversion between *Celsius* and *Fahrenheit*:  
![image (17)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967107-955fbdeb-38a8-47ff-af1d-75294215e8a2.png)  
![image (18)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967111-1bc74b73-6ac2-4767-afc0-dc7023dc6d04.png)

#### **Requirement II.** *"Include the necessary logic to convert the temperature values and update the displayed weather information accordingly."*

The required logic for this is in the `WeatherGUI` class and the methods are provided below. The explanation of the code will be given in the following section. Here, I just want to mention that the requirements have been met.

![image (19)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967116-408c9b0a-2a8d-42ec-8936-7036d86acbd4.png)  
![image (20)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967118-8b28160f-53ad-476d-a768-30f68319f6e7.png)  
![image (21)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967124-81b57142-5b09-4567-9cfc-cfa1c9f07968.png)

### **Save and Load User Preferences Mission**

#### **Requirement I.** *"Implement functionality to save the selected city and temperature unit to a Settings.txt file when the program is closed."*

Assuming that the program is in its current state and I'm closing the program: 
![image (22)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967128-85d3521f-9bff-4885-883f-aa510ed2f1bf.png)

After closing the program, the contents of the **Settings.txt** file are as follows:  
![image (23)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967131-a516e8a8-f7b8-4c18-8e4d-7059f4e6f0e5.png)

The city we were searching for is "*Dachau*".

Our preferred unit of temperature is *Celsius*. Temperature preference is not recorded as *Celsius* or *Fahrenheit*. It is recorded as "`isFahrenheit`" **boolean** value. This allows us to establish a more optimized structure as there are two possible values to be recorded. The methods that control this are provided in the 2nd requirement section of the previous heading and will be explained further in the following section.

The methods that enable saving are as follows:  
![image (24)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967133-1c2a5145-c3bc-4c0d-adb2-e5685dd1246e.png)

The methods should be used in the following order: `save_temp_pref()` and then `save_last_city()`.

#### **Requirement II.** *"When the program starts, check if the Settings.txt file exists."*
When the program starts, these methods are executed. There are control blocks at lines **28** and **41**, which check if the file exists.

![image (25)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967134-4cfc4da5-bb6a-4028-8f7b-083b4d7a13e9.png)

#### **Requirement III.** *"If the file exists, read the city and temperature unit preferences from the file and set them as the default."*

If there is a file, the code inside the "**if**" blocks reads the content of the file. If the files do not exist, the code inside the "**else**" blocks returns default values. In this case, if the files are not present, when the program is executed, you will see the weather values for the city of *Izmir* with the temperature unit set to *Celsius*.

![image (26)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967136-78a4abca-32c3-43c0-9559-32c398448b7c.png)

#### **Requirement IV.** *"If the file does not exist or the preferences cannot be read, start with an empty city and the default temperature unit."*

As stated in *Requirement III*, if the file is not present or preferences cannot be read, the program does not start with an empty city or default temperature unit. The default values we have defined are *Celsius* and *Izmir*.

### Additional Notes:
- *"Provide error handling mechanisms to handle situations where the internet connection is unavailable, or the weather data cannot be retrieved."*

    - These mechanisms are available in the `WeatherInfo` class. Even in the case of errors occurring while the program is running, the program doesn't crash; it indicates the error in the terminal. The user continues to see the information of the last searched city until they enter/select a meaningful query.

- *"Enhance the GUI by including appropriate labels, buttons, and user friendly elements to improve the overall user experience."*

    - Although our *user interface* is not perfect, it has some user-friendly features.
    - The selected temperature unit is indicated in *light blue* color.
    - If the last selected query was chosen from a *dropdown list*, the *dropdown list* is highlighted in *blue* color.
    - Weather conditions are represented with *icons*, and most common weather conditions have corresponding icons. If there is *no suitable icon*, *no icon* is displayed, but the rows and screen layout remain intact. Weather icons are taken from Google.
    - There is a logo in the top left corner indicating that it is a *weather application*.

        ![image (27)](https://github-production-user-asset-6210df.s3.amazonaws.com/71559273/248967041-259f92c2-0159-42a3-88a6-fd6438943a83.png)

- *"Consider adding additional features, such as displaying weather icons, sunrise/sunset times, or extended forecasts, to make the program more comprehensive and informative. Better GUI may result in bonus points up to 15."* 
    - In addition to the features mentioned above, the information will be displayed to include "current" and "next 3 days".

    - #### Features for now:
        - Location, current temperature, humidity, precipitation rate, wind speed (in km/h), and an icon indicating the current weather forecast will be displayed.

    - #### Features for the next 3 days:
        - For each relevant weather condition, the specific day it applies to, daytime and nighttime temperature values, precipitation rate, humidity, wind speed (in km/h), weather information for that day, and a corresponding icon will be displayed.
        - Location won't be specified because the current value already indicates the location.

*"Important: If you can not retrieve the weather data from the internet for some reason. Use same logic as User Preferences. Write some data you have generated to a text file to be read in the program and simulate the program. However, do not forget, this will make your group lose points from Retrieve Weather Data task."*

- Please note that the program has not been simulated. Although the data may not have been retrieved professionally, it is still obtained from the internet.

*According to this evaluation, out of 14 requirements of the project, 13 have been met (except for the 4th requirement under the "Save and Load User Preferences" section, which was not fulfilled and the reason was explained above), and all 3 non-essential additional aspects have been fulfilled. If we only consider the necessary requirements, approximately 92.86% of the requirements have been met.*

---
## Status
With the exception of bug fixes (if any), development of this project is complete.

---
## Inspiration
Software Engineering 226 (SE 226) Project Instructions (Izmir University of Economics, 2023, SE 226 course, Spring semester project document)
  
As a student of the Izmir University of Economics, I made this project in accordance with the SE 226 Project Instructions for the spring semester project of the SE 226 course in 2023.
  
The project conforms almost exactly to the document.
  
Since the content of the SE 226 projects that will be given in the next periods may be similar to this document, I can not share the document publicly. If you have an ethical responsibility based on this or a similar course, assignment, or task, please use this as an opinion only. If you have a question or need more information about the project, send an email to me: <ejderaysunn@gmail.com>

---
## Version
**Version 1.0.0**  

---
## Contributors

### At every stage of the project:
#### Team Members:  
&ensp;&ensp;&ensp;Ejder Aysun <ejderaysunn@gmail.com>  
&ensp;&ensp;&ensp;Murat Vermez  <muratholiday@outlook.com>  
&ensp;&ensp;&ensp;Bartu Nurgün  <bartunurgun.2@gmail.com>  

SE 226 Course Coordinator and Course Lecturer, [Assoc. Prof. Senem KUMOVA METİN](https://people.ieu.edu.tr/en/senemkumovametin/main)  
SE 226 Course Assistant, [Res. Asst. Erdem Okur](https://people.ieu.edu.tr/en/erdemokur/main)  

---
## Licence & Copyright
© Ejder Aysun, Weather Information Display Program  
Licensed under the [MIT Licence](https://github.com/EjderAysun/Weather-Information-Display-Program/blob/main/LICENCE)