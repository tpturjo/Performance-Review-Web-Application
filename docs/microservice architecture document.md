# Microservice Architecture Document:

The document explains the microservice architecture for the software process

# Contents
1) Possible microservices identified in architecture
2) Comparison to existing/component-based architecture
3) Discussion of impact on team software process

# Microservice Architecture Document:

![image](https://github.com/CS2005F23/term-project-teamm/assets/144711080/42279cdb-0b79-4458-bda7-643f765c7572)




This architecture represents a web application built using the Bottle microframework. It provides several microservices that work together to provide a solution for a web-based review 
system.

Here is an overview of the microservices and how they work together:

1. require_login and require_logout: These are decorator functions used for flow control. They check if a user is logged in or logged out before allowing access to certain services, such as the login page or the review page.

2. home: Serves the login page.

3. login: Serves the login page, where users can enter their credentials to log in.

4. change_password: Serves the change password page, where users can change their passwords.

5. public: Serves the public page, which displays all published reviews. It retrieves reviews from the database and formats them for display. It also allows searching for specific reviews.

6. create_account: Serves the create account page, where users can create a new account.

7. review: Serves the review page, where users can write and save drafts or publish reviews. It retrieves draft data from the database and displays it to the user.

8. profileEdit: Serves the profile edit page, where users can view and edit their profile information.

9. profilePage: Serves the profile page, which displays the user's profile information.

10. submit: Handles form submissions from various pages, including saving drafts, publishing reviews, adding comments, logging in, creating accounts, and editing profiles.

11. change: Handles form submissions from the change password page, allowing users to change their passwords.

12. rate: Handles form submissions for rating reviews.

13. my_posts: Serves the page displaying all posts made by the logged-in user.

14. edit_post: Handles the editing of an existing post by the logged-in user.

The microservices interact with each other to provide the complete functionality of the web application. For example, the login and create account services interact with the database 
to check credentials and create new user accounts. The review and profile services retrieve and update data from the database related to reviews and user profiles.
# Comparison to existing architecture:
In a components-based architecture, the web-based review system might start with a more straightforward management approach, with a single codebase housing all functionalities such as user login, account creation, 
review posting, commenting, rating, and profile management. However, as the system grows, the high coupling of components could make it challenging to scale or update parts of the application without affecting others. 
Additionally, resilience is a concern since the failure of a single component could jeopardize the entire application.

On the other hand, if the same system were built using a microservices architecture, each part of the system (login, account management, review handling, etc.) would be developed as a separate microservice, with its own 
codebase and deployment process. This would reduce coupling, allowing for individual parts of the system to be updated or scaled without impacting others. Communication between services, potentially through REST APIs, 
would be designed for loose coupling and resilience, so that a failure in one microservice (such as the review posting service) would not take down the entire system. A microservice architecture document would be essential in this case, detailing the responsibilities, communication protocols, and deployment strategies of each microservice, providing a clear blueprint for the system's structure and facilitating comparison with the existing components-based structure.

Thus, the shift from a components-based architecture to a microservices architecture for your web-based review system project involves a transition to a more decentralized, resilient, and scalable system design, which, 
while potentially more complex to manage initially, offers greater flexibility and fault tolerance as the system evolves.


# Discussion of impact on team software process:
In our current components-based setup, we face certain challenges due to the shared codebase. Our team has experienced merge conflicts and workflow bottlenecks, which slows down our 
feature development and complicates our deployment process. Moreover, when we need to scale, we're forced to scale the entire application, which is not always the best use of our 
resources.

With microservices, we anticipate significant improvements:

- Team Collaboration: Our developers will be able to work on different services concurrently. This parallel development approach is expected to lead to faster feature development, 
as team members will be less likely to be blocked by each other's work. This agility will enable us to overcome current bottlenecks and dependencies, fostering a more productive and
collaborative environment.

- Deployment: With microservices, we can adopt CI/CD practices, which will allow individual teams to deploy their updates independently. This means we can introduce new features and
fixes more frequently and with reduced risk, thus improving our time-to-market.

- Scaling: Each service in the microservices architecture can be scaled independently according to its specific demand. This targeted scaling is a more efficient use of resources and 
allows our team to better manage workload variations. 

- Monitoring and Logging: The move to microservices will also enhance our monitoring and logging capabilities. Each team will be able to closely monitor their respective services, 
providing us with fine-grained insights into our system's performance. This level of detail will help us maintain high availability and quickly address any issues that arise.

By embracing a microservices architecture, we're not just changing our technology stack; we're evolving our entire software development lifecycle. This will empower our teams to be
more autonomous, enable our services to be more resilient, and ultimately lead to delivering a better application.
