# conding: utf-8
import moviepy.editor as moviepy
import os

# Conversão do Bob Esponja
def bob_esponja():
    
    video_folder =  r'C:\Users\Luiza\Downloads\bob_esponja\1ª'

    os.chdir(video_folder)

    list_files = []
    for file in os.listdir( r'C:\Users\Luiza\Downloads\bob_esponja\1ª'):
        if file.endswith(".rmvb"):
            list_files.append(file)

    print(list_files)

    for f in list_files:
        name = f.split(".")[0] 
        print("Convertendo o episódio.. {}".format(f))
        clip = moviepy.VideoFileClip(f)
        clip.write_videofile(name + ".mp4")

    print("Feito")


## Pergunta se o usuário quer fazer uma conversão única ou em batch
def one_video_question():
    one_video = 0

    one_video = input("Deseja converter em batch ou apenas um vídeo? [B / Batch, U / Um] ")

    while True:

        if (one_video.lower() == "b") or (one_video.lower() == "batch"):
            one_video = False
            break
        elif (one_video.lower() == "u") or (one_video.lower() == "um"):
            one_video = True
            break
        else:
            one_video = input("Input inválido, responder com: [B / Batch, U / Um] ")
        
    return one_video

# Pergunta os formatos que serão utilizados
def format_question():
    formato = input("Forneça o formato original: ")
    if len(formato.split(".")) < 2:
        formato = "." + formato
        
    novo = input("Forneça o formato novo: ")
    if len(novo.split(".")) < 2:
        novo = "." + novo

    return formato, novo

# Converte o vídeo
def convert_video(f, novo):
    name = f.split(".")[0] 
    print("Convertendo o video.. {}".format(f))
    clip = moviepy.VideoFileClip(f)
    try:
        clip.write_videofile(name + novo)
    except ValueError as e:
        print("Erro de tipo, o formato selecionado não é compatível com a biblioteca")
        print(e)

# Main
def main():
    
    one_video = one_video_question()

    if one_video:
        f =  input("Forneça o caminho do arquivo: ")

        formato, novo = format_question()

        convert_video(f, novo)

    else:    
        video_folder =  input("Forneça a pasta de origem: ")

        formato, novo = format_question()

        os.chdir(video_folder)
        list_files = []
        for file in os.listdir():
            if file.endswith(formato):
                list_files.append(file)

        print("Arquivos a serem convertidos: ")
        print(list_files)

        for f in list_files:
            convert_video(f, novo)

        print("Feito")



if __name__ == "__main__":
    main()