#This code was written using a pair programming methodology by my friend and I, to solve a data processing problem he had for a presentation regarding the linguistics of metal music.

#This program determines linguistic compressability by searching through a string that represents a sentence's structure in chars that each correspond to a word in the sentence by what type it is - noun, verb, adjective, adverb, etc. 
#As an example, in this program's input, the sentence "Mary ate spaghetti" would be written as "NVN". If there were another substring of NVN in the file, this program will find each one after the first and replace it with a period character
#It would continue doing this with sentence structures of length ranging from MIN_WINDOW_SIZE up to MAX_WINDOW_SIZE

#I have provided comments to assist in maintaining knowledge of the program's functionality for myself, as well as to demonstrate my documentation style

#!/usr/bin/python
import fileinput
import re

#Window size determines the 
MIN_WINDOW_SIZE = 3
MAX_WINDOW_SIZE = 12

windowSize = MAX_WINDOW_SIZE
    
f = open("output3.txt", "w")
	
if __name__ == '__main__':
	words = []
	
	#Each line of the input file is stripped of whitespace, and each character is appended onto the end of an array, named words.
	for line in fileinput.input():
		stripped = line.rstrip()
		if words == '':	continue
		ch = stripped[0]
		for ch in stripped:
			words += ch

	inputLength = len(words)
	
	while windowSize >= MIN_WINDOW_SIZE:
		#compress.py looks through the input file, searching for substrings from MIN_WINDOW_SIZE to MAX_WINDOW_SIZE in length. It ignores all white space and line breaks.
		windowIndex = 0
		while windowIndex < len(words) - windowSize:
			#The window is the size of the substring being matched
			windowContent = words[windowIndex:(windowIndex+windowSize)]
			if None in windowContent:
				windowIndex += 1
				continue
			searchIndex = windowIndex + 1
			#Each time the window increments, the searchindex looks through everything ahead of it for that exact substring found in the window.
			while searchIndex < len(words) - windowSize:
				searchContent = words[searchIndex:(searchIndex+windowSize)]
				if None in searchContent:
					searchIndex += 1
					continue
				#If a match is found, a period is inserted to replace the removed later matching substrings.
				if ".".join(windowContent) == ".".join(searchContent):
					removalIndex = searchIndex
					while removalIndex < searchIndex + windowSize:
						words[removalIndex] = None
						removalIndex += 1
				searchIndex += 1
			windowIndex += 1
		windowSize -= 1
		
	#This next line is poetry in motion;it sets words to be every string in words save for the empty ones
	words = [word for word in words if word is not None]
    
	print (words)
	
	#Finally, the program outputs the length of the input versus the output, and gives the compressability index as a proportion of them
	outputLength = len(words)
	compressability = 1 - (outputLength / inputLength)
	f.write(str(inputLength))
	f.write("\n")
	f.write(str(outputLength))
	f.write("\n")
	f.write(str(compressability))