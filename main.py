#!/usr/bin/env python3
from src import MovieDataExtractor
from pathlib import Path
import json
"""
Module Docstring
"""

__author__ = "Muhammad Ghazi Muharam"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    files = list(
        Path('/home/ghazimuharam/Documents/Data Engineer/Data/Self-learning 1/movies').glob('*.json'))

    number_of_files = len(files)
    iteration = 1

    with open('output.json', 'w') as outfile:
        outfile.write('[')
        for file in files:
            print(
                f'Processing {iteration}/{number_of_files} files: {Path(file).name}')
            movie_data = MovieDataExtractor(file)

            outfile.write(movie_data.to_json())
            if iteration == number_of_files:
                break
            else:
                outfile.write(",")
                iteration += 1
        outfile.write(']')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
