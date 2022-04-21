```mermaid
classDiagram
  class Human {
    +str name
    #int Age
  }

  class Id { -int value }
  class Age { -int value }
  class Owner
  class Employee {
    +int Id

    +int get_age()
  }

  Human <|-- Owner : extends
  Human <|-- Employee : extends
  Human o-- Id
  Human o-- Age
  Owner --> Employee : use
  ````