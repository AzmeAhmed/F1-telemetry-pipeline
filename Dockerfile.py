# ==========================================
# STAGE 1: Builder (Install & build packages)
# ==========================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system dependencies required for building certain data packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages to user local directory
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# ==========================================
# STAGE 2: Final (Slim & secure runtime env)
# ==========================================
FROM python:3.11-slim AS final

WORKDIR /app

# Create a secure non-root system user for production best practices
RUN useradd -m -u 8888 appuser && chown -R appuser:appuser /app
USER appuser

# Copy installed Python packages from the builder stage
COPY --from=builder /root/.local /home/appuser/.local
COPY --from=builder /app/requirements.txt .

# Update PATH environment variable so Linux can find the packages and pytest
ENV PATH=/home/appuser/.local/bin:$PATH

# Environment variable to configure FastF1 caching inside the container
ENV FASTF1_CACHE_DIR=/home/appuser/.fastf1_cache

# Copy the entire project repository into the container
COPY . .

# Ensure the output directory exists and is writable by appuser
RUN mkdir -p src/output

# Command to execute the main application entry point
CMD ["python", "src/main.py"]
