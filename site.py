from flask import Flask
import random


app = Flask(__name__)

meme_list = [
    "https://imgflip.com/i/9skbx8",
    "https://imgflip.com/i/9skc5x",
    "https://imgflip.com/i/9skcfu",
    "https://imgflip.com/i/9skcm4"
]


def sifre_olusturucusu_talimat():
    texts = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "=", "{", "}", "[", "]", "|",  ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/", "`", "~", "£", "¥", "€", "©", "®", ":", ";", "(", ")", "[", "]", "{", "}", "<", ">", ",", ".", "?", "!", "—", "‘", "’"]

    sifre = ""
    for i in range(10):
      sifre += random.choice(texts)
    return sifre


facts_list = [
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
    "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
    "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
    "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."
]

yazi_tura_list = ["Yazı", "Tura"]

@app.route('/')
def index():
    return f'<h1>Teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!</h1><a href="/rastgele_gercek">İlginç Gerçekler</a><br><a href="/yazi_tura">Yazı tura oynamak istersen tıkla</a><br><a href ="/sifre_olusturucu"> on haneli şifre yapar(size özel yapıyor)</a><br><a href = "/memes">Acaba hangi meme çıkacak</a>'

        
@app.route('/rastgele_gercek')
def rastgele_gercek():
    return f'<h1>{random.choice(facts_list)}</h1>'

@app.route("/yazi_tura")
def yazi_tura():
    return f'<h1>{random.choice(yazi_tura_list)}</h1>'

@app.route("/sifre_olusturucu")
def sifre_olusturucu():
    result = sifre_olusturucusu_talimat()
    return f'<h1>işte şifren {result}</h1>'

@app.route("/memes")
def memes():
    meme = random.choice(meme_list)
    return f'<h1>İşte karşına çıkan meme</h1><img src ="{meme}" width = "400">' 


app.run(debug=True)
