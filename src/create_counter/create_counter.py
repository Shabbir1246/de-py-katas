def create_counter(num):


	def up(local_num = num):
		# print(local_num)
		local_num += 1
		return local_num


	def down(local_num = num):
		local_num -= 1
		return local_num
	

	counter_dic = {
		'up': up,
		'down': down
	}
	return counter_dic

counter = create_counter(10)
up = counter['up']
down = counter['down']
print(up())
print(down())
print(down())
