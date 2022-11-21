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

### Input Instructions

- `username`: Must have a minimum length of 8 characters and a maximum of 16 characters.
- `name`: Must contain only letters in upper or lower case.
- `email`: Must contain characters as letters or numbers, followed of an `@` and finally a correct subdomain.

    > hello@gmail.com

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
    git@github.com:alejoriosm04/regex-validate-gui-userform.git
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
    cd regex-validate-gui-userform/testing/
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