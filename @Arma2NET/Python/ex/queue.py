class Queue:
	QUEUE=[]
	
	def add(message):
		QUEUE.append(message)
	
	def next():
		QUEUE.pop(0)