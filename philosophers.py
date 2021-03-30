class Philosopher:
	def __init__(self, id_):
		self.id = id_
		self.right_fork_id = self.id
		self.left_fork_id = (self.id + 1) % 5
		self.right_fork_taken = False
		self.left_fork_taken = False
		self.is_eating = False
		self.is_thinking = False

	def stop_eating_and_put_forks(self, forks):
		self.left_fork_taken = self.right_fork_taken = False
		self.is_thinking = True
		self.is_eating = False
		forks[self.left_fork_id].is_taken = False
		forks[self.left_fork_id].philosopher_id = None
		forks[self.right_fork_id].is_taken = False
		forks[self.right_fork_id].philosopher_id = None
		print(f"Philosopher {self.id} stopped eating, put down forks and started thinking")

	def try_eat(self, forks):
		if self.is_eating:
			self.stop_eating_and_put_forks(forks)
			return

		if forks[self.left_fork_id].value > forks[self.right_fork_id].value:
			if not forks[self.right_fork_id].is_taken:
				forks[self.right_fork_id].is_taken = True
				forks[self.right_fork_id].philosopher_id = self.id
				print(f"Philosopher {self.id} took fork with smaller value")
				if not forks[self.left_fork_id].is_taken:
					forks[self.left_fork_id].is_taken = True
					forks[self.left_fork_id].philosopher_id = self.id
					self.is_eating = True
					self.is_thinking = False
					print(f"Philosopher {self.id} took fork with bigger value")
					print(f"Philosopher {self.id} stopped thinking and started eating")
					return
				else:
					print(f"Philosopher {self.id} took fork with smaller value, but fork with bigger value was taken by another philosopher")
					return
			elif forks[self.right_fork_id].is_taken and forks[self.right_fork_id].philosopher_id == self.id:
				print(f"Philosopher {self.id} already has fork with smaller value")
				if not forks[self.left_fork_id].is_taken:
					forks[self.left_fork_id].is_taken = True
					forks[self.left_fork_id].philosopher_id = self.id
					self.is_eating = True
					self.is_thinking = False
					print(f"Philosopher {self.id} took fork with bigger value")
					print(f"Philosopher {self.id} stopped thinking and started eating")
					return
				else:
					print(f"Philosopher {self.id} already has fork with smaller value, but fork with bigger value was taken by another philosopher")
					return
			print(f"Philosopher {self.id} can not take fork with smaller value")
			return
		if forks[self.left_fork_id].value < forks[self.right_fork_id].value:
			if not forks[self.left_fork_id].is_taken:
				forks[self.left_fork_id].is_taken = True
				forks[self.left_fork_id].philosopher_id = self.id
				print(f"Philosopher {self.id} took fork with smaller value")
				if not forks[self.right_fork_id].is_taken:
					forks[self.right_fork_id].is_taken = True
					forks[self.right_fork_id].philosopher_id = self.id
					self.is_eating = True
					self.is_thinking = False
					print(f"Philosopher {self.id} took fork with bigger value")
					print(f"Philosopher {self.id} stopped thinking and started eating")
					return
				else:
					print(f"Philosopher {self.id} took fork with smaller value, but fork with bigger value was taken by another philosopher")
					return
			elif forks[self.left_fork_id].is_taken and forks[self.left_fork_id].philosopher_id == self.id:
				print(f"Philosopher {self.id} already has fork with smaller value")
				if not forks[self.right_fork_id].is_taken:
					forks[self.right_fork_id].is_taken = True
					forks[self.right_fork_id].philosopher_id = self.id
					self.is_eating = True
					self.is_thinking = False
					print(f"Philosopher {self.id} took fork with bigger value")
					print(f"Philosopher {self.id} stopped thinking and started eating")
					return
				else:
					print(f"Philosopher {self.id} already has fork with smaller value, but fork with bigger value was taken by another philosopher")
					return
			print(f"Philosopher {self.id} can not take fork with smaller value")
			return


class Fork:
	def __init__(self, id_):
		self.id = id_
		self.value = self.id
		self.is_taken = False
		self.philosopher_id = None


if __name__ == '__main__':
	philosophers_, forks_ = [], []
	for i in range(5):
		philosophers_.append(Philosopher(i))
		forks_.append(Fork(i))
	for k in range(5):
		print(f"------{k} iteration------")
		for phil in philosophers_:
			phil.try_eat(forks_)
		print("--------------------------")
