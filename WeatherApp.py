import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO

Height = 600
Width = 500


def get_icon(weather):
    try:
        temp = (weather['main']['temp'])

        if (temp > 30):
            icon_url = 'https://img.icons8.com/color/96/000000/hot.png'
        elif (temp > 20):
            icon_url = 'https://img.icons8.com/color/96/000000/temperature.png'
        elif (temp > 10):
            icon_url = 'https://img.icons8.com/color/96/000000/temperature.png'
        elif (temp > 0):
            icon_url = 'https://img.icons8.com/color/96/000000/cold.png'
        else:
            icon_url = 'https://img.icons8.com/color/96/000000/cold.png'

        iconurl = requests.get(icon_url)
        icon_image = ImageTk.PhotoImage(Image.open(BytesIO(iconurl.content)))
    except:
        icon_url = 'https://img.icons8.com/color/96/000000/error--v1.png'
        iconurl = requests.get(icon_url)
        icon_image = ImageTk.PhotoImage(Image.open(BytesIO(iconurl.content)))
    return icon_image


def format_response(weather):
    try:
        name = (weather['name'])
        desc = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s \n' % (
            name, desc, temp)
    except:
        final_str = 'Couldn\'t retrieve data'

    return final_str


def get_weather(city):
    weather_key = 'edb1426225905c41780943f42792023a'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    ico_image = get_icon(weather)
    label_icon.configure(image=ico_image)
    label_icon.image = ico_image


root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack(fill='both', expand='true')

bgurl = requests.get(
    'https://images.wallpapersden.com/image/download/abstract-shapes-2021-minimalist_bG1lZm6UmZqaraWkpJRmbmdmrWZlbWY.jpg'
)
background_image = ImageTk.PhotoImage(Image.open(BytesIO(bgurl.content)))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#F4D03F', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('arial', 18), bg='#283747', fg='#FDFEFE')
entry.place(relwidth=0.69, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg='#E74C3C',
                   fg='#FDFEFE',
                   font=('arial', 10),
                   command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#F4D03F', bd=5)
lower_frame.place(relx=0.5,
                  rely=0.25,
                  relwidth=0.75,
                  relheight=0.6,
                  anchor='n')

label = tk.Label(lower_frame,
                 font=('arial', 18),
                 justify='left',
                 bg='#283747',
                 fg='white')
label.place(relwidth=1, relheight=0.7)

label_icon = tk.Label(lower_frame, bg='#283747')
label_icon.place(rely=0.7, relwidth=1, relheight=0.3)

root.mainloop()