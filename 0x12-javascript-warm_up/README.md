0x12. JavaScript - Warm up

1. **Why JavaScript programming is amazing:**
   JavaScript is amazing for several reasons. It is a versatile, lightweight, and widely used programming language. It is the primary language for web development, allowing developers to create dynamic and interactive websites. JavaScript supports both front-end and back-end development, making it a full-stack language. Additionally, it has a large and active community, vast ecosystem, and supports asynchronous programming through features like Promises and async/await.

2. **How to run a JavaScript script:**
   You can run a JavaScript script using a JavaScript runtime environment like Node.js or a web browser. If using Node.js, save your script with a .js extension and run it in the terminal using the command `node script.js`. For browser-based execution, embed your script within an HTML file and open it in a web browser.

3. **How to create variables and constants:**
   Variables are created using `var`, `let`, or `const`. `let` and `const` are block-scoped, while `var` is function-scoped. Constants are declared using `const` and cannot be reassigned after initialization.

   ```javascript
   let variableName = 5;
   const pi = 3.14;
   ```

4. **Differences between var, const, and let:**
   - `var`: Function-scoped, can be redeclared and reassigned.
   - `let`: Block-scoped, can be reassigned but not redeclared.
   - `const`: Block-scoped, cannot be reassigned or redeclared after initialization.

5. **Data types available in JavaScript:**
   - Primitive types: `number`, `string`, `boolean`, `null`, `undefined`, and `symbol`.
   - Complex types: `object` (including arrays and functions).

6. **How to use if, if ... else statements:**
   ```javascript
   let num = 10;
   if (num > 0) {
     console.log("Positive number");
   } else {
     console.log("Non-positive number");
   }
   ```

7. **How to use comments:**
   ```javascript
   // This is a single-line comment

   /*
    * This is a
    * multi-line comment
    */
   ```

8. **How to assign values to variables:**
   ```javascript
   let x = 5;
   x = x + 1;
   ```

9. **How to use while and for loops:**
   ```javascript
   let i = 0;
   while (i < 5) {
     console.log(i);
     i++;
   }

   for (let j = 0; j < 5; j++) {
     console.log(j);
   }
   ```

10. **How to use break and continue statements:**
    ```javascript
    for (let i = 0; i < 10; i++) {
      if (i === 5) {
        break; // exits the loop
      }
      if (i % 2 === 0) {
        continue; // skips the rest of the loop and goes to the next iteration
      }
      console.log(i);
    }
    ```

11. **What is a function and how to use functions:**
    Functions are blocks of reusable code. They are defined using the `function` keyword.

    ```javascript
    function add(a, b) {
      return a + b;
    }

    console.log(add(3, 4)); // Outputs 7
    ```

12. **What does a function that does not use any return statement return:**
    If a function does not use the `return` statement, it implicitly returns `undefined`.

13. **Scope of variables:**
    Variables declared with `var` are function-scoped, while those declared with `let` and `const` are block-scoped. Global variables are accessible throughout the entire program.

14. **Arithmetic operators and how to use them:**
    ```javascript
    let a = 5;
    let b = 3;

    console.log(a + b); // Addition
    console.log(a - b); // Subtraction
    console.log(a * b); // Multiplication
    console.log(a / b); // Division
    console.log(a % b); // Modulus
    ```

15. **How to manipulate a dictionary:**
    In JavaScript, dictionaries are represented as objects. You can add, access, and remove key-value pairs.

    ```javascript
    let person = {
      name: "John",
      age: 30,
      job: "Developer"
    };

    console.log(person.name); // Accessing value
    person.location = "City A"; // Adding a new key-value pair
    delete person.job; // Removing a key-value pair
    ```

16. **How to import a file:**
    In a Node.js environment, you can use the `require` function to import modules/files.

    ```javascript
    // Importing a module
    const myModule = require('./myModule');

    // Using the imported module
    myModule.someFunction();
    ```
