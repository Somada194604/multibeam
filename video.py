import cv2

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter('video_multibeam_repeat1.mp4', fourcc, 30.0, (1024, 768))

for i in range(0, 360, 1):
	img = cv2.imread('anim/fig_{:03}.png'.format(i))
	#print('anim/fig{:03}.png'.format(i))
	video.write(img)

for i in range(0, 360, 1):
	img = cv2.imread('anim/fig_{:03}.png'.format(i))
	#print('anim/fig{:03}.png'.format(i))
	video.write(img)

video.release()
