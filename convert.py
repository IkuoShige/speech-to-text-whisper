import glob, os

# .m4a→.mp3 m4a_dataにある.m4aの音声データをmp3_dataへmp3として保存する
for filename in glob.glob( 'm4a_data/*.m4a' ):
    a = filename[len("m4a_data")+1:][:-4] # ファイル名だけ取り出す ex) m4a_data/hoge.m4a → hoge
    os.system("ffmpeg -i m4a_data/{}.m4a -ab 256k mp3_data/{}.mp3".format(a,a))

#for filename in glob.glob( 'mp3_data/*.mp3' ):
#    a = filename[len("mp3_data")+1:][:-4] # ファイル名だけ取り出す ex) mp3_data/hoge.mp3 → hoge
#    os.system("sox mp3_data/{}.mp3 data_wav/{}.wav channels 1 rate 16k".format(a,a))
