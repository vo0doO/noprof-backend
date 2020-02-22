#!/usr/bin/env python
"""
#####################################: TODO(Проект)(vo0doo) :#################################################
# 1. Создать модель стартовой страницы под шаблон kirsanov.com                                              ##
# 2. Создать модели для блога програмиста(теги, темы, индескы, список постов, страница поста)               ##
# 3. Клиент на эти модели ----> он в папке проектов js                                                      ##
# 4. Любопытство - новости, модели(см. п. 2 + миграция парсера из устаревшей программы)                     ##
##############################################################################################################
"""

import os
import sys

# import dotenv


if __name__ == "__main__":
    # dotenv.read_dotenv()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings.base")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
