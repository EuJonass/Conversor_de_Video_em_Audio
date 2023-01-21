import moviepy.editor

# Carregar o Arquivo .mp4
video = moviepy.editor.VideoFileClip('./Videos/MeuVideo.mp4')

# Extrai apenas o Áudio do Vídeo
audio_data = video.audio

# Salva o arquivo .mp3 no caminho e com o nome selecionado
audio_data.write_audiofile('./Audios/MeuVideo.mp3')
