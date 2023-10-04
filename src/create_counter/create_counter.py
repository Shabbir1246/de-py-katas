def create_counter(num):

	# global counter
	counter = num
	def up():
		nonlocal counter
		counter += 1
		return counter


	def down():
		nonlocal counter
		counter -= 1
		return counter
	

	counter_dic = {
		'up': up,
		'down': down
	}
	return counter_dic
