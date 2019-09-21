from flask import Flask, render_template, jsonify
from flaskext.mysql import MySQL
import json

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'blog'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cur = conn.cursor()


def posts():
    cur.execute('''
        SELECT
            blog.posts.title,
            blog.user.username,
            blog.comments.comment
        FROM
            blog.posts
        LEFT JOIN
            blog.user
        ON
            blog.posts.userId = blog.user.id
        LEFT JOIN
            blog.comments
        ON
            blog.posts.id = blog.comments.postId;
    ''')
    posts = cur.fetchall()
    post_container = []
    for post in posts:
        post_container.append({
            'title': post[0],
            'username': post[1],
            'comment': post[2]
        })
    return post_container


@app.route('/api')
def api():
    return jsonify(data=posts())


@app.route('/')
def main():
    data = posts()
    return render_template('home.html', posts=data, content_type='application/json')


if __name__ == "__main__":
    app.run(debug=True)
