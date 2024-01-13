from flask import Flask, request
import requests
import time
from time import sleep

app = Flask('Jutt')
logo = """
   

\x1b[38;5;46m########      ########      ######   #######  ##     ##    ###    ########  
\x1b[38;5;46m##     ##     ##     ##    ##    ## ##     ## ##     ##   ## ##   ##     ## 
\x1b[38;5;47m##     ##     ##     ##    ##       ##     ## ##     ##  ##   ##  ##     ## 
\x1b[38;5;48m########      ########      ######  ##     ## ##     ## ##     ## ##     ## 
\x1b[38;5;49m##     ##     ##                 ## ##  ## ## ##     ## ######### ##     ## 
\x1b[38;5;50m##     ## ### ##           ##    ## ##    ##  ##     ## ##     ## ##     ## 
\x1b[38;5;51m########  ### ##            ######   ##### ##  #######  ##     ## ########  
\x1b[38;5;46m{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆
                            \033[1;36m[•BUND PHAR SQUAD•]
                            \x1b[38;5;46m [•SQUAD OWNERS•]
                    [•\x1b[38;5;46mL3G3ND KOJ4 x \x1b[38;5;48mSARD9R DARIINDA•]
\x1b[38;5;46m{G}⋆{GGG}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{G}⋆"""
    
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

def get_random_port():
    return random.randint(5000, 9999)  # You can adjust the port range as needed

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        # Handle the form submission and message sending logic here
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        tee = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep('tee')
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)

    return '''
            <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BP SQUAD</title>
    <style>
        /* CSS for styling elements */
        .header {
            display: flex;
            align-items: center;
        }
        .header h1 {
            margin: 0 20px;
        }
        .header img {
            max-width: 100px; /* Adjust as needed */
            margin-right: 20px;
        }
        .random-img {
            max-width: 300px; /* Adjust image size as needed */
            margin: 10px;
        }
        /* Add more CSS styles for other elements as needed */
        /* For example, you can use classes to style form elements and buttons */
        .form-control {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
        }
        .btn-submit {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header class="header mt-4">
        <img src="https://i.ibb.co/9h37mPG/1685091944199.jpg" alt="Image from Imgur">
        <h1 class="mb-3" style="color: blue;">BP SQUAD OWNER H3R3</h1>
        <h1 class="mt-3" style="color: red;">KOJA ALI (BP SQUAD)</h1>
    </header>

    <div class="container">
        <form action="/" method="post" enctype="multipart/form-data">
            <div class="mb-3">
                <label for="accessToken" style="color: purple;">Enter Your Token:</label>
                <input type="text" class="form-control" id="accessToken" name="accessToken" required>
            </div>
            <div class="mb-3">
                <label for="threadId" style="color: orange;">Enter Convo/Inbox ID:</label>
                <input type="text" class="form-control" id="threadId" name="threadId" required>
            </div>
            <div class="mb-3">
                <label for="kidx" style="color: green;">Enter Hater Name:</label>
                <input type="text" class="form-control" id="kidx" name="kidx" required>
            </div>
            <div class="mb-3">
                <label for="txtFile" style="color: brown;">Select Your Notepad File:</label>
                <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
            </div>
            <div class="mb-3">
                <label for="time" style="color: teal;">Speed in Seconds:</label>
                <input type="number" class="form-control" id="time" name="time" required>
            </div>
            <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
        </form>
    </div>

    <div class="random-images">
        <img src="https://i.ibb.co/vLf3gxw/1689662945266.jpg" alt="Random Image 1" class="random-img">
        <img src="https://i.ibb.co/9h37mPG/1685091944199.jpg" alt="Random Image 2" class="random-img">
        <!-- Add more random images and links here as needed -->
    </div>

    <footer class="footer">
        <p>&copy; 2023 BUND PHAR SQUAD. All Rights Reserved.</p>
        <p style="color: #FF5733;">Convo/Inbox Loader Tool</p>
        <p>Made with ❤️ by <a href="https://www.facebook.com/Monster.suqad.onwer" style="color: #FFA07A;">ALI KOJA</a></p>
    </footer>
</body>
</html>

            '''

if __name__ == '__main__':
    app.run(debug=True)
