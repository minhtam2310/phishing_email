
# 📌 Giới thiệu đề tài

Phishing Email là một trong những hình thức tấn công lừa đảo phổ biến hiện nay, nhằm đánh cắp thông tin cá nhân, tài khoản ngân hàng hoặc phát tán mã độc đến người dùng.

Đề tài tập trung nghiên cứu và xây dựng hệ thống phát hiện Phishing Email dựa trên nội dung văn bản bằng cách kết hợp kỹ thuật xử lý ngôn ngữ tự nhiên (NLP) và thuật toán học máy Random Forest.

Hệ thống được triển khai dưới dạng ứng dụng Web sử dụng Streamlit, cho phép người dùng nhập nội dung Email và nhận kết quả phân loại theo thời gian thực.

---

# 🎯 Mục tiêu đề tài

* Tìm hiểu đặc điểm và hành vi của Email lừa đảo.
* Nghiên cứu các kỹ thuật xử lý dữ liệu văn bản trong NLP.
* Xây dựng mô hình Machine Learning phát hiện Phishing Email.
* Đánh giá hiệu quả mô hình bằng các độ đo chuẩn.
* Xây dựng giao diện Web hỗ trợ kiểm tra Email trực tuyến.

---

# 📂 Bộ dữ liệu sử dụng

Đề tài sử dụng và hợp nhất bốn bộ dữ liệu công khai.

| Bộ dữ liệu     | Số lượng Email | Legitimate | Phishing |
| -------------- | -------------- | ---------- | -------- |
| CEAS_08        | 39.154         | 17.312     | 21.842   |
| Nazario        | 1.565          | 0          | 1.565    |
| Nigerian_Fraud | 3.332          | 0          | 3.332    |
| SpamAssassin   | 5.809          | 4.091      | 1.718    |

Tổng cộng:

```text
49.860 Email
```

---

# 📁 Cấu trúc thư mục dự án

```text
Cdcs_Phishingemail
│
├── app
│   ├── app.py
│   └── preprocess.py
│
├── data
│   ├── CEAS_08.csv
│   ├── Nazario.csv
│   ├── Nigerian_Fraud.csv
│   └── SpamAssasin.csv
│
├── model
│   ├── rf_model.pkl
│   └── tfidf.pkl
│
├── notebook
│   ├── main.ipynb
│   └── test.ipynb
│
├── README.md
│
└── image.png
```

---

# 📌 Mô tả chức năng từng thư mục

## 📂 app

Chứa mã nguồn của ứng dụng Web Streamlit.

### app.py

Là chương trình chính của hệ thống.

Chức năng:

* Tải mô hình Random Forest đã huấn luyện.
* Tải bộ TF-IDF Vectorizer.
* Tiếp nhận nội dung Email từ người dùng.
* Dự đoán loại Email.
* Hiển thị xác suất dự đoán.
* Hiển thị lịch sử phân tích.
* Hiển thị các từ khóa quan trọng.

---

### preprocess.py

Chứa các hàm tiền xử lý dữ liệu văn bản.

Bao gồm:

* Chuyển toàn bộ ký tự về chữ thường.
* Loại bỏ URL.
* Loại bỏ ký tự đặc biệt.
* Loại bỏ Stopwords.
* Chuẩn hóa khoảng trắng.

---

## 📂 data

Chứa toàn bộ bộ dữ liệu được sử dụng để huấn luyện và đánh giá mô hình.

Bao gồm:

* CEAS_08.csv
* Nazario.csv
* Nigerian_Fraud.csv
* SpamAssasin.csv

---

## 📂 model

Chứa các mô hình đã được huấn luyện.

### rf_model.pkl

Mô hình Random Forest đã học từ dữ liệu.

---

### tfidf.pkl

Bộ TF-IDF Vectorizer đã được huấn luyện trên toàn bộ tập dữ liệu.

---

## 📂 notebook

Chứa Notebook dùng để nghiên cứu, huấn luyện và đánh giá mô hình.

### main.ipynb
Đây là nơi chứa code chính
Bao gồm các bước:

* Khám phá dữ liệu.
* Tiền xử lý văn bản.
* TF-IDF Vectorization.
* Chia Train/Test.
* Huấn luyện Random Forest.
* Đánh giá mô hình.
* Phân tích Feature Importance.
* Lưu mô hình.

---

# 🔄 Quy trình hoạt động của hệ thống

```text
Email gốc

    │

    ▼

Tiền xử lý dữ liệu

    │

    ▼

Biểu diễn văn bản bằng TF-IDF

    │

    ▼

Random Forest

    │

    ▼

Phân loại Email

    │

    ▼

Legitimate / Phishing
```

---

# ⚙️ Tiền xử lý dữ liệu

Các kỹ thuật tiền xử lý được sử dụng:

✔ Chuyển về chữ thường

✔ Loại bỏ URL

✔ Loại bỏ ký tự đặc biệt

✔ Loại bỏ Stopwords

✔ Chuẩn hóa khoảng trắng

---

# 🧠 Mô hình Machine Learning

Thuật toán sử dụng:

```text
Random Forest
```

Thông số huấn luyện:

```python
RandomForestClassifier(

n_estimators = 150,

random_state = 42,

class_weight = "balanced",

n_jobs = -1

)
```

---

# 🔤 Biểu diễn dữ liệu văn bản

Kỹ thuật sử dụng:

```text
TF-IDF
```

Cấu hình:

```python
TfidfVectorizer(

max_features = 10000,

min_df = 3,

max_df = 0.9,

ngram_range = (1,2)

)
```

---

# 📊 Kết quả đánh giá mô hình

| Chỉ số         | Giá trị |
| -------------- | ------- |
| Accuracy       | 98.87 % |
| Precision      | 99 %    |
| Recall         | 99 %    |
| F1-score       | 99 %    |
| False Positive | 39      |
| False Negative | 77      |

Confusion Matrix:

```text
[[4242   39]

 [  77 5614]]
```

---

# 🌐 Ứng dụng Web

Framework sử dụng:

```text
Streamlit
```

Các chức năng hỗ trợ:

✅ Phân loại Email

✅ Hiển thị xác suất dự đoán

✅ Đánh giá mức độ rủi ro

✅ Hiển thị từ khóa quan trọng

✅ Xem văn bản sau tiền xử lý

✅ Lịch sử dự đoán

✅ Giải thích quy trình hoạt động của hệ thống

---

# 🚀 Hướng dẫn cài đặt

Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

Khởi chạy ứng dụng:

```bash
streamlit run app/app.py
```

---

# ⚠️ Hạn chế của hệ thống

Phiên bản hiện tại chỉ hỗ trợ phát hiện Phishing Email dựa trên **nội dung văn bản**.

Hệ thống chưa hỗ trợ phân tích:

* URL độc hại
* Hình ảnh
* Mã QR
* Tệp đính kèm
* Nội dung HTML

---

# 🔮 Hướng phát triển

Trong tương lai có thể mở rộng hệ thống bằng cách:

* Trích xuất đặc trưng từ URL.

* Phân tích nội dung HTML.

* Sử dụng OCR để xử lý hình ảnh.

* Áp dụng các mô hình học sâu như:

  * BERT
  * RoBERTa
  * DistilBERT

* Bổ sung tập dữ liệu Email tiếng Việt.

---

