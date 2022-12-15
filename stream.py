import streamlit as st
from PIL import Image
# from tensorflow.keras.utils import load_img/
# from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import load_img ,img_to_array 
# from keras.preprocessing.image import  
import numpy as np
from keras.models import load_model

info = {'Hawa Mahal' : " The Hawa Mahal is dedicated to Lord Krishna. It is said that the shape of the building resembles the crown of Krishna. More than a palace, the Hawa Mahal is also a cultural and architectural marvel that reflects a truly harmonious amalgamation of the Hindu Rajput and Islamic Mughal architectural styles?" ,
        'Taj Mahal' : " You should visit the Taj Mahal because of its historic significance and its stunning architecture. It is an important and sacred site and is one of the Seven Wonders Of The World. If you are in India, the Taj Mahal is a must-see attraction.",
        'India Gate' : " India gate or The All India War Memorial is 42-metre-high giant gate made up of sandstone, built by prominent war memorial architect Edwin Lutyens in 1921. It is a war memorial situated at the eastern end of Kingsway that is the Rajpath, is memorial to martyrs of World War (1914-21). ",
        'Lotus Temple' : " The youngest religion in the world built a temple of their faith to become a prominent landmark in the capital of a country which still practices the oldest religion in the world. This lotus-shaped temple that was dedicated in December 1986, is the designation of a place of worship, or temple",
        'Qutub Minar' : "Qutub Minar is surrounded by several historical monuments, which are altogether known as the Qutub Complex.The complex comprises Quwwat-ul-Islam Mosque, Iron Pillar of Delhi, the Tomb of Iltutmish, Alai Darwaza, the Tomb of Imam Zamin, Alai Minar, Ala-ud-dins Madrasa and Tomb, Major Smiths Cupola and Sandersons Sundial.The tower has been standing for almost 2,000 years without rusting.",
        'Sun Temple Konark' : "The 700-year-old Sun Temple is a UNESCO World Heritage Site and an architectural genius. It was built during the rule of King Narsimhadeva I (1236-1264) of the Ganga dynasty. Located on the shores of the Bay of Bengal, the temple is a colossal illustration of the Sun God Suryas chariot; its 24 wheels are adorned with emblematic designs and it is led by a horde of seven horses. Constructed in the 13th century, it is one of Indias most celebrated Brahman sanctuaries",
        'Tanjavur Temple' : "It is one of the ancient temples in India and is dedicated to Lord Shiva, one among the Three God heads in Hinduism. A fine exemplar of the ancient Dravidian architecture, this piece of art was built by the great Raja Raja Chola I in the year 1010 AD. He was an ardent devotee of Lord Shiva."}
        
link = {'Taj Mahal' :"https://en.wikipedia.org/wiki/Taj_Mahal",
        'Hawa Mahal' :"https://en.wikipedia.org/wiki/Hawa_Mahal",
        'India Gate' :"https://en.wikipedia.org/wiki/India_Gate",
        'Lotus Temple' : "https://en.wikipedia.org/wiki/Lotus_Temple",
        'Qutub Minar' : "https://en.wikipedia.org/wiki/Qutb_Minar",
        'Sun Temple Konark' : "https://en.wikipedia.org/wiki/Konark_Sun_Temple",
        'Tanjavur Temple' : "https://en.wikipedia.org/wiki/Brihadisvara_Temple,_Thanjavur"}
maps = {'Taj Mahal' :"https://www.google.com/maps/place/Taj+Mahal/@19.9014599,75.2501838,13z/data=!4m10!1m2!2m1!1staj+mahal!3m6!1s0x3bdb99f8bce5aa71:0x8e7cc1b5151f623d!8m2!3d19.9014599!4d75.3202216!15sCgl0YWogbWFoYWxaCyIJdGFqIG1haGFskgETaGlzdG9yaWNhbF9sYW5kbWFya5oBJENoZERTVWhOTUc5blMwVkpRMEZuU1VOUGJHRXpiR3hSUlJBQuABAA!16s%2Fg%2F11ptw44szl",
        'Hawa Mahal' : "https://www.google.com/maps/place/Hawa+Mahal/@26.9239363,75.8245551,17z/data=!3m1!4b1!4m5!3m4!1s0x396db14b1bd30ba5:0x860e5d531eccb20c!8m2!3d26.9239363!4d75.8267438",
        'India Gate' : "https://www.google.com/maps/place/India+Gate/@23.7023842,70.536067,6z/data=!4m10!1m2!2m1!1sindia+gate!3m6!1s0x390ce2daa9eb4d0b:0x717971125923e5d!8m2!3d28.612912!4d77.2295097!15sCgppbmRpYSBnYXRlWgwiCmluZGlhIGdhdGWSAQhtb251bWVudOABAA!16zL20vMDM1bWMz",
        'Lotus Temple' : "https://www.google.com/maps/place/Lotus+Temple/@28.553492,77.2566377,17z/data=!3m1!4b1!4m5!3m4!1s0x390ce3c16e028cd1:0x653beb1ee85ec67a!8m2!3d28.553492!4d77.2588264",
        'Qutub Minar' : "https://www.google.com/maps/place/Qutab+Minar,+Seth+Sarai,+Mehrauli,+New+Delhi,+Delhi+110016/@28.5244946,77.183329,17z/data=!3m1!4b1!4m5!3m4!1s0x390d1e065dc72379:0xf6e7259f610de1d7!8m2!3d28.5244946!4d77.1855177",
        'Sun Temple Konark' : "https://www.google.com/maps/place/Konark+Sun+Temple/@19.8875952,86.0900517,17z/data=!3m1!4b1!4m5!3m4!1s0x3a19f2a097819bbf:0xed9983ca391e3247!8m2!3d19.8875953!4d86.0945364",
        'Tanjavur Temple' : "https://www.google.com/maps/place/Brihadeeswara+Temple/@10.7829727,79.1307736,18z/data=!4m10!1m2!2m1!1sthanjavur+temple!3m6!1s0x3baab89f48fe1221:0x1d23cb40e55d84d6!8m2!3d10.7827828!4d79.1318463!15sChB0aGFuamF2dXIgdGVtcGxlWhIiEHRoYW5qYXZ1ciB0ZW1wbGWSAQxoaW5kdV90ZW1wbGXgAQA!16s%2Fm%2F047trs0"}
model = load_model('./MI.h5', compile=False)
lab = {0: 'Hawa Mahal',1: 'India Gate',2: 'Lotus Temple',3: 'Qutub Minar',4: 'Sun Temple Konark',5: 'Taj Mahal',6: 'Tanjavur Temple'}
def processed_img(location):
    img=load_img(location,target_size=(224,224,3))
    img=img_to_array(img)
    img=img/255
    img=np.expand_dims(img,[0])
    answer=model.predict(img)
    y_class = answer.argmax(axis=-1)
    y = " ".join(str(x) for x in y_class)
    y = int(y)
    res = lab[y]
    print(res)
    return res
def run():
    img1 = Image.open('./Logo/Logo.png')
    img1 = img1.resize((550,350))
    st.image(img1,use_column_width=False)
    st.title("Monument Identification")
    st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Data is based on Training the model on 7 diffrent Monuments"</h4>''',
                unsafe_allow_html=True)
    img_file = st.file_uploader("Choose an Image of Monument", type=["jpg", "png"])
    if img_file is not None:
        st.image(img_file, use_column_width=False)
        save_image_path = './upload_images/' + img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        if st.button("Predict"):
            result = processed_img(save_image_path)
            st.success("Predicted Monument is: " + result)
            for monument in info:
                if monument == result :
                     st.success("* " + info[result])
                     url = link[result]   
                     mapsurl = maps[result]
                     st.write("For More Information visit [link](%s)" % url)
                     st.write("To open in maps click [link](%s)" % mapsurl)


run()