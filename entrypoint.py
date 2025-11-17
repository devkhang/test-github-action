#!/usr/bin/env python3
import sys
import os

# Nhận args từ ENTRYPOINT ($1 = sys.argv[1])
if len(sys.argv) > 1:
    message = sys.argv[1]
    print(f"Hello {message}!")
else:
    print("No message provided!")

# Set output cho GitHub Actions (tương tự >> $GITHUB_OUTPUT)
if 'GITHUB_OUTPUT' in os.environ:
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        f.write(f"greeting={message}\n")