// 1. Given the data below, define a type alias for representing users.

let users = [  
    {
        name:'Shoha Tsuchida',
        age:99,
        company:'Coding Temple'
    },  
    {
        name:'Dylan Katina',
        age:99
    }
];

type User = {
    name: string,
    age: number,
    company?: string
}

const shoha: User = {
    name: 'Shoha Tsuchida',
    age: 99,
    company: 'Coding Temple'
}

const dylank: User = {
    name: 'Dylan Katina',
    age: 99
}

// 2. Define a type for representing the days of week. Valid values are “Monday”, “Tuesday”, etc.

type Weekdays = ('Monday'|'Tuesday'|'Wednesday'|'Thursday'|'Friday'|'Saturday'|'Sunday')

// 3. Given the Person class below, create a getter for getting the full name of a person.

class Person {
    constructor(
        public firstName:string, 
        public lastName:string) {}

    getter = ():string => {
        return `${this.firstName} ${this.lastName}`
    }
}

// 4. Create a new class called "Employee" that extends "Person" and adds a new property called salary. 

class Employee extends Person {
    constructor(
        public firstName: string,
        public lastName: string,
        public salary: number
    ) {
        super(firstName, lastName);
    }

}









// 5. Given the data below, define an interface for representing employees:
// HINT: You'll need 2 interfaces.
let employee = {
    name:'Christian Askew',
    salary:1_000_000,
    address:{
        street:'Thieves st',
        city:'Seattle',
        zipCode: 98101
    }
};

interface Address {
    street: string,
    city: string,
    zipCode: number
}

interface Empl {
    name: string,
    salary: number,
    address: Address
}