import pytube
from pytube import YouTube
import time
from pytube.cli import on_progress

while True:
    link = input('Insira o link que você deseja baixar // ou CTRL + C para sair: ')
    yt = YouTube(link, on_progress_callback=on_progress)
    
    print('[1] for Video')
    print('[2] for Audio')
    print('[3] for exit')
    print('[4] for playlist')

    format = int(input('Opção: '))

    if format == 1:
        print('Baixando . . .', yt.title)
        yt.streams.filter(progressive=True).get_highest_resolution().download('C:/Users/Administrator/Desktop/teste e arquivos') + str(print('\nDonwload finalizado! \n'))
        
    if format == 2:
        print('Baixando . . .', yt.title)
        yt.streams.filter(only_audio=True,).first().download('C:/Users/Administrator/Desktop/teste e arquivos') + str(print('\nDownload finalizado! \n'))

    if format == 3:
        print('Saindo . . .')
        time.sleep(3)
        print('Obrigado por usar o programa, até depois :) ')
        quit()
        
   
    



    








            
















