import logging
import os

# Configure the Logging
logging.basicConfig(
    filename = 'd:/Data Science AI ML/Logging/Logger/app.log',
    filemode='w',
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S'
)

print(os.getcwd())