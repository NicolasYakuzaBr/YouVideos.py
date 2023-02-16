from pytube import Playlist

link = input('Insira o link da Playlist aqui: ')

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    video.streams.get_audio_only().download()
    print('Donwload finalizado', video.title)

print('\nTodos os conteudos da playlist foram baixados com sucesso!')

