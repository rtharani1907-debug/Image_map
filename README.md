# Ex04 Places Around Me
# Date:01-10-2025
# AIM
To develop a website to display details about the places around my house.

# DESIGN STEPS
## STEP 1
Create a Django admin interface.

## STEP 2
Download your city map from Google.

## STEP 3
Using <map> tag name the map.

## STEP 4
Create clickable regions in the image using <area> tag.

## STEP 5
Write HTML programs for all the regions identified.

## STEP 6
Execute the programs and publish them.

# CODE
```
map.html
<html>
    <head>
        {% load static %}
         <title>My Area</title>
    </head>
    <body bgcolor="beige">
        <h1 align="center">
            <font color="purple"><b>ORIKKAI</b></font>
        </h1>
        <h3 align="center">
            <font color="dark blue"><b>THARANI RAMESHBABU(25018409)</b></font> 
        </h3>
        <center>
           <img src="{% static 'area.png.png' %}" usemap="#Image_map" height="600px" width="1500px">
           <map name="Image_map">
           <area shape="rect" coords="506,74,678,80" title="Resort" href="resort.html" alt="Resort">
           <area shape="rect" coords="206,54,373,60" title="School" href="school.html" alt="School">
           <area shape="rect" coords="637,375,721,331" title="Farm" href="farms.html" alt="Farm">
           <area shape="rect" coords="617,125,704,180" title="Weavers" href="weavers.html" alt="Weavers">
           <area shape="rect" coords="637,500,704,531" title="Company" href="company.html" alt="Company">
           </map>
        </center>
    </body>
</html>

company.html

<html>
    <head>
        <title>company</title>
    </head>
    <body style="background-color: rgb(243, 185, 79);">
        <h1 align="center" style= "color:rgb(241, 61, 34);">ORIKKAI</h1>
        <h2 align="center" style= "color:rgb(241, 61, 34);">The oriental insurance company</h2>
        
        <p style="background-color: rgb(227, 169, 103); font-family: Georgia, 'Times New Roman', Times, serif; font-style: normal; color:black; text-align: justify;">
          OICL was incorporated at Mumbai on 12 September 1947. The company was a wholly owned subsidiary of The Oriental Government Security Life Assurance Company Ltd and was formed to carry out general insurance business. Following the nationalisation of the life insurance business and the formation of the Life Insurance Corporation of India under statutory law, the company became a subsidiary of the Life Insurance Corporation of India from 1956 to 1973 (until the general insurance business was nationalized in the country). Following the nationalisation of the general insurance industry by the General Insurance Business (Nationalisation) Act, 1972 (GIBNA), the Government of India transferred all the shares it held of the general insurance companies to the General Insurance Corporation of India (GIC). OICL became one of the four subsidiaries of GIC, with its headquarters in New Delhi.
          With the General Insurance Business (Nationalisation) Amendment Act 2002 (40 of 2002) coming into force on March 21, 2003, GIC ceased to be a holding company of its subsidiaries. The ownership of the four erstwhile subsidiary companies and the General Insurance Corporation of India was vested with the Government of India. All company shares held by the GIC were transferred to the central government.
          The Insurance Act of 1938 was the first legislation governing all forms of insurance to provide strict state control over insurance business. Life insurance in India was completely nationalised on 19 January 1956, through the Life Insurance Corporation Act. All 245 insurance companies operating then in the country were merged into one entity, the Life Insurance Corporation of India.
          The primary regulator for insurance in India is the Insurance Regulatory and Development Authority of India (IRDAI) which was established in 1999 under the government legislation called the Insurance Regulatory and Development Authority Act, 1999.
          The history of agriculture in India dates back to the Neolithic period. India ranks second worldwide in farm outputs. As per the Indian economic survey 2020 -21, agriculture employed more than 50% of the Indian workforce and contributed 20.2% to the country's GDP.
          Pesticides and fertilizers used in Indian agriculture have helped increase crop productivity, but their unregulated and excessive use has caused different ecosystem and fatal health problems.
        </p>
        </body>
</html>

farms.html

<html>
    <head>
        <title>Farms</title>
    </head>
    <body style="background-color: rgb(26, 201, 249);">
        <h1 align="center" style= "color:rgb(175, 51, 130);">ORIKKAI</h1>
        <h2 align="center" style= "color:rgb(175, 51, 130);">Srinamo farms</h2>
        <pre>
        <p style="background-color: rgb(149, 182, 248); font-family: Georgia, 'Times New Roman', Times, serif; font-style: normal; color:black; text-align: justify;">
          - Located on the Kanchipuram Taluk, Perumbakkam, Chennai, Srinamo Farms  is an ideal relaxation home. 
          - Srinamo Farms an ideal home for families, corporates, get-togethers, birdwatchers, adventure seekers etc.
          - It is next to the lake so one can enjoy the beautiful View of the lake, plants, birds in the area.
          - This has been designed and built to allow your guests to experience and enjoy the natural ambience.
          - Air conditioned rooms with attached bathroom
          - Balcony attached with all rooms
          - Kitchen (*Basic utensils, Induction Stove, Fridge)
          - dining table
          - Living room (with Sofa-cum-bed)
          - Bar area
          - Swimming pool (shower, Changing rooms)
          - Water Slide
          - Jacuzzi
          - Kids pool
          - Tree house (100sq.ft.)
          - Music System
          - Lawn with 350 people capacity
          - Large party Lawn with more than 1700 People capacity
          - Lawn for sports like cricket,Throwball etc.
          - Parking for more than 25 Cars available
          - Fountain
          - Picnic tables
           </p>
           </pre>
           </body>
</html>

resort.html

<html>
    <head>
        <title>Resort</title>
    </head>
    <body style="background-color: palevioletred;">
        <h1 align="center" style= "color:maroon;">ORIKKAI</h1>
        <h2 align="center" style= "color:maroon;">Marutham village resort</h2>
        <p style="background-color: pink; font-family: 'Times New Roman', Times, serif; font-style: normal; color:black; text-align: justify;">
            Great care is taken to ensure guests experience comfort through top-notch services and amenities. Remain linked during your visit by utilizing the complimentary internet access available.Services offered by taxi and car hire at the resort ensure effortless exploration of Chennai.The resort offers complimentary parking for guests who arrive with their own mode of transport.Reception services featuring safety deposit boxes are available to cater to your requirements.During your stay at this fantastic resort, experience comfort and warmth from the delightful on-site fireplace on those chilly days and nights.Repeatedly enjoy your best-loved attire with the aid of the laundromat available at Marutham Village Resort . During leisurely days and evenings, in-room amenities such as room service and daily housekeeping enable you to maximize your stay in the room.The resort is completely smoke-free.In limited designated zones, smoking is exclusively permitted.Crafted for coziness, every guestroom provides an array of features, guaranteeing a tranquil night's sleep while maintaining the level of comfort.For a more enjoyable stay, select rooms at resort are equipped with linen service, blackout curtains and air conditioning.At Marutham Village Resort , a selection of rooms can be found that showcase unique design elements such as a balcony or terrace.Expand your in-room entertainment choices with various amenities, such as television offered in certain accommodations.Rest assured that your hydration needs will be met, as some guestrooms are equipped with a coffee or tea maker, bottled water and instant coffee. Maintain your cleanliness and comfort using a hair dryer and toiletries available in select guest restrooms. Begin your day on a delightful note with a scrumptious complimentary breakfast, consistently served at Marutham Village Resort .Begin your holiday mornings right with your essential cup of coffee, offered daily at the cafe on-site. During your visit, indulge in a range of delightful culinary choices at resort to enhance your experience.Concerned about your dining preferences? Fret not! Marutham Village Resort offers an assortment of culinary varieties featuring halal choices, catering to all tastes.Indulge in the numerous pursuits available at Marutham Village Resort . During your stay, the resort provides direct access to a beach, ensuring you remain near the sea throughout your visit.At the resort, enjoy a laid-back beverage experience by the poolside bar, sipping on a soothing cocktail.

        </p>

    </body>
</html>

school.html

<html>
    <head>
        <title>School</title>
    </head>
    <body style="background-color: rgb(248, 170, 251);">
        <h1 align="center" style= "color:rgb(180, 43, 107);">ORIKKAI</h1>
        <h2 align="center" style= "color:rgb(180, 43, 107);">Sangford school</h2>
        <p style="background-color: rgb(243, 121, 237); font-family: Georgia, 'Times New Roman', Times, serif; font-style: italic; color:black; text-align: justify;">
          Sangford School, located on Vandavasi Road in Kanchipuram, Tamil Nadu, is known for its commitment to providing quality education in a nurturing environment. The school caters to students from various backgrounds and emphasizes a holistic approach to learning. With a focus on both academic excellence and character development, Sangford School aims to prepare students for the challenges of the future. The curriculum at Sangford School is designed to foster critical thinking and creativity. It incorporates a blend of traditional subjects and modern educational practices, ensuring that students receive a well-rounded education. The faculty is dedicated and experienced, often going the extra mile to support students in their academic pursuits. This personalized attention helps create a positive learning atmosphere where students feel encouraged to express themselves.
          Extracurricular activities play a significant role in the school’s philosophy. Sangford School offers a variety of programs, including sports, arts, and cultural events, allowing students to explore their interests beyond academics. This focus on holistic development helps students build teamwork skills, confidence, and a sense of community. Parents often appreciate how these activities contribute to their children's overall growth.
          Feedback from parents and students highlights the school's supportive environment. Many reviews mention the approachable teachers and the strong sense of community among students. Parents feel that their children are not just receiving an education but are also developing important life skills. The school’s emphasis on values and ethics resonates well with families looking for a nurturing educational experience.
          Facilities at Sangford School are designed to enhance the learning experience. Classrooms are equipped with modern teaching aids, and the campus includes spaces for sports and recreational activities. This infrastructure supports a balanced approach to education, where students can thrive academically while also enjoying their time at school. Overall, Sangford School stands out in Kanchipuram for its dedication to fostering a well-rounded education.
          With a focus on both academic and personal development, it creates an environment where students can grow into confident and capable individuals. The positive reviews from the community reflect the school’s commitment to excellence and its role in shaping the future of its students.
    
        </p>
           </body>
</html>

weavers.html

<html>
    <head>
        <title>Weavers</title>
    </head>
    <body style="background-color: rgb(196, 230, 42);">
        <h1 align="center" style= "color:rgb(43, 72, 12);">ORIKKAI</h1>
        <h2 align="center" style= "color:rgb(43, 72, 12);">Kanchipuram weavers</h2>
        
        <p style="background-color: rgb(14, 163, 99); font-family: Georgia, 'Times New Roman', Times, serif; font-style: italic; color:black; text-align: justify;">
          The Beauty of Kanchi silk sarees
           kanchipuram silk sarees have been the ultimate accessory for creating that unique look for centuries. Originating from the picturesque village of Kanchipuram in Tamil Nadu, South India, these sarees are crafted with finesse and boast a versatility fit for any occasion! From simple elegance to elaborate designs, you can discover various stunning styles perfect for your wardrobe.Extensive ranges of collection of pure silk dhoti online, including kanchipuram silk dhoti for weddings and Kerala dhoti online as well as Pattu dhoti. Meticulously crafted for the finest traditional South Indian weddings and special occasions. The Kanjivaram sari is exclusively known for its rich gold borders and dense brocades in contrast colours. They are hand-woven purely from dyed silk-yarn and zari (silk thread made of silver and gold). The saris have an enviable reputation for richness, texture, lustre, durability and finish. 
           The art of silk weaving in Kanchipuram dates back more than 400 years. Legend has it that the weavers of Kanchipuram are descendants of Sage Markanda, the master weaver for the gods. Over centuries, these artisans have honed their skills, blending traditional knowledge with evolving techniques to create masterpieces. The Padma Saliyar and Pattu Saliyar communities are central to this tradition, often working in family units where each member contributes to different aspects of the weaving process.
           Kanchipuram silk sarees, like those offered at Hayagrivas Silk House, are celebrated for their durability, vibrant colors, and intricate patterns inspired by temple architecture, nature, and mythology. Whether you’re seeking a saree with timeless motifs or one with modern elegance, explore the range of traditional bridal Kanchipuram silk sarees and lightweight sarees for daily wear for your perfect match. Each saree is a labor of love, requiring 10-15 days to complete, depending on its complexity.
           Despite the global acclaim of Kanchipuram silk sarees, the weavers face significant challenges, including competition from power looms, rising raw material costs, and inconsistent demand. At Hayagrivas Silk House, we actively support these artisans by promoting traditional handloom products and providing a platform for their unparalleled craftsmanship. From festive collections to heirloom pieces, every purchase helps sustain the craft and its creators.
        </p>
        </body>   
</html>

views.py

from django.shortcuts import render
def fun(request):
    return render(request,'map.html')
def com(request):
    return render(request,'company.html')
def far(request):
    return render(request,'farms.html')
def res(request):
    return render(request,'resort.html')
def sch(request):
    return render(request,'school.html')
def wea(request):
    return render(request,'weavers.html')

urls.py

from django.contrib import admin
from django.urls import path
from imageapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fun),
    path('company.html',views.com),
    path('farms.html',views.far),
    path('resort.html',views.res),
    path('school.html',views.sch),
    path('weavers.html',views.wea)
]
```

# OUTPUT
![alt text](<Screenshot (28).png>)
<<<<<<< HEAD
![alt text](<Screenshot (38).png>)
=======
![alt text](<screenshot (38).png>)
>>>>>>> 37eececb8562c038617c6d27844e9145f546f4cc
![alt text](<Screenshot (34).png>)
![alt text](<Screenshot (35).png>)
![alt text](<Screenshot (36).png>)
![alt text](<Screenshot (37).png>)

# RESULT
The program for implementing image maps using HTML is executed successfully.
