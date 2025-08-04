#!/usr/bin/env python3
"""
Version detection script for iOS development environment.
This script detects installed versions of iOS development tools.
"""

import subprocess
import sys
import re
from pathlib import Path

def run_command(command):
    """Run a command and return the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout.strip()
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError, FileNotFoundError):
        return None

def detect_xcode_version():
    """Detect Xcode version."""
    xcode_version = run_command("xcodebuild -version")
    if xcode_version:
        # Extract version from output like "Xcode 15.0"
        match = re.search(r'Xcode ([^\s]+)', xcode_version)
        if match:
            return match.group(1)
    return "Not detected"

def detect_swift_version():
    """Detect Swift version."""
    swift_version = run_command("swift --version")
    if swift_version:
        # Extract version from output like "swift-driver version: 1.75.2"
        match = re.search(r'swift-driver version: ([^\s]+)', swift_version)
        if match:
            return match.group(1)
    return "Not detected"

def detect_ios_simulator():
    """Detect iOS Simulator availability."""
    simulator_path = Path("/Applications/Xcode.app/Contents/Developer/Applications/Simulator.app")
    if simulator_path.exists():
        return "Available"
    return "Not found"

def detect_cocoapods():
    """Detect CocoaPods version."""
    cocoapods_version = run_command("pod --version")
    if cocoapods_version:
        return cocoapods_version
    return "Not installed"

def detect_homebrew():
    """Detect Homebrew version."""
    homebrew_version = run_command("brew --version")
    if homebrew_version:
        # Extract version from output like "Homebrew 4.1.0"
        match = re.search(r'Homebrew ([^\s]+)', homebrew_version)
        if match:
            return match.group(1)
    return "Not installed"

def detect_macos_version():
    """Detect macOS version."""
    macos_version = run_command("sw_vers -productVersion")
    if macos_version:
        return macos_version
    return "Not detected"

def detect_ios_deployment_target():
    """Detect minimum iOS deployment target from Xcode."""
    # This would typically be set in the project, but we can check Xcode's capabilities
    xcode_version = detect_xcode_version()
    if xcode_version != "Not detected":
        try:
            version_num = float(xcode_version)
            if version_num >= 15.0:
                return "iOS 15.0+ (recommended)"
            elif version_num >= 14.0:
                return "iOS 14.0+"
            else:
                return "iOS 13.0+"
        except ValueError:
            return "iOS 15.0+ (recommended)"
    return "iOS 15.0+ (recommended)"

def generate_requirements_md():
    """Generate requirements.md content."""
    xcode_ver = detect_xcode_version()
    swift_ver = detect_swift_version()
    simulator = detect_ios_simulator()
    cocoapods_ver = detect_cocoapods()
    homebrew_ver = detect_homebrew()
    macos_ver = detect_macos_version()
    ios_target = detect_ios_deployment_target()
    
    content = f"""# iOS Development Requirements

## Detected Versions

| Tool | Version | Status |
|------|---------|--------|
| **Xcode** | {xcode_ver} | {'✅' if xcode_ver != 'Not detected' else '❌'} |
| **Swift** | {swift_ver} | {'✅' if swift_ver != 'Not detected' else '❌'} |
| **iOS Simulator** | {simulator} | {'✅' if simulator == 'Available' else '❌'} |
| **CocoaPods** | {cocoapods_ver} | {'✅' if cocoapods_ver != 'Not installed' else '⚠️'} |
| **Homebrew** | {homebrew_ver} | {'✅' if homebrew_ver != 'Not installed' else '⚠️'} |
| **macOS** | {macos_ver} | {'✅' if macos_ver != 'Not detected' else '❌'} |

## iOS Deployment Target
```
{ios_target}
```

## Recommended Versions

- **Xcode**: 15.0 or higher
- **Swift**: 5.9 or higher
- **macOS**: 13.0 (Ventura) or higher
- **iOS Deployment Target**: 15.0 or higher

## Installation Instructions

### Xcode
1. Download from the Mac App Store: https://apps.apple.com/app/xcode/id497799835
2. Or download from Apple Developer: https://developer.apple.com/xcode/

### Homebrew (Package Manager)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### CocoaPods (Dependency Manager)
```bash
# Using Homebrew
brew install cocoapods

# Or using gem
sudo gem install cocoapods
```

### Swift Package Manager
Comes bundled with Xcode, no separate installation needed.

## Verification

Run these commands to verify your setup:

```bash
xcodebuild -version
swift --version
pod --version
brew --version
```

## Project Setup

1. **Open the project**:
   ```bash
   open {{cookiecutter.project_name}}.xcodeproj
   ```

2. **Select your target device**:
   - iOS Simulator (recommended for development)
   - Physical iOS device (requires Apple Developer account)

3. **Build and run**:
   - Press `Cmd + R` in Xcode
   - Or use the Play button in the toolbar

## Troubleshooting

### Common Issues

1. **Xcode not found**: Install Xcode from the Mac App Store
2. **Simulator not working**: Reset simulator via Xcode → Window → Devices and Simulators
3. **Build errors**: Clean build folder (Cmd + Shift + K) and rebuild

### Performance Tips

- Use iOS Simulator for faster development cycles
- Enable "Metal API Validation" in simulator for better debugging
- Use Xcode's built-in Instruments for performance profiling

---
*This file was auto-generated by the iOS Hello World Template*
"""
    
    return content

if __name__ == "__main__":
    requirements_content = generate_requirements_md()
    print(requirements_content) 