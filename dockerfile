FROM alpine:3.18
RUN apk add --no-cache python3 py3-pip  # ← Cài Python (nếu cần thư viện)
COPY entrypoint.py /entrypoint.py
RUN chmod +x /entrypoint.py  # ← Làm executable
ENTRYPOINT ["/entrypoint.py"]  # ← Thay shell bằng Python