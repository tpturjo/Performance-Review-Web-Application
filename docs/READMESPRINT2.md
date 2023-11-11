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

- Unit tests are broken up into two files under the test folder. Manuel Server Module Testing.pdf contains unit testing 
instructions for the route.py file. testdatabase.py contains unit tests for the database.py and route.py file.
The user.py file did not require unit tests since it only contains setter and getter methods for the data in the userDatabase.db file.


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

#Process Model Analysis Document

- The component architecture diagram can be found in Path docs/Component_Architecture_Document.svg

# Performance Reviews

- Performance reviews can be found in the PerformanceReviews.md file. Path: docs/Process Model Analysis Document.md 

# Attribution Table

- The Attribution table containing all references used can be found in the AttributionTable.md file. Path docs/AttributionTable.md
