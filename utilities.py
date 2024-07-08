import requests,datetime,random

# Function to return date and time
def get_date():
    date=datetime.datetime.now().strftime("%H:%M - %d / %m / %Y").split("-")
    return date

# Function to retrieve weather data from an open source api
def get_weather():
    try:
        city="kashipur"
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key=FUMBF9Q526Q7BA7JFU2TNR9CA"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
            "address":data['resolvedAddress'],
            "timezone":data['timezone'],
            "desc":data['description'],
            "temp":data['days'][0]['temp'],
            }
        return weather_data
    except Exception as e:
        return e

# Function to generate random quote
def generate_quote():
    quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Believe you can and you're halfway there. - Theodore Roosevelt"
]
    return random.choice(quotes)


# Function for form validation
def form_validate(email,password):
    small, cap, num, spec = 0,0,0,0
    valid_chars = ['!','@','#','$','%','&']
    if "@" not in email or ".com" not in email:
        return "Invalid Email"
    elif password!="":
        for i in password:
            if i >= 'a' and i <= 'z':
                small+=1
            elif i >= 'A' and i <= 'Z':
                cap+=1
            elif i in ['0','1','2','3','4','5','6','7','8','9']:
                num+=1
            elif i in valid_chars:
                spec+=1
            else:
                return False
            
    if small!=0 and cap!=0 and num!=0 and spec!=0 and small+cap+num+spec == len(password):
        return True
