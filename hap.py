import smtplib
import getpass
from ImageListMaker import ImageListMaker
from SETTINGS import *
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# Import the email modules we'll need
#from email.mime.text import MIMEText




def main():

    # Create a "related" message container that will hold the HTML 
    # message and the image
    msg = MIMEMultipart(_subtype='related')

    # Create the body with HTML. Note that the image, since it is inline, is 
    # referenced with the URL cid:myimage... you should take care to make
    # "myimage" unique
    
    greeting = raw_input("Greeting: ")
    if (not greeting):
        greeting = "Good news, everyone!"
        
    message = raw_input("Message: ")
    if (not message):
        message = "Have a great day!"
    
    links = raw_input("Links: ")
    link_text = ""
    if (not links):
        link_text = "Sorry no links today, send me some so we can share the joy!"
    else:
        for line in links.split(","):
            link_text += "<p>" + line + "</p>"
            
    pictures = ""
    for i in range(10):
        pictures += "<p><img src=\"cid:image%d\" width=\"600\"/></p>" % i
    
    signature = raw_input("Signature: ")
    if (not signature):
        signature = "-(C)Atnip"
    
    content = ""
    content += "<p>" + greeting + "</p>" + "<p></p>"
    content += "<p>" + message + "</p>"
    content += "<p></p><p>" + signature + "</p><p></p>"
    content += "<p><b>Fun Links</b></p>"
    content += link_text
    content += "<p></p>" + "<p><b>And now the pictures</b></p>"
    content += pictures
    content += "<p></p>" + "<p>If you wish to no longer recieve these emails click <A HREF=\"mailto:tom.atnip@gmail.com?subject=Please remove me from <Random Cute and Awesome> mailing list\">HERE</A>"
    content += "</p><p>If you find a grammatical error click <A HREF=\"mailto:tom.atnip@gmail.com?subject=<Random Cute and Awesome> Grammar Error\">HERE</A> and specify it in the body, and if you\'re first"
    content += " I\'ll make you a cookie or something.</p><p>Suggestions and/or feedback click <A HREF=\"mailto:tom.atnip@gmail.com?subject=Comments for <Random Cute and Awesome>\">HERE</A></p>"

    
    body = MIMEText(content, _subtype='html')
    msg.attach(body)
    
    imgListMaker = ImageListMaker()
    img_list = imgListMaker.getImageList()
    
    #Attach images to email
    i = 0
    for image in img_list:
        print image
        fp = open(image, "rb")
        img = MIMEImage(fp.read(), "jpeg")
        fp.close()

        title = '<image%d>' % i
        img.add_header('Content-Id', title)  # angle brackets are important
        msg.attach(img)
        i += 1

    # Now create the MIME container for the image
    # Load the image you want to send at bytes
    # img_data = open(os.path.join(IMAGES_FOLDER, get_random_picture())).read()
    # img = MIMEImage(img_data, 'jpeg')
    # img.add_header('Content-Id', '<myimage2>')  # angle brackets are important
    # msg.attach(img)

    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = ",".join(RECIPIENTS)

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    username = raw_input("Username (GMail): ")
    password = getpass.getpass("Password (GMail): ")
    server.login(username,password)  
    server.sendmail(SENDER, RECIPIENTS, msg.as_string())
    #print msg.as_string()
    server.quit()


if __name__  == "__main__":
    main()
