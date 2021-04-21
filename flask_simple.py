from flask import Flask, render_template, url_for
app = Flask(__name__)

post = [
    {
         'author' : 'Christian Morel',
         'title' : 'Blog Post 1',
         'content' : 'First post content',
         'date_posted' : 'April 20, 2021'
    },

    {
         'author' : 'Vania Schuster',
         'title' : 'Blog Post 2',
         'content' : 'Second post content',
         'date_posted' : 'April 21, 2021'
    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = post)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
    