0x14. JavaScript - Web scraping

### 1. Why JavaScript Programming is Amazing
JavaScript is an incredibly versatile programming language that powers the interactive features of websites and web applications. Its flexibility and ease of use make it a favorite among developers for a variety of reasons:

- **Cross-platform Compatibility**: JavaScript can run on any device with a web browser, making it a universal language for both front-end and back-end development.
- **Rich Ecosystem**: JavaScript has a vast ecosystem of libraries and frameworks like React, Angular, and Vue.js, which streamline development and enhance productivity.
- **Asynchronous Programming**: JavaScript's asynchronous nature allows for non-blocking operations, enabling smooth user experiences and efficient handling of tasks like fetching data from servers without freezing the UI.
- **Community Support**: JavaScript has a vibrant and active community that continuously contributes to its growth and improvement, providing resources, tutorials, and support for developers of all levels.

Example:
```javascript
// Example of JavaScript code
console.log("Hello, world!");
```

### 2. How to Manipulate JSON Data
JSON (JavaScript Object Notation) is a lightweight data interchange format commonly used for transmitting data between a server and a web application. Manipulating JSON data in JavaScript is straightforward, as it provides built-in methods for parsing and stringify JSON objects.

Example:
```javascript
// Example of manipulating JSON data
const jsonData = '{"name": "John", "age": 30}';
const obj = JSON.parse(jsonData);
console.log(obj.name); // Output: John

obj.age = 35;
const updatedJsonData = JSON.stringify(obj);
console.log(updatedJsonData); // Output: {"name":"John","age":35}
```

### 3. How to Use Request and Fetch API
Requesting data from servers is a common task in web development, and JavaScript provides two main methods for accomplishing this: the older `XMLHttpRequest` and the newer `fetch` API. The `fetch` API offers a more modern and flexible approach to making HTTP requests and handling responses.

Example using `fetch` API:
```javascript
// Example of using Fetch API
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error fetching data:', error));
```

### 4. How to Read and Write a File Using fs Module
In Node.js, the `fs` module provides functions for interacting with the file system, allowing you to read from and write to files on your computer. This is particularly useful for handling file operations in server-side applications.

Example:
```javascript
// Example of reading and writing files using fs module
const fs = require('fs');

// Reading a file
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log('File content:', data);
});

// Writing to a file
const contentToWrite = 'This is the content to write to the file.';
fs.writeFile('example.txt', contentToWrite, (err) => {
  if (err) {
    console.error('Error writing to file:', err);
    return;
  }
  console.log('File written successfully.');
});
```