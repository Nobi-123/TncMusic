from TNCxMUSIC.core.bot import TNCx
from TNCxMUSIC.core.dir import dirr
from TNCxMUSIC.core.git import git
from TNCxMUSIC.core.userbot import Userbot
from TNCxMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = TNCx()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
