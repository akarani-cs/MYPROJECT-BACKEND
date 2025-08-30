# Movie Review API (Django + DRF)

A minimal, production-ready starter for a Movie Review API with JWT auth, search, filtering, pagination, and deploy configs.

## Quickstart

```bash
# 1) Create & activate a virtual environment (recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate

# 2) Install deps
pip install -r requirements.txt

# 3) DB setup
python manage.py makemigrations
python manage.py migrate

# 4) Create admin user (optional but useful)
python manage.py createsuperuser

# 5) Run
python manage.py runserver
```

## Endpoints

- `POST /api/auth/register/` — Create a user
- `POST /api/auth/token/` — Obtain JWT (username + password)
- `POST /api/auth/token/refresh/` — Refresh JWT
- `GET /api/users/` — List users (admin only)
- `GET/PATCH /api/users/me/` — Get/Update your profile
- `GET /api/users/{id}/` — Retrieve a user (self or admin)
- `PUT/PATCH/DELETE /api/users/{id}/` — Update/Delete (self or admin)

- `GET /api/reviews/` — List reviews (search, filter, order, paginate)
  - Search: `?search=Inception`
  - Filter: `?rating=5`
  - Order: `?ordering=-created_at` or `?ordering=rating`
- `POST /api/reviews/` — Create (auth required)
- `GET /api/reviews/{id}/` — Retrieve
- `PUT/PATCH /api/reviews/{id}/` — Update (owner only)
- `DELETE /api/reviews/{id}/` — Delete (owner only)
- `GET /api/reviews/by-movie/?title=Inception` — Reviews for a movie (paginated)

## Notes
- Replace the `SECRET_KEY` in `movie_review_api/settings.py` for production.
- Default permissions allow read by anyone, write by authenticated users; object edits only by owner.
- Pagination = 10 per page by default.
- Sorting available on `rating` and `created_at`.
- Uses SQLite by default; switch to Postgres for production.

## Deploy

### PythonAnywhere (quick)
1. Push this project to GitHub or upload the ZIP.
2. On PythonAnywhere, create a new **Django** web app (Manual config).
3. In the **Virtualenv** section, create/point to a new venv and install deps:
   ```bash
   pip install -r /path/to/requirements.txt
   ```
4. In the **WSGI config file**, point `path` to the project folder and set `os.environ['DJANGO_SETTINGS_MODULE'] = 'movie_review_api.settings'`.
5. Set `ALLOWED_HOSTS` to your PythonAnywhere domain (or `*` for quick test).
6. Run `python manage.py collectstatic` (optional for API).
7. Reload the web app.

### Heroku
1. Ensure you have the Heroku CLI installed and are logged in.
2. Create app and Postgres addon:
   ```bash
   heroku create movie-review-api-demo
   heroku addons:create heroku-postgresql:mini
   ```
3. Push code:
   ```bash
   git init
   heroku git:remote -a movie-review-api-demo
   git add . && git commit -m "Initial"
   git push heroku HEAD:main
   ```
4. Set env vars:
   ```bash
   heroku config:set DJANGO_SECRET_KEY=replace_me DJANGO_DEBUG=0 ALLOWED_HOSTS=<your-heroku-app>.herokuapp.com
   ```
5. Run migrations:
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```
6. Open app and test `/api/` endpoints.
