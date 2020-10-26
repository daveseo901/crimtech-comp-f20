# Reaction: A React Project!
In this project, you will be building an App with React to measure your reaction time! This will combine the skills we learned in Yoda Chat with some of the skills we learned in Snake.

## A. What is React?
React is a frontend framework used by the Crimson. It is developed by Facebook. Furthermore, React can also be used to build web apps.

The main object in React is the *Component*, an object managing its own states that can be rendered. There will be many times during this project where you want to visit the [React documentation](https://reactjs.org).

## B. Installing React
0. You probably know the drill by now, but you will need to pull from upstream. This means `git pull upstream master` and resolve any merge conflicts that arise.
1. Install Node.js. This is quite simple now that we have experience with the terminal! For MacOS, type `brew install node`. For Linux/WSL, use `sudo apt install nodejs`.
2. Check your versions by typing `node -v` and `npm -v`. `npm` comes packaged with Node. To run react, you will need `npm` version 5 or above.
3. If you do not have version 5 or above, run `npm install -g npm@latest`. This should get you the latest version.
4. Put your versions of `npm` and `node` into `lab3-responses.md`.
5. Next, we are ready to use React. Run `npx create-react-app reactions`, which can take a while. `cd` into the folder and run `npm start`.

Your browser should be loading up `localhost:3000` after this, and you should see a spinning react logo. If so, your installation is complete!

You can make a commit right around now.

6. If you are using Chrome, consider getting the [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) extension.

# C. Individual or Teamwork?
As with previous 2 assignments, you have an option to choose between individual and teamwork tracks. Sign up using [this Google form](https://forms.gle/FezeK1KFf3pUWCuX9).

# D. Reaction Lab!
In this lab, you will be building an app that measures your reaction time. Sadly, I had a super busy week and did not have time to write the lab in time.

Complete the items above, and check back here after your midterm interview! However, if you are super excited, below are the steps I think I am working off of to design the lab.

Rough plan:
* Basing this lab on [this website](https://humanbenchmark.com/tests/reactiontime).
* Have a component called `Game`. It will render two objects: a button and a div. 
* Have a state that stores whether the game is going or not, the last time the button is clicked, and how long to wait for.
* When we first click the button, we check `gameStarted`. If false, we should update `lastClicked`, randomize `waitTime` and change `gameStarted` to true. If true, we should check current time vs lastClicked and output the correct message:
  * If `diff < waitTime`, the person clicked early.
  * If `diff >= waitTime`, output `Your reaction time is {diff - waitTime}`.
* We need to have a big button -> some CSS work.
  * Making buttons tall tend to be the hardest part of CSS. May need to do something with `height`.
* We also need to change the color of the button after a certain amount of time. It seems like people to this with `setTimeout`.
  * On the step where we check randomize `waitTime`, we should also do a setTimeout. This will call a function that changes the color of the button. This should be doable with a bit of Javascript.
    * [This](https://forum.freecodecamp.org/t/an-easy-way-to-change-css-in-react/326708) seems to be a way to do it.
