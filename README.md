# iOS Hello World Template

A cookiecutter template for creating iOS Hello World applications using SwiftUI.

## Features

- Modern SwiftUI-based iOS app
- Clean project structure
- Unit tests setup
- UI tests setup
- Proper Xcode project configuration
- Ready-to-run Hello World application
- **Automatic Xcode project renaming and configuration**
- **Customizable bundle identifier and iOS version**

## Usage

1. Install cookiecutter if you haven't already:
   ```bash
   pip install cookiecutter
   ```

2. Generate a new iOS project:
   ```bash
   cookiecutter ios-hello-world-template
   ```

3. Follow the prompts to customize your project:
   - `project_name`: Name of your iOS app
   - `project_description`: Description of your app
   - `author_name`: Your name
   - `author_email`: Your email
   - `organization_identifier`: Your organization identifier (e.g., com.yourcompany)
   - `minimum_ios_version`: Minimum iOS version (default: 15.0)

4. The template will automatically:
   - Rename all Xcode project references
   - Update bundle identifiers
   - Configure minimum iOS version
   - Set up proper scheme names

5. Open the generated Xcode project and run it on the simulator or device.

## Project Structure

```
{{cookiecutter.project_name}}/
├── {{cookiecutter.project_name}}.xcodeproj/
├── {{cookiecutter.project_name}}/
│   ├── {{cookiecutter.project_name}}App.swift
│   ├── ContentView.swift
│   └── Assets.xcassets/
├── {{cookiecutter.project_name}}Tests/
│   └── {{cookiecutter.project_name}}Tests.swift
└── {{cookiecutter.project_name}}UITests/
    ├── {{cookiecutter.project_name}}UITests.swift
    └── {{cookiecutter.project_name}}UITestsLaunchTests.swift
```

## Automatic Configuration

This template includes post-generation hooks that automatically:

- ✅ Rename all Xcode project references from template names to your project name
- ✅ Update bundle identifiers to use your organization identifier
- ✅ Configure minimum iOS deployment target
- ✅ Rename and update Xcode schemes
- ✅ Clean up temporary files

## Requirements

- Xcode 15.0 or later
- iOS 15.0 or later
- Swift 5.9 or later
- Python 3.6+ (for cookiecutter)

## License

This template is provided as-is for educational and development purposes. 