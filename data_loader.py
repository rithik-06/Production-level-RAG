from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv

from groq import client

load_dotenv()

client = OpenAI()
reader = PDFReader()