#!/usr/bin/env python3
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[1] / 'src'
os.chdir(ROOT)
ThreadingHTTPServer(('127.0.0.1', 4173), SimpleHTTPRequestHandler).serve_forever()
