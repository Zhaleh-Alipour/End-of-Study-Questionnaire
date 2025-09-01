#### there is a weird problem in this code. I copied this from the online version (Qualtrics info. py) which works ok.
#### problem is that in the final file in the age column, it enters "how old are you", but in the online verison it doesn't return that.
#### the same is true for "unique id" column where it prints "unique id" in the first row instead of actually perticipants' unique id
import pandas as pd
import numpy as np
## 81: Complete
## 80: Unique ID
## Years of Ins = 63,65,67,69,71
## Years of Playing = 64,66,68,70,72
participants = []
def isNaN(num): #Checks if Variable has something in it
    return num != num
def getInt(str): #Gets numbers from a string, Example: From "3 yeas" Returns 3.
   s = ''.join(x for x in str if x.isdigit())
   if(s == ""):
      return 0
   return int(s)

ex = pd.read_excel('End of study Q_in-person_141.xlsx')
for index,row in ex.iterrows():
   # if(index == 0):   # I don't get this part! It should normally iterrate over indexes so we get participants one by one!
   #    continue
   # if(int(row[81]) == 1): # row "complete" it shows if participants have completed the experiment or not
   uniqueId = row[17] # UniqueID
   age = row[63]
   print(age)
   yearsOfPlaying = 0
   yearsOfIns = 0
   YOI = [81,83,85,87]
   YOP = [82,84,86,88]
   for I in YOP:
      if(isNaN(row[I]) == False):
         yearsOfPlaying += getInt(row[I])
   for I in YOI:
      if(isNaN(row[I]) == False):
         yearsOfIns += getInt(row[I])
   if row[66] == 'Right':
      LRHand = 1
   elif row[66] == 'Left':
      LRHand = 2
   else:
      LRHand = np.nan
   if row[64] == 'Female':
      Gender = 1
   elif row[64] == 'Male':
      Gender = 2
   else:
      Gender = np.nan
   if yearsOfIns >= 5:
      YOI = 2
   else:
      YOI = 1
   if yearsOfPlaying >= 5:
      YOP = 2
   else:
      YOP = 1
   tmp = {          # here we create a dictionary. One dictionary per person!
      'Unique id': uniqueId,
      'Age': age, #pd.to_numeric(age), # we use pd.to_numeric to convert strings to numbers. Notice that if there are NaN cells it doesn't give error and just returns NaN
      'Gender [1:F, 2:M]': Gender,
      'Musician_years of playing ( >= 5 -> 2 )': YOP,
      'Musician_years of instruction ( >= 5 -> 2 )': YOI,
      'years of instruction':yearsOfIns,
      'L/R Hand [1:R, 2:L]': LRHand,
      'Vis seq': row[27],
      'Vis SD': row[28],
      'Aud seq': row[29],
      'Aud SD': row[30],
      'vib seq': row[31],
      'vib SD': row[32]
   }
   participants.append(tmp) # append dictionaries to the list 'participants'. So we will have a list filled with dictionaries!
print(participants)

df = pd.DataFrame(participants) # converts the list into data frame
writer = pd.ExcelWriter('Final_inperson.xlsx', engine='xlsxwriter') # creates an excel file
df.to_excel(writer, sheet_name='sheet1', index=False)  # puts the dataframe into the excel file
writer.save()
print(df.groupby('L/R Hand [1:R, 2:L]').size())
print(df.groupby('Gender [1:F, 2:M]').size())
# a=df['Age'].mean()
# print(f'average of age is {a}')
print(df.groupby('Musician_years of instruction ( >= 5 -> 2 )').size())
print(df.groupby('Musician_years of playing ( >= 5 -> 2 )').size())
print(df.groupby('Vis seq').size())
print(df.groupby('Vis SD').size())
print(df.groupby('Aud seq').size())
print(df.groupby('Aud SD').size())
print(df.groupby('vib seq').size())
print(df.groupby('vib SD').size())
