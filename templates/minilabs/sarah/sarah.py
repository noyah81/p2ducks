from flask import Blueprint, render_template
import random


class playlistClass:
    def __init__(self, playlists):
        self._playlists = playlists

    def getplaylist(self):
        return random.choice(self._playlists)

    """Getters with decorator to allow . notation access"""

    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def getRandom(self):
        return random(self._playlists)

    @property
    def number(self):
        return self._playlists[self._playlists - 1]


# create the blueprint
sarah = Blueprint('sarah', __name__, url_prefix="/sarah", static_folder="static",
                  template_folder="templates/minilabs/sarah/")


# define the route for the minilab
@sarah.route('/playlists')
def playlists():
    playlistsList = [
        '<iframe src="https://open.spotify.com/embed/playlist/7Jv7B5XZWpxkqPf3LpWGes" width="700" height="380" '
        'frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe> ',
        '<iframe src="https://open.spotify.com/embed/playlist/4SGMSuS0g2D3zBUc2prEw7" width="700" height="380" '
        'frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>',
        '<iframe src="https://open.spotify.com/embed/playlist/4De3d8DZvxPXdCDLSnK5eQ" width="700" height="380" '
        'frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>',
        '<iframe src="https://open.spotify.com/embed/playlist/2PxGOukOIDwK1W81lhLrJ8" width="700" height="380" '
        'frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe> '
    ]

    return render_template('minilabs/sarah/sarah.html', playlist=random.choice(playlistsList))
