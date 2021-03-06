# -*- coding: utf-8 -*-

import os
import shutil
import urllib2
from django.contrib.auth.models import Group
from django.test.client import Client
import simplejson
from settings.common import BUCKET_URL, MEDIA_TEST, MEDIA_ROOT


def saved_only_one_instance_ok(instance_class):
    "Comprueba si se ha guardado una sola instancia para esa clase en BD"
    instances = instance_class.objects.all()
    return len(instances) == 1 and instances[0].id is not None


def saved_a_few_instances_ok(instance_class):
    "Comprueba si se ha guardado una sola instancia para esa clase en BD"
    instances = instance_class.objects.all()
    return len(instances) > 1 and instances[1].id is not None


def content_type_ok_ext(resp, content_type):
    """
    Muestra el tipo de contenido de una respuesta que viene desde
    un servidor externo (usando urllib)

    # image/png
    # audio/x-caf

    http://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string
    """
    return resp.code == 200 and \
           len([s for s in resp.headers.headers if "Content-Type: " + content_type in s]) != 0


# client = TestApiClient()
client = Client()

def get_file_from_bucket(file_id):
    return urllib2.urlopen(BUCKET_URL + file_id)


def check_from_bucket(file_id_list, check_removed=False):
    """
    Comprueba que los archivos indicados estén en el bucket (check_removed=False),
    o bien que no estén ya ahí (check_removed=True)
    """
    total_requested_files = len(file_id_list)
    # num de archivos correcta e incorrectamente recibidos desde el bucket
    ok_received_files = 0
    failed_received_files = 0
    for file_id in file_id_list:
        try:
            resp = get_file_from_bucket(file_id)
            if '.png' in file_id or '.jpg' in file_id:
                assert content_type_ok_ext(resp, 'image/')
            elif '.mp3' in file_id:
                assert content_type_ok_ext(resp, 'audio/mpeg')
            ok_received_files += 1
        except Exception as ex:
            failed_received_files += 1

    if check_removed:
        assert failed_received_files == total_requested_files
    elif not check_removed:
        assert ok_received_files == total_requested_files


def reset_media_test_folder():
    if os.path.exists(MEDIA_TEST):
        shutil.rmtree(MEDIA_TEST)
    else:
        if not os.path.exists(MEDIA_ROOT):
            os.mkdir(MEDIA_ROOT)
        os.mkdir(MEDIA_TEST)

def reset_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(folder_path)


def init_database():
    Group.objects.create(name='enclosure_owners')
    Group.objects.create(name='shop_owners')

