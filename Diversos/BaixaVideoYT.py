from pytube import YouTube

link = input("Digite o link do vídeo: ")
path = input("Digite onde quer salvar: ")
yt = YouTube(link)

print("Titulo: ", yt.title)

ys = yt.streams.get_highest_resolution()

print("Baixando... ")
ys.download(path)
print("Donwload Concluído!")

