DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config["database"]["name"],
        "USER": config["database"]["user"],
        "PASSWORD": config["database"]["password"],
        "HOST": config["database"]["host"],
        "PORT": config["database"]["port"],
    }
}
