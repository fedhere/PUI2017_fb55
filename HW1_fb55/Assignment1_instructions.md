# Assignment 1: 

**Set up your environment:**

1. create a directory on your computer or on your workspace on CUSP compute called PUI2017. 

2. create an environmental variable PUI2017 that points to that directory (the full directory path starting with /home on a linux box, and with /Users on a mac) so that typing 

```
$ echo $PUI2017
```
returns the full path to the directory. Save  it in your .bashrc (linux) or .bash_profile (OS X) so that every time you open a new terminal the terminal knows what the $PUI2017 env var is set to.
create an alias such that typing 

```
$ pui2017
```
takes you to that directory (hint: the alias should use the cd command). Use the env. variable $PUI2017 to do so. 

Take a screenshot of your .bashrc/.bash_profile file where one can see the alias and env. variable you created. Type this series of commands on the terminal:

``` 
pwd

pui2017

pwd
```
Take a screenshot of your terminal that shows this series of commands and their output. 

Once your environment is set up go to github online and CREATE A NEW GITHUB REPO CALLED PUI2017_<NYUid> ( this for me would be PUI2017_fb55: https://github.com/fedhere/PUI2017_fb55 ). Follow the github directions to create a repository on the command line on your local machine.  Notice that in this case you are working in the reverse order compared to the lab: you create the first instance of the repository on the remote server (on the web) and then you create a local repo to link to it on your machine. Follow the steps indicated by github to create the repo, a README.md file, and to link the online and local repos. 
