class Anime(object):{% if row.status == "OK"  %}success{% endif %}
    size = 0
    name = ''
    bitrate = 0
    nameout = ''

    def __init__(self, name):
        self.name = name
        self.createnameout()
        self.calcbitrate()

    def createnameout(self):
        self.nameout = self.name.split(r'.')
        self.nameout[1] = 'mp4'
        self.nameout = r'.'.join(self.nameout)

    def calcbitrate(self):
        text = subprocess.getoutput('ffprobe -show_format %s | sed -n \'/duration/s/.*=//p\'' % self.name)
        duration = text.split('\n')[-1][:-1]
        duration = float(duration)
        duration = int(duration)
        self.size = path.getsize(self.name)
        bitratecl = ((self.size / duration) / 1024) * 8
        self.bitrate = int(bitratecl + ((bitratecl * 20) / 100))
        print(duration, self.bitrate, bitratecl)


def mp4anime():
    filelist = listdir()
    anime = []
    [anime.append(Anime(f)) for f in filelist if f[-3:] == 'mkv']
    for a in anime:
        system('ffmpeg -i %s -b %sk -ab 256k -strict experimental -y %s' % (a.name, a.bitrate, a.nameout))


if __name__ == '__main__':
    from os import listdir, system, path
    import re
    import subprocess
    mp4anime()
