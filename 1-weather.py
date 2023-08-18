import weather

ussd = input("Enter USSD ")

if(ussd == '*222#'):
    weather.weather()
else: 
    print("Invalid Code!")
