#!/usr/bin/env python3
"""
Post-generation hook for iOS Hello World template.
This script validates inputs and sets up the generated project.
"""

import os
import re
import shutil
import json
import sys
from pathlib import Path

# Add scripts directory to path - fix the path resolution
template_dir = Path(__file__).parent.parent
scripts_dir = template_dir / "scripts"
sys.path.insert(0, str(scripts_dir))

try:
    from logger import logger
    from validator import validate_template_inputs
except ImportError:
    # Fallback if scripts are not available
    import logging
    
    # Create a simple logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
    logger = logging.getLogger("iOSTemplate")
    
    def validate_template_inputs(context):
        """Fallback validation function."""
        return True, [], []
    
    print("⚠️  Warning: Using fallback logging and validation")

def replace_in_file(file_path, old_name, new_name):
    """Replace all occurrences of old_name with new_name in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the old name with the new name
        new_content = content.replace(old_name, new_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated {file_path}")
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")

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
            print(f"🔄 Renamed scheme: {scheme_file.name} -> {new_scheme_name}")
            
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
        old_bundle_pattern = r'PRODUCT_BUNDLE_IDENTIFIER = "com\.example\.helloworldapp";'
        new_bundle = f'PRODUCT_BUNDLE_IDENTIFIER = "{organization_identifier}.{new_name.lower()}";'
        
        new_content = re.sub(old_bundle_pattern, new_bundle, content)
        
        # Write back
        with open(pbxproj_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"🔧 Updated bundle identifier to {organization_identifier}.{new_name.lower()}")

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
        
        print(f"📱 Updated minimum iOS version to {minimum_ios_version}")

def cleanup_temp_files(project_dir):
    """Clean up temporary files created during generation."""
    project_path = Path(project_dir)
    temp_file = project_path / "cookiecutter_context.json"
    if temp_file.exists():
        temp_file.unlink()
        print("🧹 Cleaned up temporary files")

def main():
    """Main function to handle post-generation tasks."""
    print("\n" + "="*50)
    print("🚀 iOS Hello World Template Generation")
    print("="*50)
    
    # Get the project directory (current working directory after cookiecutter generation)
    project_dir = os.getcwd()
    
    # Load cookiecutter context
    context_file = Path(project_dir) / "cookiecutter_context.json"
    if context_file.exists():
        print("\n📌 Loading Template Context")
        with open(context_file, 'r') as f:
            context = json.load(f)
        
        project_name = context['project_name']
        app_name = context['app_name']
        organization_identifier = context['organization_identifier']
        minimum_ios_version = context['minimum_ios_version']
        
        print("✅ Template context loaded successfully")
        
        # Validate inputs
        print("\n📌 Validating Template Inputs")
        is_valid, errors, warnings = validate_template_inputs(context)
        
        if not is_valid:
            print("❌ Template validation failed!")
            print("Please fix the errors and regenerate the template.")
            sys.exit(1)
        
        if warnings:
            print("⚠️  Template generated with warnings. Please review:")
            for warning in warnings:
                print(f"  - {warning}")
        
        print("✅ Template validation completed successfully!")
        
    else:
        print("⚠️  Template context file not found, using fallback values")
        project_name = os.path.basename(project_dir)
        app_name = project_name
        organization_identifier = "com.example"
        minimum_ios_version = "15.0"
        context = {}
    
    print(f"Project directory: {project_dir}")
    print(f"Project name: {project_name}")
    
    # Project setup steps
    print("\n📌 Project Setup")
    
    # Step 1: Rename Xcode project references
    print("📋 Step 1/4: Renaming Xcode project references")
    old_name = "HelloWorldApp"  # Original template name
    new_name = project_name
    
    rename_xcode_project_references(project_dir, old_name, new_name)
    
    # Step 2: Update bundle identifier
    print("📋 Step 2/4: Updating bundle identifier")
    update_bundle_identifier(project_dir, new_name, organization_identifier)
    
    # Step 3: Update minimum iOS version
    print("📋 Step 3/4: Updating minimum iOS version")
    update_minimum_ios_version(project_dir, new_name, minimum_ios_version)
    
    # Step 4: Generate requirements file
    print("📋 Step 4/4: Generating requirements file")
    try:
        # Try to import and run version detector
        sys.path.insert(0, str(scripts_dir))
        from version_detector import generate_requirements_md
        requirements_content = generate_requirements_md()
        
        requirements_file = Path(project_dir) / "REQUIREMENTS.md"
        with open(requirements_file, 'w') as f:
            f.write(requirements_content)
        
        print("✅ Requirements file generated: REQUIREMENTS.md")
    except Exception as e:
        print(f"⚠️  Could not generate requirements file: {e}")
    
    # Clean up temporary files
    cleanup_temp_files(project_dir)
    
    # Final success message
    print("\n" + "="*50)
    print("🚀 Generation Complete")
    print("="*50)
    print(f"✅ iOS project '{new_name}' has been successfully generated!")
    
    # Display next steps
    print("\n📌 Next Steps")
    print("1. Open the project in Xcode:")
    print(f"   cd {new_name}")
    print(f"   open {new_name}.xcodeproj")
    
    print("2. Select your target device (simulator or physical device)")
    print("3. Build and run the project (Cmd + R)")
    print("4. Check REQUIREMENTS.md for environment details")
    
    # Display project info
    if context:
        print("\n📌 Project Information")
        print(f"📱 App Name: {context.get('app_name', 'Unknown')}")
        print(f"🔧 Bundle ID: {organization_identifier}.{new_name.lower()}")
        print(f"📱 Minimum iOS Version: {context.get('minimum_ios_version', 'Unknown')}")
        print(f"👨‍💻 Author: {context.get('author_name', 'Unknown')}")
        print(f"📧 Email: {context.get('author_email', 'Unknown')}")
        print(f"🗄️ SwiftData: {context.get('use_swift_data', 'Unknown')}")
    
    print("\n🎉 Happy iOS Development!")

if __name__ == "__main__":
    main() 