from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Ali Darvishi',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Mar 27, 2023'
    },
    {
        'author': 'Sahar Hashemi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Mar 28, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
