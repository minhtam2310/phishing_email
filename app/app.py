import streamlit as st
import joblib
import os
import pandas as pd
import matplotlib.pyplot as plt
from preprocess import clean_text

# cấu hình trang
st.set_page_config(page_title="Phishing Email Detection", page_icon="🛡️", layout="wide")

# tải mô hình
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rf_model_path = os.path.join(BASE_DIR, "model", "rf_model.pkl")
tfidf_path = os.path.join(BASE_DIR, "model", "tfidf.pkl")


@st.cache_resource
def load_model():
    rf_model = joblib.load(rf_model_path)
    tfidf = joblib.load(tfidf_path)
    return rf_model, tfidf


rf_model, tfidf = load_model()

# lưu lịch sử dự đoán
if "history" not in st.session_state:
    st.session_state.history = []

# sidebar
with st.sidebar:
    st.header("📋 Project Information")

    st.markdown("""
**Đề tài**

Nghiên cứu phát hiện Phishing Email sử dụng Machine Learning

---

### Dataset

- CEAS_08
- Nazario
- Nigerian_Fraud
- SpamAssassin

### Machine Learning

- Random Forest

### Text Representation

- TF-IDF

### Programming Language

- Python

### Framework

- Streamlit
""")


# tiêu đề
st.title("🛡️ Phishing Email Detection System ")

# cảnh báo phạm vi hệ thống
st.warning(
    "⚠️ Lưu ý: Phiên bản hiện tại chưa hỗ trợ phân tích URL độc hại, hình ảnh, mã QR hoặc tệp đính kèm."
)

st.markdown(
    """
    <p style='font-size:17px'>
    Hệ thống chỉ hỗ trợ phân loại Email dựa trên
    <i><span style='color:red;'>nội dung văn bản</span></i>.
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()

# nhập nội dung email
email_text = st.text_area(
    label="📧 Nhập nội dung Email cần kiểm tra:",
    height=280,
    placeholder="""
Ví dụ:

Dear customer,

Your account has been suspended.

Please verify your account immediately by clicking the link below:

http://fake-bank.com

Thank you.
""",
)

# phân tích email
if st.button("🔍 Analyze Email", use_container_width=True):
    if email_text.strip() == "":
        st.warning("⚠️ Vui lòng nhập nội dung Email.")
    else:
        cleaned_text = clean_text(email_text)
        vector = tfidf.transform([cleaned_text])
        prediction = rf_model.predict(vector)[0]
        probability = rf_model.predict_proba(vector)[0]

        legitimate_prob = probability[0] * 100
        phishing_prob = probability[1] * 100

        if prediction == 1:
            result_label = "Phishing Email"
            risk_level = "High Risk"
            risk_color = "red"
        else:
            result_label = "Legitimate Email"
            risk_level = "Low Risk"
            risk_color = "green"

        st.session_state.history.append(
            {
                "Prediction": result_label,
                "Phishing Probability": f"{phishing_prob:.2f}%",
                "Legitimate Probability": f"{legitimate_prob:.2f}%",
                "Risk Level": risk_level,
            }
        )

        st.divider()
        st.subheader("📊 Prediction Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Legitimate Probability", f"{legitimate_prob:.2f}%")

        with col2:
            st.metric("Phishing Probability", f"{phishing_prob:.2f}%")

        st.progress(int(phishing_prob))

        if prediction == 1:
            st.error("⚠️ Phishing Email Detected")
            st.warning(
                "Email này có nhiều dấu hiệu giống Email lừa đảo. Người dùng cần thận trọng trước khi nhấn vào liên kết hoặc cung cấp thông tin cá nhân."
            )
        else:
            st.success("✅ Legitimate Email")
            st.info(
                "Email này được mô hình phân loại là Email hợp lệ dựa trên nội dung văn bản đã phân tích."
            )

        st.markdown(
            f"""
            <h4>Risk Level:
            <span style='color:{risk_color}; font-weight:bold;'>{risk_level}</span>
            </h4>
            """,
            unsafe_allow_html=True,
        )

        # biểu đồ xác suất
        st.subheader("📈 Probability Chart")

        prob_df = pd.DataFrame(
            {
                "Class": ["Legitimate", "Phishing"],
                "Probability": [legitimate_prob, phishing_prob],
            }
        )

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(prob_df["Class"], prob_df["Probability"])
        ax.set_ylim(0, 100)
        ax.set_ylabel("Probability (%)")
        ax.set_title("Prediction Probability")
        for index, value in enumerate(prob_df["Probability"]):
            ax.text(index, value + 1, f"{value:.2f}%", ha="center")
        st.pyplot(fig)

        # từ khóa quan trọng
        st.subheader("🔑 Important Words Detected")

        words = cleaned_text.split()
        feature_names = tfidf.get_feature_names_out()

        detected_words = [word for word in words if word in feature_names]

        detected_words = list(dict.fromkeys(detected_words))

        if len(detected_words) > 0:
            st.write(", ".join(detected_words[:30]))
        else:
            st.write("Không phát hiện từ khóa nổi bật.")

        # xem văn bản sau tiền xử lý
        with st.expander("🔎 View Preprocessed Text"):
            st.write(cleaned_text)

        # giải thích quy trình hệ thống
        with st.expander("⚙️ How the system works"):
            st.markdown("""
1. Nhận nội dung Email từ người dùng.
2. Tiền xử lý văn bản.
3. Chuyển văn bản sang vector TF-IDF.
4. Random Forest dự đoán.
5. Hiển thị kết quả và xác suất.
""")

# lịch sử dự đoán
if len(st.session_state.history) > 0:
    st.divider()
    st.subheader("🕘 Prediction History")

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(history_df, use_container_width=True)

# footer
st.divider()
st.caption(
    "Sinh viên thực hiện :     Nguyễn Thị Minh Hằng - Mạc Quỳnh Mai - Lê Thị Minh Tâm"
)
