# views.py
from django.http import HttpResponse

def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps Learning Portal</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Inter', sans-serif;
                background: linear-gradient(145deg, #2b2b2b, #5a3d7b); /* softened purple tone */
                margin: 0;
                padding: 50px 20px;
                color: #fff;
            }
            .wrapper {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 40px;
            }
            .container {
                background-color: #1e1e1e;
                color: #e0e0e0;
                padding: 40px 50px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(180, 130, 255, 0.2);
                max-width: 900px;
                width: 100%;
                text-align: center;
                animation: fadeIn 1s ease-in;
                border: 1px solid #a183c8;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
                color: #d2b4ff;
            }
            h2 {
                font-size: 1.8rem;
                margin: 20px 0 10px;
                color: #e0c9ff;
            }
            p {
                font-size: 1.1rem;
                color: #bbb;
                margin-bottom: 30px;
            }
            .topics {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
            }
            .btn {
                background-color: #a183c8;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-weight: 600;
                text-decoration: none;
                display: inline-block;
                transition: background 0.3s ease;
            }
            .btn:hover {
                background-color: #c8a2ff;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="wrapper">

            <!-- DevOps Container -->
            <div class="container">
                <h1>🚀 DevOps Essentials</h1>
                <p>Explore essential DevOps tools and technologies with official documentation links:</p>
                <div class="topics">
                    <a class="btn" href="https://docs.docker.com/" target="_blank">🐳 Docker</a>
                    <a class="btn" href="https://www.jenkins.io/doc/" target="_blank">⚙️ Jenkins</a>
                    <a class="btn" href="https://kubernetes.io/docs/home/" target="_blank">☸️ Kubernetes</a>
                    <a class="btn" href="https://docs.github.com/en/actions" target="_blank">🤖 GitHub Actions</a>
                    <a class="btn" href="https://www.terraform.io/docs" target="_blank">🌍 Terraform</a>
                    <a class="btn" href="https://www.ansible.com/resources/get-started" target="_blank">🛠️ Ansible</a>
                    <a class="btn" href="https://prometheus.io/docs/introduction/overview/" target="_blank">📊 Prometheus</a>
                    <a class="btn" href="https://grafana.com/docs/" target="_blank">📈 Grafana</a>
                </div>
            </div>

            <!-- AWS Container -->
            <div class="container">
                <h2>☁️ AWS Essentials</h2>
                <p>Key AWS services every DevOps engineer should know:</p>
                <div class="topics">
                    <a class="btn" href="https://docs.aws.amazon.com/ec2/" target="_blank">🖥️ EC2</a>
                    <a class="btn" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html" target="_blank">📦 ECS</a>
                    <a class="btn" href="https://docs.aws.amazon.com/lambda/latest/dg/welcome.html" target="_blank">⚡ Lambda</a>
                    <a class="btn" href="https://docs.aws.amazon.com/s3/" target="_blank">🗄️ S3</a>
                    <a class="btn" href="https://docs.aws.amazon.com/cloudformation/" target="_blank">🏗️ CloudFormation</a>
                    <a class="btn" href="https://docs.aws.amazon.com/cloudwatch/" target="_blank">🔍 CloudWatch</a>
                    <a class="btn" href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html" target="_blank">📟 AWS CLI</a>
                    <a class="btn" href="https://aws.amazon.com/iam/" target="_blank">🔐 IAM</a>
                </div>
            </div>

        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
