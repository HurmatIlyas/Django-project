from weatherman_parser import WeathermanParser
from report import Report
from weather_records import WeatherRecords


class Weatherman:
    """ This class contains a function main that will run all others."""
    def main():
        '''The main function which will run all other functions.'''
        args = WeathermanParser.parse_arguments()
        weather_records = WeatherRecords.parse_weather_records(args.path)
        filtered_weather_records = WeatherRecords.record_filters(weather_records, args.e, args.a or args.c)

        if args.e:
            Report.display_for_extreme_weather_stats(filtered_weather_records)
        if args.a:
            Report.display_for_average_weather_stats(filtered_weather_records)
        if args.c:
            Report.display_weather_records_chart(filtered_weather_records)


Weatherman.main()
