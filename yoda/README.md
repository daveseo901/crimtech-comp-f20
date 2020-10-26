# Lab 2: The Force Awakens
In this lab, we will teach you how to use some HTML, CSS and Javascript by building a chat with baby Yoda!

Written by Richard "Rick" Xu.

## A. Pull from upstream
We have another lab, so you will need to pull from remote again! So, run the following command:
```
git pull upstream master
```

If you get any merge conflicts, you need to edit the files where the conflict occurs, following git's instructions. Afterwards, run `git commit` to fix the merge conflict.

## B. Developer Mode / Inspect
In this unit you will be using a browser. It is possible to do this using Chrome, Firefox, Edge or Safari, though we will be following Chrome in this assignment.

On any website, right click and choose the **"Inspect"** option. Welcome to inspect mode/developer panel! This is super useful for web development, and let us go through what a couple panels do. Some of them have exercises. Record your answers in `lab2-responses.md`.
0. You can adjust how the browser looks! On the upper bar, there is an option called "Responsive". You can change that to, say, an iPhone X to see how the page looks on an iPhone.
1. `Elements` contains the html source code of the website. Exercise: there is an easter egg on `crimtech.github.io`. Can you find it in the soruce?
2. `Console` allows you to type JavaScript expressions. Exercise: There is some javascript on the website that defined an extra variable. What is that variable, and what is its value?
3. A webpage can contain code stored on another webpage, such as `adservice.google.com`. `Sources` allows you to see what they are. Exercise: Go to `thecrimson.com`, look at sources and put the name of another source into your responses.

## C. Welcome to Javascript
All right, another language! Javascript is a widely popular language used for web scripting.

While it is possible to run Javascript code like you would Java or C code, we usually run the code in the web. Type your code in `test.html` and any responses in `lab1-responses.md`. *Throughout this entire section, Google is your friend*.
1. Open up `test.html` in the browser and visit the console.
2. Type `console.log("Hello World")` into the console.
3. Declare a variable `y` and set it equal to your favorite string.
    * Try outputing `y.includes("hello")` and `y.repeat(10)`. What do the two functions do? Record your answer in `lab2-responses.md`.
4. We can declare functions in Javascript! Complete the function `square` so that it takes in a variable `i` and outputs `i*i`.
    * What happens when you call `square(2.5)`? Or `square("hello")`? Record your answer in `lab2-responses.md`.
5. Change the function `square` so that if the input is not a number, the function returns `-1` instead. You may find googling "javascript find type of variable" helpful.
6. Construct a function `numberString`, that on input `i` a positive whole number, output the string `123...i`. For example, `numberString(10)="12345678910"`. 
    * Your function should not crash when `i` is not a positive whole number. Add some `if`-statements to check!

That was a lot. Give yourself a pat on the back for completing them!

## D. Individual or Group Track?
Again, it's time to decide which track to follow! Please fill out the forms [here](https://forms.gle/6d2hDPMFGDo9q3uBA).

A few differences from last time: there is no extra assignment for being on the teamwork track, and you don't need to make it to a joint coding session. You just have someone else to work with. Both tracks need to fully complete the assignment.

## E. Yoda Chat Part 1: Header.
We will get started building Yoda Chat!

In this section we will be editing the `<head>` section of `yoda.html`. Note that starting this section we are giving you more freedom and somewhat less guidance. As you get deeper into CS, this trend will continue. **Google is your friend:**

> What separates an amateur and professional coder? Amateur coders believe code = algorithm + data structure. Professionals know that code = Google + reading. - Some coding website

1. Add a title to the page. 
2. Add a favicon. Notice that there is a file named `favicon.ico` in the `img/` folder. Link this to the page using the code `<link rel='shortcut icon' type='image/png' href='img/favicon.ico'>`. (Do you understand what the code does?)

After this, your tab should look like this: ![Tab Image](https://raw.githubusercontent.com/crimtech/crimtech-comp-f20/master/yoda/mdimg_/i2.JPG)

## E. Part 2: HTML Body
In this section we will be editing the `<body>` section of `yoda.html` so Yoda and his quote is on the screen. Be sure to commit often!

1. Add a `<p>` tag with the line "To yoda chat I welcome you. Yes, hmmmmm."
2. Center the text with a `<center>` tag. Your page should look like this: ![Stage 1 of Yoda Chat](https://raw.githubusercontent.com/crimtech/crimtech-comp-f20/master/yoda/mdimg_/i3.JPG)
3. Add one of the images of Yoda into the page with an `<img>` tag. Scale it so that Yoda has a prespecified height.
4. Add in a text box with a somewhat large size. Your page should look like this: ![Stage 2 of Yoda Chat](https://raw.githubusercontent.com/crimtech/crimtech-comp-f20/master/yoda/mdimg_/i4.JPG)

## F. Javascript
In this section we will be writing some plain Javascript that will allow you to talk to Yoda! People seldom write plain Javascripts now, opting for more heavyweight solutions like React and Django. However, plain Javascript is pretty fun. More importantly, React development is 95% Javascript (it uses typescript, which is Javascript with types). So, this lab will be helpful to you.
1. Add in a button that calls the `respond()` function in `response_handler.js`. You will need to add a `<script>` tag in the `<head>` section of the HTML, and set the `onclick` attribute of the button. If you have done this correctly, pressing the buttom will cause `Hello World!` to appear in your console.
2. Add code to the `respond()` function so that it changes the image and text of the page. You do not need use the input box or any fancy control flows yet. You may want to use the function `document.getElementById("some_id")`, `setattribute()` and set an ID for the image and text box.
3. Make the `response()` function log the content of the textbox onto the console.
4. Now, add `if` statements to decide which image and text the page should change to. Yoda follows the rules below. **Note: this section is pretty tricky. Read it carefully!**
    * If there is the word `cute` or `baby` in the textbox, have a picture of Baby Yoda.
    * If there is the word `force` in the textbox, Yoda should be using the force.
        * If there is both `dark` and `force` in the textbox, Yoda should be battling some Sith lord.
    * Yoda should say a random quote from either `std_quotes, dark_quotes, force_quotes`. Baby Yoda has not learned those quotes yet.
    * Yoda loves saying `hmmmmmmmmmmmmm`. We have Yoda print a large, random number of m's.
    * The folder `img/` will be useful to you.
5. Change `response()` so that it clears the textbox every time we press the button.
6. Right now we have to press the button in order to make Yoda change text. It would be a lot easier if we can just press `enter` to update the page! Search up how to do it on Google, and implement it.

Here is how my website looked after this stage: ![Final Yoda Chat](https://raw.githubusercontent.com/crimtech/crimtech-comp-f20/master/yoda/mdimg_/i6.JPG)

## G. Optional Projects
If you have time and wants to see Yoda become more powerful, try out some of these optional projects.

* You can use CSS to make the page look better. For example: add a background color; make a title for the page and make it look great; make the text bigger; change the font of the text.
* We only have 5 quotes in each category. Add more! As a first idea, put the quotes into files (see `quotes/`) and make the Javascript read the file for a random quote. If you want a more advanced solution, you can find a large list of random inspirational quotes, then use one of the "English to Yoda translator" online to make them look like they come from Yoda.
* You can add some actual "Machine Learning" or "NLP" to the page! Add what is known as "sentiment analysis" to the page by either using an API or a node JS package. This project is a little bigger than the previous entries, but it can be a lot of fun. Talk to me if you want to make it happen.
