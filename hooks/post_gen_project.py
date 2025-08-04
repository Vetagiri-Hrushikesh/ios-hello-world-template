#!/usr/bin/env python3
"""
Post-generation hook for iOS Hello World template.
This script renames all Xcode project references from the template name to the actual project name.
"""

import os
import re
import shutil
import json
from pathlib import Path

def replace_in_file(file_path, old_name, new_name):
    """Replace all occurrences of old_name with new_name in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the old name with the new name
        new_content = content.replace(old_name, new_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

def rename_xcode_project_references(project_dir, old_name, new_name):
    """Rename all Xcode project references."""
    project_path = Path(project_dir)
    
    # List of files that typically contain project references
    files_to_update = [
        f"{new_name}.xcodeproj/project.pbxproj",
        f"{new_name}.xcodeproj/project.xcworkspace/contents.xcworkspacedata",
    ]
    
    # Update each file
    for file_path in files_to_update:
        full_path = project_path / file_path
        if full_path.exists():
            replace_in_file(full_path, old_name, new_name)
    
    # Handle scheme files
    schemes_dir = project_path / f"{new_name}.xcodeproj/xcshareddata/xcschemes"
    if schemes_dir.exists():
        for scheme_file in schemes_dir.glob(f"{old_name}*.xcscheme"):
            new_scheme_name = scheme_file.name.replace(old_name, new_name)
            new_scheme_path = schemes_dir / new_scheme_name
            shutil.move(scheme_file, new_scheme_path)
            print(f"Renamed scheme: {scheme_file.name} -> {new_scheme_name}")
            
            # Update the scheme file content
            replace_in_file(new_scheme_path, old_name, new_name)

def update_bundle_identifier(project_dir, new_name, organization_identifier):
    """Update bundle identifier in project.pbxproj."""
    project_path = Path(project_dir)
    pbxproj_path = project_path / f"{new_name}.xcodeproj/project.pbxproj"
    
    if pbxproj_path.exists():
        # Read the file
        with open(pbxproj_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update bundle identifier pattern
        old_bundle_pattern = r'PRODUCT_BUNDLE_IDENTIFIER = "com\.example";'
        new_bundle = f'PRODUCT_BUNDLE_IDENTIFIER = "{organization_identifier}.{new_name}";'
        
        new_content = re.sub(old_bundle_pattern, new_bundle, content)
        
        # Write back
        with open(pbxproj_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated bundle identifier to {organization_identifier}.{new_name}")

def update_minimum_ios_version(project_dir, new_name, minimum_ios_version):
    """Update minimum iOS version in project.pbxproj."""
    project_path = Path(project_dir)
    pbxproj_path = project_path / f"{new_name}.xcodeproj/project.pbxproj"
    
    if pbxproj_path.exists():
        # Read the file
        with open(pbxproj_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update IPHONEOS_DEPLOYMENT_TARGET
        old_version_pattern = r'IPHONEOS_DEPLOYMENT_TARGET = \d+\.\d+;'
        new_version = f'IPHONEOS_DEPLOYMENT_TARGET = {minimum_ios_version};'
        
        new_content = re.sub(old_version_pattern, new_version, content)
        
        # Write back
        with open(pbxproj_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated minimum iOS version to {minimum_ios_version}")

def cleanup_temp_files(project_dir):
    """Clean up temporary files created during generation."""
    project_path = Path(project_dir)
    temp_file = project_path / "cookiecutter_context.json"
    if temp_file.exists():
        temp_file.unlink()
        print("Cleaned up temporary files")

def main():
    """Main function to handle post-generation tasks."""
    # Get the project directory (current working directory after cookiecutter generation)
    project_dir = os.getcwd()
    
    # Load cookiecutter context
    context_file = Path(project_dir) / "cookiecutter_context.json"
    if context_file.exists():
        with open(context_file, 'r') as f:
            context = json.load(f)
        
        project_name = context['project_name']
        organization_identifier = context['organization_identifier']
        minimum_ios_version = context['minimum_ios_version']
    else:
        # Fallback to directory name if context file doesn't exist
        project_name = os.path.basename(project_dir)
        organization_identifier = "com.example"
        minimum_ios_version = "15.0"
    
    old_name = "HelloWorldApp"  # Original template name
    new_name = project_name
    
    print(f"Post-generation: Renaming Xcode project references from '{old_name}' to '{new_name}'")
    
    # Rename Xcode project references
    rename_xcode_project_references(project_dir, old_name, new_name)
    
    # Update bundle identifier
    update_bundle_identifier(project_dir, new_name, organization_identifier)
    
    # Update minimum iOS version
    update_minimum_ios_version(project_dir, new_name, minimum_ios_version)
    
    # Clean up temporary files
    cleanup_temp_files(project_dir)
    
    print(f"✅ iOS project '{new_name}' has been successfully generated!")
    print(f"📱 Open {new_name}.xcodeproj in Xcode to start developing")
    print(f"🔧 Bundle ID: {organization_identifier}.{new_name}")
    print(f"📱 Minimum iOS Version: {minimum_ios_version}")

if __name__ == "__main__":
    main() 