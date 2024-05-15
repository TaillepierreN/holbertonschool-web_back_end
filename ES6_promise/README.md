Here's a comprehensive README file for your ES6 Promises project:

```markdown
# ES6 Promises

## Overview
This project focuses on understanding and utilizing ES6 Promises in JavaScript. You'll learn how to handle asynchronous operations, use the `then`, `catch`, and `finally` methods, and employ async/await syntax. By the end of this project, you'll be able to explain and use Promises effectively.

## Learning Objectives
By the end of this project, you should be able to:
- Understand the concept of Promises, their use cases, and their benefits.
- Use the `then`, `resolve`, and `catch` methods.
- Utilize every method of the Promise object.
- Apply `try` and `catch` for error handling.
- Understand and use the `await` operator.
- Write and use async functions.

## Requirements
- All files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x.
- Use allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`.
- All files should end with a new line.
- Include a `README.md` file at the root of the project folder.
- Use the `.js` file extension for your code.
- Test your code using Jest and the command `npm run test`.
- Verify your code against lint using ESLint.
- Export all of your functions.

## Setup

### Install NodeJS 12.11.x
In your home directory, run the following commands:
```bash
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v  # should output v12.11.1
npm -v  # should output 6.11.3
```

### Install Jest, Babel, and ESLint
In your project directory, run:
```bash
npm install --save-dev jest
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/cli
npm install --save-dev eslint
```

### Run `npm install`
Don't forget to run `npm install` when you have the `package.json` file.

## Tasks

### Task 0: Keep every promise you make and only make promises you can keep
**File:** `0-promise.js`

Create a function `getResponseFromAPI` that returns a Promise.

**Example:**
```javascript
import getResponseFromAPI from "./0-promise.js";

const response = getResponseFromAPI();
console.log(response instanceof Promise);  // should output true
```

### Task 1: Don't make a promise...if you know you can't keep it
**File:** `1-promise.js`

Create a function `getFullResponseFromAPI(success)` that returns a promise.

- If `success` is true, resolve the promise with an object:
  ```json
  { "status": 200, "body": "Success" }
  ```
- If `success` is false, reject the promise with an error object:
  ```json
  { "message": "The fake API is not working currently" }
  ```

**Example:**
```javascript
import getFullResponseFromAPI from './1-promise';

console.log(getFullResponseFromAPI(true));  // should output a resolved promise
console.log(getFullResponseFromAPI(false));  // should output a rejected promise
```

### Task 2: Catch me if you can!
**File:** `2-then.js`

Create a function `handleResponseFromAPI(promise)` that appends three handlers to the promise.

- When the Promise resolves, return an object:
  ```json
  { "status": 200, "body": "success" }
  ```
- When the Promise rejects, return an empty Error object.
- For every resolution, log "Got a response from the API" to the console.

**Example:**
```javascript
import handleResponseFromAPI from "./2-then";

const promise = Promise.resolve();
handleResponseFromAPI(promise);  // should log "Got a response from the API"
```

### Task 3: Handle multiple successful promises
**File:** `3-all.js`

Create a function `handleProfileSignup` that imports `uploadPhoto` and `createUser` from `utils.js`. Use these functions to collectively resolve all promises and log `body firstName lastName` to the console.

- In the event of an error, log "Signup system offline" to the console.

**Example:**
```javascript
import handleProfileSignup from "./3-all";

handleProfileSignup();  // should log "photo-profile-1 Guillaume Salva"
```

### Task 4: Simple promise
**File:** `4-user-promise.js`

Create a function `signUpUser(firstName, lastName)` that returns a resolved promise with an object:
```json
{
  "firstName": value,
  "lastName": value
}
```

**Example:**
```javascript
import signUpUser from "./4-user-promise";

console.log(signUpUser("Bob", "Dylan"));  // should output a resolved promise
```

### Task 5: Reject the promises
**File:** `5-photo-reject.js`

Create a function `uploadPhoto(fileName)` that returns a promise rejecting with an error:
```json
{ "message": "$fileName cannot be processed" }
```

**Example:**
```javascript
import uploadPhoto from './5-photo-reject';

console.log(uploadPhoto('guillaume.jpg'));  // should output a rejected promise
```

### Task 6: Handle multiple promises
**File:** `6-final-user.js`

Create a function `handleProfileSignup(firstName, lastName, fileName)` that calls `signUpUser` and `uploadPhoto`. Return an array with the following structure:
```json
[
  { "status": "status_of_the_promise", "value": "value or error returned by the Promise" },
  ...
]
```

**Example:**
```javascript
import handleProfileSignup from './6-final-user';

console.log(handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg"));  // should output a promise with an array
```

### Task 7: Load balancer
**File:** `7-load_balancer.js`

Create a function `loadBalancer(chinaDownload, USDownload)` that returns the value of the promise that resolves first.

**Example:**
```javascript
import loadBalancer from "./7-load_balancer";

const promiseUK = new Promise((resolve) => setTimeout(resolve, 100, 'Downloading from UK is faster'));
const promiseFR = new Promise((resolve) => setTimeout(resolve, 200, 'Downloading from FR is faster'));

const test = async () => {
  console.log(await loadBalancer(promiseUK, promiseFR));  // should output "Downloading from UK is faster"
}

test();
```

### Task 8: Throw an error
**File:** `8-try.js`

Create a function `divideFunction(numerator, denominator)` that throws an error if `denominator` is 0, otherwise returns the result of the division.

**Example:**
```javascript
import divideFunction from './8-try';

console.log(divideFunction(10, 2));  // should output 5
console.log(divideFunction(10, 0));  // should throw an error
```

### Task 9: Throw error / try catch
**File:** `9-try.js`

Create a function `guardrail(mathFunction)` that returns an array `queue`.

- Append the value returned by `mathFunction` to the `queue`.
- If an error is thrown, append the error message to the `queue`.
- Always append "Guardrail was processed" to the `queue`.

**Example:**
```javascript
import guardrail from './9-try';
import divideFunction from './8-try';

console.log(guardrail(() => divideFunction(10, 2)));  // should output [5, 'Guardrail was processed']
console.log(guardrail(() => divideFunction(10, 0)));  // should output ['Error: cannot divide by 0', 'Guardrail was processed']
```

## Files

### `package.json`
Your `package.json` file should include the necessary dependencies and scripts.

### `babel.config.js`
Your Babel configuration file.

### `utils.js`
Contains `uploadPhoto` and `createUser` functions for use in your tasks.

### `.eslintrc.js`
Your ESLint configuration file.

## Resources
- [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [JavaScript Promise: An introduction](https://developers.google.com/web/fundamentals/primers/promises)
- [Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
- [Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [Throw / Try](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
