from django.db import models

import bugsnag

# Create your models here.

bugsnag.notify(Exception("Test Error"))
