# Django Permission and Group Management

## Overview
This project demonstrates how to implement permissions and groups in Django. It includes:
- Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)
- User groups (`Viewers`, `Editors`, `Admins`)
- Views protected with `@permission_required`

## Setup Instructions

### 1. Migrate and Create Superuser
Run:
```sh
python manage.py migrate
python manage.py createsuperuser
