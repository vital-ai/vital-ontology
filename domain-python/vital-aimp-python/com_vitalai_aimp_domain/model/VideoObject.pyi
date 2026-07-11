
import datetime
from com_vitalai_aimp_domain.model.Card import Card


class VideoObject(Card):
        durationSeconds: float
        source: str
        thumbnailImageFileNodeURI: str
        thumbnailImageURL: str
        title: str
        url: str
        autoPlay: bool
        downloadEnabled: bool
        playing: bool
        progressBarEnabled: bool
        synchronize: bool

