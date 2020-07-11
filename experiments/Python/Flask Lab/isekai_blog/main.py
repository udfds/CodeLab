from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'title': 'Day 001',
        'content': 'Hello world!',
        'location': 'Undead Asylum'
    },
    {
        'title': 'Day 002',
        'content': 'Hello friend!',
        'location': 'Ancient Shrine'
    }
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
