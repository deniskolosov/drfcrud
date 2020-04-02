## Usage
## Setup
1. Create an environment configuration file (.env) with the following contents:
```
DJANGO_ALLOWED_HOSTS=*
DJANGO_SECRET_KEY=local
```

2. Run the project:
```bash
docker-compose up
```

3. Create app:
```bash
curl --data "name=mynewapp" http://127.0.0.1:8000/api/apps/
```

4. Create api key
```bash
cd drfcrud/
docker-compose run --rm web ./manage.py shell
from api.apps.models import AppModel
AppModel.objects.get(id=1).create_api_key()
print(AppModel.objects.get(id=1).api_key)
```

5. Check app is found by api key
```bash
curl http://127.0.0.1:8000/api/test/<api_key>
```
