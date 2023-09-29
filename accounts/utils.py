import pandas as pd
import os
from django.conf import settings
from django.shortcuts import redirect
from adminconfig.models import Xl_download_config
import datetime
from django.contrib.contenttypes.models import ContentType
def Download(modeladmin, request, queryset):
    return Model_download(queryset)
class actions():
    actions = [Download]

def Model_download(queryset):
    model=ContentType.objects.get_for_model(queryset.first()).model
    try:
        obj = Xl_download_config.objects.get(model=model)
    except Xl_download_config.DoesNotExist as e:
        print(e)
        obj = Xl_download_config.objects.create(model=model)
    finally:
        if obj.array == '':
            array = [i.name for i in queryset.first()._meta.get_fields()]
            obj.array = ','.join(array)
            obj.save()
        else:
            array = obj.array.split(',')
    data = queryset.values(*array)
    for df in data:
        for i in df:
            if type(df[i]) == datetime.datetime:
                df[i] = df[i].replace(tzinfo=None)
    panda_obj = pd.DataFrame(data)
    panda_obj.to_excel(os.path.join(settings.MEDIA_ROOT, f'{model}.xlsx'))
    return redirect(f'/media/{model}.xlsx')