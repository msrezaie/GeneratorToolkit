import yt_dlp

from django.http import HttpResponse
from django.views.generic import TemplateView


class YouTubeToMpeg(TemplateView):
    template_name = 'ytompeg/index.html'

    def post(self, request, *args, **kwargs):
        youtube_url = request.POST.get('url')
        output_format = request.POST.get('format')
        ydl_opts = {
            'format': 'bestaudio' if output_format == 'mp3' else 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'verbose': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=False)
            if output_format == 'mp3':
                filename = f"{info_dict['id']}.mp3"
                download_url = info_dict['formats'][0]['url']  # Assuming the first format is the best audio
            else:
                filename = f"{info_dict['id']}.mp4"
                download_url = info_dict['formats'][0]['url']  # Assuming the first format is the best video+audio
            response = HttpResponse()
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            response['X-Accel-Redirect'] = download_url  # Use nginx's X-Accel-Redirect to redirect to the download link
            return response