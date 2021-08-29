#  Architectures et langages de données: Advanced Programming

- [Instructor](#Instructor)
- [Syllabus](#Syllabus)
- [Program](#Program)
- [Prerequisites](#Prerequisites)
- [Preparation Before the First Session](#Preparation)
- [Grading](#Grading)
- [Resources](#Resources)

<a name="Instructor"></a>
## Instructor
Contact:
 - Wirtz Kevin
 - University of Strasbourg, BETA
 - kevin.wirtz@unistra.fr
 - On discord (Send me a mail if you need a new link for another account)

About me:
 - University degree at Strasbourg (Statistics and Econometrics).
 - Third year PHD student in Economics. (Bibliometrics, network analysis, novelty, ...)
 - R since 2016 and Python 2018.
 - Working with SQL and noSQL databases.


<a name="Syllabus"></a>
## Syllabus 

The aim of this course is to teach students a solid set of programming tools to tackle real-world problems. In a context of big-data, answering some questions might need you to cross multiple web sources. This implies knowing how to fetch available information (API/web scraping), how to clean this information depending on the format (xml/json/pdf), feed it to a database (SQL/noSQL) and lastly use your machine (CPU/GPU) and ressources (cloud/notebook) that is at your disposal to run some analysis (descriptive statistics, algorithm,...). The goal is to give you some insight for doing all of the above.

During the whole course we are going to use Python as our programming language. We start off with a basic reminder of what you learned last year in programming (list,dicts,function,numpy, pandas, beautiful soup, regex ...). We then focus on scraping libraries and api usages to let you work on your project asap (see [Grading](#Grading) ). We then tackle more advanced concepts (Coocurence, OOP, Parallelize, Decorators, Versioning, ...). We finish with an introduction to GPU programming and machine learning libraries.

The goal of the course is not to be exhaustive. Programming is a vast space of knowledge, sometimes you will do something I never done before. In the end you will learn what I know and I will learn from your questions. This also means that I can't have the answers to all of your problems, basic behavior in programming is to first do research on your side. Websites like stackoverflow/stackexchange/Quora/Youtube/Github/... all of them are your best friends when it comes to solving issues. If after your own research you are still lost then you can send me a message about your problem. Either I will have the solution because I encountered it previously, or I don't but I can guide you to the solution. In no way you should ask me to code things for you, it's your job !

<a name="Program"></a>
## Program 

30H on-site lecture

- Introduction (reminder)
- Chapter 1:  Scraping and APIs (2h)
- Chapter 2:  Advanced concepts.
- Chapter 3:  GPU programming.
- Chapter 4:  Machine learning libraries.

    <img src="img/planning.png">

<a name="Prerequisites"></a>
## Prerequisites

- Prior knowledge in Python is required and familiarity with programming concepts.
- A laptop connected to the internet and running Windows, Linux, MacOS
- Anaconda installed, see below. Choose one of the IDE (I'll be using Spyder and Jupyter-Notebook)
- One text editor ([Sublime](https://www.sublimetext.com/), [Atom](https://atom.io/), [Vim](https://www.vim.org/), ...)


If you have little experience with Python or shell programming, the following tutorials may be helpful:

- https://www.w3schools.com/python/python_intro.asp
- https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/230659-decouvrez-python
- https://pythonprogramming.net/introduction-learn-python-3-tutorials/
- https://www.anotherbookondatascience.com/chapter1.html
- https://tutorial.djangogirls.org/en/intro_to_command_line/
- https://swcarpentry.github.io/shell-novice


<a name="Preparation"></a>
## Preparation before the First Session

- Install [Anaconda](https://www.anaconda.com/products/individual) if it's not already done. If you have no previous installation of python make sure to add Anaconda to your path. If you want to work with environments please read https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file
    
    <img src="img/conda.png">

- Install [Sublime](https://www.sublimetext.com/3)


<a name="Evaluation system"></a>

## Grading

You will have three grades at the end of the semester for this module. 

### Final exam

Date: tbd.
Content: Theoretical questions and study case with a Python code to interpret and comment. Details tbd

### Project = Oral + Dossier

Date: tbd

You will have a project to do, the subject is totally free, use this opportunity to do something that interests you ! 
I want this project to be uploaded on your github following this structure:

- README.md (explain what is your project and how to run it, what were the issues, what are the key results, ...)
- scripts (folder containing all the functions and tools you will use for the analysis)
- Results.ipynb (jupyter notebook which runs the main "analysis" and explains the results of your project)

This structure is not mandatory and depending on your project you won't able to do exactly that. BUT try to do something clean (you are also evaluated on the structure)

The whole github repo will be considered as the Dossier.

For the oral you can either use the notebook or create a powerpoint. The goal of the Oral is to have a discussion around your project. 10-15 min of presentation and around 5 minutes of questions.

At the end of each chapter there will be a couple of todos. These todos are not mandatory (i'd rather you focus on projects) but if you want some training feel free to do them ! 


<a name="Resources"></a>
## Resources

- Ramalho L. Fluent python:  Clear, concise, and effective programming.” O’Reilly Media, Inc.”; 2015 Jul 30.
- Mitchell R. Web scraping with Python:  Collecting more data from themodern web.  ” O’Reilly Media, Inc.”; 2018 Mar 21.
- https://pythonprogramming.net/introduction-intermediate-python-tutorial/
- https://realpython.com/