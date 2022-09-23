from argparse import ArgumentParser


class WeathermanParser:
    """ A class to parse arguments.

    Methods
    -------
    parse_arguments:
        Returns the arguments
    """
    @staticmethod
    def parse_arguments():
        ''' Returns the list of arguments created

        Parameters
        ----------
        None

        Returns
        -------
        args: argparse.Namespace
            Contains the data path, year, month and bar chart arguments for weather files.
        '''
        parser = ArgumentParser(description="Weatherman")
        parser.add_argument('path', help='Path of a file')
        parser.add_argument('-e', help='Year')
        parser.add_argument('-a', help='Month')
        parser.add_argument('-c', help="Bar Chart")
        args = parser.parse_args()

        return args
