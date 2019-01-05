class cycle:
	def __init__(self, user_string, counter=0):
		self.u_str = user_string
		self.u_str_len = len(self.u_str)
		self.u_str_buff = None

		self.counter = counter


	def __next__(self):
		"""
		Replaces the character in the buffer (u_str_buff) by the next character
		Increases the counter by 1 
		OR resets it to 0 if the counter is at the maximum number
		else it would throw: IndexError: string index out of range
		
		Example usage:
		x = cycle(['foo', 'bar'])
		print(next(x))
		output:
		foo
		bar
		foo
		"""
		self.u_str_buff = self.u_str[self.counter]

		if self.counter < self.u_str_len:
			self.counter += 1

		if self.counter >= self.u_str_len:
			self.counter = 0

		return self.u_str_buff


	def next_item(self):
		"""
		== Updated version for this is __next__() ==
		Replaces the character in the buffer (u_str_buff) by the next character
		Increases the counter by 1 
		OR resets it to 0 if the counter is at the maximum number
		else it would throw: IndexError: string index out of range
		"""
		if self.counter >= self.u_str_len:
			self.counter = 0

		self.u_str_buff = self.u_str[self.counter]

		if self.counter < self.u_str_len:
			self.counter += 1

		return self.u_str_buff


	def get_counter(self):
		"""
		Returns the integer counter
		"""
		return self.counter