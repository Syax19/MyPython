'''
Question: 請使用者輸入介於1~1000的整數，由程式幫您判斷是奇數還是偶數。

以下將呈現基本程式碼，包裝成函數的程式碼，包裝成類別的程式碼。
'''

try:
	num = int(input("Please enter a number(1~1000):"))

	if (num % 2 == 0) and (1 <= num <= 1000):
		print(num, "is an even number")
	elif (num % 2 != 0) and (1 <= num <= 1000):
		print(num, "is an odd number.")
	else:
		print("Please enter a number within 1~1000")

except ValueError as error_name:  # 當使用者輸入非阿拉伯數字1~1000時會raise ValueError
	print(error_name)
	print("Please enter a number within 1~1000")


###### 將程式碼包裝成函數 odd_or_even ######
def odd_or_even():
	try:
		num = int(input("Please enter a number(1~1000):"))

		if (num % 2 == 0) and (1 <= num <= 1000):
			print(num, "is an even number")
		elif (num % 2 != 0) and (1 <= num <= 1000):
			print(num, "is an odd number.")
		else:
			print("Please enter a number within 1~1000")

	except ValueError as error_name:
		print(error_name)
		print("Please enter a number within 1~1000")


if __name__ == "__main__":
	odd_or_even()


###### 將程式碼包裝成類別 OddOrEven ######
###### 若有性質相似的函數可以放在同一個類別中######
class NumberIdentifier:
	def __init__(self):
		while True:
			try:
				num = int(input("Please enter a number(1~1000):"))
				self.num = num
				break
			except (ValueError, AttributeError) as error_name:  # 當使用者輸入非阿拉伯數字的其他字元時會raise ValueError
				print(error_name)
				print("Please enter a number within 1~1000")
				continue  # 當輸入錯誤時會跳回"Please enter a number(1~1000):"

	def odd_or_even(self):
		try:
			if (self.num % 2 == 0) and (1 <= self.num <= 1000):
				print(self.num, "is an even number")
			elif (self.num % 2 != 0) and (1 <= self.num <= 1000):
				print(self.num, "is an odd number.")
			else:
				print("Please enter a number within 1~1000")
		except ValueError as error_name:
			print(error_name)
			print("Please enter a number within 1~1000")


if __name__ == "__main__":
	a = NumberIdentifier()
	a.odd_or_even()
