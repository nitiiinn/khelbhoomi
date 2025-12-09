[app]

title = KhelBhoomi
package.name = khelbhoomi
package.domain = org.khelbhoomi

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pt,onnx

version = 0.1

requirements = python3,kivy,opencv,numpy,pillow,android

orientation = portrait
fullscreen = 1

# Android permissions
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET, ACCESS_NETWORK_STATE

# Features
android.features = android.hardware.camera, android.hardware.camera.autofocus

# API levels
android.api = 33
android.minapi = 21
android.ndk = 25b

# Android specific
android.enable_androidx = True
android.release_artifact = aab
android.debug_artifact = apk

# Add meta-data for camera
android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

# Gradle dependencies for camera
android.gradle_dependencies = com.android.support:support-v4:28.0.0

# Add p4a bootstrap and recipe
p4a.bootstrap = sdl2
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
