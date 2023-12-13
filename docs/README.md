# Performance Review Web Application

The web application created by our team is a cohesive platform that streamlines the process of writing, managing, and sharing reviews. 
It's built on a client-server model utilizing HTML/CSS for the front-end and the Bottle framework for server-side operations, underpinned by a 
SQLite database for data persistence. Key features include account management, password security, review drafting, and publishing with anonymous 
options, as well as interactive elements like comment systems and rating functionalities. The architecture ensures usability with an intuitive 
interface, maintainability through modular design, and testability via comprehensive API and unit tests. Scalability is anticipated, albeit with 
careful consideration of database load and session management.

## Table of Contents

- [Description of Application/Project]
- [Additional Important Information]
- [Unit Tests]
- [Docstrings]
- [Meeting Notes]
- [Code Reviews]
- [Kanban Board]
- [Project Progress]
- [Component Architecture Document]
- [Process Model Analysis Document]
- [Microservice Architecture Document]
- [Requirements Document]
- [Final Sprint Implementations]
- [Performance Reviews]
- [Attributions Table]


# Description of Application/Project

- Our Performance Review application is a dynamic web-based platform designed to streamline the process of creating, managing, 
and evaluating performance reviews. At the core of the application is a robust Python backend, with key scripts such as database.py 
for database interactions, route.py for request handling, and user.py for user data management. These scripts work in tandem with a 
userDatabase.db SQLite database, which houses essential tables like Users, Reviews, and Drafts, facilitating efficient data manipulation.

- The application's architecture is meticulously laid out in our Process Model Analysis Text Document and accompanied by a comprehensive 
Process Model Analysis Diagram. Together, they provide an in-depth look at the application's workflow and the interconnections between its 
various components.

- Running the application is straightforward thanks to the if __name__ == '__main__': block within the route.py file, which serves as the entry 
point for the server. With the simplesqlite plugin, stakeholders can easily inspect the database tables to monitor how data is managed and 
maintained throughout the application's lifecycle.

- The application's front-end is designed for ease of use, with HTML templates and CSS styling ensuring a user-friendly interface. This is 
supported by the server-side logic that not only authenticates users but also allows for the secure creation, editing, and publishing of 
reviews, including draft saving and anonymous submissions.

- In essence, this application embodies a harmonious blend of functionality and user experience, bolstered by a well-documented and scalable 
architecture.


# Additional Important Information

- We each had our assigned tasks and sections but we also assisted each other when we could. This allowed us to each 
understand the program better as a whole, while still being able to specialize in one or a few key roles.

- Unit tests (As well as other documents (microservice, Architecture, etc) were uploaded by one member of the group, but they were 
developed by all members of the group during our last several meetings.

- Code was reviewed by members of the group before it was merged into the project. Some members added comments later, 
but we never merged code that wasn't first reviewed and approved.


# Unit Tests

- Within our project, unit_test.py plays a pivotal role, encompassing a broad spectrum of tests that scrutinize every component, from user 
authentication mechanisms to data retrieval and API functionality. In parallel, our Postman suite, detailed in term-project-teamm.postman_collection.json, 
executes a series of API tests, ensuring that all endpoints meet our stringent criteria for reliability and performance. This dual-faceted testing 
strategy guarantees comprehensive coverage, and by employing continuous regression testing, we maintain the integrity of the system against new 
changes. The regression tests are designed to detect any discrepancies early on, preventing the introduction of bugs and ensuring that new code 
merges do not disrupt existing functionalities. This rigorous testing regimen is integral to our development lifecycle, instilling confidence in 
the stability of our application with each sprint and release.


- The user.py file did not require unit tests since it only contains setter and getter methods for the data in the
userDatabase.db file.


# Docstrings

- Throughout our project, every piece of code is meticulously annotated with docstrings, adhering to PEP8 and PEP257 standards. This practice 
 has been consistently applied across all scripts, including database.py, route.py, and user.py, ensuring that each function, class, and module 
is accompanied by clear, concise descriptions. These docstrings not only facilitate easier understanding and maintenance of the code but also 
serve as an invaluable guide for future developers interacting with our application. By strictly following these Python documentation 
conventions, we have significantly enhanced the readability and standardization of our codebase, contributing to the overall quality and 
sustainability of the project.


# Meeting Notes

- Meeting notes can be found in the MeetingNotes.md file. Path docs/MeetingNotes.md
- We took turns writing the meeting notes during the sprint. We also took turns filling the role of scrum master. In the meeting notes you can see who participated in each of these roles during each meeting.
- Meeting notes contain information on note takes and scrum master, attendance, discussions made, decisions made, progress made, and code reviews

- To streamline the review of these notes and enhance accessibility, we have incorporated specific keywords, enabling efficient navigation 
through the document. These include:

  - Stub Implementation: Searchable through the keyword "stub/Stub," these sections detail our approach to developing and integrating stubs into our application.
  - Code Review: Using "review/Review," this part reflects our thorough analysis and feedback on code contributions, ensuring quality and adherence to project standards.
  - Progress Report/ Regular Reports of Tasks: Found with "report/Report," these segments offer insights into ongoing tasks and responsibilities assigned to team members.
  - Discussion of SOLID Principles and Decoupling: Accessible via "decouple/Decouple," these notes focus on our adherence to SOLID principles and efforts towards decoupling components for better modularity.
  - Difficulties Encountered: Located using "difficult/Difficult," this section candidly discusses any challenges faced and the solutions employed.
  - Daily Progress: Marked by "progress/Progress," these entries provide a day-to-day account of our project's advancement.

These meeting notes serve as a comprehensive record, reflecting our project's evolution, teamwork dynamics, and our commitment to a structured, transparent development process.


# Code Reviews

- Our code review process, documented in the MeetingNotes.md file, forms a crucial part of our development strategy. Each team meeting included thorough code reviews, 
with detailed feedback provided as comments on pull requests before merging. This approach ensured consistent quality control, fostered collaborative learning, 
and helped maintain our application's integrity as we collectively reviewed and refined code submissions in real-time, adhering to established coding standards and project guidelines.

- Code reviews can be found in the MeetingNotes.md file throughout each of our meeting submissions. 
Code reviews were also made as comments on pull requests as we merged them together in team meetings.


# Kanban Board

- Kanban board can be located on our remote git under projects. Our Backlog in our Kanban board includes tasks we would have pursued
if there were additional sprints past sprint 3.


# Project Progress

- Can be found in our ProjectProgress file with path docs/ProjectProgress.md


# Component Architecture Document

- The Component Architecture Document of our project, enriched with the insights from the provided material and the detailed UML diagram, 
outlines the structure and interaction of various elements within our web application. It covers the client-side components, 
including HTML and CSS for the user interface, and server-side components like HTTP request handling in server.py, ensuring seamless 
communication and data management. The document also delves into the integral role of the SQLite database (userDatabase.db), the robust data 
structures, and the object mapping mechanisms implemented. Additionally, it comprehensively addresses session management, utility functions, 
and the testing components, ensuring a thorough understanding of the application's architecture and its functionality. This document has been 
crucial in guiding the development process, ensuring a cohesive and scalable application design. docs/Component_Architecture_Text_Document.md

- The component architecture diagram can be found in Path docs/Component_Architecture.md. UML Diagram can be found under #UML Diagram
as a hyperlink in the document.


# Process Model Analysis Document

- The Process Model Analysis Document for our project provides a detailed narrative of our agile development journey, supported by a 
comprehensive diagram that maps our workflow. It reflects on the initial challenges and the subsequent enhancements to our process, 
emphasizing the adoption of strict deadlines and effective merging strategies. The document showcases our commitment to continuous improvement, 
embedding docstring integration, and database design forethought into our workflow. This careful documentation serves not only as a record of 
our progress but also as a guide for future projects, illustrating the balance between structured planning and the flexibility required for 
dynamic project environments.

- The Process Model Analysis can be found in Path docs/Process_Model_Analysis Document.md

- The component architecture diagram can be found in Path docs/Component_Architecture.md. UML Diagram can be found under #UML Diagram
as a hyperlink in the document.


# Microservice Architecture Document

- Our project's Microservice Architecture Document delineates a transformative approach, transitioning from a monolithic structure to a 
distributed microservice framework, as illustrated in our comprehensive diagram. It identifies autonomous services such as user authentication, 
profile services, and content management, providing a stark comparison to our previous component-based model. This transition is poised to 
revolutionize our software process, offering modular development, streamlined deployment through CI/CD pipelines, and scalable services tailored 
to demand. Enhanced monitoring and independent service management will lead to a robust, agile, and more responsive application system.

- The microservice architecture document can be found in Path docs/Microservice_Architecture_Document.md


# Requirements Document

- The requirements document can be found in Path term-project-teamm/requirements.txt


# Final Sprint Implementations

- Turjo
  - In our project's final sprint, I implemented key features and ensured seamless integration with our web application's architecture. Here's a breakdown of my contributions:
  - Profile Data Retrieval: In database.py, I added the get_profile_data_by_username function to retrieve a user's profile data from the database.
  - Profile Data Update: Added the edit_profile function to update user information in the database, providing a dynamic user experience and personalization.
  - Post Editing Capability: Developed get_post_by_id and update_post functions, empowering users to edit their published content, thus enhancing the application's content management system
  - Routing and Templates: In route.py, I created the routes /profileEdit and /profile, which serve the profile editing and viewing pages using the Bottle framework. These routes integrate with the front-end templates, profile_edit.html and profile.html, to display and update user information dynamically.
  - Form Handling: Enhanced the form submission handling in route.py to include profile editing (EDIT_PROFILE) and post-editing actions, which are crucial for a complete user interaction cycle within our application.
  - HTML Page for Post Editing (templates/my_posts.html):  I created a dedicated HTML page, my_posts.html, to provide users with a user-friendly interface for editing their posts. This page features a list of the user's posts, edit forms for each post, and an update button for saving changes.
  - Unit Testing and API Integration: Each implemented feature is covered by unit tests in unit_test.py[test_edit_profile(self):,test_update_post(self): ,test_edit_nonexistent_review(self):] and Postman API tests (term-project-teamm.postman_collection.json)[GET Profile page , POST Edit Profile page,GET Updated profile page, GET My Posts page,POST Edit existing post], ensuring that all new code is thoroughly tested for functionality and integration with existing components.
  - Documentation: Each piece of code I've introduced includes comprehensive docstrings, following PEP standards, which articulate the purpose and usage of functions and routes, making the codebase maintainable and understandable. These docstrings are integral to our project's documentation strategy, ensuring clarity for all modules and public interfaces.

- Caleb
  - During sprint 3 I implemented features that primarily had to due with construction and manipulation of the database, as well as some other useful functions and features. Here's a breakdown of my contributions:
  - Updates to the userDatase.db file for further efficiency in the sprint (Changes to relational model)
  - Added the comments table and profiles table, as well as the attributes needed in each.
  - Anonymous routing function to allow for users to submit anonymous reviews.
  - Getter and setter methods for profiles table to save and retrieve user profile information.
  - Save_comment and get_comment functions to save and retrieve comment data saved in the comments table.
  - Tidied up several sections of code.
  - Unit Testing and API Integration: All coding features have associated unit tests to test code to ensure the functions do in fact work properly.
  - Documentation: Each section of code has comprehensive docstrings that briefly explain the function they are a part of, as well as the arguments and return values.

- Daniel
  - During sprint 3 I implemented several web based and routing functions and features as well as a few others. Here's a breakdown of my contributions:
  - CSS in styles.css for buttons and overall styling  
  - Helper methods in methods.py for list manipulation  
  - Require_logout method in route.py  
  - Implementation of a new “home” page (html and route.py)  
  - Javascript for “comment” functionality (pop up / retract feature) on “public.html”  
  - New database.py method “get_published_reviews_and_comments()” to retrieve   comment data from SQL.  
  - Created logos and images for the webpage. 
  - Implemented Unit tests and documentation throughout code.

- Tanjet
  - Routing part for Comment feature. Routing and post request functionality
  - Making profile.py(Data structure)
  - Sweeping the code and worked on the proofreading to see if PEP standard was met
  - Added docstring and tidied up.
  - Worked on the Microservice Architecture Document and Diagram
  - Implemented Unit tests and documentation throughout code.

  
# Performance Reviews

- Throughout our project, we've established a consistent practice of conducting performance reviews at the end of each sprint, 
including our initial and second sprints, with the process now culminating in our final sprint. These reviews have been instrumental 
in providing each team member with constructive feedback, identifying both strengths and areas for growth. Our final sprint review reflects 
a culmination of insights gained over time, noting the individual and collective progress we've made. Despite facing typical team challenges, 
we've collectively adapted and succeeded, ensuring any difficulties were addressed and managed as part of our continuous improvement within 
our Kanban/agenda items. This regular introspection has been key to our team's overall success and professional development.


- Performance reviews can be found in the PerformanceReviews.md file. Path: docs/PerformanceReviews.md 


# Attribution Table

- The Attribution table containing all references used can be found in the AttributionTable.md file. Path docs/AttributionTable.md
