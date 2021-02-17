# sean.mcwillie @
# university of maine 

# Given a file of length L, extract M number of features, each having a unique number, N, of coordinate pairs. Create a list that is composed of atomic coordinates as cartesian pairs in an ordered list, associated with each Feature.

from ast import literal_eval #allows loading a list from a file with brackets intact

################################
# File Format Assumptions
file_name = "input.txt" 

### start of file
# 1 # Feature 0:
# 2 # [[x_0_0, y_0_0], [x_0_1, y_0_1], [x_0_2, y_0_2], ... [x_0_n0, y_0_n0]]

# . # 
# . # 
# . # 

#L-1# Feature M:
# L # [[x_m_0, y_m_0], [x_m_1, y_m_1], [x_m_2, y_m_2], ... [x_m_nm, y_m_nm]]
### end of file

# It is further assumed that the data is in correct list-like syntax and contains no missing values.

################################

mainlist = []

with open(file_name) as f:
  count = 0
  
  for line in f:
        count+=1
        #print("Line # " + str(count))

        # instantiate the 1-level lists here, then add them to main list after

        if count % 2 == 0: 
          mainlist.append([list(literal_eval(line))])

mainlist.pop(0) # this gets rid of the empty sub-list that we appended to

# test statements:
print("Examples:")
print((mainlist[0][0][1])) # outputs a pair
print((mainlist[0][0][1][0])) # outputs a longitude (x value)
print((mainlist[0][0][1][1])) # outputs a latitude (y value)

# use this if you need a count of how many points are in a feature:
print(len(mainlist[0][0])) #Outputs the number of points that comprise a feature


# more test statements:
#print(mainlist[0]) #outputs all of Feature 0

#print(mainlist[1]) #outputs all of Feature 1
#print(mainlist[2]) #outputs all of Feature 2
#print(mainlist[3]) #outputs all of Feature 3

# How to interpret for passing to ArcGIS: 
# mainlist[a][b][c][d])
# in text file input we have the following ontology: Feature > an ordered[?] "Collection" of Coordinates > Coordinate Pairs > X & Y values
# a : Feature ("Feature 0")
# b : Variables (just has 0, 0 is the coordinates as a "collection", no other Feature-level variables are in this ontology)
# c : Cartesian Coordinate Pairs (this is many coordinates, can be 0 to the max # points)
# d : long/x & lat/y  (0 is x, 1 is y)