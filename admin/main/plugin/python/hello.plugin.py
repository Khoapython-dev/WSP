import sys
sys.path.append('/Applications/WSP')  # Hoặc đường dẫn thật tới project gốc

from admin.main.lib.plugin.manager_plugin import pyplugin

pyplugin.api("3c4f8b2d-5e3a-4b1c-9f0d-8e2f6b7c8d9e")  # Xác thực API key
pyplugin.writeln("Hello, World!")  # Ghi dữ liệu vào file
