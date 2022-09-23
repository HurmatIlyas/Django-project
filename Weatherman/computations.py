from statistics import mean


class Computations:
    """ A class that calculates the values like average maximum
    temperature etc.

    Attributes
    ----------
    None

    Methods
    -------
    extreme_weather_stats(yearly_weather_records):
        Returns the maximum, minimum temperature and humdity value in a year and date on
        which maximum, minimum temperature and humidity occurs
    average_weather_stats(weather_records, year, month):
        Calculates the average of highest temperatures, lowest
        temperatures and mean humidity in a month and
        displays the average.
    weather_records_bar_chart(monthly_weather_records):
       Multiplies highest temp value and lowest temp value with "+" in red
       and blue colour respectively and returns the date, max_temp_for_each_day
        and min_temp_for_each_day.
    """
    @staticmethod
    def extreme_weather_stats(yearly_weather_records):
        """ Returns the maximum and minimum temperature value and maximum humidity value
        with year and date from a dictionary of the specified
        year.

        Parameters
        ----------
        yearly_weather_records :Dict
            Dictionary containing each year maximum and minimum temperature and
            humdity along with other values. Contains year as keys
            and other values with other parameters.

        Returns
        -------
        Dict
            Contains the minimum temperature, maximum temperature value and maximum humdity
            along with the dates on which these occur.
        """
        maximum_temperature = []
        minimum_temperature = []
        maximum_humidity = []
        for month_key, month_value in yearly_weather_records.items():
            maximum_temperature_dict = max(month_value, key=lambda x: x['Maximum Temperature'])
            maximum_temperature.append(
                (maximum_temperature_dict['Maximum Temperature'], maximum_temperature_dict['Date']))
            maximum_temperature_value, maximum_temperature_date = max([[int(i[0]), i[1]] for i in maximum_temperature])
            minimum_temperature_dict = min(month_value, key=lambda x: x['Minimum Temperature'])
            minimum_temperature.append(
                ((minimum_temperature_dict['Minimum Temperature']), minimum_temperature_dict['Date']))
            minimum_temperature_value, minimum__temperature_date = min([[int(i[0]), i[1]] for i in minimum_temperature])
            maximum_humidity_dict = max(month_value, key=lambda x: int(x['Maximum Humidity']))
            maximum_humidity.append(
                ((maximum_humidity_dict['Maximum Humidity']), maximum_humidity_dict['Date']))
            maximum_humidity_value, maximum_humidity_date = max([[int(i[0]), i[1]] for i in maximum_humidity])

        return {'max_temp_value': maximum_temperature_value, 'max_temp_date': maximum_temperature_date,
                'min_temp_value': minimum_temperature_value, 'min_temp_date': minimum__temperature_date,
                'max_humid_value': maximum_humidity_value, 'max_humid_date': maximum_humidity_date}

    @staticmethod
    def average_weather_stats(monthly_weather_records):
        """ Returns the average highest temperature, lowest temperature
        and mean humidity of the specified month and year.

        Parameters
        ----------
        monthly_weather_records : Dict
            Dictionary containing month-wise weather data
        key : str
            The key for which the average needs to be find
            like 'Max TemperatureC' etc

        Returns
        -------
        mean(average_weather_records) : float
            Contains the highest, lowest and mean temperature's average for example: 36.11
        """
        maximum_temp_weather_records = [int(i['Maximum Temperature']) for i in monthly_weather_records]
        minimum_temp_weather_records = [int(i['Minimum Temperature']) for i in monthly_weather_records]
        mean_humid_weather_records = [int(i['Mean Humidity']) for i in monthly_weather_records]

        return {"average_max_temp": mean(maximum_temp_weather_records),
                "average_min_temp": mean(minimum_temp_weather_records),
                "average_mean_humdity": mean(mean_humid_weather_records)}

    @staticmethod
    def weather_records_bar_chart(monthly_weather_records):
        """ Returns the values of minimum and maximum
            temperatures of each day in the specified month and
            specified year.

            Parameters
            ----------
            monthly_weather_records : Dict
                Dictionary containing month-wise weather data

            Returns
            -------
            Dict
                Contains the date for each bar char, minimum temperature value
                maximum temperature value
            """
        weather_stats = [{"Maximum Temperature": int(i['Maximum Temperature']),
                          "Minimum Temperature": int(i['Minimum Temperature']),
                          "Date": i['Date']} for i in monthly_weather_records]

        return weather_stats
