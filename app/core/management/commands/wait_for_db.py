"""
Django commands to wait for database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for Database"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("Waiting for Database...")
        db_up = False
        while not db_up:  # equal with: db_up is False
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(
                    "Database's unavailable, please wait for 1 second..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database's available!"))
