import json
import os
import time

class get_key:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    local = None
    api_keys = []

    json_status = os.path.join(base_dir, "status.json")
    json_front = os.path.join(base_dir, "storage/message.sms")
    json_engineeer = os.path.join(base_dir, "storage/iso.sms")

    json_list = os.path.join(base_dir, "json/list.json")

    @staticmethod
    def api(key):
        # Đọc file JSON và lấy danh sách API keys
        try:
            with open(get_key.json_status, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print("[ERROR]: Không tìm thấy file status.json.")
            return None
        except json.JSONDecodeError:
            print("[ERROR]: File JSON bị lỗi cú pháp.")
            return None

        # Kiểm tra key
        api_keys = data["G_201"]["api_key"] if "G_201" in data and "api_key" in data["G_201"] else []
        if not api_keys:
            print("[ERROR]: Không tìm thấy key 'api_key' trong status.json.")
            return None

        get_key.api_keys = api_keys
        if key in api_keys:
            print("[INFO]: Key hợp lệ.")
            get_key.local = key
        else:
            print("[ERROR]: Key không tồn tại.")
            get_key.local = None

    @staticmethod
    def output(true_or_false):
        if get_key.local in get_key.api_keys:
            if true_or_false == "True":
                try:
                    with open(get_key.json_front, 'r') as file:
                        data = file.read()
                    with open(get_key.json_engineeer, 'r') as file:
                        engineer_data = file.read()
                    print("[INFO]: Output data:", data, "Engineer data:", engineer_data)
                except FileNotFoundError:
                    print("[ERROR]: Không tìm thấy file message.sms.")
            else:
                print("[INFO]: Không hiển thị output (điều kiện sai).")
        else:
            print("[ERROR]: Không xác thực được key. Vui lòng kiểm tra.")

    @staticmethod
    def delay(seconds):
        if get_key.local in get_key.api_keys:
            time.sleep(seconds)
        else:
            print("[ERROR]: Không xác thực được key. Vui lòng kiểm tra.")

    @staticmethod
    def plugin_start(bool):
        if bool == "True" or bool == "true":
            with open(get_key.json_list, 'r') as file:
                data = json.load(file)
            exec_path = os.path.join(get_key.base_dir, data["list"]['default']['lua'])
            os.system(f"lua {exec_path}")
        else:
            print("[INFO]: Không kích hoạt plugin.")
            return None
                
        


class pyplugin:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_front = os.path.join(base_dir, "storage/iso.sms")
    json_status = os.path.join(base_dir, "status.json")

    api = None
    ns = None
    
    @staticmethod
    def api(key):
        with open(pyplugin.json_status, 'r') as file:
            data = json.load(file)
        pyplugin.ns = data["G_201"]["api_key"]
        if key in pyplugin.ns:
            pyplugin.api = key
            print("[INFO]: Key hợp lệ, plua console đã hoạt động.")
        else:
            print("[ERROR]: Key không tồn tại.")
            return None

    @staticmethod
    def writeln(text):
        if pyplugin.api is None:
            print("[ERROR]: Chưa xác thực API key. Vui lòng gọi pyplugin.api(key) trước.")
            return None
        elif pyplugin.api == pyplugin.ns:
            with open(pyplugin.json_front, 'a') as file:
                file.write(text + "\n")
            print("[ INFO]: Đẩy dữ liệu thành công.")
        else:
            print("[ERROR]: Không xác thực được key. Vui lòng kiểm tra.")
            return None
    
    @staticmethod
    def scanR(question):
        if pyplugin.api is None:
            print("[ERROR]: Chưa xác thực API key. Vui lòng gọi pyplugin.api(key) trước.")
            return None
        elif pyplugin.api == pyplugin.ns:
            input_value = input(f"[ INFO]{question}: ")

    #@staticmethod
    

        