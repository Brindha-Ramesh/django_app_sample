# views.py
from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Django App</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(120deg, #84fab0, #8fd3f4);
                height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .card {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 8px 16px rgba(0,0,0,0.3);
                text-align: center;
            }
            h1 {
                color: #2c3e50;
                margin-bottom: 10px;
            }
            p {
                color: #555;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello from Docker!</h1>
            <p>This is a Django app running in a container 🚀</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
