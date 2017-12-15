# 2017 PUI Final exam

Follow the instructions. Read the [Rules](PUI2017final_RULES.ipynb) and make sure you check out the [Hints](https://docs.google.com/document/d/1lXM07wQsbxXKfCbWYP6RJlDqFOl0E1LWWzLVJ0bEmAM/edit?usp=sharing). We have a [slack channel](https://puifinal.slack.com/) where I can answer questions and post clarifications.

**Rules** 

This exam is take home. Deliver your solution as an ipython notebook uploading it to NYUclasses BY 12/18/2017 at 0:00 AM. **DO NOT POST ON GITHUB**. **Work alone**. If you have questions feel free to ask them to your instructors and TAs on the [slack channel](https://puifinal.slack.com/). High level intellectual discussion is never forbidden, so general, conceptual questions can be discussed with your class mates, but do not exchange code, or algorithms (specific solution design).

Read the full rules and grading document [here](https://github.com/fedhere/PUI2017_fb55/blob/master/final/PUI2017final_RULES.ipynb)

There are shortcuts and hints: for example you can access the crime data that is already wrangled and pivoted. Make sure you notice the shortcuts and read the hints if you are having troubles. Dont get stuck, and if you get stuck dont stay stuck!

**Motivation:**

The study of NYC crime is of broad interest in the Urban Science scene, and NYPD has provided statistics on the crime (by precinct) for several years. This is an important resource to understand and analyze urban crime. There are obvious connections between crime and wealth, which relate both to access to precious goods (opportunity), and to how easy it is to commit a crime (the neighborhood safety, or perceived safety). [It has been suggested](https://journalistsresource.org/studies/government/criminal-justice/unemployment-property-crime-burglary) that unemployment correlates strongly with burglary for example, due to both opportunity and motivation . In addition [there are several pieces of research](https://www.citylab.com/solutions/2016/04/vacant-lots-green-space-crime-research-statistics/476040/) that indicate that access to green spaces affects crime.

In this final you should explore and model NYC crime: 

- the first part of the exam is an exploratory analysis of the crime time series for the seven major felonies 2000-2016 (temporal domain). 

- The second part of the exam attempts to relate socioeconomic features to crime rate by area (spatial domain).

- Lastly, in the  extra credit, you can aggregate the socioeconomic features that I indicated at the precinct level: percentage of unemployment and median income, that natively come at the census tract level from the census bureau ACS 5-year datta, and green area, for which you have a shape file from the NYC parks department.
