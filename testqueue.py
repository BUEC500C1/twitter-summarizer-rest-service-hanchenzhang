from video_queue import run_video
import pytest

#The two test are running without API keys

def test1():
	input_user = ["@BU_Tweets","@MIT","@BarackObama","@realDonaldTrump","@atletienglish"]
	assert run_video(input_user) == 1

def test2(): # invalid user name case
	input_user = ["@BU_Tweats","@MoT","@BarObaa","@realDaldTrump","@atletiish"]
	assert run_video(input_user) == 0
# if __name__ == "__main__":
# 	main()
