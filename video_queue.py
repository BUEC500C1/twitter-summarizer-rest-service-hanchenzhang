from videoHW4 import Twitterfeed, createpng, video_convertion
import queue
import threading

def run_image(user,queue):
	textlist = Twitterfeed(user)
	if textlist == 0:
		print("text generation fail")
		return 0
		exit()
	imagelist = createpng(textlist)
	queue.put(user)
	print("image for" + user + "already inside the queue")
	return 1


def run_video(input_user):
	pipeline = 2
	#input_user = ["@BU_Tweets","@MIT","@BarackObama","@realDonaldTrump","@atletienglish"]
	video_queue = queue.Queue(len(input_user))


	for i in input_user:
		a = run_image(i,video_queue)
		if a == 0:
			return 0
			exit()


	while not video_queue.empty():
		user = video_queue.get()
		#threads = []
		if isinstance(user, str):
			#threads.append(user)
			t = threading.Thread(target=video_convertion, args=[user])
			print("thread creation:"+user)

			print("active_count:",threading.active_count())
		

			if threading.active_count() <= pipeline:
				t.run()
				print("processing start: video:"+user)
			else:
				video_queue.put(t)
				print("queue is put in a thread"+user)
		else:
			return 0
			exit()

	return 1

# if __name__ == "__main__":
# 	input_user = ["@BU_Tweets","@MIT","@BarackObama","@realDonaldTrump","@atletienglish"]
# 	run_video(input_user)