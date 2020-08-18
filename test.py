import time

string = "Hi I am"
 # "mayank you will have you to type all correct otherwise you will loose the game.If you will win the geme you can be next winner"

#timer
# def stopwatch(seconds):
#     start = time.time()
#     time.perf_counter()
#     elapsed = 0
#     while elapsed < seconds:
#         elapsed = time.time() - start
#         print ("timer count: %02d" %(elapsed))
#         time.sleep(1)  

# stopwatch(120)

words = string.split(' ')    
print(words)


score = 0
timer = 0
total_word = 0
wpm = 0
err = 0

for i in words:
	print(i) 
	word = ""
	for ch1 in i:
		char = ""
		char = str(input())
		if ch1 == char:
			word = word + str(char)
			continue

		else:
			score = score - 3
			err = err + 1	
			total_word = total_word + 1	
			print("you have error count: ",err)
			print("you are lossing the score: ",score)
			print("your word count is: ",total_word)
			break;
	if i == word:
		score = score + 2
		total_word = total_word + 1
		print("your score is ",score)
		print("your word count is: ",total_word)
