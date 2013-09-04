

class RVEngine:
	
	instance = None
	queue = []
	FrameNo = 0
	FPS = 0
	FPS_MIN = 0
	TickTime = 0
	Time = 0
	
	def __init__(self):
		return self
		
	@staticmethod
	def execute(code, callback=""):
		pkg = "[\"" + callback + "\", { " + code + " }]"
		RVEngine.queue.append(pkg)
		return pkg
	
	@staticmethod
	def execMP(code, callback=""):
		str = "[{" + code + "}] call EX_fnc_MPexec"
		return RVEngine.execute(str,callback)
		
	@staticmethod	
	def next():
		if len(RVEngine.queue) == 0:
			return "['',nil]"
				
		return RVEngine.queue.pop(0)
	
	@staticmethod
	def log(message,file=__file__):
		return RVEngine.execute('[str("' + message + '"), "' + file + '"] call EX_fnc_log');
		