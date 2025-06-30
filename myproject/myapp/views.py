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
                background: linear-gradient(145deg, #2d2f33, #0c1117);
                margin: 0;
                padding: 50px 20px;
                color: #eaf6ff;
            }
            .wrapper {
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 40px;
            }
            .container {
                background-color: #1a1c20;
                color: #dceeff;
                padding: 30px 40px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(102, 178, 255, 0.2);
                max-width: 900px;
                width: 100%;
                animation: fadeIn 1s ease-in;
                border: 1px solid #66b2ff;
            }
            h1, h2 {
                color: #87ceeb;
            }
            p {
                font-size: 1.1rem;
                color: #aacde7;
                margin-bottom: 20px;
            }
            .topics {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                margin-bottom: 20px;
            }
            .btn {
                background-color: #66b2ff;
                color: white;
                padding: 10px 16px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-weight: 600;
                text-decoration: none;
                display: block;
                transition: background 0.3s ease;
                text-align: center;
            }
            .btn:hover {
                background-color: #87ceeb;
            }
            details {
                background: #25282e;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 15px;
            }
            summary {
                font-size: 1.2rem;
                font-weight: 600;
                cursor: pointer;
                margin-bottom: 10px;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(30px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="wrapper">

            <!-- DevOps Section -->
            <div class="container">
                <h1>🚀 DevOps Essentials</h1>
                <p>Explore DevOps technologies with guided topics and official documentation:</p>
                <div class="topics">
                    <details>
                        <summary>🐳 Docker</summary>
                        <a class="btn" href="https://dockerlabs.collabnix.com/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://docs.docker.com/" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>⚙️ Jenkins</summary>
                        <a class="btn" href="https://www.jenkins.io/doc/book/pipeline/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://www.jenkins.io/doc/" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>☸️ Kubernetes</summary>
                        <a class="btn" href="https://kubernetes.io/docs/concepts/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://kubernetes.io/docs/home/" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>🤖 GitHub Actions</summary>
                        <a class="btn" href="https://docs.github.com/en/actions/learn-github-actions" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://docs.github.com/en/actions" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>🌍 Terraform</summary>
                        <a class="btn" href="https://developer.hashicorp.com/terraform/tutorials" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://www.terraform.io/docs" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>🛠️ Ansible</summary>
                        <a class="btn" href="https://www.ansible.com/blog/getting-started-automation-ansible/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://www.ansible.com/resources/get-started" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>📊 Prometheus</summary>
                        <a class="btn" href="https://prometheus.io/docs/introduction/first_steps/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://prometheus.io/docs/introduction/overview/" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>📈 Grafana</summary>
                        <a class="btn" href="https://grafana.com/tutorials/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://grafana.com/docs/" target="_blank">Official Docs</a>
                    </details>
                </div>
            </div>

            <!-- AWS Section -->
            <div class="container">
                <h2>☁️ AWS Essentials</h2>
                <p>Understand the core AWS services used in real-world DevOps workflows:</p>
                <div class="topics">
                    <details>
                        <summary>🖥️ EC2</summary>
                        <a class="btn" href="https://aws.amazon.com/ec2/getting-started/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://docs.aws.amazon.com/ec2/" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>📦 ECS</summary>
                        <a class="btn" href="https://aws.amazon.com/getting-started/hands-on/run-docker-containers-ecs-fargate/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>⚡ Lambda</summary>
                        <a class="btn" href="https://aws.amazon.com/lambda/getting-started/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://docs.aws.amazon.com/lambda/latest/dg/welcome.html" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>🗄️ S3</summary>
                        <a class="btn" href="https://aws.amazon.com/s3/getting-started/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://docs.aws.amazon.com/s3/" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>🏗️ CloudFormation</summary>
                        <a class="btn" href="https://aws.amazon.com/cloudformation/getting-started/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://docs.aws.amazon.com/cloudformation/" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>🔍 CloudWatch</summary>
                        <a class="btn" href="https://aws.amazon.com/cloudwatch/getting-started/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://docs.aws.amazon.com/cloudwatch/" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>📟 AWS CLI</summary>
                        <a class="btn" href="https://aws.amazon.com/cli/getting-started/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html" target="_blank">Official Docs</a>
                    </details>
                    <details>
                        <summary>🔐 IAM</summary>
                        <a class="btn" href="https://aws.amazon.com/iam/getting-started/" target="_blank">Topics to Cover</a>
                        <a class="btn" href="https://aws.amazon.com/iam/" target="_blank">Official Docs</a>
                    </details>
                </div>
            </div>

        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
