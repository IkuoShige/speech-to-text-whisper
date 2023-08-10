import glob, os

def convert_m4a_to_mp3():
    # .m4a→.mp3 m4a_dataにある.m4aの音声データをmp3_dataへmp3として保存する
    for filename in glob.glob( 'm4a_data/*.m4a' ):
        a = filename[len("m4a_data")+1:][:-4] # ファイル名だけ取り出す ex) m4a_data/hoge.m4a → hoge
        os.system("ffmpeg -i m4a_data/{}.m4a -ab 256k mp3_data/{}.mp3".format(a,a))

import subprocess

def convert_mp3_to_m4a(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_file
    ]

    subprocess.run(command)

if __name__ == "__main__":
    input_mp3_file = 'sample.mp3'  # 変換したいMP3ファイルのパス
    output_m4a_file = 'sample.m4a'  # 変換後のM4Aファイルのパス
    convert_mp3_to_m4a(input_mp3_file, output_m4a_file)

