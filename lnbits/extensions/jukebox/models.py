from typing import NamedTuple
from sqlite3 import Row
from fastapi.param_functions import Query
from pydantic.main import BaseModel
from pydantic import BaseModel
from typing import Optional


class CreateJukeLinkData(BaseModel):
    user: str = Query(None)
    title: str = Query(None)
    wallet: str = Query(None)
    sp_user: str = Query(None)
    sp_secret: str = Query(None)
    sp_access_token: str = Query(None)
    sp_refresh_token: str = Query(None)
    sp_device: str = Query(None)
    sp_playlists: str = Query(None)
    price: str = Query(None)


class Jukebox(BaseModel):
    id: Optional[str]
    user: Optional[str]
    title: Optional[str]
    wallet: Optional[str]
    inkey: Optional[str]
    sp_user: Optional[str]
    sp_secret: Optional[str]
    sp_access_token: Optional[str]
    sp_refresh_token: Optional[str]
    sp_device: Optional[str]
    sp_playlists: Optional[str]
    price: Optional[int]
    profit: Optional[int]


class JukeboxPayment(BaseModel):
    payment_hash: str
    juke_id: str
    song_id: str
    paid: bool
