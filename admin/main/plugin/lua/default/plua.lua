local json = require("json")  -- Đảm bảo đã có thư viện json như dkjson, cjson,...

-- Đọc file JSON
local json_path = "api.json"
local file = io.open(json_path, "r")
if not file then
    error("[ERROR] Không thể mở file: " .. json_path)
end

local raw_data = file:read("*a")
file:close()

-- Parse JSON
local ok, parsed = pcall(json.decode, raw_data)
if not ok or type(parsed) ~= "table" then
    error("[ERROR] JSON lỗi hoặc không hợp lệ trong api.json")
end

local data = parsed

-- Kiểm tra key tồn tại
if type(data.include) ~= "table" or type(data.include.msg) ~= "string" then
    error("[ERROR] Không tìm thấy đường dẫn 'include.msg' trong JSON.")
end


-- Biến shortcut
local msg_path = data.include.msg


-- Ghi ra file
local function pl_text(text)
    local f = io.open(msg_path, "w")
    if f then
        f:write(text)
        f:close()
    else
        print("[ERROR] Không thể mở file để ghi: " .. tostring(msg_path))
    end
end
local ins = "đây là plugin cơ bản!"

pl_text(ins)  -- Ghi dữ liệu vào file