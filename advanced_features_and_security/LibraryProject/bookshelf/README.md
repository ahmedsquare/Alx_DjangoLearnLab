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


# Security Measures in LibraryProject

1. **CSRF Protection**: All forms use Django’s CSRF token.
2. **XSS Prevention**: CSP headers restrict script sources.
3. **SQL Injection Prevention**: User inputs are sanitized and validated.
4. **Secure Settings**: DEBUG=False, HTTPS enforced, and secure cookies enabled.

Test cases:
- Unauthorized access should be blocked.
- Malicious scripts should be blocked by CSP.
- SQL injection attempts should not return database errors.