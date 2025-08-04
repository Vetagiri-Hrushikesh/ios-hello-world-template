# iOS Hello World Template

A professional, production-ready cookiecutter template for creating iOS Hello World applications using modern SwiftUI development practices.

## 🚀 Features

- **Modern iOS Development**: Swift + SwiftUI
- **Clean Architecture**: Well-structured project layout
- **Professional Setup**: Optimized Xcode project configuration
- **Smart Variables**: Only essential, used variables (9 total)
- **Auto-Configuration**: Automatic project setup and naming
- **Testing Ready**: Unit tests and UI tests included
- **SwiftUI Best Practices**: Modern UI development patterns

## 📋 Requirements

Run the version detection script to check your environment:

```bash
python scripts/version_detector.py > requirements.md
```

### Minimum Requirements
- **Xcode**: 15.0 or higher
- **Swift**: 5.9 or higher
- **macOS**: 13.0 (Ventura) or higher
- **iOS Deployment Target**: 15.0 or higher

## 🛠️ Installation

### 1. Install Cookiecutter
```bash
pip install cookiecutter
```

### 2. Generate Project
```bash
# From GitHub
cookiecutter https://github.com/Vetagiri-Hrushikesh/ios-hello-world-template.git

# Or from local directory
cookiecutter ios-hello-world-template
```

### 3. Follow the Prompts
The template will ask for 9 essential configuration values:

| Category | Variables | Description |
|----------|-----------|-------------|
| **Project** | 4 | Name, description, author info |
| **Configuration** | 3 | Organization ID, iOS version, SwiftData |
| **Version** | 2 | Version name and SwiftData usage |

## 📁 Project Structure

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

## 🎯 What You Get

### ✅ Ready-to-Run App
- **Hello World Screen**: Professional UI with SwiftUI
- **Version Display**: Shows app version and welcome message
- **Responsive Layout**: Works on all iOS devices
- **Dark/Light Theme**: Automatic theme support

### ✅ Development Setup
- **Xcode Project**: Properly configured project file
- **Dependencies**: All necessary iOS frameworks included
- **Build Configuration**: Optimized for development and release
- **Code Style**: Consistent Swift coding standards

### ✅ Testing Framework
- **Unit Tests**: XCTest setup with example test
- **UI Tests**: XCTest UI setup with example test
- **Test Schemes**: Configured for iOS testing

## 🚀 Quick Start

1. **Generate the project** (see Installation above)
2. **Open in Xcode**:
   ```bash
   cd {{cookiecutter.project_name}}
   open {{cookiecutter.project_name}}.xcodeproj
   ```
3. **Run the app**:
   - Select a device/simulator
   - Click the Run button (▶️) or press `Cmd + R`

## 🔧 Customization

### SwiftData Integration
- `use_swift_data`: Enable/disable SwiftData for data persistence
- Automatically configures ModelContainer and @Query properties

### iOS Version
- `minimum_ios_version`: Set minimum iOS deployment target (15.0)

### Bundle Configuration
- `organization_identifier`: Your organization's bundle identifier prefix
- Automatically generates proper bundle IDs

## 📱 App Features

### Main Screen
- **Globe Icon**: SF Symbol with proper scaling
- **Hello World Text**: Large, bold title
- **Welcome Message**: App name display
- **Version Info**: Shows current app version

### UI Components
- **SwiftUI**: Modern declarative UI framework
- **Responsive Layout**: Adapts to different screen sizes
- **Theme Support**: Automatic dark/light mode
- **Accessibility**: Built-in accessibility support

## 🧪 Testing

### Unit Tests
```bash
# In Xcode: Product → Test (Cmd + U)
# Or via command line:
xcodebuild test -scheme {{cookiecutter.project_name}} -destination 'platform=iOS Simulator,name=iPhone 15'
```

### UI Tests
```bash
# In Xcode: Product → Test (Cmd + U)
# UI tests run automatically with unit tests
```

### Test Coverage
- **Unit Tests**: App logic and data validation
- **UI Tests**: User interface interactions
- **Launch Tests**: App launch performance

## 📦 Build & Deploy

### Debug Build
```bash
xcodebuild build -scheme {{cookiecutter.project_name}} -configuration Debug
```

### Release Build
```bash
xcodebuild build -scheme {{cookiecutter.project_name}} -configuration Release
```

### Archive for App Store
```bash
xcodebuild archive -scheme {{cookiecutter.project_name}} -archivePath {{cookiecutter.project_name}}.xcarchive
```

## 🔍 Troubleshooting

### Common Issues

1. **Build Errors**
   - Clean build folder (Product → Clean Build Folder)
   - Reset package caches (File → Packages → Reset Package Caches)

2. **Simulator Issues**
   - Reset simulator (Device → Erase All Content and Settings)
   - Create new simulator (Window → Devices and Simulators)

3. **Code Signing Issues**
   - Check team selection in project settings
   - Verify bundle identifier is unique

### Performance Tips

- Use Xcode's built-in Instruments for profiling
- Enable Metal API Validation in simulator
- Use SwiftUI previews for rapid UI development

## 🚀 Advanced Features

### SwiftData (Optional)
If enabled, the template includes:
- **ModelContainer**: Data persistence setup
- **@Query**: Automatic data fetching
- **ModelContext**: Data manipulation

### Conditional Imports
- **SwiftData**: Only imported when enabled
- **SwiftUI**: Always included
- **Testing**: Proper test framework imports

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This template is provided as-is for educational and development purposes.

## 🙏 Acknowledgments

- **SwiftUI**: Apple's modern UI framework
- **Xcode**: Apple's development environment
- **Cookiecutter**: Project template generator

---

**Made with ❤️ for the iOS development community**

*Generated with iOS Hello World Template v1.0.0* 