# Performance Review Web Application
Our application allows a user to create an account and then publish reviews. It also allows a user to save one 
review draft at a time if they would prefer not to publish yet.

## Table of Contents
- [Description of Application/Project]
- [Additional Important Information]
- [Unit Tests]
- [Meeting Notes]
- [Code Reviews]
- [User Stories]
- [Kanban Board]
- [Performance Reviews]
- [Attributions Table]


# Description of Application/Project
- The performance review application we created uses code in the files: database.py, route.py, and user.py. The
application also reads and writes to an sqlite database file named userDatabase.db.


- The database.py file contains functions that interact with the userDatabase.db file to store, manipulate and 
retrieve data from the sqlite tables in the database. The functions in the database.py file allow a user to be able
to create an account, retrieve user data, store user written drafts, and store/retrieve written reviews.


- The user.py file contains a User class and Draft class. Each of the classes contains setter and getter methods 
to set and retrieve the data from the sqlite database.


- The route.py file contains the mapping functionality for the user as well as the method call to start the 
performance review application through the use of the Bottle web framework. It establishes the various routes for 
the application's web page and buttons. It also calls functions from the database.py file to manipulate the data 
from the user. 


- The application can be run using the "if __name__ == '__main__':" line of code at the bottom of the file.


- The userDatabase.db file contains the Users and Reviews tables that allow for manipulation of data for the application.
By installing the simplesqlite plugin, you can view the tables and what they contain as data as manipulated within them.


# Additional Important Information
- Due to several components of the assignment being unclear, and some components being explained in more detail later 
during the first sprint, the way in which our group implemented the sprint components (Code Reviews/structure of
meeting notes) evolved as we progressed. All the information we provided in those files are accurate and were 
recorded when we conducted meetings, but was manipulated to match form as we progressed. We kept a master copy of our 
meeting notes in a Microsoft Word document that Caleb pushed into the repo. Final formatting tweaks were made to it.
We wanted to communicate this so there is no confusion surrounding these files.


- Unit tests were uploaded by one member of the group, but they were developed by all members of the group during our 
last few meetings.


- The way in which code reviews were meant to be implemented was unclear for us during the sprint. We do not believe
they were highlighted properly, and thus our documentation of them for this sprint is not as developed as other
components. This is not to say we did not perform them during meetings, as we did review each other's code and did 
review each other's code in detail before merging pull requests. We also do not believe it to be fair to be 
penalized for our documentation of them due to the confusion we had until later into the sprint.


# Unit Tests
- Unit tests are broken up into two files under the test folder. 
Manuel Server Module Testing.pdf contains unit testing instructions for the route.py file.
testdatabase.py contains unit tests for the database.py file.


- The user.py file did not require unit tests since it only contains setter and getter methods for the data in the
userDatabase.db file.


# Meeting Notes
- Meeting notes can be found in the MeetingNotes.md file.
Path docs/MeetingNotes.md


- Meeting notes were written by each member of the group. We are mentioning
this because in the marking scheme it was said we need to do it this way, but in the
professor's agenda, he states only one person should be taking notes throughout the 
sprint. It was unclear, but it made more sense that everyone had the experience of 
being the notetaker.


- Like described in the "Additional Important Information", We submitted a properly formatted master copy of our 
meeting notes at the end of the sprint in one pull request.


- Meeting notes contain some of our code reviews.


# Code Reviews
- Some documented code reviews can be found in the MeetingNotes.md file. A large code review can be found in the
CodeReview.md file.


- Each recorded meeting contains various small segments of code reviews. As we described in the "Additional Important
Information" section, the documentation of this component of the project was unclear to us until later into the sprint.


# User Stories
- All user stories can be found in the UserStories.md file.
Path docs/UserStories.md


# Kanban Board
- Kanban board can be located on our remote git under projects. Our Backlog in our Kanban board includes tasks we 
intend to implement in future Sprints


# Performance Reviews
- Performance reviews can be found in the PerformanceReviews.md file.
Path: docs/PerformanceReviews.md


# Attribution Table
- The Attribution table containing all references used can be found in the AttributionTable.md file.
Path docs/AttributionTable.md