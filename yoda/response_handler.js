// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

function respond() {
    let text = document.getElementById("instr").value
    let name = names[randint(0, 1)]
    let mood = moods[randint(0, 2)]
    if (text.includes("cute") || text.includes("baby")) {
        name = "cute"
    }
    if (text.includes("force")) {
        mood = "force"
        if (text.includes("dark")) {
            mood = "dark"
        }
    }
    let quote = std_quotes[randint(0, 4)]
    let draw = randint(0, 2)
    if (draw == 1) {
        quote = force_quotes[randint(0, 4)]
    }
    if (draw == 2) {
        quote = dark_quotes[randint(0, 4)]
    }
    if (name == "cute") {
        let m = "m"
        quote = "yes, h" + m.repeat(randint(2, 10))
    }
    let path = "img/" + name + "-" + mood + ".jpg"
    document.getElementById("image").src = path
    document.getElementById("caption").innerHTML = quote
    console.log(text)
}

function randint(min, max) {
    min = Math.ceil(min)
    max = Math.floor(max)
    return Math.floor(Math.random() * (max - min + 1)) + min
}
