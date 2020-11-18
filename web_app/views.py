from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'web_app/index.html')

def about(request):
    context = {
        "title" : "about us"
    }
    return render(request , 'web_app/about.html', context)

def services(request):
    context = {
        "title" : "services"
    }
    return render(request , 'web_app/services.html', context)

def study(request):
    context = {
        "title" : "case study"
    }
    return render(request , 'web_app/study.html', context)

def contact(request):
    context = {
        "title" : "contact us"
    }
    return render(request , 'web_app/contact.html', context)

def case1(request):
    case = {
        "title" : "AI + Healthcare",
        "subtitle" : "Did you ever think of machines serving you?",
        "description" : "Nobody could have ever thought of machines being the saviour apart from doctors until this era of robotics. The use of artificial intelligence in healthcare sector has turned out to be a benison and will continue to better it. AI is used to replicate human cognition with the help of analysing complicated medical data.",
        "analysis" : [
            "Loads of information is gained through existing records which is processed and then analysed by AI algorithms giving out AI based solutions.",
            "AI driven computers are more efficient at diagnostics.",
            "Human errors surpass machine errors, with this error reduction is much better than ever with the help of AI.",
            "There are applications and softwares which checks symptoms, this is done by interacting with patients using technology.",
            "Earlier drug development did not always come out to be 100% best in results and clinical trials are best targeted treatments to particular patients and provide previously undiscovered insights through deep learning dictionary.",
            "Formulating medicines for rare diseases require high level skills and the latest techology eases the progression of their transportation.",
            "Major boon to the healthcare industry is the robots assisted surgeries. Better precision, improved flexibility and control.",
            "These robots are equipped with cameras, mechanical arms and surgical instruments. This will benefit doctors to get a 3D magnified view with this. Gradually leading to lesser surgery related complications. less pain and speedy recovery.",
            "One of the best things happened in healthcare industry is cancer and tumoe diagnosis and treatment.",
            "Using AI powered image anaylsation to collect data points supporting cancer discovery and further advanced treatment.",
            "Robot's real time tumor tracking capabilities, doctors and surgeons are able to treat only the affected part rather than targeting the whole body."
        ],
        "recommend" : [
            "For effective operational procedures and better management with patient flow, existing data records and softwares are to be used.",
            "Optimizing hospital efficiency, better engagement with patients and improve treatement. A journey which is effective and productive from testing to treatment which will eventually overcome operational challenges such as priorotizing patients' illness/ injury, waiting time and ambulance fastest routes. Real time patients flow optimization.",
            "For research and treatment purposes AI driven data library can be made using existing data to predict patients future sickness and hospital's healthcare costs."
        ],
        "pros_cons" : [
            "Too much dependency on machines might lead to doctors and staff overlooking into things which need surveillance.",
            "AI systems may suggest a treatment but fail to consider any potential unintended consequences.",
            "As AI systems are capable of carrying out countless jobs and activities, including multitasking, a human monitoring it might become difficult.",
            "As these systems are trained using historical data, AI can’t adapt when developments or changes in medical regulations are implemented.",
            "When machines are working using data, it can lead to lesser confidence while predicting a patient's diagnoses especially when the records are insufficient."
        ],
        "conclusion" : [
            "AI has certainly changed a lot throughout the healthcare space with mind blowing things like Robot-facilitated heart therapy. this robot enters the chest through a small incision. It navigates to certain locations of the heart itself, adheres to the surface of heart and administers therapy.",
            "Overall it has amplified human health and reducing unnecessary strain on the industry.",
            "Another thing the world is grateful for, is coping with mental health illnesses in a way using chatboxes, customized VR simulations to suit a patient's specific needs using different virtual scenarios directional 3D audio, vibrations and other stimuli, journaling moods and employing Cognitive Behavorial Therapy(CBT), reduce negative thought patterns and increase self-awareness."
        ]
    }
    return render(request , 'web_app/case_details.html' , case)

def case2(request):
    case = {
        "title" : "AI + Defense",
        "subtitle" : "How AI is in the interest of national security and defence?",
        "description" : "With enhanced technology and lesser man-power, Artificial Intelligence is not only leading the civilian domain but also in the interest of national security and defence. In the times of modern warfare, stepping up the traditional military forces is the primary decision every other country is making.",
        "analysis" : [
            "Modern arms and ammuniations incorporated with intelligent automation is the need of any defence force in this 21st century.",
            "Time is cardinal when it comes to national safety and security. Enforcing AI in the armed forces will definitley help in quicker response and advanced decision making.",
            "Larger volumes of data is collected in the shorter time which is effortlessly segregated and scrutinized for better understanding of a specific sector.",
            "Target recognition is the major part in any military operation. Drones equipped with intelligent softwares collect terabytes of data integrated and analysed by AI in minutes rather than days when manpower is used.",
            "Computers are growing rapidly in terms of intelligence and learning capabilities which further enhances with regular human interactions. This will upgrade the computers with understanding sentinments and intent.",
            "The paradigm is shifted from user interface to conversational interface raising up the bars in the war game.",
            "Combat Simulation and Training inclusive of threat awareness training elevate the AI systems. It is done through learning from regular exercises and datasets of existing records.",
            "Smart surveillance, quick mobility and mechanised international warfare are the fundamental entities of any defence force.",
        ],
        "recommend" : [
            "AI driven systems are helpful in exploring and accessing untapped geographies.",
            "Search and Rescue operations will have higher probability of success rates when advanced systems are used.",
            "Detection and clearances of various types of mines is the blessing for military, lowering the substantial loss of troops.",
            "Systems loaded with Fire detection sensors, stereo, infrared cameras, UAV, UUV, UGV, build up fire fighting robots.",
            "Intelligent combat help for defence personnels acts as additional support in tackling trial situations.",
            "Updating the existing bomb detection squads with latest AI.",
            "To erase the biasness, appoint a team of experts rather than just one expert as the input data is equally important. This points the importance of humans in the loop."
        ],
        "pros_cons" : [
            "For the interest of national security, nations will adopt both constructive and destructive AI.",
            "Changing the cyber defence architectures in a way that if AI enabled cyber attacks increase, systems to tackle sophisticated cyber threats are to be installed.",
            "Excessive automation may lead to additional security threats resulting in panicking situations."
        ],
        "conclusion" : [
            "Nations are investing in making AI a huge part of the defence sector and become the super power of the world. US alone is spending 7.4Bn USD in 2017 and expected expenditure for using AI in this field is the 18.82Bn USD. China is expected to be the giant in AI defence field by 2030.",
            "Low cost transportation with minimum human efforts has resulted in better warfare globally.",
            "Threat detection and mapping out of potential hostile environments have lessened the troop casualties.",
            "DARPA (Defence Advanced Research Project Agency) and Intelligence, Surveillance, and Reconnaissance (ISR) contribute to the bright future of AI in defence.",
            "Key companies aiming and working for the betterment of AI equipped defence sectors are- Lockheed(US), Raytheon(US), Northrop Grumman(US), IBM(US), Thales group(France), General Dynamics(US), NUIDIA(US), BAE systems(UK), Harris Corporation(US), Charles River Analytics(US), SAIC(US), Leido(US).",
            "To conclude the idea of using wholly automated systems, study highlights the importance of trust factor between humans and machines. Robots and Humans should co-exist for yielding maximum results. Experts say, this is an early stage, we still need human + machine compatibility, certification, validation and evaluation methods."
        ]
    }
    return render(request , 'web_app/case_details.html', case)

def case3(request):
    case = {
        "title" : "AI + Maritime Industry",
        "subtitle" : "Ever wished your imported item to be delivered in fewer days?",
        "description" : " Everyone likes imported things, ever wondered how you get it atyour doorstep in just a few days. Like any other industry, maritime and shipping industry is also not sparred by the canopy of AI. AI equipped systems make the transportation of vessels easier.",
        "analysis" : [
            "Best thing about AI in shipping is reduction of the impact of human error in ully human operated machines.",
            "Efficiencies in technicalities in any field is the first thing experts look for. By introducing AI there's a certain improvement in effective use of on-board systems leading to cutdown on emissions. This way experts can design more environment friendly vessels.",
            "For ease in handling and operations, shipping terminals and ports are designed to follow automated processes.",
            "As AI is all about data and predictions, systems are provided with huge datasets which are analysed and predictions are made on the basis of historical patterns. The ETA of products is provided accurately.",
            "Integrating AI with mapping techniques simplifies the process of analysing multiple naviagtional scenarios.",
            "Effeciently using AI routed maps as per different times, seasons will lead to avoiding crowded shipping lanes. This will eventualy help in reaching respective destinations sooner.",
            "All the vessels and ships are entitled to follow international rules and other regulations in general, with proper management and knowledge which will be taken care of by any AI system, marine shippers will know when they are violating the set limits.",
            "By comparing dynamic data from the real world environment with static data, the vessel can take appropriate actions.",
            "Unlike humans, machines never get bored executing what they have been programmed for. At the same time they don't take interest too!",
            "Accurately scrutinizing existing data help in spotting trends and risks in shipping lanes and ports or threat detection and natural calamities.",
            "Learning weather patterns and understanding fast and slow shipping seasons enabling fatser delivery and low costs.",
            "Duplicating human cognitive abilities with the data collected by various sensors to control onboard equipments.",
            "AI driven applications accelerate descision making processes and workflow. By this customers demands are also understood.",
            "AI based cloud applications help ships reduce fuel consumption and maintenance costs."
        ],
        "recommend" : [
            "Data fused with right knowledge will help in making decisions for optimum use of certain systems.",
            "Upgrading operations of commercial platforms by automation of controls and remote command systems. This will aid in improving passenger safety in ferries and cruiseliners.",
            "Installing AI based systems help the ship perform easily in rough winter weather, handling snow and stong winds and using the data collected through the sensors, it will create pictures to locate hazard around the ship and to navigate among them.",
            "With the right use of knowledge, economies, maritime affairs and forecasting ocean shipping markets are easily understood and managed.",
            "For better future expeditions and predictions one can develop a knowledge platform which enables industrial companies to help understand human  expertise and data from around the globe into a computational knowledge paradigm."
        ],
        "pros_cons" : [
            "High installation costs may hamper companies from using it much more efficiently.",
            "Improving shipping speed, handling products, optimizing warehouse/ terminal operations are considered prominent in shipping industry and which is deteriorated when system behaviour fails to make correct predictions.",
            "As most of the predictions and solutions are based on big data and if there are glitches in these datasets, AI driven systems can give solutions which are not reliable completely."
        ],
        "conclusion" : [
           "Since we're living a swift life and want everything at a blink of an eye, boosting the use of AI in transportation industry will definitely be a bonus for everyone.",
           "For better utilization of this technology companies must make use of their existing historical records."
        ]
    }
    return render(request , 'web_app/case_details.html', case)

def case4(request):
    case = {
        "title" : "AI + Telemeds",
        "subtitle" : "How about meeting a doctor from the comfort of your home?",
        "description" : "With the rising effective necessity in the health care technology, many things which weren't possible before are now carefully and efficiently executed. One such thing is consulting and treating patients over a distance, virtually.",
        "analysis" : [
            "Telemedicine is a telecommunication technology, specifically used for remote diagnosis and treatment of patients.",
            "Telemedicine is a process of helping and caring for patient when doctors and patients are not physically present together.",
            "By using video conferencing technology it is now feasible to deliver health care services to off the map locations.",
            "Patients can conveniently opt for online appointment for diagnosis and treatment without having to book a traditional clinic appointment.",
            "There are times patients are unable to reach out to doctors physically, In such case virtual services hold much importance to both patients and doctors.",
            "Telemedicine is easily available and more accessible, It helps in increasing patient engagement.",
            "For the new set of latest generation, Telemeds being tech savvy it has got good numbers of intelligent features.",
            "It's also of better help to senior citizens, old patients from the rural parts of the country.",
            "Telemeds come in three basic types - 1) Interactive medicine - Communication is directly linked between patients and doctors. 2) Store and Forward - In this, the confidential information of the patient is shared with the practitioner from another location. 3) Remote patient monitoring - This type requires mobile medical devices. Patients at remote and isolated areas will be monitored through these devices.",
            "Softwares design predominantly for telemeds services include the room for virtual waiting hall, EHR and lastly he payment function."
        ],
        "recommend" : [
            "For maintaining data and records of the patient, each patient should be given a unique personal account where all the visits, random and primary healthcare provider visits are stored. Next time any provider needs to see the history he can access it easily.",
            "Training the faculty of this new technology is needed and it is a one time investment since AI algorithm, are cost efficient than conventional methods. This will definitely help patient instead of spending money and time both in expensive lab tests.",
            "The AI algorithm should be well before and the data provided to the AI should be checked before hand. This will reduce the chances of wrong or insufficient data."
        ],
        "pros_cons" : [
            "Reduced care continuity. When a patient telemeds services is connected to a random healthcare provider, care continuity suffers. The patient has to explain everything about his problem to the provider. Now when the patient's primary healthcare provider tunes in, he may not have access to the data or records from early visits by another doctor which might lead to incomplete history of patient and may increase the risk of not knowing the patient completely.",
            "Technology training and Equipment. Staff needs to be well trained to use digital services which costs time and money both. This will include training on the new system for building new telemed modules and programs, which will eventually help patient.",
            "Since consultation happens online, connection and network between both patients and doctors should be strong failing which might result into incomplete consultation, wrong interpretation of information.",
            "AI works by collecting different types of data from many patients who are facing similar symptoms. Lack of data may provide inaccurate diagnosis and doctors can treat the patient wrongly."
        ],
        "conclusion" : [
          "Larger hospital can use existing work flow along with the telehealth solution to lessen the disruption of adopting telemedicine.",
          "Telemedicine is only possible when patients and doctors both have essential equipment, the basic one being video call devices. Simple telemed kit have mobile or computer medical devices, such as ECG or vital science monitors."
        ]
    }
    return render(request , 'web_app/case_details.html', case)

def case5(request):
    case = {
        "title" : "AI + Education",
        "subtitle" : "How exhilarating is it to see computers teaching humans!",
        "description" : "Artificial Intelligence in our lives has come out to be a boon for humans' growth and development. One such major boost which has been witnessed is in education sector. How exhilarating is it to see computers teaching humans!",
        "analysis" : [
           "Study says use of AI in learning field is certainly innovative and enjoyable by students.",
           "Living in the tech world, smartness overpowers educational traditions. Smart content is easily available.",
           "As everyone is unique, each student gets a customized curriculum and study plan as per his/her requirements and interests.",
           "Internet is an ocean of knowledge and information, AI technology will effectively help envision wider picture and will be the land of multiple opportunities in near future.",
           "Time and place can never hinder underprivileged students' potential. Learning anytime and anywhere is the foremost quality everyone reaches out for.",
           "Developed in a way wherein students are interacted with the help of different modules which progresses the process of corrective measures.",
           "Intelligent Tutoring System leads in coaching students especially in their weaker areas.",
           "Real Time virtual learning definitely attracts more students because of the availability and immediate doubt solving.",
           "Nucleus of the whole idea is Universal accessibility and user-friendliness."
        ],
        "recommend" : [
           "Introduction of intelligent game-based learning environments will further better the interaction, increase the possibility of engaging more students learning through AI and make learning fun.",
           "Classrooms to be led by AI assisted teachers for optimum results so as to embrace the personal connection between a teacher and a student.",
           "Facilitating a teacher's role by granting AI a chance of bringing judgement free trial and error learning.",
           "Infusing modern content according to students' choices and interests."
        ],
        "pros_cons" : [
           "Prior investment in installation of hardware and software is the highest but in a longer run sustainability remains intact.",
           "Early learning might lead to young generation getting addicted to technology.",
           "Some grading softwares can cause unnecessary biasness due to inbuilt biasness while feeding existing information.",
           "Benefits of AI in education undoubtedly transcends the cons remarkably."
        ],
        "conclusion" : [
            "World is growing, so is internet and technology, schools need to level up and exhibit their relevance.",
            "More the incorporation of AI in education, more the effectiveness of technology in students' lives.",
            "Renowned examples are set by CRAM101 using algorithms in MCQs, chapter summaries, true or false, flashcards, another one is NETEX LEARNING which uses aural and visual content and design digital curriculum and CARNEGIE LEARNING's mika software which believes in learning sciences and artificial intelligence technology, provides personalized tutoring and real-time feedback, etc."
        ]
    }
    return render(request , 'web_app/case_details.html', case)

def case6(request):
    case = {
        "title" : "AI + Chatbot",
        "subtitle" : "What if I say that your query was solved by a chatbot?",
        "description" : "Our lives have become faster as technology evolves. Even the smallest of tasks are efficiently done by just one click. Whether it is just solving queries online or playing your favourite music in the house, everything is performed automatically.",
        "analysis" : [
            "Chatbot is basically a chat robot. A software application with instant messaging services.",
            "Humans are highly fascinated with auto operation and chatbot is one such AI driven gadget which is one of the greatest trends.",
            "In simple words, chatbots behave as human's conversational partners on an online conversation platform via text/ text-to-speech mode.",
            "Chatbots are widely differentiated based on different uses.",
            "The traditional plain chatbots are more inclined towards automaton and AI chatbots impress the high end brands with their ability to learn and grow with time and gain experience.",
            "Industries using human resources rigorously install chatbots as their virtual assistants because the AI factor and automation bring fruitful results.",
            "For chatbots to operate ideally and effectively it undergoes consistent tuning and testing. The most important test they need to pass before getting deployed is the Turing test. This will test the computer program's ability to hold the conversation like a human in real time. When the judge fails to distinguish between the human and program it means the chatbot can now be operated actively.",
            "The working of chatbot is broadly explained in 4 steps i.e. 1) input from user, 2) Analysis of user's request (one of the most important steps), 3) Identifying user's intent and entities, 4) composing the reply.",
            "The most used programming languages for building a chatbot are Java and C++ but Python remains easier for inexperienced team.",
            "Database is of paramount importance in chatbots. The data is stored in different forms as existing conversations, the training period and in terms of ML, NLP to learn the context.",
            "Virtual assistants like chatbots help save a lot of time, money and resources especially in the time of crisis.",
            "For customer service chatbots are actually a bonus for accelerating the response time more efficiently to customer queries.",
            "Chatbots are essentially a boon in healthcare industry. The online services include consultation through conversations."
        ],
        "recommend" : [
            "As explained above, there's a definite increase in lead conversion rate and customer service elevation when the website becomes interactive.",
            "Along with chatbot service, live meetings with the team or the combination of both will sort of decrease the chance of customers terminating due to frustration.",
            "With the help of chatbots, companies can take surveys to find customer's insights and the data collected can be used to make the information readily available on website.",
            "Chatbots are invented to provide quick response and such immediate support to customers may lead to exponential growth in leads generation.",
            "From a business perspective speed is the most important for generating qualified leads. Making chatbots available with live meetings will resolve the issues faster and effectively.",
            "Problems don't look at the clock hence making your chatbot service available around the clock will enhance Customer satisfaction."
        ],
        "pros_cons" : [
            "If the chatbot is inexperienced and unable to solve real problems, the customer may get frustrated and switch towards brands which embrace automation and AI more productively.",
            "As the companies are in a cut throat competition, putting much pressure on sales and marketing teams for better performance, installing chatbot in replacement of humans won't really help as situations where complex queries require better response handling. This can deter the customer from future expeditions.",
            "Chatbots can't show emotions and sometimes certain things need support which only human service can provide. But you can now teach your chatbot to be empathetic based on certain messages.",
            "Building a chatbot from scratch requires knowledge and experience in coding",
            "It is difficult to solve queries which require advanced knowledge and relying solely on chatbots wouldn't be great."
        ],
        "conclusion" : [
            "Not everyone prefers chatbots for complete reliance hence human interaction is equally important. Co-existence of both is a solution for all age groups.",
            "With time, companies realize the need of the giving out the best and installation of chatbots eases the process which results in better marketplace.",
            "Companies can actually save money by deploying various chatbots where human interaction is not needed."
        ]
    }
    return render(request , 'web_app/case_details.html', case)

