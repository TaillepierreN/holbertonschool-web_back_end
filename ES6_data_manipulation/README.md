# ES6 Data Manipulation

**Amateur**  
**By:** Johann Kerbrat, Engineering Manager at Uber Works  
**Weight:** 1  
**Migrated to checker v2:**  
Your score will be updated as you progress.

## Resources

Read or watch:

- Array
- Typed Array
- Set Data Structure
- Map Data Structure
- WeakMap

## Learning Objectives

By the end of this project, you should be able to explain to anyone, without the help of Google:

- How to use `map`, `filter`, and `reduce` on arrays
- Typed arrays
- The `Set`, `Map`, and `WeakMap` data structures

## Requirements

- All your files will be executed on Ubuntu 18.04 LTS using NodeJS 12.11.x
- Allowed editors: vi, vim, emacs, Visual Studio Code
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `.js` extension
- Your code will be tested using Jest and the command `npm run test`
- Your code will be verified against lint using ESLint
- Your code needs to pass all the tests and lint. You can verify the entire project running `npm run full-test`
- All of your functions must be exported

## Setup

### Install NodeJS 12.11.x

In your home directory:

```sh
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y
nodejs -v
# Expected output: v12.11.1
npm -v
# Expected output: 6.11.3

Install Jest, Babel, and ESLint
In your project directory:

# Install Jest
npm install --save-dev jest

# Install Babel
npm install --save-dev babel-jest @babel/core @babel/preset-env

# Install ESLint
npm install --save-dev eslint

Configuration files
package.json
babel.config.js
.eslintrc.js

And…
Don’t forget to run npm install when you have the package.json
