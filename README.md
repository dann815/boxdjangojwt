# boxdjangojwt  
Read the comments in the code.  They will help :)  
Everything important is at /box/views.py  


### Step 0: Pull code  
git clone https://github.com/dann815/boxdjangojwt.git 

### Step 1: Install packages
python 2.7.10  **Note: Does not work with 3.x**  
django 1.8  
pip install boxsdk  
pip install boxsdk[jwt]  

### Step 2: Generate your RSA keys  
openssl genrsa -out rsakey.pem 2048  
openssl rsa -pubout -in rsakey.pem -out rsapublic.pem  

### Step 3: Input your RSA keys  
cat rsapublic.pem | pbcopy  
Add the public key to your app at developers.box.com  
Put the private key in your project folder at /box/rsakey.pem  

### Step 4: Set environment variables  
On Mac: Open ~/.bash_profile in a text editor and add the following lines (with your values from developers.box.com)  
export BOX_SDK_CLIENTID=1234567890ABCD  
export BOX_SDK_CLIENTSECRET=ABCDEFGHI1234  
export BOX_SDK_EID=123456  

### Step 5: Run the code  
python manage.py runserver  
Navigate to http://localhost:8000/box/  

#### Box SDK can be found at
https://github.com/box/box-python-sdk  

Contact: DanK@box.com
