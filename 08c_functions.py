def percent(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100 # return back with the value
    return p
marks1 = [45,78,86,77]
#percentage1 = (sum(marks)/400)*100
#percentage1 = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
percentage1 = percent(marks1)
marks2 = [75,98,88,78]
#percentage2 = (sum(marks)/400)*100
percentage2 =percent(marks2)
print(percentage1, percentage2)
