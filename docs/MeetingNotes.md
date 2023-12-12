~~# Meeting Notes
# Sprint Cycle 3



## Nov 17, 2023
**Recorded by:** Daniel  
**Scrum master:** Turjo  
**Venue:** DISCORD      
**Time:** 12:00 PM - 1:16 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjett

**Professor's Suggestions & Topics To Discuss:**
- Discussion for Sprint 3 direction and features to implement.
- Discuss potential changes to process and architecture documents.

**New features/plans**
- Profile Page (requires Caleb to implement profile: email, date/birth, address, education) Turjo will do the routing part, Daniel could to the HTML part. (3 task) (HTML / SQL/ ROUTE)
- Comment on reviews. (3 task)  (HTML / SQL/ ROUTE)
- Implement “Home” page where you are given the option to directly go to reviews, or choose to log in. New HTML page (HTML/Route)
- Anonymous reviews. Users can leave reviews anonymously. (HTML / ROUTE) 
- Architecture document will be enhanced based on the implementation of our code and feedback from our document in sprint 2.
 
**Decoupling/Solid:** 
- We looked at route.py together, and found some bloat and naming inconsistencies. We will fix that throughout the sprint. 

**Deadlines:**
- Deadline for stubs due Tuesday Nov21 for everyone.
- Daniel: HTML stubs for routing buttons/comment button/ anonymous button.
- Caleb: Anonymous route.py stub
- Tanjett: Comment on review route.py stub
- Turjo: route.py Stub for profile

**Decisions:** 
- Drop “Change Username” feature idea. 
- Still considering other features to implement
- Next Meeting Monday @ class time.
- Caleb will work on an anonymous stub for future use to allow for anonymous reviews.
- Daniel will work on HTML stubs for buttons that will be implemented at a later time.
- Tanjet will work on a stub for commenting on reviews to be implemented at a later time.
- Turjo will work on a stub for user profiles that will be implemented at a later time.






## Nov 21, 2023
**Recorded by:** Caleb 
**Scrum master:** Daniel  
**Venue:** Student CS Lab     
**Time:** 1:00 PM - 2:00 PM  
**Attendance:** Caleb, Daniel, Turjo

**Professor's Suggestions & Topics To Discuss:**
- discuss changes to process and architecture documents for sprint 3.
- discuss our current progress.

**Progress Report**
- Profile Edit Page (HTML and functionality).
- Safeguard 'login' page. Won't be able to access login page unless signed out.
 
**Difficulties:**  
- Several members are showing up late to meetings.

**Decoupling/Solid:** 
- Plans to decouple route.py we will come up with how to decouple route.py by next time and present. 

**Deadlines:**
-  Deadline for stubs due Tuesday Nov21 for everyone.
-  Caleb: Anonymous route.py stub
-  Tanjett: Comment on review route.py stub
-  Turjo: route.py Stub for profile

**Decision:** 
- Refer to decoupling section.
- Our decoupling plans will alter our architecture design, making it more concise and broken up.
- The team will be implementing our remaining planned features today, and then discussing future plans 
edits, and implementations during the next meeting.

**Code Review:**
- Stubs work fine.

**Next Meeting:**
- tonight around 10pm via discord  





## Nov 21 2023
**Recorded by:** Tanjet  
**Scrum master:** Turjo  
**Venue:** Discord  
**Time:* 10:00 PM - 11:20 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet

**Professor's Suggestions & Topics To Discuss:**
- Discuss incomplete tasks left over from sprint 2.  
- Discuss the progress of the stub and the approach for its implementation.

**Progress Report:**
- Turjo completed the stub route.py for the profile, meeting the deadline.  
- Daniel finished HTML stubs for routing buttons/comment button/anonymous button, meeting the deadline.  
- Caleb is working on the anonymous route.py stub and the new database table for the profile. The deadline has been extended to tomorrow, November 22, by 2:00 PM.  
- Tanjeet is working on the comment on the review route.py stub. The deadline has been extended to tomorrow, November 22, by 2:00 PM.  

**Difficulties:**  
- Nothing to report.

**Code Review:**

*Daniel’s Code:*

- Caleb: The code is clean. Looks good to merge.  
- Turjo: Your CSS code looks fantastic and greatly enhances the project's appearance. Let's seamlessly merge it for an even better overall design!  
- Tanjet: Great job with CSS and HTML. The page looks better than before.  

*Turjo's Code:*  
- Daniel: Looks great. No reason for any conflicts.  
- Caleb: Stub passed, and the code looks good. Good to merge.  
- Tanjet: Stub passes as it should. Good to merge


**Decisions:**  
- Daniel's and Turjo's pull request merged.  
- Pull request extension for Caleb and Tanjet until tomorrow (Wednesday).  
- Meeting tomorrow at 2:00 PM on Wednesday.  





## Nov 22 2023
**Recorded by:** Turjo  
**Scrum master:** Caleb  
**Venue:** Discord  
**Time:** 2:00 PM - 3:40 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet  

**Professor's Suggestions & Topics To Discuss:**  

- Current progress and future code to implement.  
- code review of new pull requests.  

**Progress Report:**  
- Caleb completed the anonymous route.py stub.
- Caleb has implemented the profiles and comments tables to the database.
- Caleb has implemented a getter method for the profiles table and a set method stub
- Tanjet finished working on the comment on the review route.py stub.

**Difficulties:**  
- Several members are still showing up late to meetings.

**Decoupling/Solid:**  
- Still working on decoupling for route.py file for further optimization and simplification.

**Code Review:**  

*Caleb’s Code:*  

- Turjo: The changes appear seamless and conflict-free. It looks good and is ready for merging.
- Daniel: Thanks for updating the DB. It follows the attributes, exactly as we discussed in our meetings.

*Tanjett’s Code:*  
- Daniel: Looks good no conflicts found. Cleaning up the code is great. I think cleaning up code is better near the end of the cycle.
- Caleb: stub implementation looks good. He made some spacing changes in the code, but nothing dysfunctional. 
- Turjo: While there are just a few added lines, I suggest creating a separate commit and pull request to clean things up and align with our guidelines. This way, our changes will be more organized, and we can have confidence that the existing code remains intact. As it stands, everything looks great—the stub isn't introducing any inconsistencies. Ready for merging!


**Decisions:**
- Caleb's and Tanjet's pull request merged.
- The deadline for decoupling route.py will be November 29.
- Turjo: Will continue to work on route.py Stub for profile and will be working on functionality for an edit_profile function.
- Tanjett: Will continue  to work on Comment on review route.py stub
- Next meeting is on November 23 at 1:00PM.





## Nov 23, 2023
**Recorded by:** Daniel
**Scrum master:** Caleb  
**Venue:** Student CS Lab  
**Time:** 1:00 PM - 2:20 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Current progress and future code to implement.  
- code review of new pull requests.  

**Difficulties:**  
- None

**Decoupling/Solid:**  
- Still working on decoupling for route.py file for further optimization and simplification.

**Progress Report:**
- Daniel has pushed his HTML pages to accommodate new profile page
- Tanjet's stub for comment on review pushed and merged. New data structure created for profiles. 
- Turjo's stub for profile pushed and merged. Updated database method for profiles.

**Code review:**

*Daniel's code*
- Caleb: CSS Code styling make the site look much nicer and is functional. Good to merge
- Turjo: The CSS styling is looking great! Well-chosen styles contribute to a visually appealing and cohesive design. Good job!
- Tanjet: CSS looks great. Styling is perfect for our assignment and makes the interface looks better

*Turjo's code*
- Caleb: It was necessary to remove the change_username method, as that was a method we likely were not going to implement. 
Code looks good and is good to merge
- Daniel: Looks good. Don't see any errors
- Tanjet: Method works fine for the profile

*Tanjet's code*
- Caleb: Methods look useful and functional, code looks good to merge
- Daniel: Getter and setters will be very useful in handling data with many moving comps. Nice.
- Turjo: This basic user representation is a well-defined constructor and has accessor/mutator methods for username, 
first name, last name, email, and address, ensuring a clear and organized structure. Can be merged.

**Decisions:**
- Daniel will push his methods.py, route.py update before next meeting
- Caleb will keep working on post request handling for anonymous functionality (route.py)
- Caleb will work on database.py methods for review comment functionality. 
- Caleb's deadline for his features/code will be November 28.




## Nov 24, 2023
**Recorded by:** Tanjet
**Scrum master:** Turjo  
**Venue:** Discord  
**Time:** 2:00 PM - 3:00 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Discuss changes to architecture document/alternative architecture document.
- Discuss how to shorten meetings.
- Code review and discussing progress.

**Difficulties:**  
- Meetings have been taking too long, partly due to members not being on time and due to not always staying focused
on the core meeting discussion points. We need to fix these two issues going forward.

**Progress Report:**
- Daniel: Update public html and JavaScript to accommodate comment function.
- Tanjet: post request handling for comment (route.py) 
- Turjo: post request handling for edit_profile functionality (route.py)

**Code Review:**

*Daniel's code*
- Caleb: Code is more properly optimized and good to merge.
- Tanjet: Great improvement
- Turjo: looks good

* Tanjet's code*
- Caleb: Simple but functional routing addition. Good to merge
- Daniel: action = 'comment' now looks much better in the action cluster
- Turjo: Nothing here to conflict. Can be merged.

* Turjo's code*
- Caleb: The code is functional and works, just needs doc strings. Good to merge.
- Daniel: routing looks fine and logical. Don't forget the comments before final submission
- Tanjet: Code looks good.

**Decisions:**
- We will be adding new modules/sections to our component architecture document and text document based on new features
we have currently implemented and will implement as we go forward. Most changes will reflect changes to the database,
routing, and interface enhancements.
- Meetings seem to be taking quite a while. We will work on being more efficient to waste less time to shorten them.
- We will all actively make sure were on time to meetings and that we will stay focused and keep discussions unrelated 
to the meeting to a minimum.
- A new feature brought up in the meeting to organize reviews by topic will be added to backlog features to be worked on
if we feel it's necessary.






## Nov 25, 2023
**Recorded by:** Caleb
**Scrum master:** Tanjet 
**Venue:** Discord  
**Time:** 2:00 PM - 2:45 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Discuss what details on testing or code review might be added to the process document
- Discuss current progress and merge pull requests.

**Difficulties:**  
- Nothing to report.

**Progress Report:**
- Turjo: edit_profile routing functionality implemented.

**Code Review:**

*Turjo's code*
- Caleb: Good simple routing function. Good to merge.
- Daniel: Code looks straightforward. Easy readability.
- Tanjet: Good to merge.

**Decisions:**
- Decided not to add anything extra regarding our code review to the document. We have not changed anything from our methods
used in sprint 2. We decided our method is efficient for our team and it wouldn't make sense to alter it at this time.
- We will put more time into decoupling and cleaning up portions of the code in our files where needed.





## Nov 26, 2023
**Recorded by:** Daniel
**Scrum master:** Caleb  
**Venue:** Discord  
**Time:** 2:00 PM - 2:20 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Discussing current progress.

**Difficulties:**  
- Due to personal related issues, Caleb needs an extension on the deadline of his anonymous routing and commenting code 
database methods.

**Progress Report:**
- Nothing to report

**Code Review:**
- Nothing to report

**Decisions:**
- Caleb's deadline will be extended to December 1. 
- Daniel will be adding the HTML and routing code for comments on reviews functionality. His deadline will be 
December 1.





## Nov 30, 2023
**Recorded by:** Turjo
**Scrum master:** Daniel 
**Venue:** Student CS Lab  
**Time:** 1:00 PM - 1:40 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Task someone to make sure external package installs are correctly represented in the repository.
- Discuss current progress and merge pull requests.

**Difficulties:**  
- Nothing to report.

**Progress Report:**
- Caleb: userDatabase.py file updated because of a discovered small bug with the comment table foreign key. All database 
tables working correctly. Anonymous stub in the route.py file filled in and implemented. 
Comments table functions implemented in the database.py file.
- Daniel: Added HTML and routing code for comment on reviews functionality in the . Removed an unused stub in templates.

**Code Review:**

*Caleb's code*
- Turjo: Nothing looks wrong. Can be merged.
- Daniel: Looks good. Can't think anything to add on.
- Tanjet: Code looks good. Good to merge.

*Daniel's code*
- Turjo: The indexes of the comment-data list could be reformed such that it is more intuitive. 
Other than that it works well with no errors.
- Caleb: Code is functional and not too complicated. It is good to merge. 
- Tanjet: Code looks good. Good to merge.

**Decisions:**
- Caleb will make sure external package installs are correctly represented in the repository. His deadline is for
December 3.
- Turjo will update and implement the edit post stub, and fill in any missing doc strings. Deadline is for December 3.
- Our application is nearly finished for the sprint. Some small edits and tweaks will be made going forward.





## Dec 1, 2023
**Recorded by:** Tanjet
**Scrum master:** Turjo  
**Venue:** Discord  
**Time:** 3:00 PM - 3:50 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Discuss current progress and merge pull requests.
- Discuss any further possible decoupling of code.
- Discuss Deadlines

**Difficulties:**  
- Struggled to find more ways to decouple our code. At the application's current state, it may due more harm than good.

**Decoupling/Solid:**  
- route.py action handlers methods such as rate() can use decoupling, but other handlers such as checkCredential(), 
Save, comment, login and many other handlers will not see any benefit of decoupling.
Verdict: Due to too many data sets being called via request.forms and simple data processing, there is more harm to 
breaking up route.py to 2 files (app_logic.py and route.py (http request)). 
Decoupling of route.py will not commence.

**Progress Report:**
- Caleb: Removed  save_by_draft function in the database.py file as it is not useful to the program. Also tidied up several 
pieces of code in the .py files.

**Code Review:**

*Caleb's code*
- Turjo: Good job tidying the code. It looks better now.
- Daniel: Thanks for wiping out the unnecessary things from the code. it looks now more nice and polished.
- Tanjet: Code looks good. Good to merge. 

**Decisions:**
- Tanjet and Turjo will work on our microservices architecture document. Deadline is for December 3.
- Caleb will work on the requirements.txt list and instructions. Deadline is now for December 3.
- Caleb and Daniel will edit the UML and architecture document/architecture document. Deadline is for December 3.
- Performance reviews deadline will be for December 4.
- We will all work on the README file for sprint 3. Deadline is for December 4.





## Dec 2, 2023
**Recorded by:** Caleb
**Scrum master:** Turjo  
**Venue:** Discord  
**Time:** 10:30 AM - 11:15 PM  
**Attendance:** Daniel, Turjo 

**Professor's Suggestions & Topics To Discuss:**
- Nothing to report.

**Difficulties:**  
- During testing a bug was discovered in profileEdit. 
- A backup of the database had to be re-uploaded.

**Decoupling/Solid:**  
- Nothing to report.

**Progress Report:**
- Daniel and Turjo worked on and fixed the bug in profileEdit. Added to backlog.
- Daniel accidentally made a change to the database and then re-uploaded a copy of the database before the change.

Backlog
    Refer to Progress Report

**Code Review:**
- Nothing to report

**Decisions:**
- Nothing to report





## Dec 3, 2023
**Recorded by:** Daniel
**Scrum master:** Tanjet 
**Venue:** Discord  
**Time:** 2:00 PM - 2:40 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Current progress and future code to implement.
- Code review and merge pull requests.
- Re-discuss deadlines

**Difficulties:**  
- Nothing to report

**Decoupling/Solid:**  
- Nothing to report

**Progress Report:**
- Turjo: Updated the stub functionality and HTML code for editing a review submission. Also removed some debugging code.

**Code Review:**

*Turjo's code*
- Daniel: view My Post re-direct button could be better on a different page like 'profile' or 'write-review' page. 
That's where most people I would argue to go find their own information. Having that button in public is not terrible, 
so maybe the 'view-my-post' button could reside in all three pages. Most ideally, we need a side bar or a drop down menu 
to access this (added to backlog).
- Caleb: The code is functional but could be more optimized. Good to merge
- Tanjet: The code and methods look and work fine. Good to merge.
* Note - We all agreed with Daniel suggestion and Turjo implemented My Post re-direct button in all three pages on spot.

**Decisions:**
- Several deadlines have been moved due to the change in sprint 3's deadline.
- Turjo and Caleb will now be working together on the UML architecture document/process document.
- Tanjet and Daniel will now be working together on the microservice document.


**Deadlines:**
- Due to the change in the due date of sprint 3 and preparation of exams, the following deadlines will be adjusted:

- Caleb and Turjo's deadline for UML and architecture document will be moved to December 9.
- Caleb's deadline for requirements.txt list and instructions will be moved to December 9.
- Tanjet and Daniel's deadline for our microservices architecture document will be moved to December 9.
- The performance reviews deadline will be moved to December 10.
- The README file deadline will be moved to December 10.





## Dec 5, 2023
**Recorded by:** Caleb
**Scrum master:** Daniel 
**Venue:** Student CS Lab  
**Time:** 1:00 PM - 2:10 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Work on unit tests.

**Difficulties:**  
- Nothing to report.

**Progress Report:**
- We've completed almost all unit tests for our code.

**Code Review:**
- Daniel: unittest name should be changed as unittest.py is the same as the library name. This can cause errors. 
Will create backlog and Kanban for this issue.
- Caleb: After the update fixing the directory error, Tests work well.
- Tanjet: Although there was a directory error, unit test working fine.

**Decisions:**
- We've completed almost all unit tests for our code. We will each make final tweaks before submitting into a document 
for Turjo to format them together and push to our remote repo.





## Dec 7, 2023
**Recorded by:** Tanjet
**Scrum master:** Turjo
**Venue:** Discord  
**Time:** 11:40 PM - 12:05 AM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Discuss current progress and merge pull requests.
- Re-discuss deadlines due to change in

**Difficulties:**  
- Unit test got directory error. Turjo will look on it.

**Progress Report:**
- Turjo: Has pushed our unit tests. Unit tests have now been implemented.
- Tanjet: Has pushed the microservice architecture document that he and Daniel were working on.

**Code Review:**
- Nothing to report.

**Decisions:**
- Due to the change in the due date of sprint 3 and preparation of exams, the following deadlines will be adjusted:

- Caleb's deadline for requirements.txt list and instructions will be moved to December 11.
- Caleb and Turjo's deadline for UML and architecture document will be moved to December 11.
- The performance reviews deadline will be moved to December 12.
- The README file deadline will be moved to December 12.

- Hypotheticals file will be implemented based on feedback from sprint 2 by each team member. Deadline will be for 
December 14.





## Dec 10, 2023
**Recorded by:** Turjo
**Scrum master:** Caleb 
**Venue:** Discord  
**Time:** 3:30 PM - 3:55 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Discuss current progress and merge pull requests.

**Difficulties:**  
- Based on the 

**Progress Report:**
- Turjo: Has pushed the UML diagram and architecture document that he and Caleb were working on. Also he corrected the unit test directory problem and unit test is running fine.
- Caleb: Has pushed our meeting notes that we had recorded in an ongoing document.

**Code Review:**
- Nothing to report.

**Decisions:**
- Nothing to report.





## Dec 12, 2023
**Recorded by:** Turjo
**Scrum master:** Caleb 
**Venue:** Discord  
**Time:** 6:20 PM - 6:40 PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**
- Discuss current progress.

**Difficulties:**  
- Nothing to report.

**Progress Report:**
- Turjo has pushed tweaks and fixes to the microservice file, process model document, project progress file, 
and component architecture document.
- Caleb has pushed the requirements.txt file.

**Code Review:**
- Nothing to report.

**Decisions:**
- Nothing to report.





 