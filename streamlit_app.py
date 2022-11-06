import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Maher Ali, Data Scientist | Machine Learning Engineer.
##### *Resume* 
''')

image = Image.open('ms.jpg')
st.image(image, width=200)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Highly motivated data scientist with in-depth knowledge of research or statistical models. 
- Innovator with the ability to develop new solutions and interpretations. 
- Strong communication skills. and able to learn new techniques or tools easily, Able to work independently and as part of a team,
- I am looking for a position in Data Science with a forward-thinking company. 
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand"  target="_blank">Maher Ali Ragab</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelors of Management Information Systems**,  *Higher Institute of Administrative Sciences*',
'2018-2022')
# st.markdown('''
# - GPA: `3.89`
# - Research thesis entitled `Computer-aided molecular design for biological and chemical applications : Quantum chemical and machine learning approach`.
# - Received Royal Golden Jubilee Ph.D. Scholarship of `2.152 million THB` covering tuition and stipend.
# - Thesis awarded `1st` Prize by the National Research Council of Thailand.
# ''')

txt('**Data Science Diploma (Machine Learning & AI)**, *Space Code Academy*',
'10/9/2021-16/4/2022')
st.markdown('''
## - Certifications:
- https://drive.google.com/file/d/1R9e8Ja0Xna97KoZvPNM95tE9_WGROJqP/view?usp=sharing.
''')


#####################
st.markdown('''
## projects
-**Machine-Learning-PROJECTS**
''')
txt4('PHPML','Perth House Prices Prediction using Machine Learning', 'https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/Perth%20House%20Prices%20Prediction')
txt4('CPpML', 'Car Price Prediction using Machine Learning', 'https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/Car%20price%20prediction%20using%20Linear%20regression')
txt4('MICPLR', 'Medical insurance cost prediction using linear regression','https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/Medical%20insurance%20cost%20prediction%20using%20linear%20regression')
txt4('SP', 'Salary Prediction', 'https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/ml-app-salaryprediction')
txt4('SPWAS', 'Salary Prediction Web App With Streamlit','https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/ml-app-salaryprediction')
txt4('BMSPML', 'Big Mart Sales Prediction using Machine Learning', 'https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/Big%20Mart%20Sales%20Prediction%20using%20Machine%20Learning')
txt4('CMCPML', 'Company Market Cap Prediction using Machine Learning', 'https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/company-market-cap-prediction')
txt4('MPCK', 'Mobile Price Classiﬁcation- KNN', 'https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/Mobile%20Phone%20Price%20Prediction%20With%20Pipeline')
txt4('MPhPPP', 'Mobile Phone Price Prediction With Pipeline', 'https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/Mobile%20Phone%20Price%20Prediction%20With%20Pipeline')
txt4('DSMCS', ' Data Science for Marketing Case-study', 'https://github.com/Maher-AI/Machine-Learning-Projects/tree/main/Data%20Science%20for%20Marketing%20Case-study')
txt4('DPLR', 'Diabetics prediction using Logistic Regression', 'http://codes.bio/hemopred/')

st.markdown('''
- **Deep-Learning-PROJECTS**
''')

txt4('CNN', 'Gender and Age Prediction - Image Classiﬁcation & CNN','https://github.com/Maher-AI/Deep-Learning-Projects/tree/main/Gender%20and%20Age%20Prediction%20-%20Image%20Classification%20-%20CNN')
txt4('CNN', 'Facial Emotion Recognition - Image Classiﬁcation - CNN','https://github.com/Maher-AI/Deep-Learning-Projects/tree/main/Facial%20Emotion%20Recognition%20-%20Image%20Classification%20-%20CNN')
txt4('Sound Classiﬁcation', 'Speech Emotion Recognition - Sound Classiﬁcation','https://github.com/Maher-AI/Deep-Learning-Projects/tree/main/Speech%20Emotion%20Recognition%20-%20Sound%20Classification')
txt4('MediaPipe', 'AI Hand Pose Estimation with MediaPipe - Detect Left and Right Hand','https://github.com/Maher-AI/Deep-Learning-Projects/tree/main/AI%20Hand%20Pose%20Estimation%20with%20MediaPipe%20-%20Detect%20Left%20and%20Right%20Hand')
txt4('Mediapipe', 'AI Face Body and Hand Pose Detection with Mediapipe','https://github.com/Maher-AI/Deep-Learning-Projects/tree/main/AI%20Face%20Body%20and%20Hand%20Pose%20Detection%20with%20Mediapipe')
txt4('CNN', 'Classiﬁcation of mountains, trees, and ice using convolutional neural networks','https://github.com/Maher-AI/Deep-Learning-Projects/tree/main/Classification%20of%20mountains%2C%20trees%2C%20and%20ice%20using%20convolutional%20neural%20networks')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `PowerBI`, `Tableau`, `Google Data Studio`')
txt3('Machine Learning', '`Scikit-Learn`')
txt3('Deep Learning', '`TensorFlow`, `Keras`')
# txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`,`R Shiny`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/maher-ali-206981235/')
txt2('GitHub', 'https://github.com/maher-ai')
txt2('wuzzuf', 'https://wuzzuf.net/profile')
# txt2('', 'https://github.com/chaninlab/')
# txt2('', 'https://github.com/dataprofessor')
# txt2('ORCID', 'http://orcid.org/0000-0003-1040-663X')
txt2('tableau', 'https://public.tableau.com/app/profile/maher7021')
# txt2('ResearcherID', 'http://www.researcherid.com/rid/F-1021-2010')
# txt2('ResearchGate', 'https://www.researchgate.net/profile/Chanin_Nantasenamat')
# txt2('Publons', 'https://publons.com/a/303133/')

st.markdown('''
##  Languages
- Arabic-A1
- English-C2
''')


