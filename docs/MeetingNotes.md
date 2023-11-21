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
