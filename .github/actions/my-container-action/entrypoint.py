#!/usr/bin/env python3
import sys
import os
from datetime import datetime

# Nhận positional args từ ENTRYPOINT ($1 = sys.argv[1])
if len(sys.argv) > 1:
    message = sys.argv[1]
    print(f"Hello {message} from Container Action!")
else:
    message = "Default Hello!"
    print("No message provided, using default.")

# Set output cho GitHub Actions (dùng ở workflow cha)
if 'GITHUB_OUTPUT' in os.environ:
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f"greeting={message}\n")
        f.write(f"timestamp={datetime.now().isoformat()}\n")

# Exit thành công (0 = pass workflow)
sys.exit(0)