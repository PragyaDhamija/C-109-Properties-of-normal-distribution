import random
import plotly.figure_factory as pff
import statistics
import plotly.graph_objects as pgo

diceResult = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1+dice2)
fig = pff.create_distplot([diceResult],["Result"], show_hist=False)
#fig.show()

mean = statistics.mean(diceResult)
median = statistics.median(diceResult)
mode = statistics.mode(diceResult)
std = statistics.stdev(diceResult)
#print(mean,median,mode)

first_std_start, first_std_end = mean-std, mean+std
second_std_start, second_std_end = mean-(2*std), mean+(2*std)
third_std_start, third_std_end = mean-(3*std), mean+(3*std)

fig.add_trace(pgo.Scatter(x=[mean,mean],y=[0,0.17],mode = "lines+markers", name = "MEAN"))
fig.add_trace(pgo.Scatter(x=[first_std_start,first_std_start], y=[0,0.17], mode = "lines+markers", name = "First STD start"))
fig.add_trace(pgo.Scatter(x=[first_std_end,first_std_end], y=[0,0.17], mode = "lines+markers", name = "First STD end"))
fig.add_trace(pgo.Scatter(x=[second_std_start,second_std_start], y=[0,0.17], mode = "lines+markers", name = "Second STD start"))
fig.add_trace(pgo.Scatter(x=[second_std_end,second_std_end], y=[0,0.17], mode = "lines+markers", name = "Second STD end"))
fig.add_trace(pgo.Scatter(x=[third_std_start,third_std_start], y=[0,0.17], mode = "lines+markers", name = "Third STD start"))
fig.add_trace(pgo.Scatter(x=[third_std_end,third_std_end], y=[0,0.17], mode = "lines+markers", name = "Third STD end"))

#fig.show()

data_within_1std = [i for result in diceResult if result>first_std_start and result<first_std_end]
data_within_2std = [i for result in diceResult if result>second_std_start and result<second_std_end]
data_within_3std = [i for result in diceResult if result>third_std_start and result<third_std_end]


#print( " Mean of data is  : {}".format(mean) )

print("{} % of data that lies within first std".format(len(data_within_1std)*100.0 / len(diceResult)))
print("{} % of data that lies within second std".format(len(data_within_2std)*100.0 / len(diceResult)))
print("{} % of data that lies within third std".format(len(data_within_3std)*100.0 / len(diceResult)))