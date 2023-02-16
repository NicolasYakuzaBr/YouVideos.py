from pytube import YouTube
from pytube.cli import on_progress

while True:

    print('Only Videos.mp4 Downloader')
    
    link  = input('Insira o link aqui: ')

    yt = YouTube(link, on_progress_callback=on_progress)
    
    print('Título:', yt.title)
    print('Canal: ', yt.author)
    print('Descrição: ', str(yt.description))
    print('---------------------------------')
    print('Baixando...', yt.title)
    yt.streams.filter(progressive=True).get_highest_resolution().download()
    print('\nDonwload Finalizado!\n')
    
    Comando = int(input('Deseja sair ou continuar? | [1] - Sair | [2] - Continuar: '))
    if Comando == 1:
        print('Até a próxima :) ')
        quit()
    
    if Comando == 2:
        continue

    





  









