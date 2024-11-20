from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/menu")
def menu():
    menu_items = [
        {"name": "Мишачий Класик ", "description": "Сир, томати, базилік", "price": "150 грн"},
        {"name": "Пепероні від Тома", "description": "пепероні, шинка, ковбаски, соус барбекю", "price": "180 грн"},
        {"name": "Джеррі в Сирі", "description": "Моцарела, горгонзола, пармезан, чеддер", "price": "200 грн"},
        {"name": "Сирний Джеррі", "description": "моцарела, чеддер, пармезан, рікотта, любов ", "price": "250 грн"},
        {"name": "Томовий Барбекю", "description": "курка, бекон, соус барбекю, червоний лук", "price": "300 грн"},
    ]
    return render_template("menu.html", menu_items=menu_items)


if __name__ == "__main__":
    app.run(debug=True)
