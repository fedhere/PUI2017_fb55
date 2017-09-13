# Basic commands for text editors

**vi**

you should know the ABC of vi because it is often set up as the default environment for github. So github may open a vi editor on your behalf, and you must know how to get out of there.

open as 

``` 
vi <filename>
```

vi has several working *modes*. In general you will want to be in a single mode at a time.
type *i* to begin inserting text

type *esc* to exit the insert mode (or whichever mode you are in)

type *:q* to exit without saving

type *:wq* to save and exit

type *r* to replace a character

type *R* to replace an indefinite number of characters

type *0* to move to the beginning of a li ne

type *p* to paste in the line below where you are

type *P* to paste in the line above where you are

type *u* to undo

type */*\<text\> to search \<text\>

type *n* to move to the next instance of \<text\> 

type *N* to move to the previous instance of \<text\>



**emacs**

open as 
``` 
emacs <filename>
```
this will pop a window. If your connection is slow you may want to use 
```
emacs -nw <filename>
```
instead to open emacs directly on the terminal, with limited functionality

you can type away.

to save type  *ctrl+x ctrl+s*

to exit type *ctrl+x ctrl+c*

to copy a line type *ctrl+k*

to paste the content of your clipboard type *ctrl+y*

to undo type *ctrl+_* (that is *ctrl+shift+-*)

**nano**

Mohit already mentioned this :

type
```
nano <filename>
```

type your content

save the file by typing *ctrl+o* and exit using *ctrl+x*
