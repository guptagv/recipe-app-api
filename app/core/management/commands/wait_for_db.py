"""
Django Command to wait for DB to be available
"""

import time
from psycopg2 import OperationalError as Psycopg2opError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for DB"""
    def handle(self, *args, **options):
        """Entry point to command"""
        self.stdout.write('Waiting for the database.....')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2opError, OperationalError):
                self.stdout.write('Database Unavailable, waiting 1 sec....')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available'))
