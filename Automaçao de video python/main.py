from moviepy.editor import vfx, VideoFileClip, concatenate_videoclips

video1 = VideoFileClip("video teste.mp4").subclip (11, 31). fx(vfx.fadeout,1)
video2 = VideoFileClip("video testee.mp4").subclip (0, 9). fx(vfx.fadein,1). fx(vfx.fadeout, 2)

video_concatenado = concatenate_videoclips([video1, video2])
video_concatenado.write_videofile("VideoEditado.mp4")

