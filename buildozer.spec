[app]

title = Meu App Kivy
package.name = meuappkivy
package.domain = org.exemplo

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.sdk = 34
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
android.copy_libs = 1
android.archs = arm64-v8a
android.allow_backup = True

source.exclude_exts = spec,pyc,pyo,db,sqlite3
source.exclude_dirs = tests,bin,.git,.github,__pycache__

[buildozer]

log_level = 2
warn_on_root = 1
bin_dir = ./bin
