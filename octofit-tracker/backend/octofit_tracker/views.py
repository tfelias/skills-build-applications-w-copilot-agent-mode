from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit Tracker API!",
        "documentation_url": "https://[upgraded-zebra-rvxvrpgjp5r3pxxr]-8000.app.github.dev/docs"
    })