from rest_framework_simplejwt.tokens import RefreshTokendef create_user_token(user):    refresh_token = RefreshToken().for_user(user)    access_token = refresh_token.token    return {        'access_token': access_token,        'refresh_token': refresh_token    }