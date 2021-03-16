# --------------
import numpy as np
new_record=[[50,9,4,1,0,0,40,0]]
data=np.genfromtxt(path,delimiter=",",skip_header=1)
census=np.concatenate((data,new_record))

age=census[:,0]
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)


race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
lenghts=[len_0,len_1,len_2,len_3]
minority_race=lenghts.index(min(lenghts))
print(minority_race)

senior_citizens=census[census[:,0]>60]
working_hours_sum=np.sum(senior_citizens[:,6])
senior_citizen_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizen_len
print(working_hours_sum)
print(avg_working_hours)


high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print(avg_pay_high)
print(avg_pay_low)


