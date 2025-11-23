import streamlit as st
import streamlit.components.v1 as components

# 1. Configure the Streamlit page
st.set_page_config(page_title="Dashboard Hub", layout="wide")

# 2. Your HTML & CSS Code
# IMPORTANT: This must be wrapped in triple quotes (""") so Python treats it as text, not code.
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        /* ----- Global Styling ----- */
        body {
            margin: 0;
            font-family: "Poppins", sans-serif;
            background: linear-gradient(135deg, #d9f056, #c6f742);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }

        /* ----- Header ----- */
        header {
            text-align: center;
            padding: 30px 20px;
            background: rgba(11, 134, 235, 0.863);
            backdrop-filter: blur(8px);
            border-bottom: 2px solid rgba(13, 183, 226, 0.795);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            width: 100%;
            box-sizing: border-box;
        }

        header h1 {
            font-size: 32px;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 2px;
            animation: fadeInDown 1s ease;
        }

        /* ----- Navigation Menu ----- */
        .dashboard-nav {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 40px;
            gap: 20px;
            padding-bottom: 40px;
            width: 100%;
        }

        /* ----- Navigation Button Style ----- */
        .nav-item {
            text-decoration: none;
            font-size: 20px;
            color: #fff;
            background: rgba(218, 48, 48, 0.918);
            padding: 14px 25px;
            width: 280px;
            text-align: center;
            border-radius: 12px;
            transition: 0.3s ease-in-out;
            border: 1px solid rgba(216, 11, 11, 0.973);
            transform: scale(1);
            cursor: pointer;
            display: block;
        }

        /* ----- Hover Effects ----- */
        .nav-item:hover {
            background: #4f46e5;
            transform: scale(1.06);
            box-shadow: 0 0 15px #4f46e5;
        }

        /* ----- Active Button ----- */
        .nav-item.active {
            background: #cf1212;
            box-shadow: 0 0 18px rgba(10, 6, 15, 0.5);
            transform: scale(1.07);
        }

        /* ----- Fade Animation ----- */
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* ----- Responsive ----- */
        @media (max-width: 600px) {
            .nav-item { width: 90%; font-size: 18px; }
            header h1 { font-size: 22px; }
        }
    </style>
</head>
<body>
    <header>
        <h1>Interactive Multi-Dashboard Web Application</h1>
    </header>

    <nav class="dashboard-nav">
        <a href="https://liveweather-b6xdypvrjpxv5yzk2w7deo.streamlit.app/" target="_blank" class="nav-item active">LIVE WEATHER</a>
        <a href="https://cryptodashboardlive-eejx4koj7t5wvkyeuou5hz.streamlit.app/" target="_blank" class="nav-item">CRYPTO DASHBOARD LIVE</a>
        <a href="https://news-dashboard-gbfxoy46ttutjpevyrws7k.streamlit.app/" target="_blank" class="nav-item">NEWS DASHBOARD</a>
    </nav>
</body>
</html>
"""

# 3. Render the HTML
components.html(html_code, height=800, scrolling=True)

# 4. Hide Default Streamlit Elements
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
