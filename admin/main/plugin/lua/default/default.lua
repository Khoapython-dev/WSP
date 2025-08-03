local json = require("json")  -- Đảm bảo bạn có thư viện json, ví dụ: dkjson, cjson, hoặc tự viết.

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

-- Dữ liệu chính
local data = parsed

-- Kiểm tra key tồn tại
if type(data["include"]) ~= "table" or type(data["include"]["msg"]) ~= "string" then
    error("[ERROR] Không tìm thấy đường dẫn 'include.msg' trong JSON.")
end
if type(data["Default.plugin"]) ~= "table" or type(data["Default.plugin"]["MSG"]) ~= "table" or type(data["Default.plugin"]["MSG"]["status"]) ~= "table" or type(data["Default.plugin"]["MSG"]["status"]["join-code-server"]) == "nil" then
    error("[ERROR] Không tìm thấy thông tin 'Default.plugin.MSG.status.join-code-server'.")
end

-- Plugin giả định
local plugin = {}

-- Biến shortcut
local msg = data["include"]["msg"] or ""
local push_path = data["include"]["msg"]

-- Ghi ra file
function pl_text(text)
    local file = io.open(push_path, "w")
    if file then
        file:write(text)
        file:close()
        print("[INFO] Đã ghi: " .. text .. " | status: " .. tostring(data["Default.plugin"]["MSG"]["status"]["join-code-server"]))
    else
        print("[ERROR] Không thể mở file để ghi: " .. tostring(push_path))
    end
end

pl_text("Hello, World!")  -- Gọi hàm để ghi ra file
return plugin  -- Trả về plugin để sử dụng trong các phần khác của ứng dụnglua default.lua
