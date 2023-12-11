# Process Model Analysis Document

This document presents a comprehensive analysis of the process model for the Team M Performance Review System. It aims to clarify the process undertaken, document the evolution of the process 
model, and propose future improvements.

## Contents
- Process Model Diagram 
- Elements of process 
- Distinction Between Process, Process Model, and Tasks 
- Comparison with the old process 
- Ideas and areas of improvement

## Process Model Diagram
![Process Model (Team M)1 ](https://github.com/CS2005F23/term-project-teamm/blob/master/docs/Asset/final%20process%20model%20diagram.jpeg?raw=true)

## Elements of Process

- Team Meetings: Our team planned ahead and conducted meetings after every class to discuss task assignments for group members. We selected a note-taker and a scrum master. The note-taker 
recorded our progress since the last meeting. We discussed the professor's suggestions and topics, reviewed each team member's code, and noted any difficulties they faced. At the end of our 
meeting, we made final decisions and approved or denied pull requests.


- Feature Selection: In this step, our team chooses which new features to add to our project based on our goals and the project's requirements, ensuring that each addition is valuable and
aligns with our overall objectives.  


- Task Assignment: During the team meeting, we picked our own features and distributed our work. After selecting the features, we fairly assigned tasks to team members and set deadlines for 
committing and making pull requests, considering member skill and workload. For example, Daniel focused on HTML, Turjo on routing, Caleb on the database, and Tajeet on method implementations.


- Code Implementation: All team members worked on their tasks and reported any difficulties during team meetings, requesting help from other team members.


- Review and Testing: Our team reviewed and provided constructive feedback on each pull request. We ensured the quality of code and verified functionality with unit and API testing before 
accepting any pull request. If a bug was found or the code did not meet the standard, we sent it back to the code implementation phase.


- Documentation: Throughout the project, we maintain detailed documentation that covers everything from system design to code changes, providing a clear record of our progress and decisions for
future reference.


- Deployment: After thoroughly reviewing and accepting pull requests, we integrate the completed features into the main project, ensuring that each addition works seamlessly with the existing 
components.


- Backlog Management:  We keep an organized backlog, which is a list of tasks and improvements yet to be addressed, helping us prioritize and keep track of what needs to be done next for the project's continual development.


Our process model is strongly based on agile principles, which focus on adapting to changes and delivering work in small, manageable parts. We use the scrum framework, which includes short work
periods called sprints, daily team meetings, and retrospective meetings. This setup allows us to regularly check and improve our work methods after each sprint, making sure we are always working
in the best way based on our most recent results.


## Distinction Between Process, Process Model, and Tasks

Process refers to the sequence of steps our team follows, including planning, coding, reviewing, and deploying. It is the actual sequence of events that happen during the project.

The Process Model is the visual or theoretical representation of the process, abstracting the details into a structure that is repeatable and understandable. It guides the project's workflow 
and includes roles like the Scrum master and note-taker, helping us maintain an agile approach.

Tasks are the individual activities that occur within our process. They include specific actions like writing code, testing features, and attending meetings. Tasks are the actionable items that
team members complete and are often represented as items in our sprint backlog.



## Old process and comparison to new process:
In our initial cycle, we faced challenges due to the lack of code reviews and deadlines. However, in the second cycle, we introduced deadlines, which significantly improved our ability to deliver on time. Our current process has seen timely commits and valuable feedback from team members, leading to considerable enhancements in our work.

During our first cycle, we didn't adequately document and report our difficulties, a practice we rectified in our subsequent cycles. We also encountered merging conflicts and challenges with using GitHub, which we worked to resolve.

For our final sprint, we focused on adhering strictly to our agenda to make our meetings shorter and more productive. This approach addressed the issues we faced in the initial stages, leading to a noticeable decrease in meeting duration and an increase in productivity. While our second sprint saw us rushing to complete tasks at the last minute, in our final sprint, we maintained strict adherence to deadlines, enabling us to finish all coding tasks on time.

In our second sprint, we faced considerable challenges with GitHub merging conflicts, significantly impeding our progress. These issues were a major setback, slowing our workflow and causing frustration. But we learned from this. By our final phase, we had adapted: every team member diligently updated their project before submitting pull requests, a strategy that effectively prevented merging conflicts. This important change made our work process much smoother and turned our final sprint into a great example of efficient and easy teamwork.

Overall, the way we set up our work process has helped guide our team, making how we work together and the results of our project much better. Adding in organized reviews, being strict about deadlines, and sticking to our meeting plan, especially in our last round, made everything go smoother and more efficiently, improving how well we work together


## Ideas and areas of improvement:
We completed our final sprint and realized that we could significantly improve our process model by adding some additional phases. For instance, 
in our documentation phase, we previously only documented our meeting notes. This approach led to a significant workload before the deadline to 
complete the readme and other documentation. Integrating docstrings with the development process rather than post-coding is a practice we will 
adopt to improve code clarity and reduce end-cycle documentation efforts. By formalizing this step, we will not only enhance our documentation 
quality but also distribute the workload more evenly throughout the project timeline.

Another critical aspect we need to focus on is our database structure. In this project, we had to change our database structure twice, which 
resulted in the need to modify our code and unit tests, creating unnecessary work. To prevent such inefficiencies in the future, our process model
will include a dedicated phase for database design and integrity checks at the start of the project. This formalization offers a clear benefit: it
provides a structured approach to validate the database early on, thereby minimizing the risk of disruptive changes later in the development cycle.

However, we must be cautious. While formalization brings organization and predictability, it can also introduce a level of rigidity. To navigate 
this, we will introduce flexibility within our formal structures. For instance, we will allow for periodic 'adaptation windows' where the process
model can be re-evaluated and adjusted in response to project realities. This will ensure that our process model remains a facilitator, not a 
barrier, to innovation and agility.

By embracing a formal yet flexible process model, we aim to improve our efficiency and output quality while maintaining the nimbleness needed to 
adapt to changing requirements and challenges
