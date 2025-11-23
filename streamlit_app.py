<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Application</title>

    <!-- Merged CSS -->
    <style>
        /* ----- Global Styling ----- */
        body {
            margin: 0;
            font-family: "Poppins", sans-serif;
            background: linear-gradient(135deg, #d9f056, #c6f742);
            color: white;
            min-height: 100vh;
        }

        /* ----- Header ----- */
        header {
            text-align: center;
            padding: 30px 20px;
            background: rgba(11, 134, 235, 0.95);
            backdrop-filter: blur(8px);
            border-bottom: 3px solid rgba(13, 183, 226, 0.95);
            box-shadow: 0 4px 10px rgba(0,0,0,0.25);
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
            margin-top: 50px;
            gap: 22px;
        }

        /* ----- Navigation Button Style ----- */
        .nav-item {
            text-decoration: none;
            font-size: 20px;
            font-weight: 600;
            color: #fff;
            background: rgba(218, 48, 48, 0.95);
            padding: 15px 25px;
            width: 300px;
            text-align: center;
            border-radius: 14px;
            transition: 0.3s;
            border: 2px solid rgba(216, 11, 11, 1);
            box-shadow: 0 3px 8px rgba(0,0,0,0.25);
            transform: scale(1);
        }

        /* ----- Hover Effects ----- */
        .nav-item:hover {
            background: #4f46e5;
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 0 18px #4f46e5;
        }

        /* ----- Active Button ----- */
        .nav-item.active {
            background: #cf1212;
            box-shadow: 0 0 20px #5d0a0a;
            transform: scale(1.08);
        }

        /* ----- Click Animation ----- */
        .nav-item:active {
            transform: scale(0.97);
        }

        /* ----- Fade Animation ----- */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* ----- Responsive ----- */
        @media (max-width: 600px) {
            .nav-item {
                width: 90%;
                font-size: 18px;
                border-radius: 12px;
            }

            header h1 {
                font-size: 22px;
            }
        }
    </style>

</head>
<body>

    <header>
        <h1>Interactive Multi-Dashboard Web Application</h1>
    </header>

    <nav class="dashboard-nav">
        <a href="https://liveweather-b6xdypvrjpxv5yzk2w7deo.streamlit.app/" class="nav-item active">LIVE WEATHER</a>
        <a href="https://cryptodashboardlive-eejx4koj7t5wvkyeuou5hz.streamlit.app/" class="nav-item">CRYPTO DASHBOARD LIVE</a>
        <a href="https://news-dashboard-gbfxoy46ttutjpevyrws7k.streamlit.app/" class="nav-item">NEWS DASHBOARD</a>
    </nav>

</body>
</html>