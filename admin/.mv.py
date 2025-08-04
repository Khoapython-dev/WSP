import os, json

def get_total_plugin():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # /Applications/WSP/admin

    json_path = os.path.join(base_dir, "main/lib/api/status.json")
    json_front = os.path.join(base_dir, "main/plugin/status.json")

    os.makedirs(os.path.dirname(json_front), exist_ok=True)

    with open(json_path, 'r') as file:
        data = json.load(file)

    with open(json_front, 'w') as file:
        json.dump(data, file, indent=4)

    print("[INFO] Plugin JSON copied thành công!")


def get_total_message():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # /Applications/WSP/admin

    msg = os.path.join(base_dir, "main/plugin/lua/default/cache/msg.int")
    msg_front = os.path.join(base_dir, "main/data/storage/message.sms")
    

    with open(msg, 'r') as file:
        data = file.read()
    
    ens = data


    with open(msg_front, 'w') as file:
        file.write(ens)

def get_total_sms():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # /Applications/WSP/admin

    smt = os.path.join(base_dir, "main/data/storage/message.sms")
    sms = os.path.join(base_dir, "main/lib/plugin/storage/message.sms")

    with open(smt, 'r') as file:
        data = file.read()  

    with open(sms, 'w') as file:
        file.write(data)

get_total_message()
get_total_sms()


