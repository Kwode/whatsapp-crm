from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv(override=True)

database_url = os.getenv("DATABASE_URL")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_API")

supabase: Client = create_client(
    supabase_url=supabase_url,
    supabase_key=supabase_key
)

engine = create_engine(database_url)

session = sessionmaker(autoflush=False, autocommit = False, bind=engine)

print(supabase_key)
print(supabase_url)
print(database_url)


