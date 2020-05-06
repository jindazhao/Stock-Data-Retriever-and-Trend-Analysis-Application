import urllib.request
import json


class Stock:

    def return_all_data_stock(symbol):
        api_key = "G3UER06K80CNLHNV"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" \
              + str(api_key)
        data = urllib.request.urlopen(url)
        data = json.load(data)

        print("Data: " + data)


    def compare_lowest(symbol, date): # date must be in the form yyyy-mm-dd
        api_key = "G3UER06K80CNLHNV"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" \
              + str(api_key)
        data = urllib.request.urlopen(url)
        data = json.load(data)
        current = data["Time Series (Daily)"][date]["3. low"]
        lowest = float(data["Time Series (Daily)"][date]["3. low"])
        lowest_date = date
        for item, datte in data["Time Series (Daily)"].items():
            if float(datte["3. low"]) <= float(lowest):
                 lowest = datte["3. low"]
                 lowest_date = item


        print("Data: " + str(date) + "'s lowest is: " + str(current) + "$/per share compared to " + str(lowest_date) +
              " at " +
              str(lowest) + "$/per share")


    def today_data(symbol):
        api_key = "G3UER06K80CNLHNV"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" \
              + str(api_key)
        data = urllib.request.urlopen(url)
        data = json.load(data)
        iter(data["Time Series (Daily)"])

        print("Data: " + next(iter(data["Time Series (Daily)"].items())))

    def data_from_this_date(symbol, date):
        api_key = "G3UER06K80CNLHNV"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" \
              + str(api_key)
        data = urllib.request.urlopen(url)
        data = json.load(data)

        print("Data: " + data["Time Series (Daily)"][date])

    ## counts the number of lows repeated beneath a certain bracket the gives a percentage of how likely it will hit it
    def predict_low_of_next(symbol, today_date, percentage_in_integer): # the variable is how low it will go in percent form
        api_key = "G3UER06K80CNLHNV"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" \
              + str(api_key)
        datea = urllib.request.urlopen(url)
        data = json.load(datea)
        multiplier = (100 - percentage_in_integer) / 100

        percent_low = float(data["Time Series (Daily)"][today_date]["3. low"]) * multiplier

        counter = 0


        for item, date in data["Time Series (Daily)"].items():
            if float(date["3. low"]) <= float(percent_low):
                counter = counter + 1



        print("There is a " + str(counter / len(data["Time Series (Daily)"]) * 100) + "% likelihood of falling below " +
              str(percent_low) + "$")


        #return counter / len(data["Time Series (Daily)"] * 100)




    def predict_high(symbol, price):
        api_key = "G3UER06K80CNLHNV"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" \
              + str(api_key)
        datea = urllib.request.urlopen(url)
        data = json.load(datea)

        counter = 0

        for item, date in data["Time Series (Daily)"].items():
            if float(date["3. low"]) >= price:
                counter = counter + 1

        print("There is a " + str(counter / len(data["Time Series (Daily)"]) * 100) +
              "% likelihood of climbing to or above " + str(
            price) + "$")


    def predict_low(symbol, price):
        api_key = "G3UER06K80CNLHNV"
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&apikey=" \
              + str(api_key)
        datea = urllib.request.urlopen(url)
        data = json.load(datea)

        counter = 0

        for item, date in data["Time Series (Daily)"].items():
            if float(date["3. low"]) <= price:
                counter = counter + 1

        print("There is a " + str(counter / len(data["Time Series (Daily)"]) * 100) +
              "% likelihood of falling below " + str(price) + "$")

    print("Welcome to Jinda's Stock Data Python Application!")
    symbol = input("Please in a valid symbol in all caps: ")
    keep_going = True
    while keep_going:
        print("____________________________________________")
        print("Menu Options:                               |\nD - View All Data                           |" +
              "\nT - View Today's Data                       |\nC - Compare the Lowest Low                  |" +
                    "\nF - Retrieve Data From a Certain Date       |\nPP - Predict Lowest from Percentage         |" +
                    "\nPH - Predict Likelihood of the Highest Low  |\nPL - Predict Likelihood of the Lowest Low   |" +
                    "\nQ - Quit                                    |")
        print("                                            |")
        command = input("Please Choose one of the following: ")

        if command == "D":
            return_all_data_stock(symbol)
        elif command == "T":
            today_data(symbol)
        elif command == "C":
            date_today = input("Please input the today's date in the form yyyy-mm-dd: ")
            compare_lowest(symbol, date_today)
        elif command == "F":
            date_retrieved = input("Please input the date of which you would like to retrieve the data from in the " +
                               "form of yyyy-mm-dd: ")
            data_from_this_date(symbol, date_retrieved)
        elif command == "PP":
            percentage = input("Please input the drop in percentage that you would like predicted: ")
            date_today = input("Please input today's date in the form yyyy-mm-dd: ")
            predict_low_of_next(symbol, date_today, float(percentage))
        elif command == "PH":
            price = input("Please input the high price that you would like predicted: ")
            predict_high(symbol, price)
        elif command == "PL":
            price = input("Please input the low price that you would like predicted: ")
            predict_low(symbol, price)
        elif command == "Q":
            print("See you next time!")
            keep_going = False












