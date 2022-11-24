class Person {
    constructor(last, first) { this.last = last; this.first = first }
    get fullName() { return `${this.last}, ${this.first}` }
  }
  
  let fred = new Person('Flintstone', 'Fred')
  console.log(fred.fullName)
  