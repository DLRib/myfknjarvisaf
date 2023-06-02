import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Definir as credenciais do cliente
client_id = 'ffba4fa3f74b447cad5dbf5620ab68f7'
client_secret = 'c175b9df6038472192de08173797246c'

# Criar o objeto de autenticação
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Criar uma instância do cliente Spotipy
sp = spotipy.Spotify(auth_manager=auth_manager)

# ID da playlist que você deseja reproduzir
playlist_id = '1Z9VOScNTndZEyvna8ZJoL'

# Inicie a reprodução da playlist
sp.start_playback(context_uri=f"spotify:playlist:{playlist_id}")
