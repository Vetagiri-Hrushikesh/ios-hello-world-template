#!/usr/bin/env python3
"""
Pre-generation hook for iOS Hello World template.
This script stores cookiecutter variables for use in post-generation.
"""

import json
import os

def main():
    """Store cookiecutter context for post-generation use."""
    # Get cookiecutter context
    context = {
        'project_name': '{{cookiecutter.project_name}}',
        'app_name': '{{cookiecutter.app_name}}',
        'organization_identifier': '{{cookiecutter.organization_identifier}}',
        'author_name': '{{cookiecutter.author_name}}',
        'author_email': '{{cookiecutter.author_email}}',
        'minimum_ios_version': '{{cookiecutter.minimum_ios_version}}',
        'version_name': '{{cookiecutter.version_name}}',
        'use_swift_data': '{{cookiecutter.use_swift_data}}'
    }
    
    # Store context in a temporary file
    with open('cookiecutter_context.json', 'w') as f:
        json.dump(context, f)

if __name__ == "__main__":
    main() 