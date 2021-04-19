import json
from pathlib import Path


class MovieDataExtractor:
    original_title = ''
    budget = 0
    genres = ''
    popularity = 0
    release_date = ''
    revenue = 0
    runtime = 0
    vote_average = 0
    vote_count = 0
    spoken_languages = ''

    def __init__(self, path) -> None:
        self.path = path
        self.load_file()
        self.set_movie_data()

    def load_file(self):
        if(Path(self.path).stat().st_size == 0):
            self.json = {}
        else:
            with open(self.path) as f:
                self.json = json.load(f)

    def set_movie_data(self):
        self.set_original_title()
        self.set_budget()
        self.set_genres()
        self.set_popularity()
        self.set_release_date()
        self.set_revenue()
        self.set_runtime()
        self.set_vote_average()
        self.set_vote_count()
        self.set_spoken_languages()

    def set_original_title(self):
        try:
            self.original_title = self.json['original_title']
        except KeyError:
            self.original_title = ''

    def set_budget(self):
        try:
            self.budget = self.json['budget']
        except KeyError:
            self.budget = 0

    def set_genres(self):
        try:
            list_genres = self.json['genres']
            genres = []
            for genre in list_genres:
                genres.append(genre['name'])
            self.genres = ', '.join(genres)
        except KeyError:
            self.genres = ''

    def set_popularity(self):
        try:
            self.popularity = self.json['popularity']
        except KeyError:
            self.popularity = 0

    def set_release_date(self):
        try:
            self.release_date = self.json['release_date']
        except KeyError:
            self.release_date = ''

    def set_revenue(self):
        try:
            self.revenue = self.json['revenue']
        except KeyError:
            self.revenue = 0

    def set_runtime(self):
        try:
            self.runtime = self.json['runtime']
        except KeyError:
            self.runtime = 0

    def set_vote_average(self):
        try:
            self.vote_average = self.json['vote_average']
        except:
            self.vote_average = 0

    def set_vote_count(self):
        try:
            self.vote_count = self.json['vote_count']
        except:
            self.vote_count = 0

    def set_spoken_languages(self):
        try:
            list_spokens = self.json['spoken_languages']
            spokens = []
            for spoken in list_spokens:
                spokens.append(spoken['name'])
            self.spoken_languages = ', '.join(spokens)
        except:
            self.spoken_languages = ''

    def to_json(self):
        class_dict = self.__dict__

        filters = ['path', 'json']

        for filter_dict in filters:
            class_dict.pop(filter_dict)

        return json.dumps(class_dict, ensure_ascii=False)
