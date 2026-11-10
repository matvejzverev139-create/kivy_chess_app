[app]
title = Chess Overlay
package.name = chessoverlay
package.domain = org.chess
source.dir = .
source.exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 30
android.ndk = 25b
android.accept_sdk_license = True
# Оставляем только arm64 для ускорения сборки
android.archs = arm64-v8a
log_level = 2
warn_on_root = 1
