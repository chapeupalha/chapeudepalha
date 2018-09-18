from random import randint
import os
import datetime


def update_filename(instance, filename):
    file_type = filename.rsplit('.', 1)[1]
    new_name = str(instance.participante.id) + "_" + str(instance.tipo_documento.nome_bd) + "." + str(file_type)

    day = datetime.datetime.now()
    path = "zz_99_media/documento_participante/%s/%s/%s/%s" % (day.year, day.strftime('%m'), day.strftime('%d'), instance.participante.id)

    return os.path.join(path, new_name)
