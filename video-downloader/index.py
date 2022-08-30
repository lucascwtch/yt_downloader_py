import PySimpleGUI as sg
from pytube import YouTube

sg.change_look_and_feel('DarkBrown4')

def executar_download_video(link, path):
    video = YouTube(link)
    video.streams.get_highest_resolution().download(output_path=path)
    
def executar_download_audio(link, path):
    audio = YouTube(link)
    audio.streams.get_by_itag(251).download(output_path=path)



layout = [[sg.Text('Link do video:           '), sg.InputText(), sg.Text('by: Cwtch',)],
          [sg.Text('Diretório para salvar: '),
           sg.InputText(), sg.FolderBrowse()],
          [sg.Text('Download: '), sg.Button('Video', size=(10,1)), sg.Button('Áudio', size=(10,1)), sg.Text('', size=(13,1)), sg.Button('Fechar', size=(15,1))]],

# layout = [[sg.VPush()],
#          [sg.Push(), sg.Column(layout, element_justification='l'), sg.Push()],
#          [sg.VPush()]]

popup = sg.Window('Download de Cria', layout, size=(560,100), grab_anywhere=True)

while True:
    event, values = popup.read()
    if event == 'Fechar' or event == sg.WIN_CLOSED:
        break
    elif event == 'Video':
        executar_download_video(values[0], values[1])
        sg.popup_ok('Download completo!')
    elif event == 'Áudio':
        executar_download_audio(values[0], values[1])
        sg.popup_ok('Download completo!')
        

popup.close()
