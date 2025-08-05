import re

class Dab:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data: dict, indent: int = 4):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write("@ Tệp này được tạo bởi thư viện DAB\n")
            f.write("*/data:\n")
            for key, value in data.items():
                if isinstance(value, dict):
                    f.write(" " * indent + f"#/{key}:\n")
                    for subkey, subval in value.items():
                        f.write(" " * (indent * 2) + f"{subkey}={repr(subval)}\n")
                    f.write(" " * indent + f"{key}</end>\n")
                else:
                    f.write(" " * indent + f"{key}={repr(value)}\n")
            f.write("data<end>\n")

    def read(self, field: str, output_dict: dict):
        with open(self.filename, "r", encoding="utf-8") as f:
            content = f.read()

        section_pattern = re.compile(r"#/" + re.escape(field) + r":(.*?)" + re.escape(field) + r"</end>", re.DOTALL)
        match = section_pattern.search(content)
        if match:
            block = match.group(1)
            for line in block.strip().splitlines():
                if '=' in line:
                    key, value = line.strip().split("=", 1)
                    output_dict[key.strip()] = eval(value.strip())
        else:
            # Nếu là dòng đơn (key=value) nằm ngoài list
            pattern = re.compile(rf"{field}\s*=\s*(.+)")
            match = pattern.search(content)
            if match:
                output_dict[field] = eval(match.group(1).strip())
