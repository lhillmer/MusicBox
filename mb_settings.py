import configparser

config = configparser.ConfigParser(delimiters=('='))
config.read('/var/www/MusicBox/mb_config.ini')
