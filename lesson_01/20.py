totalSeconds=int(input("Enter ceconds: "))
days=totalSeconds//(24*3600)
hours=(totalSeconds%(24*3600))//3600
minutes=(totalSeconds%3600)//60
seconds=totalSeconds%60
print(days,"day(s),", hours,"hour(s),", minutes,"minute(s),", seconds,"second(s).")