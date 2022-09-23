import csv
import os
from datetime import datetime


class WeatherRecords:
    """ A class that holds the data structure used for calculations.

    Attributes
    ----------
    None

    Methods
    -------
    parse_weather_records(path):
        Returns a dictionary containing weatherman data
        present in weatherman directory is appended.
    record_filters(args_values, weather_records):
        Returns yearly and monthly date as per required.
    """
    @staticmethod
    def parse_weather_records(path):
        """ Returns a dictionary as all the text files data
        present in weatherman directory is appended.

        Parameters
        ----------
        path : str
            Contains the data path.

        Returns
        -------
        weatherman_records: Dict
            A dictionary containg all data. This dictionary
            contains another dictionary that contains the data of one year.
            The key will be month and the value
            will be a list which will contain the whole month data.
            It will look like this: {year:{month:[{d            A dictionary containg all data. This dictionary
            contains another dictionary that contains the data of one year.
            The key will be month and the value
            will be a list which will contain the whole month data.
            It will look like this: {year:{month:[{day1}, {day2}, and so on]}}
        """
        weatherman_records = {}
        for files in os.listdir(path):
            with open(path + files) as files:
                weather_files = files.readlines()
                weather_files_records = csv.DictReader(weather_files[0:-1])

                for row in weather_files_records:
                    record = WeatherEntry().validate_weather_records(row)
                    if record is not None:
                        if '' not in record:
                            date = datetime.strptime(record[0], '%Y-%m-%d')
                            weather_records = {"Date": record[0],
                                               "Maximum Temperature": record[1],
                                               "Minimum Temperature": record[2],
                                               "Maximum Humidity": record[3],
                                               "Mean Humidity": record[4]}
                            weatherman_records.setdefault(date.year, {}).setdefault(date.month, []).append(weather_records)

        return weatherman_records

    @staticmethod
    def record_filters(weather_records, year, month=None):
        """ Returns a dictionary that contains yearly data and monthly data
            of the given year or month.

        Parameters
        ----------
        year : str
            Contains the year inputted by user.
        month : str
            Contains the month given in inputonth]

        Returns
        -------
        yearly_weather_records: Dict
            A dictionary containing month as key and value is the list of dictionaries
            containig each month's each day.
            The key will be month and the value
            will be a list which will contain the whole month data.
            It will look like this: {month:[{day1}, {day2}, and so on}]}
        monthly_weather_records: List
            A list containing dictionaries for each day in specific month.
            It will look like this: [{day1}, {day2}, and so on}]
        """
        if month is not None:
            date_splitted = datetime.strptime(year or month, "%Y/%m")
            year = int(date_splitted.year)
            month = int(date_splitted.month)
            filtered_weather_records = weather_records[year][month]
        else:
            year = int(year)
            filtered_weather_records = weather_records[year]

        return filtered_weather_records


class WeatherEntry:
    def validate_weather_records(self, single_record):
        single_record = [single_record.get('PKT', single_record.get('PKST')),
                         single_record['Max TemperatureC'],
                         single_record['Min TemperatureC'],
                         single_record['Max Humidity'],
                         single_record[' Mean Humidity']]

        if all(single_record):
            return single_record
