# Microservice Architecture Document:

The document explains the microservice architecture for the software process

# Contents
1) Possible microservices identified in architecture
2) Comparison to existing/component-based architecture
3) Discussion of impact on team software process

# Microservice Architecture Document:

![image](https://github.com/CS2005F23/term-project-teamm/assets/144711080/42279cdb-0b79-4458-bda7-643f765c7572)




This architecture represents a web application built using the Bottle microframework. It provides several microservices that work together to provide a solution for a web-based review system.

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

The microservices interact with each other to provide the complete functionality of the web application. For example, the login and create account services interact with the database to check credentials and create new user accounts. The review and profile services retrieve and update data from the database related to reviews and user profiles.
# Comparison to existing architecture:
Overall, these microservices work together. Microservice Architecture Document ether to create a web-based review system where users can log in, create accounts, write and publish reviews, add comments, rate reviews, and manage their profiles. 
Existing diagrams such as UML diagram provide a visual representation of the system's structure and components, while a microservice architecture document outlines the different microservices, their responsibilities, communication protocols, and deployment details.
Moreover, the microservice architecture document outlines the design and structure of a system based on a microservice architecture approach. It provides details about the different microservices, their responsibilities, deployment strategies, communication protocols, and more. Without the microservice architecture document, it is difficult to directly compare the code to it. We can, however, analyze the code based on microservice architecture principles and patterns. For example, if the code is structured in a modular way with separate components responsible for specific functionalities, if it uses a distributed communication mechanism like REST APIs, or if it exhibits loose coupling between different parts of the system, then it aligns with some microservice architecture principles.
# Discussion of impact on team software process:
With microservices, our team can work on different services concurrently. This parallel development approach allows for faster feature development and enables teams to overcome any bottlenecks or dependencies. Additionally, microservices can be deployed independently, allowing for more frequent deployments and quicker time-to-market. The TSP can benefit from these streamlined development and deployment practices by facilitating efficient coordination between teams and their respective services. Microservice architecture inherently supports scalability and resilience. Each service can be independently scaled based on demand, enabling the TSP to effectively handle varying workloads. Teams can monitor and optimize the performance of their specific services, ensuring that the system remains responsive and resilient even under heavy usage. TSP can incorporate these scalability and resilience considerations as part of its performance and testing activities.
