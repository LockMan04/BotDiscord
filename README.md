# AgentBot — Agent-first Discord Music Bot

AgentBot là một Discord bot hướng tới trải nghiệm "agent": thay vì nhớ từng lệnh, bạn chỉ cần nói bằng ngôn ngữ tự nhiên — bot sẽ hiểu, chọn công cụ phù hợp và thực thi.

## Tính năng chính
- Agent (Natural Language Actions): hiểu ý định từ câu lệnh tự nhiên và tự quyết định chuỗi hành động cần thiết.
- Music agent: tìm bài, thêm vào queue, join voice, phát/pause/skip/stop, tự tiếp tục phát playlist.
- AI Chat: hội thoại nhiều lượt với persona, trả lời tự nhiên và ngữ cảnh.
- Tools tiện ích: ảnh động vật, tạo meme, tra cứu thời tiết, thông tin server, v.v.
- Hành động chuỗi (chaining): kết hợp nhiều bước (ví dụ: tìm playlist → thêm hàng loạt → bắt đầu phát).
- Quyền & giới hạn: có thể giới hạn hành động trong kênh hoặc theo role.

## Demo — ví dụ yêu cầu bằng ngôn ngữ tự nhiên
- "Vào voice với tao"  
  → Bot join voice channel hiện tại.

- "Phát See You Again"  
  → Bot tìm bài, thêm vào queue và phát ngay.

- "Tạo playlist 1 giờ chill và phát"  
  → Agent tìm và thêm nhiều bài theo chủ đề rồi bắt đầu phát.

- "Dừng nhạc" / "Tạm dừng" / "Tiếp tục"  
  → Bot pause hoặc resume playback.

- "Bỏ bài hiện tại, phát bài tiếp theo"  
  → Bot skip và play bài tiếp.

- "Cho xem ảnh mèo dễ thương"  
  → Bot trả về ảnh/gợi ý ảnh.

- "Làm meme từ ảnh này với chữ 'Khi deploy xong'"  
  → Bot tạo meme và gửi kết quả.

- "Hôm nay ở Hà Nội bao nhiêu độ?"  
  → Bot trả dữ liệu thời tiết.

## Nguyên tắc dùng
- Giao tiếp bằng câu tự nhiên; càng rõ mục tiêu càng chính xác kết quả.
- Agent sẽ tự quyết định tool và chuỗi hành động; chỉ can thiệp khi cần chỉnh thủ công.
- Bot ưu tiên trải nghiệm trực quan, giảm nhu cầu nhớ lệnh tường minh.

## Mục tiêu
- Giảm gánh nặng nhớ lệnh, tăng hiệu quả tương tác: bạn nói — AgentBot tự lo phần còn lại.

## Liên hệ
- Tác giả: LockMan04.

## Chú thích
- ⚠️Chỉ là file `main.py` demo. Các tính năng chưa được public, vui lòng liên hệ tôi để tìm hiểu thêm⚠️
