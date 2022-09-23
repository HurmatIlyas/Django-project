from computations import Computations


class Report:
    """ A class to print all results.

    Class constants
    ----------
    Bed_Color
        contains color code for red
    Blue_Color
        contains color code for blue

    Methods
    -------
    display_for_extreme_weather_stats(args_values, weather_records):
        Displays the highest temperature, lowest temperature and max humidity
        of a given year.
    display_for_avg_weather_stats(args_values, weather_records):
        Displays the average highest temperature, average lowest temperature
        and average mean humidity of a given year.
    display_bar_chart(args_values, weather_records)
        Multiplies highest temp value and lowest temp value with "+" in red
        and blue colour respectively and displays the date, the bar chart
        containing the number of + for highest and lowest temperature and also
        the temperature.
        """
    RED_COLOUR = '\033[31m'
    BLUE_COLOUR = '\033[94m'

    @staticmethod
    def display_for_extreme_weather_stats(yearly_weather_records):
        """ Displays a minimum, maximum
            temperatures, max humidity in the specified month
            of specified year.

        Parameters
        -------
        yearly_weather_records :
            Contains yearly weather data

        Prints
        -------
            Contains the date on which high, low temp, max
            humidity, and dates on which these occurs

        """
        weather_extremas = Computations.extreme_weather_stats(yearly_weather_records)

        print(f'{weather_extremas["max_temp_value"]} on {weather_extremas["max_temp_date"]}\n\
                {weather_extremas["min_temp_value"]} on {weather_extremas["min_temp_date"]}\n\
                {weather_extremas["max_humid_value"]} on {weather_extremas["max_humid_date"]}')

    @staticmethod
    def display_for_average_weather_stats(monthly_weather_records):
        """ Displays average of minimum, maximum
            temperatures and mean humidity in the specified month
            of specified year.

        Parameters
        -------
        monthly_weather_records:
            contains the monthly data

        Prints
        -------
        avg_values : str
            Contains average values of maximum, minimum temperature and mean
            humidity
         """
        avg_values = Computations.average_weather_stats(monthly_weather_records)
        print(f'{avg_values["average_max_temp"]}\n\
                {avg_values["average_min_temp"]}\n\
                {avg_values["average_mean_humdity"]}')

    @staticmethod
    def display_weather_records_chart(monthly_weather_records):
        """ Displays bar char displaying maximum and minimum temperature.

        Parameters
        -------
        monthly_weather_records
            Contains monthly weather data
        Print
        -------
            Prints a horizontal bar chart with dates
        """
        weather_records_chart = Computations.weather_records_bar_chart(monthly_weather_records)

        for i in weather_records_chart:
            print(f'{Report.BLUE_COLOUR}{i["Date"]}{"+" * abs(int(i["Minimum Temperature"]))}\
                    {Report.RED_COLOUR}{"+" * abs(int(i["Maximum Temperature"]))}\
                    {i["Minimum Temperature"]}-{i["Maximum Temperature"]}')
