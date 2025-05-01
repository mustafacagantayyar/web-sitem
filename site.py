from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
    "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
    "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
    "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."
]

yazi_tura_list = ["Yazı", "Tura"]

@app.route('/')
def index():
    return f'''
        <h1>Teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!</h1>
        <a href="/rastgele_gercek">İlginç Gerçekler</a><br>
        <a href="/yazi_tura">Yazı tura oynamak istersen tıkla</a>
    '''

@app.route('/rastgele_gercek')
def rastgele_gercek():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/yazi_tura")
def yazi_tura():
    return f'<p>{random.choice(yazi_tura_list)}</p>'

app.run(debug=True)
