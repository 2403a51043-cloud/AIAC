// Import readline for user input
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter numbers: ", (input) => {
  // Split input by spaces and convert to numbers
  const numbers = input.split(" ").map(Number);

  // Filter even numbers (like Python list comprehension)
  const evenNumbers = numbers.filter(n => n % 2 === 0);

  console.log(evenNumbers);
  rl.close();
});
