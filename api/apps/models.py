import uuid

from django.db import models, IntegrityError


class AppModel(models.Model):
    name = models.CharField(db_index=True, max_length=255)
    api_key = models.UUIDField(editable=False, null=True, unique=True)

    def create_api_key(self):
        while True:
            try:
                key = uuid.uuid4()
                self.api_key = key
                self.save()
            except IntegrityError as e:
                if "duplicate" in e.message:
                    continue
            break
