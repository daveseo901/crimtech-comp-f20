# Reaction: A React Project!
In this project, you will be building an App with React to measure your reaction time! This will combine the skills we learned in Yoda Chat with some of the skills we learned in Snake.

## A. What is React?
React is a frontend framework used by the Crimson. It is developed by Facebook. Furthermore, React can also be used to build web apps.

The main object in React is the *Component*, an object managing its own states that can be rendered. There will be many times during this project where you want to visit the [React documentation](https://reactjs.org).

## B. Installing React
0. You probably know the drill by now, but you will need to pull from upstream. This means `git pull upstream master` and resolve any merge conflicts that arise.
1. Install Node.js. This is quite simple now that we have experience with the terminal! For MacOS, type `brew install node`. For Linux/WSL, use `sudo apt install nodejs`.
2. Check your versions by typing `node -v` and `npm -v`. `npm` comes packaged with Node. To run react, you will need `npm` version 5 or above and node version 8 or above.
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

# E. Setting Up.
Run `npx create-react-app reactions` in this folder. The terminal will report any installation error. If so, you can either fix them by seraching on Google or call us over.

Next, *delte the `reacitons/src` folder* and copy the `src` folder into `reactions/src`. This contains the starter code we will use to write the app.

The style of thinking necessary for building a react app is quite different from what you may learn in CS 50, so we try to provide you with more guidance here.

# F. React App
Overview: The user will click on the button, which makes it turn red. That starts the counting. At some point in the future, the button will turn green. The user should try to click on the button as soon as possible. Then, here are the states that should be stored in the `Panel` variable:
* `start_time` will store the last time when `start_count` is called.
* `ran_once` will store whether or not the user has played the game once.
* `counting` will store whether or not we are currently counting (playing the game).
* `true_duration` will store how long it's supposed to take before the button turns green.
* `color` stores the color of the button.

# G: The `start_count` function
When we start the counting, we need to set the following states:
* `start_time` should be set to the current time. In react, the function `window.performance.now()` stores how many milliseconds it has been since the website was loaded. It should be helpful.
* `true_duration` should be set to some random value between 2s and 7s.
* `counting` should now be True.
* `color` should be dark red.

Note about react: instead of writing `this.state.counting = true;`, you should use `this.setState({counting:true});`. The setState function informs React that a state has been changed. If you change a state variable directly, you can mess up the react framework.

# H: Change color to red after `true_duration` seconds.
Look iunto a function called `setTimeout`, and make a function that will change the color of the button to be green. The button should turn green after exactly `true_duration` seconds.

Note about React: if you write `this.setState({counting:true}); console.log(this.state.counting);` you may sometimes find that `this.state.counting` is not set to True. This is because the `setState` function is not guaranteed to change the state right then and there.

# I: The `end_count` function
If at most `this.state.true_duration` seconds have passed, do nothing. Otherwise, we need to set the following states:
* `ran_once` should be set to true: we have ran once, after all.
* `counting` should be set to false: we have finished the game.
* `reaction_time` should be set to the difference between (the number of seconds that have elapsed) and `this.state.true_duration`.

# J: The `render` function
You should change the `msg` variable depending on what `this.state` is.
* If `this.state.counting` and the button is red, msg is `Wait for Green`.
* If `this.state.counting` and the button is green, msg is `Click!`.
* Otherwise, if you have ran once, msg is `Your reaction time is {this.state.reaction_time} ms`.
* Otherwise, we have never run the test. So, msg is `Click me to begin!`

# K: CSS
Right now the box is small and hard to click on. Let us make it big and nice to click on! Please also align the text in the center.

We recommend using a flex box, which you can learn more about at (https://www.w3schools.com/css/css3_flexbox.asp)[w3schools]. Consider using `justify-content` and `align-items`.

# L: Submit!
Submit your assignment like usual :)
