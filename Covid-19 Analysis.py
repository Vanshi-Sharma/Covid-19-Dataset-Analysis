import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Covid-19 dataset.csv")
#print(df)
df["Date"] = pd.to_datetime(df["Date"])

df["Week"] = df["Date"].dt.isocalendar().week
df["Month"] = df["Date"].dt.month_name()
df["Weekday"] = df["Date"].dt.day_name()
#print(df)
# filling missing values usinf fillna method
df["7Day_MA_Cases"]=df["7Day_MA_Cases"].fillna(df["7Day_MA_Cases"].median())
#print(df["7Day_MA_Cases"])

#Filter rows where Daily_Cases > 180.
filtered = df[df["Daily_Cases"] > 180]
#print(filtered)

#for days in df[df["Daily_Deaths"]>3]["Date"]:
    #print(days)

#calculate total number of cases
total_sum=df["Daily_Cases"].sum()
print("The total sum of daily cases:",total_sum)
mean=df["Daily_Cases"].mean()
print("The mean of daily cases:",mean)
median=df["Daily_Cases"].median()
print("The median of daily cases:",median)
std=df["Daily_Cases"].std()
print("The standard deviation of daily cases:",std)

sum=df.groupby("Month")["Daily_Cases"].sum()
print("The daily cases according to each month:\n",sum)
sum1=df.groupby("Month")["Daily_Deaths"].sum()
print("The daily deaths according to each month:\n",sum1)

weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

df["Weekday"] = pd.Categorical(df["Weekday"],
                               categories=weekday_order,
                               ordered=True)

sorted_df = df.sort_values("Weekday")
#print(sorted_df)


sns.set_style("whitegrid")
fig,axs=plt.subplots(1,4,figsize=(15,5))

columns=["Daily_Cases","Daily_Deaths","Daily_Tests","7Day_MA_Cases"]
print(df[columns].corr())

sns.heatmap(data=df[columns].corr(),annot=True,linewidth=2,linecolor="black",ax=axs[0])
axs[0].set_yticklabels(axs[0].get_yticklabels(), rotation=45)
axs[0].set_title("Correlation Heatmap")

sns.regplot(data=df,x="Daily_Cases",y="Daily_Tests",ax=axs[1])
axs[1].set_title("Daily Cases vs Daily Tests")
sns.despine()

sns.barplot(data=df,x="Weekday",y="Daily_Cases",palette="Set1",hue="Month",ax=axs[2])
axs[2].set_title("Weekly Daily Cases by Month")
axs[2].set_xticklabels(axs[2].get_xticklabels(), rotation=45)
sns.despine()

sns.kdeplot(data=df,x="Daily_Deaths",hue="Month",palette="Set1",fill=True,ax=axs[3])
axs[3].set_title("Daily Deaths Distribution (KDE)")
sns.despine()

plt.suptitle("Covid-19 Dashboard",fontsize=18,fontweight="bold")
plt.tight_layout()
#plt.savefig("dashboard")
plt.show()


