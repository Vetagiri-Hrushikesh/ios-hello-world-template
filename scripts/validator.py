#!/usr/bin/env python3
"""
Validation system for iOS Hello World template.
Validates user inputs and environment requirements.
"""

import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from .logger import logger

class iOSTemplateValidator:
    """Validator for iOS template inputs and environment."""
    
    def __init__(self):
        """Initialize the validator."""
        self.errors = []
        self.warnings = []
    
    def validate_project_name(self, name: str) -> bool:
        """Validate project name."""
        if not name:
            self.errors.append("Project name cannot be empty")
            return False
        
        if not re.match(r'^[A-Za-z][A-Za-z0-9_]*$', name):
            self.errors.append("Project name must start with a letter and contain only letters, numbers, and underscores")
            return False
        
        if len(name) > 50:
            self.errors.append("Project name must be 50 characters or less")
            return False
        
        # Check for reserved words
        reserved_words = ['ios', 'swift', 'xcode', 'cocoa', 'app', 'test', 'main']
        if name.lower() in reserved_words:
            self.warnings.append(f"Project name '{name}' might conflict with iOS reserved words")
        
        return True
    
    def validate_organization_identifier(self, org_id: str) -> bool:
        """Validate organization identifier."""
        if not org_id:
            self.errors.append("Organization identifier cannot be empty")
            return False
        
        # iOS bundle identifier rules
        if not re.match(r'^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)*$', org_id):
            self.errors.append("Organization identifier must follow iOS bundle naming conventions (e.g., com.example)")
            return False
        
        if len(org_id) > 100:
            self.errors.append("Organization identifier must be 100 characters or less")
            return False
        
        return True
    
    def validate_ios_version(self, version: str) -> bool:
        """Validate iOS version."""
        if not version:
            self.errors.append("iOS version cannot be empty")
            return False
        
        # iOS version pattern (e.g., 15.0, 16.1, 17.0)
        version_pattern = r'^\d+\.\d+$'
        if not re.match(version_pattern, version):
            self.errors.append("iOS version must be in format X.Y (e.g., 15.0)")
            return False
        
        try:
            major, minor = map(int, version.split('.'))
            if major < 13 or major > 18:
                self.warnings.append("iOS version should be between 13.0 and 18.0 for best compatibility")
        except ValueError:
            self.errors.append("Invalid iOS version format")
            return False
        
        return True
    
    def validate_email(self, email: str) -> bool:
        """Validate email address."""
        if not email:
            self.warnings.append("Email address is empty (optional but recommended)")
            return True
        
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            self.errors.append("Invalid email address format")
            return False
        
        return True
    
    def validate_version_name(self, version: str) -> bool:
        """Validate version name (semantic versioning)."""
        if not version:
            self.errors.append("Version name cannot be empty")
            return False
        
        # Semantic versioning pattern
        semver_pattern = r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?(\+[a-zA-Z0-9.-]+)?$'
        if not re.match(semver_pattern, version):
            self.warnings.append("Version name should follow semantic versioning (e.g., 1.0.0)")
        
        return True
    
    def validate_swift_data_choice(self, choice: str) -> bool:
        """Validate SwiftData choice."""
        if choice.lower() not in ['true', 'false']:
            self.errors.append("SwiftData choice must be 'true' or 'false'")
            return False
        
        return True
    
    def validate_environment(self) -> bool:
        """Validate development environment."""
        logger.subsection("Environment Validation")
        
        # Check Xcode
        try:
            result = subprocess.run(['xcodebuild', '-version'], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                # Extract version
                import re
                match = re.search(r'Xcode ([^\s]+)', result.stdout)
                if match:
                    version = match.group(1)
                    logger.success(f"Xcode {version} is installed")
                    
                    # Check if version is recent enough
                    try:
                        version_num = float(version)
                        if version_num < 15.0:
                            self.warnings.append(f"Xcode {version} is older than recommended (15.0+)")
                    except ValueError:
                        pass
                else:
                    logger.success("Xcode is installed")
            else:
                self.errors.append("Xcode is not properly installed")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.errors.append("Xcode is not installed")
        
        # Check iOS Simulator
        simulator_path = Path("/Applications/Xcode.app/Contents/Developer/Applications/Simulator.app")
        if simulator_path.exists():
            logger.success("iOS Simulator is available")
        else:
            self.warnings.append("iOS Simulator not found")
        
        # Check macOS version
        try:
            result = subprocess.run(['sw_vers', '-productVersion'], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                macos_version = result.stdout.strip()
                logger.success(f"macOS {macos_version} detected")
                
                # Check if macOS is recent enough
                try:
                    major_version = int(macos_version.split('.')[0])
                    if major_version < 13:
                        self.warnings.append(f"macOS {macos_version} is older than recommended (13.0+)")
                except (ValueError, IndexError):
                    pass
            else:
                self.warnings.append("Could not determine macOS version")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.warnings.append("Could not check macOS version")
        
        # Check Homebrew (optional but recommended)
        try:
            result = subprocess.run(['brew', '--version'], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                logger.success("Homebrew is installed")
            else:
                self.warnings.append("Homebrew is not installed (recommended for package management)")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.warnings.append("Homebrew is not installed (recommended for package management)")
        
        # Check CocoaPods (optional)
        try:
            result = subprocess.run(['pod', '--version'], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                logger.success("CocoaPods is installed")
            else:
                self.warnings.append("CocoaPods is not installed (optional dependency manager)")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.warnings.append("CocoaPods is not installed (optional dependency manager)")
        
        return len(self.errors) == 0
    
    def validate_all(self, context: Dict[str, str]) -> Tuple[bool, List[str], List[str]]:
        """Validate all template inputs."""
        logger.section("Template Validation")
        
        # Validate required fields
        required_fields = {
            'project_name': self.validate_project_name,
            'organization_identifier': self.validate_organization_identifier,
            'minimum_ios_version': self.validate_ios_version,
            'version_name': self.validate_version_name,
            'use_swift_data': self.validate_swift_data_choice,
        }
        
        for field, validator in required_fields.items():
            if field in context:
                if not validator(context[field]):
                    logger.error(f"Validation failed for {field}: {context[field]}")
            else:
                self.errors.append(f"Required field '{field}' is missing")
        
        # Validate optional fields
        if 'author_email' in context:
            self.validate_email(context['author_email'])
        
        # Validate environment
        self.validate_environment()
        
        # Log results
        if self.errors:
            logger.error(f"Found {len(self.errors)} validation errors")
            for error in self.errors:
                logger.error(f"  - {error}")
        
        if self.warnings:
            logger.warning(f"Found {len(self.warnings)} warnings")
            for warning in self.warnings:
                logger.warning(f"  - {warning}")
        
        if not self.errors and not self.warnings:
            logger.success("All validations passed successfully!")
        
        return len(self.errors) == 0, self.errors, self.warnings

def validate_template_inputs(context: Dict[str, str]) -> Tuple[bool, List[str], List[str]]:
    """Validate template inputs and return results."""
    validator = iOSTemplateValidator()
    return validator.validate_all(context) 