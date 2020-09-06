"""Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour."""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours_dict={}
relevant_lines = sorted([ info.split()[5].split(':')[0] for info in handle if info.startswith('From ')])

for time in relevant_lines:
    hours_dict[time]=hours_dict.get(time,0)+1

for hour, count in hours_dict.items():
    print(hour, count)
