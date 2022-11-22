<h1 align="center">
    <tt>> Regex Validate GUI Userform</tt>
</h1>

A GUI user form with Tkinter that uses Regex to validate the user inputs. Also, it saves the records in a database to be able to log in and see the user information.

Project for the second-semester course "Programming Languages" (ST0244) taught at EAFIT University by prof Edison Valencia.

## Features

- 🔍 Checks valid syntax of user inputs, according to certain parameters.

- 🧬 Analyzes the expressions with a regex process.

- 🗝 Saves your information in a database, to be accessed for you at any time with your username and password.

## Motivation

The main aim of this project was to use regular expressions in a useful situation and go further with the project, creating something user-friendly with a GUI.

In other words, learn how to use the Python Regex Library (`re`) and one of the Python GUI libraries (`Tkinter`).

## Documentation

**Note:** Please read the [Input Instructions](#input-instructions).

In the following documentation, we specified, some questions proposed by the prof for the presentation of this and how to use correctly the program.

### Questions

<details><summary>Project Questions</summary>

**1. What was the chosen programming language and why?**

    The chosen programming language was Python. The reasons why it was chosen 
    were essentially based on the large number of tools provided by a high-level 
    language such as Python, because in the case of reading regular expressions, 
    the library "re” located in the Python standard libraries module was very 
    helpful when interpreting patterns in String expressions or phrases. In 
    addition, the library provides an approach and allows to understand in a 
    great way the operation of a regular expression and the behavior of reading 
    the characters when carrying out the compilation work. In this same sense, 
    Python is a language that allows the programmer to work very efficiently 
    with String type data, since actions such as slicing, concatenation, 
    conversion and iteration of text strings become a much clearer and more 
    concise task taking into account the variety of functions that Python 
    provides to modify strings. On the other hand, this language also has many 
    possibilities when it comes to implementing Graphic User Interfaces (GUI), 
    since the idea of carrying out a graphic part within the project was 
    explored so that it would be reflected, in a way more familiar to the user, 
    the importance and daily use of regular expressions; therefore, having 
    worked with this language allowed executing the visual scope of the project 
    and linking the interface with the logical part of the program.

**2. What is your general opinion of the chosen programming language?**

    From our perspective, we believe that the chosen language represents a large 
    number of benefits and learning within the development of a project, since 
    it adapts appropriately to the needs of the programmer and users, and offers 
    a wide variety of options when executing an action, such as being able to 
    offer different programming paradigms when choosing a coding style where the 
    most strengthened is the imperative paradigm, followed by object-oriented 
    programming and certain part of functional programming; along the same 
    lines, we consider that Python is a very ordered and concise language that 
    allows ideas to be illustrated with the support of various libraries, 
    functions and applications integrated or compatible with Python, for example 
    in the field of data analysis, databases, etc. Likewise, we consider that 
    Python is a very versatile language when it comes to developing applications 
    or user interfaces, this is reflected, for example, in applications such as 
    Netflix and Spotify whose main programming language is Python.

**3. What is your appreciation of the way of input and output of data in this programming language?**

    
    Taking into account that within the project we worked with regular 
    expressions, it was necessary to be able to interact with the user so that 
    an expression could be read and interpreted. For this, the input() function 
    was used, which is part of the Python language by default and its function 
    is based on receiving data on the screen, stopping the reading flow until 
    the user enters certain information. We consider that this data collection 
    is very convenient in terms of the needs of developers since it is a 
    function that already comes with the Python package, compared to Java, for 
    example, where a function as essential as requesting data by keyboard must 
    be done by importing the module "java.util.Scanner" where this same Scanner 
    must be initialized for its use. Due to the above, data entry in Python is 
    quick and simplified with the input() function whose value it will receive 
    by default will be a string type, which is ideal when working with text 
    strings, as it was in the case of this project. On the other hand, in the 
    data output there is the print() function, which is a tool with a large 
    number of features that allow you to modify the output values in a more 
    profitable way, because with print(), actions such as formatting strings or 
    String Interpolation, printing several lines of text, the specification of 
    parameters that print() receives, are activities that over time have evolved 
    and become more comfortable to use when programming, which makes the screen 
    output more accurate.

**4. How is the handling of data types and data structures in this programming language?**

    Regarding data handling, Python is a very flexible interpreted language 
    since it is dynamically typed and allows the management of different types 
    of data within the same block of code, for example, in functions, which can 
    receive as a parameter and return different types of data. Likewise, Python 
    offers different tools when working with large data flows and for this 
    reason it is very popular in the field of data science and big data 
    management. Regarding data structures, Python is a language that allows easy 
    understanding of the use of data structures and different algorithms due to 
    its syntactic simplicity, as the programmer seeks to focus more on the 
    operation of the given data structure/algorithm and not worry so much about 
    the format or basic structure of the code. In addition to the above, Python 
    is a language that has a wide variety of collections and libraries that 
    allow working with different data structures such as stacks and queues, as 
    well as data structures such as linked lists and trees can be observed with 
    object-oriented programming, which facilitates the execution of data 
    analysis projects that, for example, must be added to complex data 
    structures.

</details>


### Input Instructions

We used the Python Regex Library (`re`) to analyze the expressions according to certain patterns, created from Regular Expressions theory.

- `username`: Must have a minimum length of 8 characters and a maximum of 16 characters.
- `name`: Must contain only letters in upper or lower case.
- `email`: Must contain characters as letters or numbers, followed of an `@` and finally a correct subdomain.

        hello@gmail.com

- `Date of Birth`: You can enter your birth date in the following formats:
                  
        - 10/10/2015 (dd/mm/yyyy)
        - 10-10-2015 (dd-mm-yyyy)
        - 10 NOV 2010 (dd [English Abbreviation for Month] yyyy)
        - 10 NOVIEMBRE 2010 (dd [Spanish Month] yyyy)
                  
    **You must be 18 years or older in order to create an account**

- `Credit Card`: The credit card number must be only American Express, Visa or Mastercard. The `ExpDate` must have one of the following formats (mm/yy) or (mm--yy). And the CVV must contain 3 digits.

- `Password`: The password to be accpeted, must have at least, upper and lower case letters, special symbols and a length of 8 characters. Remember the special symbols allowed are the following:
    
        --> '$'  '@'  '_'  '*'  '!'  '¡'  '-'  '#'

### Caveats

- The database is a `.txt` file, the data contained there is not protected. See [Contribute](#contribute).

- The program has some bugs that are not solved because of its complexity and the time of development of the project. See [Contribute](#contribute).

- Take into account to create your development environment to run correctly the program. This program is not compiled.

- Save your credetials in a Password Manager to access your information. At the moment, the program has not a Password Recovery system.


## Install

We designed the project to be able to run either on a GUI or your terminal.

### GUI

1. Clone the project on your machine.

    ```bash
    git clone git@github.com:alejoriosm04/regex-validate-gui-userform.git
    ```
2. Go to the project directory (or wherever you stored it).

    ```bash
    cd regex-validate-gui-userform/src/
    ```
3. Install the dependencies using `pip`

    ```bash
    pip install -r requirements.txt
    ```
4. Run the program.

    ```bash
    python3 main.py
    ```
### Terminal

If you have problems running the `GUI` program with Tkinter, you will be able to use the user form in your terminal. At the moment, the `CLI` program is not linked with the database.

1. Go to the project directory (or wherever you stored it).

    ```bash
    cd regex-validate-gui-userform/cli/
    ```
2. Run the program.

    ```bash
    python3 main.py
    ```

## Demo

![Demo of regex-validate-gui-userform-v0.1](https://i.imgur.com/F0fG98U.gif)

### Screenshots

<div align="center">
  <img src='https://i.imgur.com/nVO37Fd.png' height='280px'/>
  <img src='https://i.imgur.com/XDUCJlR.png' height='280px'/>
  <img src='https://i.imgur.com/OYYUQkh.png' height='280px'/>
</div>

## Contribute

Since this is the authors' coursework, we will not review pull requests. However, this project can be used as a basis for developing new features.

Authors in the future might add new features like link the program to a MongoDB Database in the cloud, add new features and solve some bugs.

## Authors

[Lina Ballesteros](https://github.com/linasofi13) and [Alejandro Ríos](https://github.com/alejoriosm04) developed the entire program.

<a href="https://github.com/alejoriosm04/regex-validate-gui-userform/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=alejoriosm04/regex-validate-gui-userform" />
</a>

<!-- Made with [contrib.rocks](https://contrib.rocks).
-->

## License

Copyright (c) 2022, Lina Sofia Ballesteros Merchan, Alejandro Rios Muñoz. All rights reserved.
