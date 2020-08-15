def convert(stringofname):
	name = []
	start = []
	end = []
	for i in range(len(stringofname)):
		if stringofname[i] == '@': start.append(i)
		if (stringofname[i] == ',' or stringofname[i] == ']'): end.append(i)

	if (len(start) != len(end)):
		print("transformation failure")
		return 0;

	for i in range(len(start)):
		name.append(stringofname[start[i]:end[i]])
	print(name)
	return name

if __name__ == "__main__":
	input_user = "[@BU_Tweets, @MIT, @BarackObama, @realDonaldTrump, @atletienglish]"
	convert(input_user)