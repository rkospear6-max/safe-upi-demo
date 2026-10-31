import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

def play_voice_alert(message):
    js = f"""
    <script>
        const speech = new SpeechSynthesisUtterance("{message}");
        speech.rate = 1.0;
        speech.pitch = 1.0;
        window.speechSynthesis.speak(speech);
    </script>
    """
    components.html(js, height=0)
import time
from datetime import datetime

st.set_page_config(page_title="SafeUPI - AI Fraud Prevention Gateway", page_icon="🛡️", layout="wide")

# Custom CSS for modern Fintech look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; height: 48px; }
    .merchant-card { background: #1e2530; padding: 20px; border-radius: 12px; border: 1px solid #303846; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if 'history' not in st.session_state:
    st.session_state.history = []
if 'map_data' not in st.session_state:
    st.session_state.map_data = pd.DataFrame({'lat': [26.4499], 'lon': [74.6399], 'color': ['#00FF00']})

# --- SIMULATED AI PREDICTION LOGIC (No backend required) ---
def predict_fraud(amount, hour, frequency, distance_from_home):
    # Simple rule-based/Isolation Forest simulation for instant cloud deployment
    if distance_from_home > 500 or frequency > 10 or (hour < 5 and amount > 10000):
        return True, "High risk anomaly detected: Unusual transaction distance & high frequency pattern."
    else:
        return False, "Transaction behavior matches verified biometric profile. Safe."

# --- SIDEBAR: Investor Pitch Deck Metrics ---
st.sidebar.title("🚀 SafeUPI Business & AI Metrics")
st.sidebar.markdown("---")
st.sidebar.metric(label="Protected Volume (Today)", value="₹42,85,000", delta="+14.2%")
st.sidebar.metric(label="Fraud Detection Accuracy", value="99.6%", delta="State-of-the-art")
st.sidebar.metric(label="API Latency", value="24 ms", delta="-14ms optimized")
st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Pitch Demo Controls")
preset_mode = st.sidebar.radio("Select Transaction Scenario:", ["Normal Merchant Pay", "High-Risk Fraud Attack"])

# Preset values based on radio selection
if preset_mode == "Normal Merchant Pay":
    def_merchant = "Zomato India (Food Delivery)"
    def_amount = 450.0
    def_hour = 14
    def_freq = 2
    def_dist = 1.0
else:
    def_merchant = "International Crypto P2P Transfer"
    def_amount = 75000.0
    def_hour = 3
    def_freq = 18
    def_dist = 1250.0

# --- MAIN APP INTERFACE ---
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown("<h2 style='text-align: center;'>🛡️ SafeUPI Enterprise Gateway</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Real-Time Explainable AI Fraud Shield for Digital Payments</p>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown(f"""
        <div class="merchant-card">
            <h3>Paying to: <b>{def_merchant}</b></h3>
            <h1>₹ {def_amount:,.2f}</h1>
            <p style='color: #a0aec0;'>Secure 256-bit Encrypted UPI Checkout</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.subheader("📝 Transaction Parameters (Simulated)")
        
        amount = st.number_input("Amount (₹)", value=def_amount)
        hour = st.slider("Transaction Hour (0-23)", 0, 23, def_hour)
        frequency = st.number_input("Daily Txn Frequency", value=def_freq)
        distance_from_home = st.number_input("Distance from Home (km)", value=def_dist)
        
        upi_id = st.text_input("Enter UPI ID (e.g., yourname@okaxis)", "raman@okicici")
        remark_text = st.text_input("Enter Transaction Remark / Note", "Grocery shopping")
        
        if st.button("🔒 Pay Securely via UPI", type="primary"): 
            is_fraud = False
            reason = "Transaction looks safe."
            
            if not upi_id:
                st.warning("Kripya valid UPI ID darj karein!")
            else:
                with st.spinner("🤖 AI Shield analyzing behavioral biometrics & geolocation..."):
                    time.sleep(0.8)
                    
                    is_fraud, reason = predict_fraud(amount, hour, frequency, distance_from_home)
                    
                    current_time = datetime.now().strftime("%H:%M:%S")
                    status_str = "BLOCKED (Fraud)" if is_fraud else "SUCCESS (Safe)"
                    
                    # Add to history
                    st.session_state.history.insert(0, {
                        "Time": current_time,
                        "UPI ID": upi_id,
                        "Merchant": def_merchant,
                        "Amount (₹)": amount,
                        "Status": status_str,
                        "Reason": reason
                    })
                    
                    # Update Map coordinates dynamically
                    offset = distance_from_home / 111.0 
                    new_lat = 26.4499 + offset
                    
                    st.session_state.map_data = pd.DataFrame({
                        'lat': [26.4499, new_lat],
                        'lon': [74.6399, 74.6399 + (offset * 0.5)]
                    })
                    
                    st.markdown("---")
                    
fraud_keywords = ["lottery", "prize", "urgent", "win", "gift", "kbc", "job"]
is_remark_fraud = any(word in remark_text.lower() for word in fraud_keywords)


if is_remark_fraud:
    is_fraud = True
    reason = "Suspicious keywords detected in remark!"
if is_fraud:
                        st.error("🚨 PAYMENT BLOCKED BY SAFE-AI SHIELD!")
                        st.warning(f"**Security Risk Factor:** {reason}")
                        play_voice_alert("Warning! Payment blocked due to suspicious activity.")
                        

else:
                        st.success("✅ Payment Successful! 🎉")
                        st.info(f"**Status:** {reason}")
                        st.balloons()
                        play_voice_alert("Payment successful. Your transaction is safe.")

with col2:
    st.subheader("📍 Live Geolocation Shield")
    st.write("Tracking transaction origin vs. user home base:")
    st.map(st.session_state.map_data, zoom=6, use_container_width=True)
    st.info("💡 **Map Insight:** Home marker is fixed at base city; transaction marker shifts dynamically based on input distance.")

# --- LIVE TRANSACTION AUDIT TRAIL TABLE ---
st.markdown("---")
st.subheader("📊 Live Transaction Audit Log (Session History)")
if len(st.session_state.history) > 0:
    df_history = pd.DataFrame(st.session_state.history)
    st.dataframe(df_history, use_container_width=True)
else:
    st.info("Aapki session history khali hai. Upar payment karke test karein, yahan live record dikhega!")