
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class Movie(Card):
        durationSeconds: float
        genre: str
        imageFileNodeURI: str
        imageURL: str
        imdbRating: float
        longDescription: str
        pg: str
        rottenTomatoesRating: float
        shortDescription: str
        thumbnailImageFileNodeURI: str
        thumbnailImageURL: str
        title: str
        year: int

