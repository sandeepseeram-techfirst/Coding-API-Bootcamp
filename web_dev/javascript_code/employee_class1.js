class Person {
    constructor(last, first) { this.last = last; this.first = first }
    get fullName() { return `${this.last}, ${this.first}` }
    set fullName(value) {
      const parts = value.split(/,\s*/)
      this.last = parts[0]
      this.first = parts[1]
    }
  }
  
  let fred = new Person('Flintstone', 'Fred')
  console.log(fred.fullName)
  fred.fullName = 'Astaire, Fred'
  console.log(fred)