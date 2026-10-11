# *****************************************************

# Numpy Lab | AGENDA
# =====================
#   - Finding out the NPS (Net promoter score)
#   - Fiitbit case study

# ***********************************************************

# Case Study:
# ===========

# NPS (Net Promoter score)
# ========================

'''
NPS (Net Promoter score)
========================

How likely is it that you would recommend [company x] to a friend or colleagues?
0 1 2 3 4 5 6 7 8 9 10
Not at all likely   Extremely likely


* How to calculate NPS:

    Detractors : Respondents with a score of 0-6
    Passive : Respondents with a score of 7-8
    Promotors : Respondents with a score of 9-10

    Net Promoter Score = % Promoters - % Detractors

    If NPS >= 70:
        world class
    

'''





import os
print("Current Working Directory:", os.getcwd())

path = 'Module-3 Data Analytics and Visualisation - Python Libraries\\Day 16, 19 Sep 2025 Numpy- Lab\\'

survey_path = f'{path}survey.txt'

# NPS Case Study
import numpy as np
score = np.loadtxt(fname=survey_path, dtype=int)

# How do I get first 10 elements?
print(score[:10])


# Detractors are used 

fit_path = f'{path}fit.txt'

data = np.loadtxt(fit_path,dtype=str)

# date, step_count, mood, calories_burned, sleep_hours, status


# print(data[:10])

# We can extract data like followinf and by using Transpose as well
# date = data[:,1]


date, step_count, mood, calories_burned, sleep_hours, status = data.T

step_count = step_count.astype('int')
sleep_hours = sleep_hours.astype('int')
calories_burned = calories_burned.astype('int')


# print(step_count)







# Question : What is average step count on "Active" days?

print(status=="Active")
print(step_count)
print(step_count[status=="Active"])
print(np.mean(step_count[status=="Active"]))
# 3226.5714285714284



# Question :  Find avg calories burned when status is inactive
print(np.mean(calories_burned[status=="Inactive"]))
# 86.48148148148148

# Question : How many days had more than 5000 steps and burned more than 150 calories
print(np.sum((calories_burned>150) & (step_count>5000)))
# 17


# What number of days had a "Sad" mood?
print(np.sum(mood=="Sad"))
# 29


# Find the percent as well?

print((np.sum(mood=="Sad")*100)/len(mood=="Sad"))
# 30.208333333333332


# What is the maximum number of steps taken on days with less than 6 hours of sleep?


# Which mood had the highest average step count?


# Is there a correlation in number of steps and the mood a person has

print(np.unique(mood))
# ['Happy' 'Neutral' 'Sad']
print(np.mean(step_count[mood=='Happy']))
# 3392.725

print(np.mean(step_count[mood=='Neutral']))
# 3153.777777777778

print(np.mean(step_count[mood=='Sad']))
# 2103.0689655172414


#===========================================================================
# Assignment
#===========================================================================

# Q1. Filter Scores
'''
What NumPy technique is used to filter scores where respondents are detractors (score ≤ 6)?

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/291/original/survey.txt?1749800323

Choose the correct answer from below:

1.np.where(score > 6)

2.score[score <= 6]

3.np.select(score == 6)

4.score(score <= 6)
'''
# Ans : 2

#===========================================================================


# Q2. Promoters Percentage

'''
Which of the following correctly calculates the percentage of Promoters (where score >= 9) from the NumPy array score?

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/291/original/survey.txt?1749800323


Choose the correct answer from below:

1.percentage promoters = (num promoters / total) * 100

2.percentage_promoters = (score >= 9 / total) * 100

3.percentage_promoters = (len(score[score >= 9]) / total) * 100

4.percentage_promoters = len(score[score >= 9]) * 100
'''
# Ans : 3



#===========================================================================


# Q3. Code Calculation

'''
What does this line of code calculate?

nps = percentage_promoters - percentage_detractors

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/291/original/survey.txt?1749800323


Choose the correct answer from below:

1.Number of respondents who are promoters.

2.Total percentage of neutral respondents.

3.Net Promoter Score (NPS).

4.Percentage of detractors only.
'''
# Ans : 3


#===========================================================================


# Q4. Active Days

'''
What is the average step count on "Active" days?

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367


Choose the correct answer from below:

1.np.mean(step_count[data[:,5] == 'Active'])

2.np.mean(step_count[data[:,5] != 'Active'])

3.np.mean(step_count[data[:,2] == 'Active'])

4.np.mean(step_count[data[:,1] == 'Active'])
'''

# Ans : 1

#===========================================================================

# Q5. Calories

'''
How many days had more than 5000 steps and burned more than 150 calories?

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367


Choose the correct answer from below:

1.np.sum((step_count > 5000) & (calories > 150))

2.np.sum((step_count > 150) & (calories > 5000))

3.np.sum((step_count > 150) | (calories > 5000))

4.np.sum(step_count + calories > 5150)
'''

# Ans : 1


#===========================================================================

# Q6. Sad Mood

'''
What percentage of days had a "Sad" mood?

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367


Choose the correct answer from below:

1.80

2.50

3.30

4.10
'''


data = np.loadtxt('https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367',dtype='str')
mood = data[:,2]
print((np.sum(mood=='Sad')/len(mood))*100)
# 30.208333333333332

# Ans : 3

#===========================================================================

# Q7. Steps

'''
What is the maximum number of steps taken on days with less than 6 hours of sleep?

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367


Choose the correct answer from below:

1.7422

2.6500

3.8000

4.5642

'''
# Ans : 

data = np.loadtxt('https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367',dtype='str')
hours_of_sleep = data[:,4].astype('int')
step_count = data[:,1].astype('int')
print(np.max(step_count[hours_of_sleep<6]))
# 7422

# Ans : 1

#===========================================================================

# Q8. Inactive days
'''
What are the average calories burned per hour of sleep on "Inactive" days?

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367


Choose the correct answer from below:

1.18.62

2.15.98

3.23.78

4.11.24
'''

data = np.loadtxt('https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367',dtype='str')
calories_burned = data[:,3].astype('int')
active = data[:,5]
hours_of_sleep = data[:,4].astype('int')
print(np.mean(calories_burned[active=='Inactive']/hours_of_sleep[active=='Inactive']))

# 18.62282480893592

# Ans : 1

#===========================================================================


# Q9. Average step count

'''
Select the correct code snippet -> Which mood had the highest average step count?

Dataset: Link
A.

 np.unique(mood)[  
    np.argmax([  
        np.mean(step_count[mood == m]) for m in np.unique(mood)])]
B.

np.argmax([  
    np.mean(step_count)])
C.

np.unique(mood)[  
    np.argmax([  
        step_count[mood == m].min()   
        for m in np.unique(mood)])]
D.

np.argmax([  
    np.mean(step_count == m)   
    for m in np.unique(mood)])


Choose the correct answer from below:

A

B

C

D


'''
# Ans : 1


#===========================================================================

# Q10. Calories Burned

'''
Calculate the correlation between step count and calories burned.

Dataset:https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367

Choose the correct answer from below:

0.98

1.0

0.66

0.75
'''

data = np.loadtxt('https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367',dtype='str')
calories_burned = data[:,3].astype('int')
step_count = data[:,1].astype('int')
print( np.corrcoef(step_count, calories_burned)[0,1])
# 0.9892596952985985

# Ans : 1

#===========================================================================

# Q11. Median Sleep

'''
On how many days was the mood "Sad" and sleep less than the median sleep?

Select the correct code snippet.

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367


Choose the correct answer from below:

1.np.sum((mood == 'Sad') & (sleep < np.median(sleep)))

2.np.mean((mood == 'Sad') & (sleep <= np.median(sleep)))

3.len((mood == 'Sad') & (sleep < np.median(sleep)))

4.np.count_nonzero((sleep < mood) & 'Sad')

'''
# Ans : 1

#===========================================================================

# Q12. Happy Mood

'''
What is the standard deviation of step count only for "Happy" mood days?

Dataset:


Choose the correct answer from below:

1.2088.40

2.3081.60

3.2085.90

4.1008.90
'''

data = np.loadtxt('https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367',dtype='str')
mood = data[:,2]
step_count = data[:,1].astype('int')
print( np.std(step_count[mood=='Happy']))

# 2088.4016254961593

# Ans : 1

#===========================================================================

# Q13. Frequent number of Hours
'''
What is the most frequent number of hours slept?

Dataset:

Choose the correct answer from below:

5

3

10

7

'''

data = np.loadtxt('https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367',dtype='str')
mood = data[:,2]
hours_of_sleep = data[:,4].astype('int')


unique, counts = np.unique(hours_of_sleep, return_counts=True)
print(unique[counts==counts.max()])
# 5

# Ans : 1


# Q14. Lowest Average Calories

'''
Which mood has the lowest average calories burned on days with more than the median hours of sleep and a step count above 4000?

Dataset:


Choose the correct answer from below:

'Sad'

'Neutral'

'Happy'

'Cannot be determined'
'''
# median_sleep = np.median(df['hours_of_sleep']) 
# result = df[(df['hours_of_sleep'] > median_sleep) & (df['step_count'] > 4000)].groupby('mood')['calories'].mean().idxmin()

# Ans : 2

#===========================================================================

# Q15. Longest Streak

'''
What is the longest streak (in days) where 'Inactive' days had calories burned less than the daily mean across the full dataset?

Dataset:

Choose the correct answer from below:

2

8

4

1

'''

daily_mean = np.mean(calories_burned)
print(daily_mean)



max_streak = 0 
current_streak = 0 
for i in range(len(active)): 
    if active[i] == 'Inactive' and calories_burned[i] < daily_mean:
        current_streak += 1
        max_streak = max(max_streak, current_streak) 
    else: current_streak = 0 
print(max_streak)
# 8




#===========================================================================
# Additional Problems
#===========================================================================

# Q1. Stack up

# Which of the following is used to stack arrays column wise?

'''
Choose the correct answer from below:

1.hsplit()

2.vsplit()

3.hstack()

4.vstack()

'''
# Ans : 3

#===========================================================================


# Q2. Split the difference

'''
Which of the following code snippet will raise an error?

A.

arr = np.arange(10)
np.split(arr, 3)

B.

arr = np.arange(10)
np.split(arr, 5)

C.

arr = np.arange(10)
np.split(arr, [2,5])

D.

arr = np.arange(10)
np.split(arr, [5, 12])

'''
# Ans : A


#===========================================================================

# Q3. Row vs column

# Given a 2D array, which of the following will split the array row-wise?

'''
Choose the correct answer from below:

1.hsplit()

2.vsplit()

3.hstack()

4.vstack()
'''
# Ans : vsplit()

#===========================================================================

# Q4. Copy types

import numpy as np
arr = np.array([2,4,6,8,10])
c0 = arr
c0[0] = 12
arr = np.array([2,4,6,8,10])
c1 = arr.view()
arr[0] = 12
arr = np.array([2,4,6,8,10])
c2 = arr.copy()
arr[0] = 12

'''
Choose the correct answer from below, please note that this question may have multiple correct answers

1.c1 represents shallow copy and c2 represents deep copy


2.c1 represents deep copy and c2 represents shallow copy.


3.If arr and c1 are printed after line 4 and 7 respectively, they would have printed 12 as first element.


4.If c1 and c2 are printed after line 7 and 10 respectively, they would print 12 as first element of array.
'''

# Ans :1, 3

#===========================================================================

# Q5. Dark dimension

'''
Given a 3D array of shape (2,2,2)

arr = array([[[0, 1], 
             [2, 3]], 
 
            [[4, 5], 
             [6, 7]]])

What will be the output of arr[:, 0:,:1]?


A.

array([[2, 3], 
       [6, 7]])

B.

array([[0, 1], 
       [4, 5]])

C.

array([[[0], 
        [2]], 

       [[4], 
        [6]]])
D.

array([[[0, 1], 
        [2, 3]], 

       [[4, 5], 
        [6, 7]]])
'''

# Ans : 3

#===========================================================================


# Q6. Median Step Count

'''
On days when the person was 'Sad' and burned fewer than average calories, what is the median step count?

Dataset : https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367

Choose the correct answer from below:

351

314

158

651
'''


print(np.median(step_count[(mood == 'Sad') & (calories_burned<np.mean(calories_burned))]))
# 651

# Ans : 4

#===========================================================================


# Q7. Step count, sleep and sad

'''
How many days had below-median step count, above-average sleep, and the mood was not 'Sad'?

Dataset:https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367

Choose the correct answer from below:

12

13

10

11


'''

print(np.sum((step_count<np.median(step_count)) &(hours_of_sleep>np.mean(hours_of_sleep))&(mood!='Sad')))

# 13
# Ans : 2

#===========================================================================


# Q8. Correlation of Sleep

'''
What is the correlation between hours of sleep and calories burned, only for days marked as 'Active'?

Dataset:https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367


Choose the correct answer from below:

0.98

0.02

-0.11

0.04
'''
print(np.corrcoef(hours_of_sleep[active=='Active'], calories_burned[active=='Active'])[0,1])
# 0.03816228531580669

# Ans : 4

#===========================================================================


# Q9. Highest ratio of Calories

'''
Which date corresponds to the day with the highest ratio of calories burned to hours of sleep?

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367

Choose the correct answer from below:

'07-11-2017'

'06-10-2017'

'11-10-2017'

'13-10-2017'
'''

print(date[np.argmax(calories_burned/hours_of_sleep)])
# 07-11-2017

# Ans :1

#===========================================================================

# Q10. Consecutive days

'''
Find the 3-day period (consecutive days) with the maximum total calories burned. What is the starting date of that period?

Dataset: https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/132/292/original/fit.txt?1749800367

Choose the correct answer from below:

'06-10-2017'

'12-12-2017'

'11-11-2017'

'08-10-2017'
'''




rolling_sums = np.convolve(calories_burned,np.ones(3,dtype='int'),mode='valid')


print(rolling_sums)

max_idx = np.argmax(rolling_sums)

start_date = date[max_idx]
print(start_date)
# 12-12-2017

# Ans : 2

#===========================================================================

