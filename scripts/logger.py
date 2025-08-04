#!/usr/bin/env python3
"""
Professional logging utility for iOS Hello World template.
Provides structured logging with different levels and formatting.
"""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

class TemplateLogger:
    """Professional logger for template operations."""
    
    def __init__(self, log_file: Optional[str] = None, level: str = "INFO"):
        """Initialize the logger."""
        self.logger = logging.getLogger("iOSTemplate")
        self.logger.setLevel(getattr(logging, level.upper()))
        
        # Create formatters
        console_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%H:%M:%S'
        )
        
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # File handler (optional)
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(file_formatter)
            self.logger.addHandler(file_handler)
    
    def info(self, message: str):
        """Log info message."""
        self.logger.info(f"ℹ️  {message}")
    
    def success(self, message: str):
        """Log success message."""
        self.logger.info(f"✅ {message}")
    
    def warning(self, message: str):
        """Log warning message."""
        self.logger.warning(f"⚠️  {message}")
    
    def error(self, message: str):
        """Log error message."""
        self.logger.error(f"❌ {message}")
    
    def debug(self, message: str):
        """Log debug message."""
        self.logger.debug(f"🔍 {message}")
    
    def step(self, step_number: int, total_steps: int, message: str):
        """Log a step in a process."""
        self.logger.info(f"📋 Step {step_number}/{total_steps}: {message}")
    
    def section(self, title: str):
        """Log a section header."""
        self.logger.info(f"\n{'='*50}")
        self.logger.info(f"🚀 {title}")
        self.logger.info(f"{'='*50}")
    
    def subsection(self, title: str):
        """Log a subsection header."""
        self.logger.info(f"\n📌 {title}")
        self.logger.info(f"{'-'*30}")

def create_logger(log_file: Optional[str] = None) -> TemplateLogger:
    """Create and return a template logger instance."""
    return TemplateLogger(log_file)

# Global logger instance
logger = create_logger() 