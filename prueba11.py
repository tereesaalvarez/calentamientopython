import random
import seaborn as sns
import matplotlib.pyplot as plt
iterations=10000
variables=['work','salary','conditions','career_advancement','social_impact','job_security','life_balance','location','atmosphere','travel']
def Monte_Carlo(grade):
final_results=[]
weight=[0.15,0.09,0.12,0.11,0.12,0.02,0.11,0.07,0.1,0.11]
for n in range(iterations):
results=[]
for i in range(len(variables)):
value = weight[i] * (random.uniform(grade[i][0], grade[i][1]))
results.append(value)
final_results.append(sum(results))
return final_results
a = Monte_Carlo([[4,9],[8.5,10],[5,9],[8.5,9.5],[3,7],[4,9],[3,8],[7.5,8],[5,9],[0,6]])
b = Monte_Carlo([[5,10],[4,4],[7,9],[2,8],[6,9.5],[8.5,10],[8,10],[0,7],[3,9],[0,3]])
c = Monte_Carlo([[4,7],[6,8],[6,9],[6.5,9],[2,6],[6.5,9],[5.5,9],[9.5,9.5],[5,9],[4,9]])
#Plot the results
fig = plt.figure(figsize=(10,6))
sns.distplot(a)
sns.distplot(b)
sns.distplot(c)
fig.legend(labels=['Job A','Job B','Job C'])
plt.title('Monte-Carlo Distributions')
plt.show()