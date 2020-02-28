import tweepy
from PIL import Image,ImageDraw,ImageFont
import keys
import os
import re
from urllib import request
import time
import json

def Twitterfeed(account):
	consumer_key = keys.consumer_key
	consumer_secret = keys.consumer_secret
	access_key = keys.access_token
	access_secret = keys.access_secret

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	try: #cases when api key apply
		all_tweets = api.user_timeline(screen_name = account,count=10, tweet_mode = 'extended')
		alltext = []
		for status in all_tweets:
			tweet= status._json
			text = tweet['full_text']
			text_clean = re.sub(r"http\S+", "", text)
			alltext.append(text_clean)

	# cases when api key does not apply:
	except (tweepy.TweepError):
		try:
			file = './json_file_reference/'+account+'.json'
			with open(file) as f:
				alltext = json.load(f)
		# cases when user name not valid
		except Exception: 
			print("not valid user name")
			return 0
			exit()
	
	return alltext
	#createpng(alltext)
	#video_convertion(account)

def createpng(textlist):
	thebackground = "Boston_University_block_logo.png"
	im=Image.open(thebackground)
	im = im.resize((1080,720))
	font_name = r'./Artifakt Element Black Italic.tff'
	#imagelist = [];
	i = 0
	for tweet in textlist:
		text = tweet
		im1 = im.resize((1080,720))
		dr = ImageDraw.Draw(im1)
		dr.text((10, 360), tweet, font=ImageFont.truetype(font_name, 36), fill="#000000") 
		im1.save("image/test%d.png"%i)#Users/zhanghanchen/Desktop/spring2020/EC500/HW4/image
		#print(im1)
		#imagelist.append(im1)
		i = i + 1;

	#return imagelist

def video_convertion(user_name):
	ffmpegcommand = "ffmpeg -r 0.333 -f image2 -s 1080x720 -start_number 0 -i image/test%d.png -vframes 10" \
	" -vcodec libx264 -crf 25  -pix_fmt yuv420p output_"+ user_name +".mp4"
	p = os.popen(ffmpegcommand)
	p.close()


def run(input_user):
	textlist = Twitterfeed(input_user)
	createpng(textlist)
	video_convertion(input_user)

def main(): 

	start = time.perf_counter()
	users = ["@BU_Tweets","@MIT","@BarackObama","@realDonaldTrump","@atletienglish"]
	for user in users:
		run(user)

	end = time.perf_counter()
	print("time:",end-start)

if __name__ == '__main__':
	main()
