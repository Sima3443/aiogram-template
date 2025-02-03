# Aiogram2 peewee template

- `Aiogram 2`
- `i18n`
- ORM: `Peewee`
- Database: `MongoDB, Redis`

## 📥 How to Install?

### 1. Clone the Repository
First, clone the repository and navigate to its directory:

```bash
git clone https://github.com/devvsima/aiogram2-template.git
cd tgbot
```

### 2. Setting up a virtual environment ".venv"

#### Linux
Install dependencies and activate the virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

#### Windows
Similar steps for Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

> 💡 Note: The name `.venv` can be changed to anything else you wish.

### 3. Setting environment variable

First, copy the `.env.dist` file and rename it to `.env`:

```bash
cp .env.dist .env
```

Then edit the environment variables file:

```bash
vim .env
# or
nano .env
```

### 4. Bot settings

#### `ADMINS` - Admin IDs
Add admin IDs, separating them with commas

```bash
# example
ADMINS=12345678,12345677,12345676
```

#### `TOKEN` - Bot token from [@BotFather](https://t.me/BotFather)
Add your bot token:

```bash
# example
BOT_TOKEN=123452345243:Asdfasdfasf
```

### 5. Configuring the PostgreSQL database

Set the database connection parameters:

- `DB_NAME` - database name
- `DB_HOST` - database host (default = 'localhost')
- `DB_PORT` - database port (default = `5432`)
- `DB_USER` - database user
- `DB_PASS` - database password

### 6. Configuring Redis

Redis is used for caching and storing session data. Set up the Redis connection parameters in the `.env` file:

- `REDIS_HOST` - Redis server host (default: `localhost`)
- `REDIS_PORT` - Redis server port (default: `6379`)
- `REDIS_DB` - Redis database index (default: `5`)
- `REDIS_URL` - Redis connection URL (optional)

Example:
```bash
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=5
```

Ensure that Redis is installed and running before launching the bot. You can start Redis with:
```bash
redis-server
```

---

Now the bot is ready to run! 🎉
