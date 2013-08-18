import webapp2
import random




mathHeader="""
<font size=50 color=red>
Welcome to Multiple Choice Math!
<br><br><br></font>
"""


punishVid1="""<font size =100>
Ooops you missed that last one! Try this one!
</font>
"""





rewardVid1="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/R424MGHDFDc?autoplay=1&start=20&end=30" frameborder="0" allowfullscreen></iframe>
"""
#cars2

rewardVid2="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/R424MGHDFDc?autoplay=1&start=54&end=59" frameborder="0" allowfullscreen></iframe>
"""
#cars2

rewardVid3="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/R424MGHDFDc?autoplay=1&start=67&end=74" frameborder="0" allowfullscreen></iframe>
"""
#cars2

rewardVid4="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/2BlMNH1QTeE?autoplay=1&start=70&end=81" frameborder="0" allowfullscreen></iframe>
"""
#toy story 3

rewardVid5="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/2BlMNH1QTeE?autoplay=1&start=115&end=125" frameborder="0" allowfullscreen></iframe>
"""
#toy story 3

rewardVid6="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/pkqzFUhGPJg?autoplay=1&start=80&end=90" frameborder="0" allowfullscreen></iframe>
"""
#up

rewardVid7="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/SPHfeNgogVs?autoplay=1&start=55&end=63" frameborder="0" allowfullscreen></iframe>
"""
#finding nemo


rewardVid8="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/tmHhtrR9nyM?autoplay=1&start=17&end=32" frameborder="0" allowfullscreen></iframe>
"""
#incredibles


rewardVid9="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/5e16U8UsT4I?autoplay=1&start=48&end=60" frameborder="0" allowfullscreen></iframe>
"""
#walle


rewardVid10="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/WGByijP0Leo?autoplay=1&start=48&end=60" frameborder="0" allowfullscreen></iframe>
"""
#cars


rewardVid11="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="http://www.youtube.com/embed/WGByijP0Leo?autoplay=1&start=16&end=26" frameborder="0" allowfullscreen></iframe>
"""
#cars


rewardVid12="""<font size = 300>
CORRECT!
<br><br><br></font><iframe width="560" height="315" src="//www.youtube.com/embed/-WdC4DaYIeQ?autoplay=1&start=20&end=30" frameborder="0" allowfullscreen></iframe>
"""
#incredibles



rewardVids=[rewardVid1, rewardVid2, rewardVid3, rewardVid4, rewardVid5, rewardVid6, rewardVid7, rewardVid8, rewardVid9, rewardVid10, rewardVid11, rewardVid12]

punishVids=[punishVid1]




Q1="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="4">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q2="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q3="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+0 = 
	</font>
	<br>
	<label>
	<font size = 300>
	1
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	0
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q4="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	0
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	1
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q5="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	2
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q6="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+3 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	2
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q7="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	2
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q8="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q9="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	6
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q10="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q11="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q12="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	0+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	6
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q13="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+0 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	1
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	2
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q14="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	2
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	0
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	3
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q15="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	2
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	5
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q16="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+3 = 
	</font>
	<br>
	<label>
	<font size = 300>
	2
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	4
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q17="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q18="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	3
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q19="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q20="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	11
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q21="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	0
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q22="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	1+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	10
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q23="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+0 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	2
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	1
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q24="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q25="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	2
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	5
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q26="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+3 = 
	</font>
	<br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q27="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q28="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	6
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q29="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q30="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q31="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q32="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	2+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q33="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+0 = 
	</font>
	<br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	2
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	6
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q34="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	5
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q35="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	9
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q36="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+3 = 
	</font>
	<br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q37="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q38="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	9
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q39="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q40="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	10
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q41="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q42="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	3+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	11
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q43="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+0 = 
	</font>
	<br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	4
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q44="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q45="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	9
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q46="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+3 = 
	</font>
	<br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	17
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	18
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q47="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	11
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q48="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q49="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	10
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q50="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q51="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	12
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q52="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	4+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	16
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	13
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q53="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+0 = 
	</font>
	<br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q54="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	4
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q55="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q56="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+3 = 
	</font>
	<br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q57="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	14
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q58="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q59="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q60="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	9
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q61="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	13
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q62="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	5+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	13
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q63="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+0 = 
	</font>
	<br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	6
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q64="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q65="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	10
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q66="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+3 = 
	</font>
	<br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q67="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	13
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q68="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	11
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q69="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	14
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q70="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q71="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	13
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q72="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	6+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q73="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+0 = 
	</font>
	<br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	5
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	9
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q74="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	3
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	5
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q75="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q76="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+3 = 
	</font>
	<br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q77="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	15
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q78="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	10
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q79="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	10
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q80="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	11
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q81="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	11
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q82="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	7+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	16
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q83="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	8+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	6
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q84="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	8+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	8
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	11
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q85="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	8+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	7
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q86="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	8+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	13
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q87="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	8+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	15
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q88="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	8+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	21
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	16
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q89="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	8+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	16
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	17
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	18
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q90="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+0 = 
	</font>
	<br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	10
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q91="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+1 = 
	</font>
	<br>
	<label>
	<font size = 300>
	7
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q92="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	14
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q93="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+2 = 
	</font>
	<br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	9
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q94="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+3 = 
	</font>
	<br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	10
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	13
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q95="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+4 = 
	</font>
	<br>
	<label>
	<font size = 300>
	13
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	25
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	22
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q96="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+5 = 
	</font>
	<br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label>
	<label>
	<font size = 300><br>
	8
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q97="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+6 = 
	</font>
	<br>
	<label>
	<font size = 300>
	18
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	14
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="1">
	</font>
	</label>
	<label>
	<font size = 300><br>
	11
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q98="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+7 = 
	</font>
	<br>
	<label>
	<font size = 300>
	23
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	20
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	12
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	16
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q99="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+8 = 
	</font>
	<br>
	<label>
	<font size = 300>
	4
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="2">
	</font>
	</label><br>
	<label>
	<font size = 300>
	16
	<input type="radio" name="q2" value="4">
	</font>
	</label>
	<label>
	<font size = 300><br>
	17
	<input type="radio" name="q2" value="1">
	</font>
	</label>

	<input type="submit">
</form>
"""

Q100="""
<form action="/quiz">
	<br><br><br>
	<font size = 300>
	9+9 = 
	</font>
	<br>
	<label>
	<font size = 300>
	11
	<input type="radio" name="q2" value="3">
	</font>
	</label><br>
	<label>
	<font size = 300>
	18
	<input type="radio" name="q2" value="1">
	</font>
	</label><br>
	<label>
	<font size = 300>
	15
	<input type="radio" name="q2" value="2">
	</font>
	</label>
	<label>
	<font size = 300><br>
	23
	<input type="radio" name="q2" value="4">
	</font>
	</label>

	<input type="submit">
</form>
"""

questions=[Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16,Q17,Q18,Q19,Q20,Q21,Q22,Q23,Q24,Q25,Q26,Q27,Q28,Q29,Q30,Q31,Q32,Q33,Q34,Q35,Q36,Q37,Q38,Q39,Q40,Q41,Q42,Q43,Q44,Q45,Q46,Q47,Q48,Q49,Q50,Q51,Q52,Q53,Q54,Q55,Q56,Q57,Q58,Q59,Q60,Q61,Q62,Q63,Q64,Q65,Q66,Q67,Q68,Q69,Q70,Q71,Q72,Q73,Q74,Q75,Q76,Q77,Q78,Q79,Q80,Q81,Q82,Q83,Q84,Q85,Q86,Q87,Q88,Q89,Q90,Q91,Q92,Q93,Q94,Q95,Q96,Q97,Q98,Q99,Q100]



class IntroPage(webapp2.RequestHandler):
  def get(self):
	self.out.write(form)


class MainPage(webapp2.RequestHandler):
  def get(self):
       self.response.out.write(mathHeader)
       self.response.out.write(random.choice(questions))




class QuizHandler(webapp2.RequestHandler):
	def get(self):
	     q2=self.request.get("q2")
	     if q2=="1": 	
		rewardToggle=rewardVids.pop()
		rewardVids.insert(0,rewardToggle)
	     	self.response.out.write(rewardToggle)
		self.response.out.write(random.choice(questions))
	     else:
		punishToggle=punishVids.pop()
		punishVids.insert(0,punishToggle)
		self.response.out.write(punishToggle)
		self.response.out.write(random.choice(questions))




app = webapp2.WSGIApplication([ ('/intro', IntroPage),
				('/quiz', QuizHandler),
				('/', MainPage),
								
],
                              debug=True)

