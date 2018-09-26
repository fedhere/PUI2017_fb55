## pulls all updates from the students repos in the file PUI2016_Tue.csv or PUI2016_Thu.csv"
## run as
#####$ python pullallgits.py Tue
## or
#####$ python pullallgits.py Thu
##
##must have env variable PUI2018 set up and pointing to a
import os
import sys
import glob


### checking env variable is set up
puidir = os.getenv("PUI2018")
if puidir is None:
	print ("make sure the env variable PUI2018 is set up")
	sys.exit()


### moving to work into puidir
os.chdir(puidir + "/" + sys.argv[1])
print (puidir)
cwd = os.getcwd()
print (" you are in %s"%cwd)

### checking you are in the right repo
if not (cwd + '/').replace('//', '/') == (puidir + '/' + sys.argv[1] + "/").replace('//', '/'):
        print ("something is wrong:I cannot go to the PUI2018 directory")

allrepos = glob.glob("PUI2018*")

for repo in allrepos:
        os.chdir(puidir + "/" + sys.argv[1] + "/" + repo)
        os.system("git pull")
        os.chdir(puidir + "/" + sys.argv[1])
        

