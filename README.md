# Voice Recorder

Ứng dụng ghi âm lệnh giọng nói tự động cho Windows, macOS và Linux.

## Tính năng

- ✅ Ghi âm 20 sample tự động cho mỗi lệnh
- ✅ Phát beep trước khi ghi âm
- ✅ Tự động tạo thư mục theo cấu trúc
- ✅ Hỗ trợ đa nền tảng (Windows, macOS, Linux)
- ✅ Build tự động với GitHub Actions

## Download

Tải về từ [GitHub Releases](../../releases/latest):

- **Windows**: `VoiceRecorder-Windows.exe`
- **macOS**: `VoiceRecorder.dmg`
- **Linux**: `VoiceRecorder-Linux.out`

## Cài đặt và sử dụng

### Windows
1. Tải `VoiceRecorder-Windows.exe`
2. Double-click để chạy
3. Cho phép truy cập microphone nếu được hỏi

### macOS
1. Tải `VoiceRecorder.dmg`
2. Mở file DMG và kéo app vào Applications
3. Chạy từ Applications
4. Cho phép truy cập microphone trong System Preferences > Security & Privacy > Privacy > Microphone

### Linux
1. Tải `VoiceRecorder-Linux.out`
2. Mở terminal và chạy:
   ```bash
   chmod +x VoiceRecorder-Linux.out
   ./VoiceRecorder-Linux.out
   ```

## Hướng dẫn sử dụng

1. Chạy ứng dụng
2. Nhập lệnh theo format: `bat_den/bac/nam/3/sang`
   - 5 tham số được phân tách bởi dấu `/`
3. Nói sau khi nghe tiếng beep
4. Ứng dụng sẽ ghi 20 sample tự động
5. File được lưu trong thư mục `recorded_wav_dataset/`

## Cấu trúc thư mục

```
recorded_wav_dataset/
├── bat_den/
│   ├── bac/
│   │   ├── nam/
│   │   │   ├── 3/
│   │   │   │   ├── sang_00.wav
│   │   │   │   ├── sang_01.wav
│   │   │   │   └── ...
```

## Development

### Yêu cầu hệ thống
- Python 3.8+
- Dependencies: `sounddevice`, `scipy`, `numpy`, `pygame` (Windows only)

### Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Chạy từ source code
```bash
python record_dataset.py
```

### Build thủ công

#### Windows
```bash
pyinstaller --onefile --console --name "VoiceRecorder" record_dataset.py
```

#### macOS
```bash
# Cài đặt dependencies
brew install portaudio
pip install sounddevice scipy numpy pyinstaller

# Build
pyinstaller --onefile --console --name "VoiceRecorder" record_dataset_mac.py
```

#### Linux
```bash
# Cài đặt dependencies
sudo apt-get install portaudio19-dev python3-pyaudio
pip install sounddevice scipy numpy pyinstaller

# Build
pyinstaller --onefile --console --name "VoiceRecorder.out" record_dataset_linux.py
```

## GitHub Actions

Dự án sử dụng GitHub Actions để build tự động cho cả 3 nền tảng:

1. **Push code** lên GitHub
2. **GitHub Actions** sẽ tự động build cho Windows, macOS và Linux
3. **Download artifacts** từ Actions tab
4. **Tạo release** khi tag version (vd: `v1.0.0`)

### Tạo release mới

```bash
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actions sẽ tự động tạo release với tất cả executables.

## Troubleshooting

### Windows
- Nếu Windows Defender cảnh báo, chọn "More info" > "Run anyway"
- Đảm bảo microphone được kết nối

### macOS
- Nếu app không mở được, right-click > "Open" để bypass Gatekeeper
- Kiểm tra microphone permissions trong System Preferences

### Linux
- Cài đặt audio drivers: `sudo apt-get install pulseaudio`
- Kiểm tra microphone: `arecord -l`

## License

MIT License - Xem file LICENSE để biết thêm chi tiết.
