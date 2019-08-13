# Development Environment

The Develepment Environment is about the collection of tools and processes all the developers should do in order to work in a collaborative work place.

As part of the development environment all the developers should have and/or know:

  - A basic knowledge on operating systems
  - A programing language
  - Version control system 
  - IDE (Integrated Development Environment)

# Basic knowledge of operating systems

## The Terminal
Basically when dealing with operating systems we have to approaches to excute comands and tasks:
1) From the graphical user interface (GUI).
2) From the terminal.

Why stick to terminal?
1) Not everything has a GUI.
2) Sometimes the GUI is badly designed. With Terminals, you won't need to look through stupid tabs and menus trying to find a button that looks like it will do what you are trying to do.
3) The terminal is keyboard only, no need to use your mouse.

Getting used to the terminal is a bit complicated at first, but once you are used to it, you won't be able to remember how your life used to be before using it.

### In Windows you can open the terminal by excuting the command CMD from your Start Menu Search!

## Basic comands

When we are programing, there are basic commands we have to know to deal with operating systems such as:

    list, create, delete directories 

### In Windows you can perform these tasks as following:

    dir <DIRECTORY> - List the content of the specified directory
    md <DIRECTORY> - create a directory
    cd <DIRECTORY> - Get into the directory
    cd .. - Get out of a directory and goes to the external level
    rmdir <DIRECTORY> - Delete a directory

# A programing language
There are many types of programming languages, sometimes a programing language follow a programing paradigma, but sometimes the are created multipurpose.

Python is a programming language that supports multiple programming paradigms, including procedural, object-oriented, and functional programming. 

Learn more about it here: https://www.python.org/

Installing python: 
https://www.python.org/downloads/windows/

after you run the installer you shoud type on your terminal:

    python --version
    
and you should get the version of the python installed on your computer

    Python 2.7.10

when you run pyhton on your terminal by typing python and pressing enter, you should get the following python prompt:

    Python 2.7.10 (default, Feb 22 2019, 21:55:15) 
    [GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

from here you can start basic operations such as:

    >>> A = 5
    >>> B = 6
    >>> print("The some of A plus B is %s" % str(A+B))
    The some of A plus B is 11

# Version control system
A version control system is a tool that alows you to save your code in a way that you can restore previous versions when needed. Sometimes we mess up our codes and we would need to restore a version where things were correct. this is what the version control system enable.

There are many different version control systems but GIT is the most used one and it provides a lot of smart funcionatilites. 
You can learn about git at the link below
https://git-scm.com/

You can use a version control system local and remote, in order to have a remote version of your code you have to create a REPOSITORY on github server. 
http://github.com

Since you have your account the steps of creating a Repository and upload your code go as follow:

    On your machine
    1 - Go into the directory containing the project.
    2 - Type "git init" <enter>
    3 - Type "git add ." <enter> to add all of the relevant files.
    4 - Type "git commit -m 'first commit' "

Now that you have a local repository, it is time to connect to the github server

    On github.com
    1 - Go to github.com
    2 - Log in to your account.
    3 - Click the new repository button in the top-right. You’ll have an option there to initialize the repository with a README file, but I don’t.
    4 - Click the “Create repository” button.
    
Now you have a repository created on line and you need to upload the files

    1 - Go into the directory containing the project.
    2 - git remote add origin https://github.com/<YOUR GITHUB USERNAME>/< YOUR NEW_REPO>
    3 - git push -u origin master

That's it, you have now your code saved on github!

# IDE (Integrated Development Environment)

A IDE is a place where you can edit your software, you can create your application structure with folders and files. IDE's provide sintaxe highlight and code completeness capabilities which allows you to produce code fast.

There are many paid and free options, for python Sublime 3 is a good one
You can know more about it by reading the documentation of sublime on the link below
https://www.sublimetext.com/



