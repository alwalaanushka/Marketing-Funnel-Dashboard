import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Marketing Funnel Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
MAIN BACKGROUND
===================================================== */

.stApp{
    background-color:#020b1c;
    color:white;
}

/* =====================================================
REMOVE STREAMLIT HEADER + WHITE SPACE
===================================================== */

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

/* REMOVE TOP TOOLBAR */

[data-testid="stToolbar"]{
    display:none;
}

/* REMOVE TOP WHITE LINE */

div[data-testid="stDecoration"]{
    display:none;
}

/* REMOVE TOP SPACE */

.block-container{
    padding-top:0rem !important;
    margin-top:0rem !important;
    padding-left:1rem;
    padding-right:1rem;
    padding-bottom:1rem;
    max-width:100%;
}

/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"]{
    background-color:#010814;
    width:260px !important;
}

/* SIDEBAR TEXT */

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* =====================================================
METRIC CARDS
===================================================== */

.metric-card{
    background:#071b34;
    padding:20px;
    border-radius:15px;
    border:1px solid #123456;
    box-shadow:0px 0px 12px rgba(0,0,0,0.5);
}

/* METRIC TITLE */

.metric-title{
    font-size:18px;
    color:white;
}

/* METRIC VALUE */

.metric-value{
    font-size:42px;
    font-weight:bold;
    color:white;
}

/* METRIC GROWTH */

.metric-growth{
    color:#39ff6c;
    font-size:16px;
    font-weight:bold;
}

/* =====================================================
CHART BOX
===================================================== */

.chart-box{
    background:#071b34;
    padding:20px;
    border-radius:15px;
    border:1px solid #123456;
    margin-top:15px;
}

/* =====================================================
TITLES
===================================================== */

h1,h2,h3,h4{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("""
<h1 style='text-align:center;color:white;'>
📊 FUNNEL<br>DASHBOARD
</h1>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Funnel Analysis",
        "Performance",
        "Channels",
        "Campaigns",
        "Reports",
        "Insights",
        "Settings"
    ]
)

# =========================================================
# COMMON DATA
# =========================================================

stages = [
    "Website Visitors",
    "Leads",
    "Qualified Leads",
    "Opportunities",
    "Customers"
]

values = [10000,7000,5000,3000,1500]

dropoff = [30,28.57,40,50]

# =========================================================
# OVERVIEW PAGE
# =========================================================

if page == "Overview":

    st.title("📊 Marketing Funnel & Conversion Performance Analysis")

    # =====================================================
    # METRICS
    # =====================================================

    c1,c2,c3,c4,c5 = st.columns(5)

    cards = [
        ("Website Visitors","10,000","↑ 12.5%"),
        ("Leads","7,000","↑ 8.7%"),
        ("Qualified Leads","5,000","↑ 6.3%"),
        ("Opportunities","3,000","↑ 5.1%"),
        ("Customers","1,500","↑ 4.2%")
    ]

    for col,card in zip([c1,c2,c3,c4,c5],cards):

        title,value,growth = card

        with col:

            st.markdown(f"""
            <div class='metric-card'>
                <div class='metric-title'>{title}</div>
                <div class='metric-value'>{value}</div>
                <div class='metric-growth'>{growth} vs last year</div>
            </div>
            """, unsafe_allow_html=True)

    # =====================================================
    # MAIN CHARTS
    # =====================================================

    left,right = st.columns([1.1,1])

    with left:

        st.markdown("<div class='chart-box'>", unsafe_allow_html=True)

        st.subheader("Marketing Funnel")

        funnel = go.Figure(go.Funnel(
            y=stages,
            x=values,
            textinfo="value+percent initial",
            marker={
                "color":[
                    "#1f77ff",
                    "#2ecc71",
                    "#ffcc00",
                    "#8e44ff",
                    "#ff4d6d"
                ]
            }
        ))

        funnel.update_layout(
            paper_bgcolor="#071b34",
            plot_bgcolor="#071b34",
            font=dict(color="white"),
            height=550
        )

        st.plotly_chart(funnel,use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with right:

        st.markdown("<div class='chart-box'>", unsafe_allow_html=True)

        st.subheader("Conversion Drop-Off Analysis")

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=stages,
            y=values,
            marker_color="#1f77ff"
        ))

        fig.add_trace(go.Scatter(
            x=stages[1:],
            y=dropoff,
            mode="lines+markers+text",
            text=[f"{i}%" for i in dropoff],
            textposition="top center",
            line=dict(color="#39ff6c",width=4),
            yaxis="y2"
        ))

        fig.update_layout(
            paper_bgcolor="#071b34",
            plot_bgcolor="#071b34",
            font=dict(color="white"),
            height=550,

            yaxis=dict(title="Customers"),

            yaxis2=dict(
                title="Drop-off %",
                overlaying="y",
                side="right"
            )
        )

        st.plotly_chart(fig,use_container_width=True)

        st.error(
            "Biggest Drop-off Stage : Opportunities → Customers"
        )

        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # BOTTOM CHARTS
    # =====================================================

    b1,b2,b3 = st.columns([1.1,1,1])

    with b1:

        st.markdown("<div class='chart-box'>", unsafe_allow_html=True)

        st.subheader("Funnel Conversion Rate")

        pie = go.Figure(data=[go.Pie(
            labels=stages,
            values=values,
            hole=0.65
        )])

        pie.update_layout(
            paper_bgcolor="#071b34",
            plot_bgcolor="#071b34",
            font=dict(color="white"),
            height=400
        )

        st.plotly_chart(pie,use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with b2:

        st.markdown("<div class='chart-box'>", unsafe_allow_html=True)

        st.subheader("Top Channels by Conversion Rate")

        channel_df = pd.DataFrame({
            "Channel":[
                "Organic Search",
                "Email Campaign",
                "Social Media",
                "Paid Search",
                "Direct"
            ],
            "Rate":[18.5,16.2,14.3,13.1,10.4]
        })

        bar = px.bar(
            channel_df,
            x="Rate",
            y="Channel",
            orientation="h",
            text="Rate"
        )

        bar.update_layout(
            paper_bgcolor="#071b34",
            plot_bgcolor="#071b34",
            font=dict(color="white"),
            height=400
        )

        st.plotly_chart(bar,use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with b3:

        st.markdown("<div class='chart-box'>", unsafe_allow_html=True)

        st.subheader("Key Insights")

        st.success("Overall conversion rate is 15.50%")
        st.warning("Biggest drop-off occurs at Opportunities → Customers")
        st.info("Improve lead nurturing to increase Qualified Leads")
        st.success("Focus on Organic Search and Email Campaigns")

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FUNNEL ANALYSIS
# =========================================================

elif page == "Funnel Analysis":

    st.title("📊 Funnel Analysis")

    df = pd.DataFrame({
        "Stage":stages,
        "Users":values
    })

    st.dataframe(df,use_container_width=True)

    fig = px.line(
        df,
        x="Stage",
        y="Users",
        markers=True
    )

    fig.update_layout(
        paper_bgcolor="#071b34",
        plot_bgcolor="#071b34",
        font=dict(color="white")
    )

    st.plotly_chart(fig,use_container_width=True)

# =========================================================
# PERFORMANCE
# =========================================================

elif page == "Performance":

    st.title("📈 Performance Dashboard")

    perf = pd.DataFrame({
        "Month":[
            "Jan","Feb","Mar","Apr",
            "May","Jun","Jul","Aug"
        ],
        "Revenue":[
            20000,25000,28000,32000,
            36000,41000,46000,52000
        ]
    })

    fig = px.area(
        perf,
        x="Month",
        y="Revenue"
    )

    fig.update_layout(
        paper_bgcolor="#071b34",
        plot_bgcolor="#071b34",
        font=dict(color="white")
    )

    st.plotly_chart(fig,use_container_width=True)

# =========================================================
# CHANNELS
# =========================================================

elif page == "Channels":

    st.title("📢 Marketing Channels")

    df = pd.DataFrame({
        "Channel":[
            "Organic Search",
            "Email Campaign",
            "Social Media",
            "Paid Search",
            "Direct"
        ],
        "Conversion Rate":[
            18.5,16.2,14.3,13.1,10.4
        ]
    })

    st.dataframe(df,use_container_width=True)

# =========================================================
# CAMPAIGNS
# =========================================================

elif page == "Campaigns":

    st.title("🎯 Campaign Performance")

    campaign = pd.DataFrame({
        "Campaign":[
            "Google Ads",
            "Facebook Ads",
            "Instagram Ads",
            "Email Campaign"
        ],
        "ROI":[140,120,110,160]
    })

    fig = px.bar(
        campaign,
        x="Campaign",
        y="ROI",
        text="ROI"
    )

    fig.update_layout(
        paper_bgcolor="#071b34",
        plot_bgcolor="#071b34",
        font=dict(color="white")
    )

    st.plotly_chart(fig,use_container_width=True)

# =========================================================
# REPORTS
# =========================================================

elif page == "Reports":

    st.title("📄 Advanced Reports Dashboard")

    r1,r2,r3,r4 = st.columns(4)

    r1.metric("Visitors","10,000","+12%")
    r2.metric("Leads","7,000","+8%")
    r3.metric("Customers","1,500","+5%")
    r4.metric("Revenue","$52,000","+15%")

# =========================================================
# INSIGHTS
# =========================================================

elif page == "Insights":

    st.title("💡 Business Insights")

    st.success("Organic Search gives best conversion.")
    st.warning("Customer drop-off is high after Opportunities.")
    st.info("Improve email nurturing campaigns.")

# =========================================================
# SETTINGS
# =========================================================

elif page == "Settings":

    st.title("⚙️ Dashboard Settings")

    st.toggle(
        "Enable Dark Mode",
        value=True
    )

    st.checkbox(
        "Enable Animations",
        value=True
    )

    st.checkbox(
        "Email Notifications",
        value=True
    )

    st.checkbox(
        "Weekly Reports",
        value=True
    )

    st.slider(
        "Refresh Rate",
        5,
        60,
        15
    )

    if st.button("💾 Save Settings"):

        st.success(
            "Settings Saved Successfully!"
        )