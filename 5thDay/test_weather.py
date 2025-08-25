import pandas as pd
weather_date={
	"location": "New York City",
	"forecast": [
		{
			"date": "2023-10-27",
			"time": "09:00:00",
			"temperature": 52.12,
			"feels_like": 50.5,
			"humidity": 79,
			"description": "overcast clouds",
			"wind_speed": 10.36,
			"wind_dir": 190
		},
		{
			"date": "2023-10-27",
			"time": "12:00:00",
			"temperature": 55,
			"feels_like": 54,
			"humidity": 75,
			"description": "light rain",
			"wind_speed": 12,
			"wind_dir": 195
		}
	]
}



forcast=weather_date['forecast']
print(forcast)
df= pd.DataFrame(forcast)
print(df)
max_temp=df['temperature'].max()
min_temp=df['temperature'].min()
print(max_temp)
print(min_temp)






