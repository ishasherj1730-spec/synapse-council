# Synapse Council
# Main Streamlit Interface
import streamlit as st
from datetime import datetime
import re
import time
from agents import council_agent

st.set_page_config(
    page_title="Synapse Council",
    page_icon="🧠",
    layout="wide"
)
st.markdown("""
<style>

.hero-box{
    animation: float 2s ease-in-out infinite;
}

@keyframes float{
    0%{
        transform:translateY(0px);
    }
    50%{
        transform:translateY(-4px);
    }
    100%{
        transform:translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* Background glow */

[data-testid="stAppViewContainer"]{
background:
radial-gradient(circle at 20% 20%,
rgba(139,92,246,0.12) 0%,
transparent 25%),

radial-gradient(circle at 80% 10%,
rgba(6,182,212,0.10) 0%,
transparent 25%),

#0E1117;
}


/* Logo glow */

[data-testid="stSidebar"] img{
filter:
drop-shadow(0 0 8px rgba(139,92,246,0.6))
drop-shadow(0 0 12px rgba(6,182,212,0.5));
}


/* Button hover effect */

.stButton > button:hover{
transform: translateY(-2px);
transition: 0.2s;
box-shadow: 0 0 12px rgba(139,92,246,0.35);
}


/* Fade in animation */

.main{
animation: fadeIn 0.6s ease;
}

@keyframes fadeIn{
from{
opacity:0;
transform:translateY(10px);
}
to{
opacity:1;
transform:translateY(0px);
}
}

</style>
""", unsafe_allow_html=True)


if "history" not in st.session_state:
    st.session_state.history = []
if "council_response" not in st.session_state:
    st.session_state.council_response = None
if "selected_report" not in st.session_state:
    st.session_state.selected_report = None
if "current_chat" not in st.session_state:
    st.session_state.current_chat = None
if "question_box" not in st.session_state:
    st.session_state.question_box = ""
with st.sidebar:
    col1, col2, col3 = st.sidebar.columns([1, 2, 1])

    with col2:
        st.image("logo.png", width=500)
    st.subheader(
        "Multi-Agent Decision Intelligence System",
    )
    st.divider()
    st.subheader("⚡ Actions")

    if st.button(
        "➕ New Decision",
        use_container_width=True
    ):
        st.session_state.question_box = ""
        st.session_state.council_response = None
        st.session_state.current_chat= None
        st.rerun()


    st.subheader("📊 Session Stats")

    st.metric(
        "Decisions Analyzed",
        len(st.session_state.history)
    )

    st.subheader("🕒 Recent Decisions")

    if not st.session_state.history:

        st.caption(" Your decision history will appear here.")

    else:

        for idx, item in enumerate(
            reversed(st.session_state.history[-10:])
        ):

            preview = (
                item["question"][:30] + "..."
                if len(item["question"]) > 30
                else item["question"]
            )

            

            if st.button(
                f"📄 {preview}",
                key=f"history_{idx}",
                use_container_width=True
            ):

                st.session_state.question_box = item["question"]

                st.session_state.current_chat = item

                st.rerun()
    

st.markdown(
    """
    <h1 style="
        text-align:center;
        margin-bottom:0;
        font-weight:800;
        background:linear-gradient(
            90deg,
            #8B5CF6,
            #06B6D4
        );
        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
        filter:drop-shadow(
            0 0 8px rgba(139,92,246,.35)
        );
    ">
        Synapse Council
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='
    text-align:center;
    color:#9CA3AF;
    font-size:20px;
    '>
    Multiple Minds. One Decision.
    </h4>
    """,
    unsafe_allow_html=True
)
left,center,right = st.columns([1,3,1])
with center:
    st.markdown(
        """
        <div class="hero-box" style="
            text-align:center;
            padding:15px;
            border-radius:14px;
            background:#111827;
            border:1px solid #374151;
            margin-bottom:15px;
        ">
            <h2>Welcome Isha Sherj,</h2>

            Describe a decision and get expert AI guidance.
        </div>
        """,
        unsafe_allow_html=True
    )
if "question_box" not in st.session_state:
    st.session_state.question_box = ""

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button(" German or French?"):
        st.session_state.question_box = (
            "Should I learn German or French?"
        )

with col2:
    if st.button(" Buy Laptop now?"):
        st.session_state.question_box = (
            "Should I buy a laptop now or wait?"
        )

with col3:
    if st.button("Walk or Drive?"):
        st.session_state.question_box = (
            "Should I walk or drive to the office which is just 2 kms away ?"
        )
        
with col4:
    if st.button("Study now ?"):
        st.session_state.question_box = (
            "Should I study now or later?"
        )

with col5:
    if st.button("Gym or Yoga?"):
        st.session_state.question_box = (
            "Should I do gym or yoga?"
        )
question = st.text_area(
    "",
    height=200,
    key="question_box"
)


if st.button("🏛️ Convene Council"):
    if not question or question.strip() == "":
        st.warning("Please enter a decision first before convening the council.")
        st.stop()

    status = st.empty()

    with st.spinner("🏛️ Council members are debating your decision..."):

        agents = [
            "📊 Dr. Logic joined",
            "⚠️ Risk Sentinel joined",
            "🚀 Opportunity Scout joined",
            "🔮 Future Visionary joined",
            "⚖️ Ethics Guardian joined",
            "👑 Council Chair joined"
        ]

        for agent in agents:
            status.info(agent)
            time.sleep(1.5)

        status.info(
            "🧠 Council is analyzing your decision..."
        )

        council_response = council_agent(question)
        
        decision_match = re.search(
            r"Final Decision:\s*(.*)",
            council_response
        )
    
        confidence_match = re.search(
            r"Confidence:\s*(\d+)",
            council_response
        )

        consensus_match = re.search(
            r"Consensus:\s*(\d+)",
            council_response
        )

        final_decision = (
            decision_match.group(1)
            if decision_match
            else "Unknown"
        )

        confidence = (
            int(confidence_match.group(1))
            if confidence_match
            else 75
        )

        consensus = (
            int(consensus_match.group(1))
            if consensus_match
            else 70
        )
       
       
        chat_data = {
            "question": question,
            "response": council_response,
            "final_decision": final_decision,
            "consensus": consensus,
            "time": datetime.now().strftime(
                "%d %b %H:%M"
            )
        }

        st.session_state.history.append(chat_data)

        st.session_state.current_chat = chat_data
        

        status.success(
        "✅ Council discussion completed!"
        )
        
    
chat = st.session_state.current_chat
if chat:
    
    st.subheader("🏆 Final Council Verdict")

    st.markdown(
        f"""
        <div style="
            padding: 20px;
            box-shadow: 0 0 15px rgba(0,255,153,0.3);
            border: 1px solid #00ff99;
            border-radius: 12px;
            background-color: #111;
            text-align: center;
        ">
            <p style="color:#ffffff; font-size:18px; margin-bottom:10px;">
            Recommended Decision
            </p>
            <p style="color:#00ff99; font-size:20px; font-weight:bold;">
                {chat["final_decision"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()

    st.subheader(
        "🔍 Why such a decision is made?"
    )

            

    with st.expander(
        "View Full Council Report",
        expanded=False
    ):
        st.markdown(chat["response"])
        
    
    st.download_button(
        "📄 Download Report",
        data=chat["response"],
        file_name="synapse_council_report.txt",
        mime="text/plain"
    )

    st.markdown(
        """
        <div style="text-align:center; color:gray;">
         🧠 Synapse Council • Multi-Agent Decision Intelligence System 
        </div>
        """,
        unsafe_allow_html=True
    )
    
