from flask import Flask
from flask import render_template


app=Flask(__name__)

@app.route('/')
def base():
    return render_template("base_home1.html")

@app.route('/clothes/')
def clothes():
    context = [{'type': 'Вид одежды', 'color': 'Цвет', 'size': 'Размер', 'price': 'Цена'},
        {'type': 'Пальто', 'color': 'Синий', 'size': 46, 'price': 10000},
            {'type': 'Платье', 'color': 'Зеленое', 'size': 42, 'price': 5000},
            {'type': 'Брюки', 'color': 'Черные', 'size': 50, 'price': 15000}
            ]
    return render_template("clothes.html", context=context)

@app.route('/shoes/')
def shoes():
    context = [{'type': 'Вид обуви', 'color': 'Цвет', 'size': 'Размер', 'price': 'Цена'},
               {'type': 'Ботинки', 'color': 'Синий', 'size': 36, 'price': 7000},
            {'type': 'Туфли', 'color': 'Красные', 'size': 39, 'price': 15000},
            {'type': 'Сапоги', 'color': 'Черные', 'size': 41, 'price': 35000}
            ]
    return render_template("shoes.html", context=context)

@app.route('/jacket/')
def jacket():
    context = [{'type': 'Куртка', 'color': 'Сиреневый', 'size': 56, 'price': 300000},
            ]
    return render_template("jacket.html", context=context)

@app.route('/about/')
def about():
    
    txt = 'Много хорошего о нас'
    return render_template("about.html", txt=txt)

@app.route('/contacts/')
def contacts():
    context = [{'phone': 'Телефон', 'mail': 'Почта'},
            {'phone': '+7233454254', 'mail': 'sddfasdf.sdfaf@mail.ru'},
            {'phone': '+7233564254', 'mail': 'our.mail@mail.ru'}
            ]
    return render_template("contacts.html", context=context)




if __name__=='__main__':
    app.run(debug=True)