# PUI2017 HW 5.

## ASSIGNED READING:


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


Follow the skeleton notebook in [Assignment 2](https://github.com/fedhere/PUI2017_fb55/tree/master/HW5_fb55/Assignment2.ipynb)

Generate N samples from a distribution of your choice, **but not a Gaussian** with a chosen mean μ and standard deviation σ:   N(μ, σ) and calculate the mean of each sample (all samples should have the same size n). 

Assess the validity of the Z-test: If the samples are drawn from the distribution you are testing the z-values you calculate should follow a N(0,1) distribution (a Gaussian with mean 0 and standard deviation 1). Show that the distribution of z -statistics (find the formula in a statistics book or in last week’s slides) that you calculated (one for each sample) is indeed consistent with N(0,1).


### Grading: 

your plots need to indiate the correct behavior, which demonstrated that as the parameter of the binomial and poisson distributions increase they look increasingly more Gaussian. Remember to include comments and captions to your figure that indicate what the figure shows (and demonstrate your understanding)




## Assignment 2: Compare Tests for Goodness of fit

Test whether a Gaussian model for the age distribution of citibike drivers is a sensible model, or if you can find a better fit with another distribution. Use 2 tests chosen from: KS, AD, KL, chisq to do this. Test at least 2 distributions. 


Optional (extra credit): Divide your sample geographically: by Borrow (Manhattan vs Brooklyn) and see if you notice any differences in how the age distribution can be modeled. You can do this with the chisq test: is the chisq better for the fit to Manhattan vs Brooklyn?


### GRADING: 

Your notebook should show the distributions, the models, clearly state the H0 null hypothesis, and properly interpret the tests (remember captions, significance, etc etc)

### Grading 

All cells that are marked "for you to do" (or similar...) and that contain missing values should be filled.

The second null hypothesis should be stated (for the "Convicted of a felony after 3 years" data).

Both tests, Z and chi-sq, should be completed for the "Convicted of a felony after 3 years" data.

The result of the test in term the rejection of the Null should be stated in all cases (for both tests and both for the original "Ever employed in a CEO transitional job" data and the "Convicted of a felony after 3 years data").

## Assignment 4: Tests of correlation using the scipy package with citibike data.

Use the following are 3 tests to assess correlation between 2 samples of citibike data:
- Pearson’s test 
- Spearman’s test 
- K-S test

There is a skeleton notebook that works on a similar question, age of male vs female riders. Follow it to see how to set up the assignment[notebook citibikes_compare_distributions.ipynb](https://github.com/fedhere/PUI2017_fb55/blob/master/HW4_fb55/citibikes_compare_distributions.ipynb). 


Use: trip duration of bikers that ride during the day vs night. State your result in words in terms of the Null Hypothesis

Use: trip duration of bikers for trips originating in Manhattan, and in Brooklyn. Use at least 2 months of citibike data. The citibike data can be accessed from the [citibike website](https://www.citibikenyc.com/system-data) - make sure you do it in a reproducible way, or in the CUSP data facility at the path /gws/open/Student/citibike


### Grading 

A notebook should be completed as the cell by cell instructions indicate.

You must state the Null Hypothesis, according to what you know about the test and the **scipy.stats** package documentation **for three scipy.stats function**, corresponding to the three tests.

You must put the caluclated statistics and the p-value in the context of null hypothesis rejection in each case.
