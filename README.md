# Automatic-Vehicle-number-plate-system-using-edge-detection-according-to-the-color-shade-of-the-vehicle
Detect a vehicle number plate using python and it's libraries for machine learning with efficiency related to the color shade of the Vehicle.

IMPLEMENTATION

Install python opencv and other requirements from requirements.txt 

create folder anpr > and paste the .py files inside it. 

create folder "data/images" inside the anpr directory and here store the images which'll be used for processing.

inside the .py files on line 15 i.e

image_path = "{}/{}".format(images_dir, "car_17.jpg")

Instead of car_17.jpg use the file name of the car inside " ".

Process the image of Car having dark shade of color with anpr.py

Process the image of car having light shade of color with anpr2.py 

This is done for better efficiency.

Use print.py to read the license plate image and store the number in a txt file in the data directory.

Next step is to run the sendsms.py file using your own api url from any free sms sending service. I got mine from sms4india.com. This will read the drivers.csv file where details of the car owner is saved. It will check if the license number matches any from the list and send an sms with the details invoking the reason too. In my case it was speeding ticket.

If you face any problem, just email.
