import glob, ffmpeg, pymediainfo

extensions = [
    '.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.3mm', '.3p2', '.60d',
    '.787', '.89', '.aaf', '.aec', '.aep', '.aepx', '.aet', '.aetx', '.ajp',
    '.ale', '.am', '.amc', '.amv', '.amx', '.anim', '.aqt', '.arcut', '.arf',
    '.asf', '.asx', '.avb', '.avc', '.avd', '.avi', '.avp', '.avs', '.avs',
    '.avv', '.axm', '.bdm', '.bdmv', '.bdt2', '.bdt3', '.bik', '.bin', '.bix',
    '.bmk', '.bnp', '.box', '.bs4', '.bsf', '.bvr', '.byu', '.camproj',
    '.camrec', '.camv', '.ced', '.cel', '.cine', '.cip', '.clpi', '.cmmp',
    '.cmmtpl', '.cmproj', '.cmrec', '.cpi', '.cst', '.cvc', '.cx3', '.d2v',
    '.d3v', '.dat', '.dav', '.dce', '.dck', '.dcr', '.dcr', '.ddat', '.dif',
    '.dir', '.divx', '.dlx', '.dmb', '.dmsd', '.dmsd3d', '.dmsm', '.dmsm3d',
    '.dmss', '.dmx', '.dnc', '.dpa', '.dpg', '.dream', '.dsy', '.dv',
    '.dv-avi', '.dv4', '.dvdmedia', '.dvr', '.dvr-ms', '.dvx', '.dxr', '.dzm',
    '.dzp', '.dzt', '.edl', '.evo', '.eye', '.ezt', '.f4p', '.f4v', '.fbr',
    '.fbr', '.fbz', '.fcp', '.fcproject', '.ffd', '.flc', '.flh', '.fli',
    '.flv', '.flx', '.gfp', '.gl', '.gom', '.grasp', '.gts', '.gvi', '.gvp',
    '.h264', '.hdmov', '.hkm', '.ifo', '.imovieproj', '.imovieproject',
    '.ircp', '.irf', '.ism', '.ismc', '.ismv', '.iva', '.ivf', '.ivr', '.ivs',
    '.izz', '.izzy', '.jss', '.jts', '.jtv', '.k3g', '.kmv', '.ktn', '.lrec',
    '.lsf', '.lsx', '.m15', '.m1pg', '.m1v', '.m21', '.m21', '.m2a', '.m2p',
    '.m2t', '.m2ts', '.m2v', '.m4e', '.m4u', '.m4v', '.m75', '.mani', '.meta',
    '.mgv', '.mj2', '.mjp', '.mjpg', '.mk3d', '.mkv', '.mmv', '.mnv', '.mob',
    '.mod', '.modd', '.moff', '.moi', '.moov', '.mov', '.movie', '.mp21',
    '.mp21', '.mp2v', '.mp4', '.mp4v', '.mpe', '.mpeg', '.mpeg1', '.mpeg4',
    '.mpf', '.mpg', '.mpg2', '.mpgindex', '.mpl', '.mpl', '.mpls', '.mpsub',
    '.mpv', '.mpv2', '.mqv', '.msdvd', '.mse', '.msh', '.mswmm', '.mts',
    '.mtv', '.mvb', '.mvc', '.mvd', '.mve', '.mvex', '.mvp', '.mvp', '.mvy',
    '.mxf', '.mxv', '.mys', '.ncor', '.nsv', '.nut', '.nuv', '.nvc', '.ogm',
    '.ogv', '.ogx', '.osp', '.otrkey', '.pac', '.par', '.pds', '.pgi',
    '.photoshow', '.piv', '.pjs', '.playlist', '.plproj', '.pmf', '.pmv',
    '.pns', '.ppj', '.prel', '.pro', '.prproj', '.prtl', '.psb', '.psh',
    '.pssd', '.pva', '.pvr', '.pxv', '.qt', '.qtch', '.qtindex', '.qtl',
    '.qtm', '.qtz', '.r3d', '.rcd', '.rcproject', '.rdb', '.rec', '.rm',
    '.rmd', '.rmd', '.rmp', '.rms', '.rmv', '.rmvb', '.roq', '.rp', '.rsx',
    '.rts', '.rts', '.rum', '.rv', '.rvid', '.rvl', '.sbk', '.sbt', '.scc',
    '.scm', '.scm', '.scn', '.screenflow', '.sec', '.sedprj', '.seq', '.sfd',
    '.sfvidcap', '.siv', '.smi', '.smi', '.smil', '.smk', '.sml', '.smv',
    '.spl', '.sqz', '.srt', '.ssf', '.ssm', '.stl', '.str', '.stx', '.svi',
    '.swf', '.swi', '.swt', '.tda3mt', '.tdx', '.thp', '.tivo', '.tix', '.tod',
    '.tp', '.tp0', '.tpd', '.tpr', '.trp', '.ts', '.tsp', '.ttxt', '.tvs',
    '.usf', '.usm', '.vc1', '.vcpf', '.vcr', '.vcv', '.vdo', '.vdr', '.vdx',
    '.veg', '.vem', '.vep', '.vf', '.vft', '.vfw', '.vfz', '.vgz', '.vid',
    '.video', '.viewlet', '.viv', '.vivo', '.vlab', '.vob', '.vp3', '.vp6',
    '.vp7', '.vpj', '.vro', '.vs4', '.vse', '.vsp', '.w32', '.wcp', '.webm',
    '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv', '.wmx', '.wot', '.wp3', '.wpl',
    '.wtv', '.wve', '.wvx', '.xej', '.xel', '.xesc', '.xfl', '.xlmv', '.xmv',
    '.xvid', '.y4m', '.yog', '.yuv', '.zeg', '.zm1', '.zm2', '.zm3', '.zmv'
]


def main():
    file_directory = (r"")
    directories = open("blacklist.txt", "a+")
    transcode_files = []
    blacklist_list = []
    extension = "mkv

    video_files = file_search(file_directory)
    directories = open("blacklist.txt")
    lines = directories.readlines()
    for line in lines:
        blacklist_list.append(line.strip())
    for video in video_files:
        media_info = pymediainfo.MediaInfo.parse(video)
        for track in media_info.tracks:
            if track.track_type == "Video":
                format = str(track.format)
            if not list_check(video, blacklist_list) or format == "HEVC":
                out = video.split(".")
                directories = open("blacklist.txt", "a+")
                directories.write(f"{out[0]+{extension}\n")
                transcode_files.append(video)

    for file in transcode_files:
        out = file.split(".")
        transcode(file, 10000000, out[0], extension, "libx265")
        print(file)


def transcode(file, bitrate, output, type, encoder):
    print("Transcoding ", file)
    stream = ffmpeg.input(file)
    stream = ffmpeg.output(stream,
                           output + " transcoded " + "." + type,
                           video_bitrate=bitrate,
                           vcodec=encoder)
    ffmpeg.run(stream)


# Takes a list and compares users input against it
def list_check(user_input, c_list):
    for item in c_list:
        if item == user_input:
            return True
    return False


def file_search(file_direct):
    files = []
    for x in extensions:
        temp = glob.glob(file_direct + f"/**/*{x}", recursive=True)
        files.extend(temp)
    return files


main()
