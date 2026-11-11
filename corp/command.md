docker compose up -d
export DATABASE_URL="postgresql://litellm:pw@localhost:5432/litellm"


prisma generate --schema="$(python -c "import litellm, os; print(os.path.join(os.path.dirname(litellm.__file__), 'proxy', 'schema.prisma'))")"

sk-pc0WLFep6d_uV3rsqX9krA