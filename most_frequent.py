def most_frequent(list):
  return max(set(list), key = list.count)
  
  
list = [1,2,1,2,3,2,1,4,2]
most_frequent(list)
