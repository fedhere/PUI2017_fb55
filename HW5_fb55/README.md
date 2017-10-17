# PUI2017 HW 5.

## ASSIGNED READING:

[POINTS OF SIGNIFICANCE - Analyzing outliers: influential or nuisance? (Naomi Altman & Martin Krzywinski Nature 2016)](
https://www.nature.com/nmeth/journal/v13/n4/pdf/nmeth.3812.pdf)

## ASSIGNMENTS:

### Submission Info:

Work in groups of up to 5 as usual, and you are encouraged to. 
Create a HW4\_\<nyuID\> directory in your PUI2017\_\<nyuID\> repository. 
Include a README.md that briefly summarizes the scope of the homework (so we know you understand what you did), 
and states with whome you worked and what you specifically contributed to. 


Submit each assignment as separate notebooks as usual in your PUI2017 repo in the HW5_fb55 directory. Remember the README with the statement of how you contributed to the work in your group

Keep in mind that we will look for possible cases of plagiarism, 
and if the code appears too similar to that of people that you did not work with to be original work 
(there are automated ways to look for plagiarism in code) you will be penalized.

## Assignment 1: Test the Z test: 
(all simulated data)


Generate N samples from a distribution of your choice, **but not a Gaussian** with a chosen mean μ and standard deviation σ:   N(μ, σ) and calculate the mean of each sample (all samples should have the same size n). 

Assess the validity of the Z-test: If the samples are drawn from the distribution you are testing the z-values you calculate should follow a N(0,1) distribution (a Gaussian with mean 0 and standard deviation 1). Show that the distribution of z -statistics (find the formula in a statistics book or in last week’s slides) that you calculated (one for each sample) is indeed consistent with N(0,1).


### Grading: 
you must:

plot your original distribution

plot at least one of the samples

plot the distribution of z statistics

fit the z-statistics with a gaussian model and assess the goodness of fit with a simple test (AD or KS).

** REMOVED CAUSE WE HAVE NOT COVERED IT YET find the best fit values for the model parameters (mean and standard deviation) by minimizing the model chi square. **

plots need have caption, axis labels, etx and comment your figures and test results appropriately (to demonstrate your understanding).




## Assignment 2: Compare Tests for Goodness of fit
Follow the skeleton notebook [Assignment 2](https://github.com/fedhere/PUI2017_fb55/blob/master/HW5_fb55/Assignment2_instructions.ipynb)
Test that in fact binomial and Poisson distribution look increasingly more similar to Gaussians as the mean of the distribution increases.


### GRADING: 

Your notebook should show the distributions, the models, clearly state the H0 null hypothesis, and properly interpret the tests (remember captions, significance, etc etc)

## Assignment 3: investigate linear relationships between fire arm possession, homicides by fire arms, and mass shootings for different countries, considering also the country GDP


Follow instructions in [this skeleton notebook](https://github.com/fedhere/PUI2017_fb55/blob/master/HW5_fb55/Assignment3_instructionsUpdated.ipynb)

### Grading 
Usual grading scheme applies. Remember that succesfully fitting a line to data is not sufficient. Comment on what conclusions can be drawn from your analysis (and don't jump to conclusions!)
