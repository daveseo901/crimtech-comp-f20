## Python Tutorial
In the `python` folder you will have an assignment that gets you familiar with python. Complete the python assignment by **Friday, 09/25**. Then, you don't need to do any work until your Joint Coding Session.

## Acclimating to the Codde
Run `cp snake_starter_code.py snake.py` to make a copy of the game, and run `python snake.py`. You should see a board with a red and black dot. The two blue dots represent the snake, and the red dot is the apple.

The board has 24 squares. The top left square has location (0,0), and the bottom right (23,23).

We have two classes within `snake.py`: a `Snake` class and an `Apple` class. Then, we have a loop inside `main` that runs this game. You will see that there are many comments with `TODO` written on them. We will be implementing them in the next sections.

The snake's head body is represented by the `body` variable, which is a list containing the body from the head to the tail. So, `self.body[0]` would be referencing the head, and `self.body[:-1]` would reference everything except the tail.

## Joint Coding Session
You are in a team of 4, and should assign one person to the following 4 roles:
1. Generalist
2. Class Master
3. Movement Expert
4. Game Designer

Note: don't worry if you can't finish all the tasks. **As long as you tried your best, you pass this assignment**.

`git pull git@github.com:crimtech/snake-<your team name>.git`

This is a WIP. Exact roles will change by Wednesday.

## Generalist
As the generalist, your goal is to help with the rest of the team by giving an extra pair of eyes/fingers, and merging all the code together.

## Class Master
As the class master, you will help the team implement some of the miscellaneous features

`git checkout -b classes`

1. Check for collision.
Now that the snake is moving, it will go off the screen into the vast void of sadness. That's not good! Change the `collision` function to return True if the snake is out of bounds. Change `move` to call the `kill` function when the snake goes out of bounds.

Self Collisions: But, the snake can collide with itself! Change the `collision` function so that it returns `True` if the snake's head has hit another part of its body.

2. Turning the snake.
We need to be able to turn the snake. Modify the `turn` function so that after the function is called, `self.direction` is set to the new direction.

Tip: You may need to make the snake longer and slow down time (decrease the tick_time variable) to test this.

3. Moving the apple.
When the snake ate an apple, we need to move it! Move it to a location that is not on the snake.

`git push`

## Movement Expert
As the movement expert, you are in charge of the `move` function, the key function in the snake class.

`git checkout -b movements`

1. Move the snake!
Let's get the snake moving! Change the `move` function so that it will move the snake 1 unit in the correct direction.

Tips: Use the dictionary `DIR` and `self.direction` to figure out which way to move the snake. Change `self.direction` to make sure that the snake moves correctly in all directions.

2. Detect Collisions and kill the snake.

3. Growing the snake.
The snake needs to grow! Change `move` so that the snake will grow in length once it eats an apple.

Tip: Start debugging by setting the coyote time amount to be much higher than 0.1 second.

`git push`

## Game Designer
As the game designer, you are in charge of making the pieces fit together.

`git checkout -b gamedev`

1. Eating the apple.
Detect when the snake is eating the apple. Right now, have the program print out "the snake at an apple!" when that occurs. In the next two parts, we will implement what happens when the snake moves the apple.

2. Display the score.
Display the score of the player. You will need to search up on Google how to display pygame text on screen.

3. Incremental difficulty
Right now the difficulty of the game is constant. However, we should challenge the player more as their snake gets longer. Change your code so that the snake moves faster as it gets longer, but maintain a good difficulty curve -- people don't like impossible games.

## The Snake game competition
The comper/comper team who makes the best snake game, as judged by the CrimTech board, will win a merch of choice from [pythongear.com](https://www.pythongear.com/). If a team wins this, they will each get a nice Python sticker.