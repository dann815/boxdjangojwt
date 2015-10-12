# boxdjangojwt

Box Python SDK: https://github.com/box/box-python-sdk
### Step 1: Install python, django, and the SDKs OR use the provided /venv 

python 2.7

django 1.8

pip install boxsdk

pip install boxsdk[jwt]

OR source venv/bin/activate


### Step 2: Generate your RSA keys

openssl genrsa -out rsakey.pem 2048

openssl rsa -pubout -in rsakey.pem -out rsapublic.pem


### Step 4: Input your RSA keys

Add the public key to your app at developers.box.com 

Put the private key in your project folder at /box/rsakey.pem


### Step 5: Set environment variables

On Mac: Open ~/.bash_profile in a text editor and add the following lines (with your values from developers.box.com)

export BOX_SDK_CLIENTID=1234567890ABCD

export BOX_SDK_CLIENTSECRET=ABCDEFGHI1234

export BOX_SDK_EID=123456


### Step 6: Run the code

python manage.py runserver

Navigate to http://localhost:8000/box/
