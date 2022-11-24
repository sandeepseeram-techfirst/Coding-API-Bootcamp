JavaScript "use strict"
https://www.w3schools.com/js/js_strict.asp
The purpose of "use strict" is to indicate that the code should be executed in "strict mode". 
With strict mode, you can not, for example, use undeclared variables. 
The numbers in the table specify the first browser version that fully supports the directive. 
You can use strict mode in all your programs.

A constant is a variable that never changes. You use the const keyword instead of let.

const steps = require('./steps.js') to test the steps inside js code. 


The parseInt and parseFloat functions convert strings to numbers.

JavaScript has the usual + - * / operators that you know from other programming languages.

String literals can be delimited with single quotes or double quotes, 'like this' or "like that".


A JavaScript object is nothing like an object in an OO language such as C++ or Java. It is simply a set of properties, each with a name and value:

Example:
const harry = { name: 'Harry', age: 42 }

Destructuring is a convenient way to get values out of an array or object. 

An expression is made up of literals, variables, operators, and function calls. Every expression has a value.
A statement (declaration, assignment, branch, loop, and so on) is executed for its effect. Statements don't have values.
A Boolean value is either true or false. The name comes from the logician George Boole who discovered the laws of logic way back when.

A Boolean value is either true or false. The name comes from the logician George Boole who discovered the laws of logic way back when.


$ node --use-strict
Welcome to Node.js v12.16.3.
Type ".help" for more information.
> 'Hello' === 'Hel' + 'lo'
true
> 6 * 7 === 42
true
 
The opposite of === is !==:


JavaScript has four comparison operators: <, <=, >, >=


JavaScript has two "bottom" values: undefined and null. Some library functions prefer to return undefined to indicate the absence of a value. Others return null.


Loops: 
JavaScript has the classic three-part for loop of all languages that trace their heritage back to the C language.

let items = ['Eggs', 'Spam', 'Hash browns', 'Salsa']
for (let i = 1; i <= items.length; i++)
   console.log(`${i}. ${items[i - 1]}`)

for (const item of items) 
   console.log(`* ${item}`)

functions: 
A function has input variables (or parameters) and produces a result (or return value). Here is an example:

function average(x, y) {
  return (x + y) / 2
}
average(6, 7)
6.5