# Automatic-Vehicle-number-plate-system
Detect a vehicle number plate using python and it's libraries for machine learning.
IMPLEMENTATION
The project has been implemented using python and its li- braries including deep learning and other models of python. The data has been saved in the anpr folder directory. We run the python files using terminal, which takes image from the directory as an input. This image is processed through dif- ferent filters to get the outlines of the vehicle from the input data, which are blur, grayscale, noise reduction, transform- ing into binary image etc. The edges are projected over the
2. Projection of edges on image using contours
The edges are projected over the original image using drawContour() function using the variables of edges as pa- rameters. The value (106,0,255) is used for the colour which is magenta. Here’s an sample we found in our research:
3. Finding the Plate( Region of interest)
Now the number of details in the image are minimised using the more efficient algorithms for edge detection, so remaining are the details of the car and it’s features, from which the perimeter of an projecting edge forming an arc is found. This value of perimeter when multiplied by 0.02 gives the number of edges of that arc. If the number of edges of an arc gives 4, it saves it as a region of interest and writes “data/images/plate.png” in the directory. We found This sample in our research :
4. Image to String conversion
Using python image library, Numpy, pytesseract and their features like optical character recognition, the text from “data/images/plate.png” is extracted , stored and displayed. The stored number is in txt file “data/images/numbers.txt”.
Sample from our research
5.Getting information from license database.
The value of number plate extracted from the car is com- pared with the list of number plates in the database after removing all the whitespaces from the text. If there’s a match in the database, mobile number of the owner of vehi- cle is stored and via text message or other services is issued a speeding ticket (in our research) or other services as im- plemented.
6.Increasing efficiency
In our research we have checked if a car is having a darker shade of colour or white. We parsed the car having darker shade of colour through one algorithm and the one with white through another for better precision efficiency.
7.Getting efficiency
We tested on over 50 images of cars from Tamil Nadu and a few overseas using haar cascades and our algorithm. Our
     original image using magenta. All the edges which makes an arc and recorded into consideration. Now if one of these projected arc has 4 as the number of edges and text inside it, it stores it as a region of interest as a .png extension. This extension is used to get the license number using deep learn- ing and stored in txt file. Now this number is matched with a database of car owners. If any service for example, a speed- ing ticket has to be issued to the owner, it can now automat- ically be done using anpr.
1. Detection of Edges using Canny and Laplacian Algo- rithms.
The camera in traffic signals captures the image of a speed- ing vehicle and transfers it as an input to our system. This image is first filtered as grayscale , then blur to remove noise from the image. To increases the efficiency threshold parameter is used to create the blur image. Edges are then found using the above algorithms.
 
researched algorithm plotted a greater efficiency than the former one. Therefore we recommend using our method for number plate localisation and identifying the vehicle.
A. Improvements
6. Yoh-Han Pao, “Adaptive Pattern Recognition and Neural Network.” Pearson Education Asia, 2009. 
7. M. M. Shidoret,S. P. Narote, Vishwakarma Institute of Technology, University of Pune, Pune, India, Sinhgad College of Engineering, University of Pune, Pune, India IJCSNS International Journal of Computer Science and Network Security, VOL.11 No.2, Feb. 2011
8. Abd Kadir Mahamad, Sharifah Saon, and Sarah Nurul Oyun Abdul Aziz, “A Simplified Malaysian Vehicle Plate Number Recognition”, Springer International Publishing Switzerland 2014  
9. Amar Badr Mohamed M. Abdelwahab, Ahmed M. Thabet, and Ahmed M.Abdelsadek, “Automatic Number Plate Recognition Sys- tem”, Annals of the University of Craiova, Mathematics and Comput- er Science Series Volume 38(1), 2011, Pages 62{71ISSN: 1223-6934.  
10. Op tasia S ystems P te Ltd, “ The World L eader in License Pla te Reco gn ition T echnology” 22 November 2008.  
11. Xiangjian He et al, "Division of characters on vehicle License Plate", tenth Workshop on Sight and sound Sign Handling, Oct. 2008, pp. 399-402.
12. Mei Yu and Yong Deak Kim, “An approach to Korean license plate recognition based on vertical edge matching”, IEEE Worldwide Gath- ering on System, Man and Cybernetics, 2000, vol.4, pp. 2975-2980.
V.
• •
•
Better algorithm may perhaps be used to remove noise from the imager for a better efficiency.
Images having license plate over a black back- ground are to be processed using a different algo- rithm anpr2.py which uses a threshold value to form a perfect black-whirte image.
Use of infrared cameras may make the system more efficient to use as it gives vivid images of vehicle even in unfavorable conditions.
RESULTS DISCUSSION
The efficiency of getting the license plate from the im- age and predicting it’s text using the algorithm in our topic’s research is quite better than the other ones mentioned in the related work. Hence we recommend it stilll with some limi- tations.
VI. CONCLUSION
The images we had were of decent quality and the pre- diction of the number plate could be better using infrared and other effective cameras. The noisiness and shapes from an image could be better handled. And threads like ambigu- ous characters (5,S 1,I O,0 C,G A,4) can be better see- mented using deep learning approach.
Also the system should not be affected by factors like speed, font-size, plate style, and lighting conditions. The main objective of this research is not producing a complete accurate result but to work on the invariance of the algo- rithms on different images of vehicles based on their respec- tive features.
