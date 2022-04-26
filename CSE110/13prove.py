tempature = int(input("What is the temperature? "))

wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (speed ** 0.16)) + (0.4275 * temp * (speed ** 0.16))