# Advanced Software Design 2024

# General rules

1. Complete tasks at the practice session to get practice scores for everyone in a team  
     
2. Complete tasks and before the next practice to get project scores for everyone in a team  
   

All solutions must be submitted to this form: [https://tiny.cc/asd-project](https://tiny.cc/asd-project) 

3. The persons who report the task at the blackboard get \+1 personal practice score  
     
4. If team does not report at the session, record a short video and post it to the form above  
     
5. Students who make significant contribution to the task get \+1 personal practice point   
   

# Task 8 \- due 5/11/2024

This is an individual programming and design analysis task for two weeks.

Please submit solutions to the Project submit form. No video or slides are needed.

You are asked to practice design methods to solve classical software design problems using Java8+ or Python3.

**Problem A.** Key Word in Context (KWIC)  
For problem description see [https://en.wikipedia.org/wiki/Key\_Word\_in\_Context](https://en.wikipedia.org/wiki/Key_Word_in_Context) 

**Problem B.** Eight Queens (8Q)  
For problem description see [https://en.wikipedia.org/wiki/Eight\_queens\_puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle) 

**Method 1\.** Abstract Data Types  
This is similar to object-oriented design method, use any of the approaches to identify classes and provide rationale for eliciting them.

**Method 2\.** Main/Subroutine with stepwise refinement (also Shared Data)  
See Parnas paper for description of the method. Try to follow the steps of the procedure as closely as possible.

**Method 3\.** Pipes-and-filters  
See Garlan and Shaw paper for description of the method.   
Most of the time you would implement this as a set of independent programs connected using primitive data pipes. There should be no direct invocations between modules / programs.

**Method 4\.** Implicit invocation (event-driven)  
See Garlan and Shaw paper for description of the method.  
In general, any asynchronous or event-driven programming framework will help.   
A simpler solution could employ the Observer/Listener pattern instead of direct invocations.

**What to do**

1. Apply any of the methods to solve Problem A and any other method to solve Problem B. A total of two implementations.

2. Compare your solution to problems A and B with the solutions by two of your teammates (or classmates if less than three in a team) who applied **different** methods. 

   Use the following checklist:   
   a) in which case it is easier to change the implementation algorithm in each of the modules?   
   b) in which solution it is easier (= seemingly less effort) to change data representation  c) in which solution it is easier to add additional functions to the modules  
   d) which solution is seemingly more performant?  
   e) if you are asked to implement a similar program, which of the solutions would you reuse?

   Show the results as a table. Justify and explain the comparison.

3. Try to combine your results into a single table for all methods. Put the table in markdown to the repository

You get \+1 individual point for solving two tasks at step 1\. and another \+1 point for comparing solutions at step 2\.

Please put your individual solution to the **team project repository** and submit a direct link to the solution. Supply a readme along with the solution on how to run it and a sample input if needed.

References:

1. "On the criteria to be used in decomposing systems into modules" by D L Parnas  
2. "An Introduction to Software Architecture" by David Garlan and Mary Shaw

# Topics so far

[https://tiny.cc/asd-lecture-req](https://tiny.cc/asd-lecture-req)  
[https://tiny.cc/asd-lecture-req2](https://tiny.cc/asd-lecture-req2)  
[https://tiny.cc/asd-lecture-modeling](https://tiny.cc/asd-lecture-modeling)   
[https://tiny.cc/asd-lecture-ddd](https://tiny.cc/asd-lecture-ddd)   
[https://tiny.cc/asd-lecture-interactions](https://tiny.cc/asd-lecture-interactions)  
[https://tiny.cc/asd-lecture-behaviors](https://tiny.cc/asd-lecture-behaviors)  
[https://tiny.cc/asd-lecture-bigpicture](https://tiny.cc/asd-lecture-bigpicture)

# Final task 1 \- due 25/10/2024

This is the final task for Module 1\. The goal is to compose a full report out of **fixed** tasks 2-3 and 4-6.

That is, do include previous results on the project **after fixing mistakes**.  
Here is the template [https://tiny.cc/asd-template-final-1](https://tiny.cc/asd-template-final-1)

Submission checklist

- Structure of the slides follow the template  
- Repository and document storage contains features, personas, jobs, storymap, use cases texts and diagrams, interactions table or collaboration diagrams, final class diagram with ddd stereotypes, responsibilities table  
- There are links to the source material in the repo/storage on the slides   
- For each use case you can explain which feature it belongs to  
- For each class there is a use case and feature it implements  
- There are at least 2 use cases with text per team member  
- There are at least 2 non-utility, domain classes per team member

In case your project does not satisfy the sizing constraints, **do elaborate your requirements first\!**

Video report is mandatory for the final task 1\.

**Overall grading criteria** for the final task 1 (max 12).

- Excellent grade (11)

  Project contains no errors, has all parts, and is larger than required for the team size.  
  Team successfully defended the project, and members’ contributions are clearly stated.

- Good grade (9)

  Project contains no major errors, has all parts, and is large enough for the team size.  
  Team is able to answer questions on the project, and members’ contributions are clearly stated.

- Satisfactory grade (7)

  Project contains no major errors, has most parts, may not be as large as needed for the team size.  
  Team is able to answer questions on the project, and members’ contributions are not clearly stated.

- Failed grade (\<5)

  Project contains major errors, missing many parts, too small for the team.  
  Team cannot answer questions on the project or members’ contributions are not clearly stated.

# Task 7 \- due 15/10/2024

Solve behavior modeling tasks using UML2. This is a research and self-study activity. You will need to find out about new concepts using the references and links provided.

You will get individual points for studying and explaining new concepts to other students. Prepare a short 5-7 minutes report on the topic. A report shall include a correct solution of the bullet from the task as an example. 

The most elaborate and precise report for each new concept gets the point.

A team gets a project point if it correctly solves all of the tasks and bullets in a chosen category. 

There are a total of eight new concepts in four modeling tasks (one in a bullet). There are three categories. No more than four teams per category. You may coordinate concepts and categories with the other teams. Please, at most two reports on the same concept.

There is an extra Task 3 for activity modeling. Solve it at will.

Results of the task include  
\- a PDF with solved tasks in the chosen category and rationale for the solution  
\- a video recording with an explanation of a new concept (if not reported at class)

NOTE: This time the quality of the solution is of top priority.

NOTE: Explain concepts from the same category your team solves tasks in.

NOTE: Each task contains many bullets. You have to solve all of them before assuming it solved.

The link to the tasks will be available at the practice\!

# Task 6 \- due 08/10/2024

Develop an interaction model for your product. Use use cases from Task 5 and apply CRC modeling technique to devise collaborations and interaction sequences.

Overall process:

1. Make a list of high priority Use Cases and candidate classes

2. Apply a CRC role-playing method to elaborate class interactions within the system. Write down the responsibilities of each participating class. Introduce new classes/roles whenever necessary.

3. Build a cooperations table to indicate which classes participate in which use cases. Update class diagram if needed

4. Check that DDD stereotypes are up to date.

NOTE: try to follow “know, do, interact” classification of responsibilities at step 2

NOTE: when preparing a talk on a task, consider justifying the design and providing rationale instead of just retelling what is already shown in the slides/repo.

HINT: do not consider user interface as part of the doman, avoid ‘form’, ‘screen’ classes. Think of API.

HINT: You may wish to use GRASP responsibility patterns to justify your design decisions.

See the task report template  
[https://tiny.cc/asd-template-analysis](https://tiny.cc/asd-template-analysis) 

# Task 5 \- due 01/10/2024

Develop an analysis model for your product. Use features and stories from Task 3 as a source of requirements.

Note: if you had “wrong scope” taint for the previous task you are strongly advised to talk to your professor.

Optional extra: discuss, explain and get feedback on your requirements from the HSE MLOps team or AI Center Framework team (your customers).

Overall process:

1. Detail use cases for job/user stories.   
   A rule of thumb: function/user level Use case \<=\> user/job story in product (business) requirements

2. Build a Glossary of candidate classes with either Abbot’s methods, checklists or both based on use cases, stories, features. Check for duplicates  
     
3. Use “SIAOUT” criteria to classify them as attributes, classes, values. Extract operations and relations as verbs and/or communication/interaction acts.  
     
4. Draw a draft class model from 2\. and 3\.  
     
5. Assign DDD stereotypes to classes from 4\.

NOTE: steps 1 and 2 may come in parallel

HINT: you may spot generalization at this step, use it sparingly, check that it is not coincidental / or specific to a particular context.

NOTE: keep your repo up to date with task reports

See the task report template  
[https://tiny.cc/asd-template-draft](https://tiny.cc/asd-template-draft) 

# Task 4 \- due 24/09/2024

Solve static modeling tasks using UML2 and ER diagrams.

The first student who solves a task, consults the professor, and if the solution is OK, writes down the solution on the whiteboard and receives an individual point.

NOTE: Each task contains many bullets. You have to solve all of them before presenting the solution.

NOTE: Write down a model of task statement first, then add only that has been changed to solve each bullet.

Each team with at least one member who got an individual point gets a project point.

Each team that submits all six tasks solved using the chosen modeling tools gets a project point.

There are a total of six tasks.

The link to the tasks will be available at the practice\!

# Task 3 \- due 17/09/2024

Develop product requirements. Follow these steps:

1. Prepare product scope and feature hypotheses (Task 2\)  
2. Conduct a JTBD interview with another team to understand customer journey  
3. Analyze the results and make corrections to the product  
4. Obtain a feedback from the other team using a “paper” prototype of the product  
5. Finalize features and jobs for the product (storymap), develop a report and work products

HINT: search for JTBD interview on the Web and watch a few example interviews  
HINT: at step 2 ask for past experience, avoid assumptions and early judgements  
HINT: use a checklist and/or canvas to help with the interview

See the report template  
[https://tiny.cc/asd-template-product](https://tiny.cc/asd-template-product) 

# Task 2 \- due 10/09/2024

Define product scope as a product customer (“business requirements”). Name the product.

Reminder:

**`Product name`**  
**`List of team members`**

**`Product description`**

`E.g. My Custom Printer is a mobile app for office workers to quickly print documents from a smartphone over wifi or bluetooth. …` 

**`Similar systems [if topic is new]`**

`e.g. Super Printer App, …`

**`Feature list`**

* `Feature 1 (Name + 3-5 sentences)`  
* `Feature 2 (Name + 3-5 sentences)`  
* **`Print a document.`** `Users can print documents on an installed printer using a print dialog.`


**`Constraints`**

`Any technical constraints and requirements`

Result \- a doc in your repo/wiki, post a link in the course chat.

Scope description \- 5-10 sentences.  
List of features \- 7-12 features.

Report on the product at the blackboard.

# Task 1 \- due 10/09/2024

Form a team, come up with a name for the team.

Select tools for the team to develop a software product:

1. Repo (n.b. Github may ban)  
2. Task tracker   
3. Wiki/docs storage  
4. Team chat  
5. Modeling tool (see [https://tiny.cc/asd-tools](https://tiny.cc/asd-tools))

Everyone must agree on the tools. You will use the tools for tasks in Module 1\.

Write on the blackboard and send to the course chat: team name, members, tools.

Make tools 1-3 accessible to teachers and all course students. If you have a link to another team's project DO NOT SEND it to anyone.

