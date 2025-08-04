"""
iOS Hello World Template Scripts Package
"""

from .logger import logger, create_logger
from .validator import validate_template_inputs, iOSTemplateValidator

__all__ = ['logger', 'create_logger', 'validate_template_inputs', 'iOSTemplateValidator'] 