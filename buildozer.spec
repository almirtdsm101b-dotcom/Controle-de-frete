[app]

# (str) Title of your application
title = Meu App Kivy

# (str) Package name
package.name = meuappkivy

# (str) Package domain (needed for android/ios packaging)
package.domain = org.exemplo

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3==3.11.10,kivy==2.3.0

# (str) Custom source folders for requirements
# requirements.source.kivy =

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientations (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY

#
# OSX Specific
#

# (str) path to a custom macOS icon
#mac.icon.filename = %(source.dir)s/data/icon.icns

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 28c

# (bool) Use --private data storage (True) or --public (False)
#android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) pattern to match files from the package path to be included as a reserve
#android.add_reserve_regex = lib/armeabi-v7a/.*\.so

# (list) Android additionnal libraries to include (.so)
#android.add_libs_armeabi_v7a = libs/android/armeabi-v7a/*.so
#android.add_libs_arm64_v8a = libs/android/arm64-v8a/*.so
#android.add_libs_x86 = libs/android/x86/*.so
#android.add_libs_x86_64 = libs/android/x86_64/*.so

# (bool) Indicate whether the application should be copied to the device
android.copy_libs = 1

# (list) Pattern to match files from the source.dir that will be excluded
source.exclude_exts = spec,pyc,pyo,db,sqlite3

# (list) List of directory to exclude from the source.dir
source.exclude_dirs = tests,bin,.git,.github,__pycache__

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file to include as an AndroidManifest.xml addition
#android.add_aars =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Copy Python modules to a separate directory instead of a zip file
#android.no_byte_compile_python = False

# (str) Python for android branch to use, default master
#p4a.branch = master

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes
#
