from flask import Flask, render_template, request
from mazegenerator import randomized_dfs_maze

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.jinja')

@app.get("/maze")
def show_maze():
    size = int(request.args.get('size'))
    if size > 100 and not request.args.get('confirmation'):
        return render_template("confirmation.jinja", size=size)
    return render_template('maze.jinja', board=randomized_dfs_maze(size))

if __name__ == "__main__":
    app.run()