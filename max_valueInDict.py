import operator

# Returns max value for the keys value pairs in my_dict

max(my_dict.items(), key=operator.itemgetter(1))[0]
