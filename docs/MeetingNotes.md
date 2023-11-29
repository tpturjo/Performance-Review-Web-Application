# Meeting Notes
# Sprint Cycle 3



## Nov 17, 2023
**Recorded by:** Daniel  
**Scrum master:** Turjo  
**Venue:** DISCORD      
**Time:** 12:00PM - 1:16PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjett

  1) **Point of discussion**
  - Discussion for Sprint 3 direction.

  2) **Point of discussion**
  Two new items for sprint 3:
  - a document analyzing the alternative of a microservices architecture for the project. Include in this document:
  - a comparison of a microservices approach to the project to the existing (components-based) approach
  - a discussion on how the architecture and code would be different under a microservices architecture
  - a discussion of how the software process would be different under a microservices architecture
  - a project requirements specification effective with setuptools and/or another build tool.

  3) **New features**
  New Features Plans:
  - Profile Page (requires Caleb to implement profile: email, date/birth, address, education) Turjo will do the routing part, Daniel could to the HTML part. (3 task) (HTML / SQL/ ROUTE)
  - Comment on reviews. (3 task)  (HTML / SQL/ ROUTE)
  - Implement “Home” page where you are given the option to directly go to reviews, or choose to log in. New HTML page (HTML/Route)
  - Anonymous reviews. Users can leave reviews anonymously. (HTML / ROUTE) 
 
  4) **Decoupling/Solid:** 
  - We looked at route.py together, and found some bloat and naming inconsistencies. We will fix that throughout the sprint. 

  5) **Deadlines:**
  - Deadline for stubs due Tuesday Nov21 for everyone.
  - Daniel: HTML stubs for routing buttons/comment button/ anonymous button.
  - Caleb: Anonymous route.py stub
  - Tanjett: Comment on review route.py stub
  - Turjo: route.py Stub for profile

  6) **Decision:** 
  - Drop “Change Username” feature idea. 
  - Still considering other features to implement
  - Next Meeting Monday @ class time.





## Nov 21, 2023
**Recorded by:** Caleb 
**Scrum master:** Daniel  
**Venue:** Student CS Lab     
**Time:** 1:00PM - 2:00PM  
**Attendance:** Caleb, Daniel, Turjo

  1) **Point of discussion**
  Two new items for sprint 3:
  - discuss changes to process and architecture documents for sprint 3.
  - discuss our current progress.

  2) **New features**
  - Profile Edit Page (HTML and functionality).
  - Safeguard 'login' page. Won't be able to access login page unless signed out.
 
  3) **Decoupling/Solid:** 
  - Plans to decouple route.py we will come up with how to decouple route.py by next time and present. 

  4) **Deadlines:**
  -  Deadline for stubs due Tuesday Nov21 for everyone.
  -  Caleb: Anonymous route.py stub
  -  Tanjett: Comment on review route.py stub
  -  Turjo: route.py Stub for profile

  5) **Decision:** 
  - Refer to decoupling section.
  - Our decoupling plans will alter our architecture design, making it more concise and broken up.
  - The team will be implementing our remaining planned features today, and then discussing future plans 
edits, and implementations during the next meeting.

  6) **Code Review:**
  - Stubs work fine.

  7) **Next Meeting:**
  - tonight around 10pm via discord  

## Nov 21 2023
**Recorded by:** Tanjet  
**Scrum master:** Turjo  
**Venue:** Discord  
**Time:* 10:00 P.M - 11:00 P.M  
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
- None

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
- Daniel's and Turjo's pull request mergerd.  
- Pull request extension for Caleb and Tanjet until tomorrow (Wednesday).  
- Meeting tomorrow at 2:00 PM on Wednesday.  

## Nov 22 2023
**Recorded by:** Turjo  
**Scrum master:** Caleb  
**Venue:** Discord  
**Time:** 2:00 PM - 3:00PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet  

**Professor's Suggestions & Topics To Discuss:**  

- Current progress and future code to implement.  
- code review of new pull requests.  

**Progress Report:**  
- Caleb completed the anonymous route.py stub and the new database table for the profile, meeting the deadline.   
- Tanjeet finished working on the comment on the review route.py stub, meeting the deadline.  


**Difficulties:**  
- None

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
- Caleb's and Tanjet's pull request mergerd.
- The deadline for decoupling route.py will be November 29.
- Turjo: Will continue to work on route.py Stub for profile.
- Tanjett: Will continue  to work on Comment on review route.py stub
- Next meeting is on November 23 at 1:00PM.

## Nov 23, 2023
**Recorded by:** Daniel 

**Scrum master:** Caleb  
**Venue:** Discord  
**Time:** 2:00 PM - 3:00PM  
**Attendance:** Caleb, Daniel, Turjo, Tanjet 

**Professor's Suggestions & Topics To Discuss:**  

- Current progress and future code to implement.  
- code review of new pull requests.  

**Difficulties:**  
- None

**Decoupling/Solid:**  
 - Still working on decoupling for route.py file for further optimization and simplification.

**Progress Report:**
 - Daniel has pushed his HTML pages to accomodate new profile page 
 - Caleb has implemented the profiles and comments tables to the database.
 - Tanjet's stub for comment on review pushed and merged. New data structure created for profiles. 
 -Turjo's stub for profile pushed and merged. Updated database method for profiles.
**Code review:**
*Turjo's code*
 - Caleb:Code looks good. Also it was necessary to remove the change_username method, as that was a method we likely were not going to implement. Good to merge
 - Daniel:Looks good. Don't see any errors
 - Tanjet: Method works fine for the profile
*Tanjet' code*
 - Caleb: Methods looks good, code looks good to merge
 - Daniel: Getter and setters will be very useful in handling data with many moving comps. Nice.
 - Turjo:This basic user representation is a well-defined constructor and has accessor/mutator methods for username, first name, last name, email, and address, ensuring a clear and organized structure. Can be merged.

**Decisions:**
- Tanjet, Turjo and Caleb's pull request merged and closed. Deadline met.
- Daniel will push his methods.py, route.py update before next meeting
- Caleb will keep working onpost request handling for anonymous functionality (route.py)
- Next meeting Nov 24



**New features/code**
- Caleb: post request handling for anonymous functionality (route.py)
- Daniel: update methods.py & database.py for data output to html. Add routing for home.html require_login routing function. (route.py)
- Tanjet: post request handling for ‘comment’ functionality (route.py) 
- Turjo: profile_edit.html and profile.html routing (route.py)

*Deadlines:**
Everyone to push by Nov 24(sat)






 