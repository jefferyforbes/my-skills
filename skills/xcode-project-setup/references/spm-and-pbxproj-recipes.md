# Xcode Project Setup: SPM & PBXProj Modification Recipes

This reference provides safe patterns for linking Swift Package Manager dependencies and modifying \`project.pbxproj\` files without corruption.

---

## 1. Swift Package Manager Link Structure
A Swift package reference in \`project.pbxproj\` requires 4 interconnected sections:
1. \`XCRemoteSwiftPackageReference\`: URL and version rules.
2. \`XCSwiftPackageProductDependency\`: Product name and target package.
3. \`PBXBuildFile\`: Links the product dependency into the target's frameworks build phase.
4. \`PBXFrameworksBuildPhase\`: Contains the build file reference.

---

## 2. Safe PBXProj Modification Rules
- Always create a backup: \`cp project.pbxproj project.pbxproj.bak\`.
- Generate unique 24-character hexadecimal UUIDs for all new PBX objects.
- Validate project syntax with \`plutil -lint project.pbxproj\` before building.
