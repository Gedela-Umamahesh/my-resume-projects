#!/bin/bash

# ==========================================
# DevOps Automated Backup Script
# Author: Gedela Umamahesh
# ==========================================

# Configuration
BACKUP_DIR="/c/Users/gedel/OneDrive/Desktop/my_resume_projects/backups"
SOURCE_DIR="/c/Users/gedel/OneDrive/Desktop/my_resume_projects/portfolio-app"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_NAME="portfolio_backup_$TIMESTAMP.tar.gz"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo "=========================================="
echo "Starting Backup Process at $(date)"
echo "=========================================="

# Compress source folder into backup destination
tar -czf "$BACKUP_DIR/$BACKUP_NAME" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")"

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "[SUCCESS] Backup completed successfully!"
    echo "[INFO] Archive saved at: $BACKUP_DIR/$BACKUP_NAME"
else
    echo "[ERROR] Backup failed!" >&2
    exit 1
fi

echo "=========================================="