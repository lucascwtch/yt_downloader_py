import PySimpleGUI as sg
from pytube import YouTube


def executar_download_video(link, path):
    video = YouTube(link)
    video.streams.get_highest_resolution().download(output_path=path)
    
def executar_download_audio(link, path):
    audio = YouTube(link)
    audio.streams.get_by_itag(251).download(output_path=path)



layout = [[sg.Text('Link do video:           '), sg.InputText()],
          [sg.Text('Diretório para salvar: '),
           sg.InputText(), sg.FolderBrowse()],
          [sg.Button('Download'), sg.Button('Áudio')],
          [sg.Button('Fechar')]]

popup = sg.Window('Donwload de Vídeos com Python', layout)

while True:
    event, values = popup.read()
    if event == 'Fechar' or event == sg.WIN_CLOSED:
        break
    elif event == 'Download':
        executar_download_video(values[0], values[1])
        sg.popup_ok('Download completo!')
    elif event == 'Áudio':
        executar_download_audio(values[0], values[1])
        sg.popup_ok('Download completo!')
        

popup.close()
