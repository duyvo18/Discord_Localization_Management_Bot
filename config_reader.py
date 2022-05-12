"""
Configuration Reader for Localization Management Bot.

Classes

    ConfigReader -- The implementation class of this module.
    
"""

from typing import Dict, List
import configparser
from csv import reader


class ConfigReader():
    """
    Static class to read "Config" and "Admins" files for Localization Management Bot, in which:

    Config:
        Contains secrets such as bot token. Defaulted to "config.ini".

    Admins:
        Contains the list of Regional Admins' ID, and their responsible Regions.
        Defaulted to "regional_admins.csv"

        The Admins file format must follows:
            Contains a header.

            Contains two columns: "Regional Admin ID" and "Region".

            Each row defines a single Admin ID and Region relation.

            An Admin who is responsible for many Regions should be divided into multiple rows.


    Static Methods
    ---
    get_admins(path='regional_admins.csv'):
        Read "Admins" file to get the list of all regional admins and their responsibled regions.

    get_config(section, option, path='config.ini'):
        Read the "Config" file at specified section, option.

    """

    _config_path = 'config.ini'
    _admins_path = 'regional_admins.csv'

    @staticmethod
    def get_admins(path: str = None) -> Dict[str, List[str]]:
        """
        Read regional admins file to get the dictionary of Regional Admins
        to their responsibled Regions.

        Parameters:
        ---

        path:
            Relative path to a csv file listing all Regional Admins
            and their responsibled Regions.

            The value of {None} would takes the default path of "./regional_admins.csv"

        Returns:
        ---

        A type {Dict} with keys are Regional Admins' ID and
        values are the list of corresponding Regions.

        """

        try:
            if not path:
                path = ConfigReader._admins_path

            with open(path, mode='rt', encoding='UTF-8', newline=None) as file:
                csv_reader = reader(file)

                admins_dict = {}

                for row in csv_reader:
                    id, region = row[:2]

                    admins_dict[id] = admins_dict.get(id, []) + [region]

                return admins_dict

        except OSError or ValueError as e:
            print("\n> WARNING: Cannot read Admin file.\n")

    @staticmethod
    def get_config(section: str, key: str, path: str = None) -> str:
        """
        Get a value from the configuration file at a specific section and key.

        The configuration file must follows INI format: https://en.wikipedia.org/wiki/INI_file


        Parameters:
        ---

        section:
            The name of the section in the configuration file.

        key:
            The name of the key at the specified section.

        path:
            The path to the configuration file.

            If {None} is passed, the value would be defaulted to "./config.ini"


        Returns:
        ---
        The value at the specified key, section.

        """

        if path == None:
            path = ConfigReader._config_path

        config_parser = configparser.ConfigParser()

        ret = config_parser.read(path, encoding='UTF-8')

        if ret != [path]:
            raise OSError(f"Cannot read config file at {path}.")

        return config_parser.get(section=section, option=key, raw=True, fallback=None)


if __name__ == '__main__':
    print(ConfigReader.get_config("Tokens", "bot_token"))
    print(ConfigReader.get_admins())
