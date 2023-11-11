# Performance Review Web Application


Our application allows a user to create an account and then publish reviews. It also allows a user to save one review draft at a time if they would prefer not to publish yet.

## Table of Contents

- [Description of Application/Project]
- [Additional Important Information]
- [Unit Tests]
- [Meeting Notes]
- [Code Reviews]
- [Kanban Board]
- [Component Architecture Document]
- [Process Model Analysis Document]
- [Performance Reviews]
- [Attributions Table]

# Description of Application/Project
- The performance review application we created uses code in the files: database.py, route.py, and user.py. The application also reads and writes to an SQLite database file named userDatabase.db.

- The specifics of the program and code can be found in the Process Model Analysis Text Document and Process Model Analysis Document.

- The application can be run using the "if name == 'main':" line of code at the bottom of the file.

- The userDatabase.db file contains the Users, Reviews, and Drafts tables that allow for manipulation of data for the application. By installing the simplesqlite plugin, you can view the tables and what they contain as data as manipulated within them.

# Additional Important Information

- We each had our assigned tasks and sections but we also assisted each other when we could. This allowed us to each understand the program better as a whole, while still being able to specialize in one or a few key roles.
- Unit tests were uploaded by one member of the group, but they were developed by all members of the group during our last few meetings.
- We have implemented a few stubs in our program. A few of these were transformed into working methods as we progressed sprint 2. A few were implemented and 
left as stubs for implementation in the next sprint, or due to issues and error that arose. Information for this can be found in the meeting notes.

# Unit Tests

Path docs/test

Our unit testing setup for the term project is divided into two distinct parts, each focusing on a different aspect of the project:

Testing for Route.py Using Postman:

We have dedicated a set of unit tests specifically for our route.py file.
These tests are designed in accordance with the guidelines provided by our professor.
We utilize Postman, a popular API testing tool, to conduct these tests. This approach allows for a comprehensive evaluation of our routing logic.
The test suite is encapsulated in a file named term-project-teamm.postman_collection.
To demonstrate adherence to the professor's instructions, we've exported this Postman collection file. This export serves as proof of our methodical and structured testing process.
Testing for Database.py Using PyCharm:

The second part of our testing focuses on the database.py file.
This segment aims to validate the functionality and reliability of our database interactions.
The tests are designed to be run through PyCharm, an Integrated Development Environment (IDE), making the process straightforward and efficient.
To execute these tests, one simply needs to navigate to the testdatabase.py program in PyCharm and run the main function.
The outcome of these tests is immediately visible upon execution, providing instant feedback on the database's performance.
This test suite comprises 9 individual tests, all of which have been successfully passed, indicating robust database functionality.

In summary, our unit testing framework is bifurcated into two main sections: one for routing using Postman and the other for database functionality using PyCharm. Both sections have been rigorously tested and have met all required standards, ensuring the reliability and efficiency of our project components.


- The user.py file did not require unit tests since it only contains setter and getter methods for the data in the
userDatabase.db file.


# Meeting Notes

- Meeting notes can be found in the MeetingNotes.md file. Path docs/MeetingNotes.md
- We took turns writing the meeting notes during the sprint. We also took turns filling the role of scrum master. In the meeting notes you can see who participated in each of these roles during each meeting.
- Meeting notes contain information on note takes and scrum master, attendance, discussions made, decisions made, progress made, and code reviews

- USE CONTROL FIND to search these keywords to navigate our meeting note:
  - Stub Implementation  (keyword: stub/Stub)
  - Code Review  (keyword: review/Review)
  - Regular Reports of Task (keyword: report/Report)
  - Discussion of solid (keyword: decouple/Decouple)
  - Difficulties (keyword: difficult/Difficult)
  - Daily Progress (keyword: progress/Progress)



# Code Reviews

- Code reviews can be found in the MeetingNotes.md file throughout each of our meeting submissions. 
Code reviews were also made as comments on pull requests as we merged them together in team meetings.

# Kanban Board
- Kanban board can be located on our remote git under projects. Our Backlog in our Kanban board includes tasks we intend to implement in future Sprints


# Component Architecture Document

- The component architecture diagram can be found in Path docs/Component_Architecture_Document.svg
- The component architecture text document contains more detailed information of our architecture. It can be found in Path docs/Component_Architecture_Text_Document.md

# Process Model Analysis Document

- The Process Model Analysis can be found in Path docs/Process Model Analysis Document.md
- The component architecture diagram can be found in Path docs/Component_Architecture_Document.svg


# Performance Reviews

- Performance reviews can be found in the PerformanceReviews.md file. Path: docs/Process Model Analysis Document.md 

# Attribution Table

- The Attribution table containing all references used can be found in the AttributionTable.md file. Path docs/AttributionTable.md
