import streamlit as st
import datetime
from io import BytesIO
from fpdf import FPDF
import base64

# ---------- إعداد الواجهة ---------- #
st.set_page_config(page_title="تحليل الشخصية", page_icon="🧠", layout="centered")
st.markdown("<h2 style='text-align: center;'>🧠 أهلاً بك في تطبيق تحليل الشخصية</h2>", unsafe_allow_html=True)
st.markdown("---")

# ---------- اختيار اللغة ---------- #
language = st.selectbox("🌍 اختر اللغة / Choose Language", ["العربية", "English"])

# ---------- إدخال البيانات ---------- #
if language == "العربية":
    name = st.text_input("👤 اسمك:")
    age = st.number_input("🎂 عمرك:", min_value=0, max_value=120, step=1)
    status = st.selectbox("💍 الحالة الاجتماعية:", ["اعزب", "متجوز", "خاطب"])
else:
    name = st.text_input("👤 Your Name:")
    age = st.number_input("🎂 Your Age:", min_value=0, max_value=120, step=1)
    status = st.selectbox("💍 Marital Status:", ["single", "married", "engaged"])

# ---------- زر التحليل ---------- #
if st.button("🔍 تحليل / Analyze"):
    msg = ""

    if language == "العربية":
        if status == "اعزب":
            msg += f"{name}، لازم تتجوز 😅\n"
        elif status == "متجوز":
            msg += f"{name}، ربنا يسعدك 👏\n"
        elif status == "خاطب":
            msg += f"{name}، ألف مبروك 💍\n"
        else:
            msg += "مش فاهم حالتك الاجتماعية 😅\n"

        if age >= 60:
            msg += "ربنا يديك الصحة 🙏"
        elif age >= 30:
            msg += "أنت راجل ناضج ومحترم 👨‍💼"
        elif age >= 20:
            msg += "في عز شبابك 💪"
        elif age >= 16:
            msg += "لسه شاب صغير، شد حيلك 💼"
        else:
            msg += "أنت لسه بيبي 👶"
    else:
        if status == "single":
            msg += f"{name}, it's time to get married 😅\n"
        elif status == "married":
            msg += f"{name}, may your marriage be happy 👏\n"
        elif status == "engaged":
            msg += f"{name}, congratulations on your engagement 💍\n"
        else:
            msg += "Sorry, I didn't understand your marital status 😅\n"

        if age >= 60:
            msg += "Wishing you good health 🙏"
        elif age >= 30:
            msg += "You are mature and respectable 👨‍💼"
        elif age >= 20:
            msg += "You're in the prime of your youth 💪"
        elif age >= 16:
            msg += "You're still young, keep pushing 💼"
        else:
            msg += "You're still a baby 👶"

    st.success(msg)

    # ---------- زر تحميل PDF ---------- #
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.multi_cell(0, 10, txt=f"{name} - {age} - {status}\n\n{msg}")
    pdf_bytes = BytesIO()
    pdf.output(pdf_bytes)
    pdf_bytes.seek(0)
    b64 = base64.b64encode(pdf_bytes.read()).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="result.pdf">📄 تحميل النتيجة كـ PDF</a>'
    st.markdown(href, unsafe_allow_html=True)

    # ---------- زر المشاركة ---------- #
    share_text = f"{name} - {age} - {status}\n\n{msg}"
    share_link = f"https://wa.me/?text={share_text.replace(' ', '%20').replace('\n', '%0A')}"
    st.markdown(f"[📲 مشاركة على واتساب]({share_link})")

    # ---------- حفظ النتيجة في ملف محلي ---------- #
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("result.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}]\n{name} - {age} - {status}\n{msg}\n\n")

# ---------- توقيع المطور ---------- #
st.markdown("---")
st.markdown("تم التطوير بواسطة **عبد الله محمد عبد الفتاح / صاصا** ❤️")
st.markdown("بمساعدة **ChatGPT** 🤖")
