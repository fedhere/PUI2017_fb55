# PUI2017 HW 3.

## ASSIGNED READING:

- [The Earth is Round (p<0.05)](http://ist-socrates.berkeley.edu/~maccoun/PP279_Cohen1.pdf), Jacob Cohen 1994. A critique of _p_-value based science. 


## ASSIGNMENTS:

## Submission Info:
### You can work in groups, and you are encouraged to. Create a HW3\_\<netID> directory in your PUI2017\_\<netID> repository. Include a README.md that briefly summarizes the scope of the homework (so we know you understand what you did), and states with whome you worked and what you specifically contributed to.  Submit Assignment 1, Assignment 2 and Assignment 3 by pushing the notebooks into your PUI2017\_\<netID>/HW3\_\<netID>  repository.  Keep in mind that we will look for possible cases of plagiarism, and if the code appears too similar to that of people that you did not work with to be original work (there are automated ways to look for plagiarism in code) *you will be penalized*. 


### Assignment 1: Write an ipython notebook that demonstrates visually in a data-driven way the Central Limit Theorem. 
A skeleton notebook is [here](https://github.com/fedhere/PUI2017_fb55/blob/master/HW3_fb55/Assignment1.ipynb)

- GENERATE  100 samples of different sizes N (N>10 & N<2000) from each of 5 different distributions (500 samples in total), _all with the same population mean_
- Include a _Normal_, a _Poisson_, a _Binomial_, a _Chi-Squared_ distribution, and 1 more of your choice.    
- For each sample plot the sample mean (dependent var.) against the sample size N (independent var.) (if you want you can do it with the sample standard deviation as well). 
- Describe the behavior you see in the plots in terms of the law of large numbers.
- PLOT the distributions of all sample means (together for all distributions). _Mandatory_: as a histogram. _Optional_: in any other way you think is convincing
 
__Extra Credit__: FIT a gaussian to the distribution of means            

### GRADING: 

Your notebook must: 
- generate the distributions, correctly generated for each of the 5 ditributions, all with same mean.
- display all plots: a scatter plot per distribution and a histogram of all distributions, usual rules for plotting applying: visible and readable axes, title, legend, caption. 
- each plot must have a caption which describes the plot in terms of Central Limit Theorem


### Assignment 2: Set up the work for data-driven inference based on CitiBike data. You should, even more than usual, work in groups for this!

### I developed an example [here] (https://github.com/fedhere/PUI2017_fb55/blob/master/HW3_fb55/citibikes_gender.ipynb)

  
Work on [compute](https://github.com/fedhere/PUI2016_fb55/blob/master/computationalResources.md). 
Choose a citibikes [dataset within the CUSP data facility (DF)](https://datahub.cusp.nyu.edu/dataset) ( the path should be gws/open/Student/citibike ) or download citibike data from their website.

1. Fire off a Jupyter notebook with Jupyter Hub --[here](https://datahub.cusp.nyu.edu/documents/guides/Jupyter_Notebook_from_your_browser_Mac.pdf) for Mac and Linux and [here](https://datahub.cusp.nyu.edu/documents/guides/Jupyter_Notebook_from_your_browser_Windows.pdf) for Windows--
and switch to the Kernel PUI2017_Python2 or PUI2017_Python3 from the Jupyter dropdown menu under Kernels -> Change Kernel.

   Write a Jupyter Notebook on compute. This will require you to use the JupyterHub ([instructions here](https://datahub.cusp.nyu.edu/documents/guides/Jupyter_Notebook_from_your_browser_Mac.pdf) ). Write a notebook that:

2. States the question you want to ask, and formulates the Null and Alternative hypothesis (remember the confidence level!)
3. Use pandas to read in the CitiBike files, either from the DF, or locally, but you must be able to download them on the spot (so the TA can reproduce your work). 
3. Display the top few rows of the DF in your notebook. This table __must be rendered__.
5. Display the reducted dataframe. This table __must be rendered__.
6. Plot your data distributions.

### GRADING: 

Your notebook must display
- the complete formulation of the hypothesis to be tested
- the data tables for the unreducted datasets (first few columns)
- the data tables for the reducted datasets (first few columns)
- the plots for each dataframe, with usual rules for plotting applying: visible and readable axes, title, legend, caption. 

## Assignment 3: Finish z-test lab and turn it in as a notebook .

I am looking for here is: seeing a good Null/alternative hypothesis statement and treatment, with a clear Null and Alternative spelled out AND written out as a formula, and a good interpretation of the Z value you obtain in terms of ability or inability to reject the Null Hypothesis. 
Here is the forumla

<img src="http://www.sciweavers.org/tex2img.php?eq=Z%20%3D%20%5Cfrac%7B%5Cmu_%7Bpop%7D%20-%20%5Cmu_%7Bsample%7D%7D%7B%5Csigma%20%2F%20%5Csqrt%7BN%7D%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="Z = \frac{\mu_{pop} - \mu_{sample}}{\sigma / \sqrt{N}}" width="154" height="44" /> 

This is also in the slides attached (in a more readable format).

The chapter of Statistics In a Nutshell that covers these topics is called Inferential statistics. It is chapter 3 in the hard copies of the book in the CUSP library, but it was moved to chapter 7 in the online book version which is in the link. Same content more or less.


### GRADING: 

Your notebook must display
- the complete formulation of the hypothesis (Null and Alternative) to be tested in words and formula
- the download of the data (which is in https://github.com/fedhere/PUI2017_fb55/blob/master/Lab3_fb55/times.txt, but you must get the raw data!)
- the calculation of the z statistics (with the given formula and the data processed from the data file)
- the comparison of the statistis with the significance threshold and the conclusions about the Null Hypothesis

