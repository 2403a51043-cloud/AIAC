const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let students = [];

function askName() {
    rl.question("Enter student name (or press Enter to finish): ", function(name) {
        if (name === "") {
            // Finished entering names, print the list
            console.log("\nStudent List:");
            students.forEach(student => console.log(student));
            rl.close();
        } else {
            students.push(name);
            askName(); // Ask next name
        }
    });
}
askName();
