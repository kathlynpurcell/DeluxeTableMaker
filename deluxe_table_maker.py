# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:16:26 2019

@author: kpurc
"""
###this is incredibly simple so please take note of the directions###
###program to make deluxe table for AAStex###

##include .txt file of data, seperated by a tab (default for Excel, can be changed in line 33), 
##with header formatted the same as the rest of the data in the same directory as the program##
##see the attached samlpe input if this is comfusing##


#program

#open the file (read it line by line) and open the new file
tabName=input("What is the name of the file you want to convert? (include '.txt')\n")
table = open(str(tabName), 'r+')
table_line = table.readline()
new = open("DeluxeTable.txt", 'w+')

#make the column lines for formatting
new.write("\\begin{deluxetable}{c|")
ask_first = input("How many columns do you have? \n")
ask=int(ask_first)-1 #this is so we can use the input as an index

#start the header line for the AAStex file
while ask != 0:
    new.write("l|")
    ask = ask - 1
new.write("}" + "\n\n")


#make the header from the first line of the .txt file
    ###if delimiter is not a tab change that here###
column = table_line.split("\t")
n = int(ask_first)
while n != 0:
    if (n == 0):
        n=0
    else:
        if (n == int(ask_first)):
            new.write("\\tablehead{ \n" + "\colhead{" + column[int(ask_first) - n] + "}")
            n = n-1
        else:
            new.write(" & \colhead{" + column[int(ask_first) - n] + "}")
            n = n-1

#go to the second line so we dont have two headers
table_line = table.readline()

#print the data of the table to the new .txt file in deluxetable format 
new.write("\n" + "}" + "\n\n\n" + "\startdata" + "\n")
print("Running")
while table_line:
    formatted_line = table_line.replace("\t","&")
    new.write(formatted_line + "\\\ \hline" + "\n")
    table_line = table.readline()
    print(".")

#close up the data part of the table
new.write("\enddata" + "\n\n")

#optionally add a caption
caption = input("Add a caption now, if no caption enter 0 \n")
if (caption == "0"):
    new.write("\n")
else:
    new.write("\caption{" + caption + "} \n\n")

#finish the whole table in LaTex
new.write("\end{deluxetable}" + "\n")



#close everything and tell the user its done
table.close()
new.close()
print("Done! Saved as DeluxeTable.txt. Its ready to use in AASTex")

