## clones all the students repos in the file PUI2016_Tue.csv or PUI2016_Thu.csv"
## run as
#####$ python gitallrepos.py Tue
## or
#####$ python gitallrepos.py Thu
##
##must have env variable PUI2016 set up and pointing to a
import pandas as pd
import os
import sys

### read in file
tmp = pd.read_csv('PUI2018_' + sys.argv[1] + '.csv')[['GitHub handle','Net ID']]
tmp.dropna(inplace=True)
tmp['GitHub Link'] = tmp['GitHub handle'].apply(lambda x:'https://github.com/' + x) 

### checking env variable is set up
puidir = os.getenv("PUI2018")
if puidir is None:
	print ("make sure the env variable PUI2018 is set up")
	sys.exit()

### creating puidir if needed
if not os.path.isdir(puidir):
        os.system("mkdir -p %s"%puidir)
        #print ("make sure %s exists and is a directory"%puidir)
	#sys.exit()

### moving to work into puidir
os.chdir(puidir)
print (puidir)
cwd = os.getcwd()
print (" you are in %s"%cwd)

### checking you are in the right repo
if not (cwd + '/').replace('//', '/') == (puidir + '/').replace('//', '/') and not (cwd + '/').replace('//', '/').replace('gpfs1','home') == (puidir + '/').replace('//', '/'):

        print ("something is wrong:I cannot go to the PUI2018 directory")

### creating subdir for students session and moving to work in there
if not os.path.isdir(puidir + '/' + sys.argv[1]):
        os.system("mkdir %s"%sys.argv[1])
os.chdir(puidir + '/' + sys.argv[1])

## prining the repo names and cloning
for i,n in enumerate(tmp['Net ID'].values):
        print (tmp['GitHub Link'].values[i]+"/PUI2016_"+n)

for i,n in enumerate(tmp['Net ID'].values):
        os.system ("git clone " + tmp['GitHub Link'].values[i]+"/PUI2018_"+n)

