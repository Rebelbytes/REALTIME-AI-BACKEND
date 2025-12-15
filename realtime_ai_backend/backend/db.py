from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = "https://infwwbmzwdbipgxfqkde.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImluZnd3Ym16d2RiaXBneGZxa2RlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjU3OTgyNDEsImV4cCI6MjA4MTM3NDI0MX0.r0-mQZptXdPxV92gMjIwpe6-Y0IB9kgaLN6l0Y783rY"

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase URL and Key must be set")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
