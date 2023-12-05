from .models import Profile  # Import your Profile model

def profile_context(request):
    profile = None

    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass

    return {'profile': profile}
