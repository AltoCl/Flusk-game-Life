from flask import Flask, render_template
from game_of_life import GameOfLife
app=Flask(__name__,template_folder='templates')


#@app.route("/")
#def home():
    #GameOfLife(25, 25)
    #return "Hello, Flask!"


@app.route("/")
def base():
    GameOfLife(25, 25)
    return render_template('index.html')
@app.route("/live")
def live():

    game = GameOfLife()
    a = game.world
    game.gen = game.gen + 1
    if game.gen > 1:
        game.form_new_generation()
    #print(game.old_world[1][1])
    return render_template('live.html',game = game)



# if __name__ == "__main__":
# app.run(host = "0,0,0,0", port = 5000)
