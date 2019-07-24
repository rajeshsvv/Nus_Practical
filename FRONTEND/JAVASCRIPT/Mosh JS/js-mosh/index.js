// console.log('Hi Hello Javascript');



// let va="John";
// console.log(va);

// let firstName,secondName;       //first way

// let firstName="john";           //second way
// let secondName="Nirjan";

// const interestRate=.3;
// interestRate=.3;
// console.log(interestRate);


// let name='josh';
// let age=30;
// let isApproved=true;
// let thirdName=undefined; //if we dont initialize by default its value is undefined. also explicitly mention undefined
// let fourthname=null;
// let selectedColour=null;


/*
let person={
    name:"john",
    age:30.569
}
let selection='name';
person.name="Ritu";
person['name']="kristofer";

console.log(person.name)
*/


/*
let selectedColours=['red','blue'];
selectedColours[2]='yellow';
selectedColours[3]=9;
console.log(selectedColours);
console.log(selectedColours[1]);
*/


//function declaration:
//Performing a task
function greet(name,lastName)
{
    console.log("Hello greet "+name+" "+lastName);

}
greet('hari',"neetu");
greet('seeta',21);


//calculating the value
function square(number)
{
    return number*number;
}


console.log(square(20));