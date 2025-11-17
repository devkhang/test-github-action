# Base image nhẹ (Alpine Linux 3.18 – kích thước ~5MB)
FROM alpine:3.18

# Cài Python 3 (cần cho entrypoint.py)
RUN apk add --no-cache python3

# Copy script chính vào container
COPY entrypoint.py /entrypoint.py

# Làm executable (bắt buộc để ENTRYPOINT chạy)
RUN chmod +x /entrypoint.py

# Định nghĩa entrypoint – chạy Python script đầu tiên
ENTRYPOINT ["/entrypoint.py"]