from django.http import JsonResponse
from .models import AboutBlock

def about_blocks_api(request):
    blocks = AboutBlock.objects.all()
    data = {
        "blocks": [
            {
                "title": block.title,
                "content": block.content,
            } for block in blocks
        ]
    }
    return JsonResponse(data)
